#!/usr/bin/env python3
"""FRACTAL repository doctor (C-087/C-088 supporting machinery).

Reports repository identity, signing, tier shape, secrets hygiene, and remote
posture. ``--write`` applies only the two deterministic repairs described by
C-087: the fresh-clone allowed-signers rebind and missing secrets-layer ignore
entries. Privileged controls remain instructions for the human operator.

Stdlib-only. Exit 0 = healthy (warnings allowed); exit 1 = at least one error.

Usage:  python3 doctor.py [--write]
"""
import argparse
import collections
import glob
import json
import math
import os
import re
import subprocess
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SECRET_IGNORES = (".env", ".env.*", "secrets/")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(message)
        print("  ERR:", message)

    def warn(self, message):
        self.warnings.append(message)
        print("  WARN:", message)


def git(arguments):
    return subprocess.run(
        ["git", *arguments],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_value(arguments):
    result = git(arguments)
    return result.stdout.strip() if result.returncode == 0 else None


def normalized_config_path(value):
    expanded = os.path.expanduser(value)
    if not os.path.isabs(expanded):
        expanded = os.path.join(REPO, expanded)
    return os.path.realpath(expanded)


def check_identity(report):
    print("1. Git identity")
    for key in ("user.name", "user.email"):
        value = git_value(["config", "--get", key])
        if value:
            print(f"  {key}: {value}")
        else:
            report.warn(f"{key} is unset for this repository")


def check_allowed_signers(report, write):
    print("2. Allowed-signers binding")
    expected = os.path.join(REPO, ".allowed_signers")
    if not os.path.isfile(expected):
        print("  not present")
        return False

    configured = git_value(
        ["config", "--local", "--get", "gpg.ssh.allowedSignersFile"]
    )
    bound = configured is not None and normalized_config_path(configured) == os.path.realpath(expected)
    if bound:
        print(f"  bound: {configured}")
        return True
    if write:
        result = git(
            ["config", "--local", "gpg.ssh.allowedSignersFile", os.path.abspath(expected)]
        )
        if result.returncode:
            report.error("could not write the repo-local allowed-signers binding")
            return True
        print(f"  FIXED: bound to {os.path.abspath(expected)}")
        return True
    detail = "unset" if configured is None else f"points to {configured}"
    report.error(
        f"repo-local gpg.ssh.allowedSignersFile {detail}; expected {os.path.abspath(expected)}"
    )
    return True


def check_signing(report, signing_infra):
    print("3. Signing shape")
    if not signing_infra:
        print("  signing not adopted (tier-1)")
        return
    result = git(["log", "--format=%G?"])
    if result.returncode:
        report.error("git log could not inspect commit signatures")
        return
    counts = collections.Counter(line.strip() for line in result.stdout.splitlines() if line.strip())
    order = ("G", "N", "B", "E", "U", "X", "Y", "R")
    distribution = [f"{status}={counts.get(status, 0)}" for status in order if status in {"G", "N"} or counts.get(status)]
    distribution.extend(
        f"{status}={count}" for status, count in sorted(counts.items()) if status not in order
    )
    print("  distribution: " + (" · ".join(distribution) if distribution else "no commits"))
    for status in ("B", "E", "U"):
        if counts.get(status):
            report.error(f"{counts[status]} commit(s) have signing status {status}")


def check_tier():
    print("4. Tier detection")
    agenda_matches = glob.glob(
        os.path.join(REPO, "Claude", "Context Packages", "*Agenda*Board*")
    )
    components = (
        ("check_versions.py", os.path.isfile(os.path.join(HERE, "check_versions.py"))),
        ("close.py", os.path.isfile(os.path.join(HERE, "close.py"))),
        (
            "Governance Protocol directory",
            os.path.isdir(
                os.path.join(REPO, "Claude", "Project Governance", "Governance Protocol")
            ),
        ),
        ("Agenda Board file", any(os.path.isfile(path) for path in agenda_matches)),
        ("signing infra", os.path.isfile(os.path.join(REPO, ".allowed_signers"))),
    )
    for label, present in components:
        print(f"  {label}: {'present' if present else 'absent'}")


def append_secret_ignores(path, missing):
    existing = ""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as source:
            existing = source.read()
    prefix = "" if not existing or existing.endswith("\n") else "\n"
    if existing and not existing.endswith("\n\n"):
        prefix += "\n"
    addition = "# Secrets layer (C-087)\n" + "\n".join(missing) + "\n"
    with open(path, "a", encoding="utf-8") as target:
        target.write(prefix + addition)


def secret_patterns():
    # Split sentinels so the doctor does not diagnose its own source as a value.
    definitions = (
        ("AWS access key", "AK" + r"IA[A-Z0-9]{16}"),
        ("GitHub classic token", "gh" + r"p_[A-Za-z0-9]{30,}"),
        ("GitHub fine-grained token", "github" + r"_pat_[A-Za-z0-9_]{30,}"),
        ("Slack bot token", "xo" + r"xb-[A-Za-z0-9-]{20,}"),
        ("API secret key", "s" + r"k-[A-Za-z0-9_-]{20,}"),
        ("Google API key", "AI" + r"za[A-Za-z0-9_-]{30,}"),
    )
    return [(label, re.compile(pattern)) for label, pattern in definitions]


PRIVATE_KEY_RE = re.compile(
    r"-----" + r"BEGIN [A-Z0-9 ]*" + r"PRIVATE KEY-----"
)
LONG_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9+/=_-])[A-Za-z0-9+/=_-]{48,}(?![A-Za-z0-9+/=_-])")
HEX64_RE = re.compile(r"^[0-9a-fA-F]{64}$")
INTEGRITY_HASH_RE = re.compile(r"sha(?:1|256|384|512)-[A-Za-z0-9+/=]{20,}")
DATED_IDENTIFIER_RE = re.compile(
    r"[A-Za-z][A-Za-z0-9-]*(?:_[A-Za-z][A-Za-z0-9-]*)*"
    r"_\d{4}-\d{2}-\d{2}"
    r"(?:_[A-Za-z][A-Za-z0-9-]*)*"
)
DOCTOR_ROSTER = os.path.join(HERE, "doctor_roster.json")


def load_cleared_tokens(path=DOCTOR_ROSTER):
    """Per-instance known-innocent declarations — jurisdiction data, not code.
    An absent or unreadable roster contributes nothing: detection never
    narrows by accident."""
    try:
        with open(path, encoding="utf-8") as source:
            data = json.load(source)
    except (OSError, ValueError):
        return frozenset()
    tokens = data.get("cleared_tokens", []) if isinstance(data, dict) else []
    return frozenset(token for token in tokens if isinstance(token, str))


def declared_innocent(value, cleared):
    """Tier 2 of the three-tier secrets lane (the pre-code design, ratified
    2026-08-21): a long token is silenced only when it positively matches a
    declared class — an integrity hash carrying its own sha-N- tag, a dated
    document identifier in the governed filename grammar (C-012), or an
    exact per-instance cleared token. Tier 1 (explicit credential patterns)
    never consults this; everything unmatched falls through to tier 3, the
    entropy heuristic."""
    if INTEGRITY_HASH_RE.fullmatch(value):
        return True
    if DATED_IDENTIFIER_RE.fullmatch(value):
        return True
    return value in cleared


def entropy(value):
    counts = collections.Counter(value)
    size = len(value)
    return -sum((count / size) * math.log2(count / size) for count in counts.values())


def heuristic_secret(line, match):
    value = match.group(0)
    if re.match(r"\.(?:md|py|jsonl|html|docx|txt|json)\b", line[match.end():], re.I):
        return False
    if HEX64_RE.fullmatch(value):
        nearby = line[max(0, match.start() - 40):match.end() + 40]
        if "content_hash" in nearby:
            return False
    if not (re.search(r"[A-Z]", value) and re.search(r"[a-z]", value) and re.search(r"\d", value)):
        return False
    return entropy(value) >= 4.5


def tracked_files(report):
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        report.error("git ls-files could not enumerate tracked files for the secrets scan")
        return []
    return [item.decode("utf-8", "surrogateescape") for item in result.stdout.split(b"\0") if item]


def scan_secrets(report):
    hits = []
    patterns = secret_patterns()
    cleared = load_cleared_tokens()
    for relative in tracked_files(report):
        normalized = relative.replace(os.sep, "/")
        if normalized == ".allowed_signers":
            continue
        if "/_events/" in "/" + normalized and normalized.endswith(".jsonl"):
            continue
        path = os.path.join(REPO, relative)
        if os.path.islink(path) or not os.path.isfile(path):
            continue
        try:
            with open(path, "rb") as source:
                raw = source.read()
        except OSError:
            report.error(f"{normalized}: tracked file could not be read for the secrets scan")
            continue
        if b"\0" in raw:
            continue
        for number, line in enumerate(raw.decode("utf-8", "replace").splitlines(), 1):
            occupied = []
            if PRIVATE_KEY_RE.search(line):
                hits.append((normalized, number, "private-key block"))
            for label, pattern in patterns:
                for match in pattern.finditer(line):
                    hits.append((normalized, number, label))
                    occupied.append(match.span())
            for match in LONG_TOKEN_RE.finditer(line):
                if any(match.start() < end and start < match.end() for start, end in occupied):
                    continue
                if declared_innocent(match.group(0), cleared):
                    continue
                if heuristic_secret(line, match):
                    hits.append((normalized, number, "high-entropy long token"))
    for path, number, kind in hits:
        report.error(f"{path}:{number}: likely secret value ({kind}; value redacted)")
    if not hits:
        print("  tracked-file secrets scan: no likely values found")


def check_secrets(report, write):
    print("5. Secrets guard")
    path = os.path.join(REPO, ".gitignore")
    entries = set()
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as source:
            entries = {
                line.strip() for line in source
                if line.strip() and not line.lstrip().startswith("#")
            }
    missing = [entry for entry in SECRET_IGNORES if entry not in entries]
    if missing and write:
        try:
            append_secret_ignores(path, missing)
            print("  FIXED: appended missing secrets-layer ignore entries")
        except OSError as exc:
            report.error(f"could not update .gitignore: {exc}")
    elif missing:
        report.error(".gitignore is missing: " + ", ".join(missing))
    else:
        print("  .gitignore: secrets-layer entries present")
    scan_secrets(report)


def check_remote():
    print("6. Remote")
    origin = git_value(["remote", "get-url", "origin"])
    print(f"  origin: {origin}" if origin else "  origin: not bound")


def privileged_instructions():
    print("7. Privileged posture")
    print("  FileVault: human — confirm full-disk encryption is enabled in operating-system settings.")
    print("  2FA/passkey: human — confirm privileged accounts use a passkey or phishing-resistant 2FA.")
    print("  Custody key ceremony: human — create, store, and test custody keys outside the repository per the governing ceremony.")


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply deterministic repository fixes")
    return parser.parse_args()


def main():
    args = arguments()
    report = Report()
    print(f"FRACTAL repository doctor — repo: {REPO}")
    check_identity(report)
    signing_infra = check_allowed_signers(report, args.write)
    check_signing(report, signing_infra)
    check_tier()
    check_secrets(report, args.write)
    check_remote()
    privileged_instructions()
    if report.errors:
        print(f"\nFAIL — {len(report.errors)} error(s), {len(report.warnings)} warning(s).")
        raise SystemExit(1)
    print(f"\nPASS — repository posture is healthy ({len(report.warnings)} warning(s)).")


if __name__ == "__main__":
    main()
