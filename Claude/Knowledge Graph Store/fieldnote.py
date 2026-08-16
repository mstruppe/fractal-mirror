#!/usr/bin/env python3
"""FRACTAL fieldnote tool — capture and intake for field observations (C-094).

The machine half of /fieldnote, graduated beside the store tools when the
friends-beta added the intake half (fieldnotes entry 39; the graduation
trigger recorded in the tool's first home, Site/fieldnote.py).

CAPTURE — deterministic routing and attribution (Max's ruling of record,
2026-08-16): the target is a fact, not an interpretation. A missing or
unknown target is a hard error and NOTHING is written. A valid capture
appends one immutable machine-format block (Fractal Fieldnote Format v0.1)
to the resolved ledger; everything judgmental (titles, cures, implications)
stays outside the block, on the AI/human side (the C-073 split).

PARSE — the intake half: validate ledger files against the format and emit
the entries as JSON. Whole-or-nothing: any invalid block fails the intake
loudly with no partial output.

Roster authority lives in `fieldnote_roster.json` beside this tool — a
machine-read fact, not an interpretation; command-file tables are
projections of it. The roster also declares this instance's name.

Usage:
  python3 fieldnote.py <target> <report text ...>        append a capture block
  python3 fieldnote.py --kind friction <target> <text>   capture with a stated kind
  python3 fieldnote.py --resolve <target>                print route + next id, write nothing
  python3 fieldnote.py --list                            print the roster, write nothing
  python3 fieldnote.py parse <file> [<file> ...]         validate + emit entries as JSON

Where this tool and Fractal_Fieldnote_Format_v0.1.md disagree, the document
wins (the S4-2.1 rule).
"""
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROSTER_FILE = HERE / "fieldnote_roster.json"

KINDS_STATABLE = ("friction", "green", "vision", "question", "capture")
ID_RE = re.compile(r"^FN-(\d{4})$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{4}$")
KEY_ORDER = ("id", "ts", "author", "instance", "target", "kind", "report")
FENCE_OPEN = "```fieldnote"
FENCE_CLOSE = "```"


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    print("Nothing was written.", file=sys.stderr)
    sys.exit(1)


def load_roster() -> dict:
    if not ROSTER_FILE.is_file():
        die(f"roster file not found: {ROSTER_FILE.name} (expected beside this tool)")
    try:
        roster = json.loads(ROSTER_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        die(f"roster file unreadable: {exc}")
    if (
        not isinstance(roster, dict)
        or not isinstance(roster.get("instance"), str)
        or not roster["instance"]
        or not isinstance(roster.get("targets"), dict)
        or not roster["targets"]
        or not all(
            isinstance(k, str) and k and isinstance(v, str) and v
            for k, v in roster["targets"].items()
        )
    ):
        die('roster file must be {"instance": "<Name>", "targets": {"<word>": "<ledger path>", ...}}')
    return roster


def print_targets(roster: dict, stream) -> None:
    print(f"Instance: {roster['instance']} · registered targets:", file=stream)
    for word, ledger in roster["targets"].items():
        print(f"  {word:8} -> {ledger}", file=stream)


def git_identity() -> str:
    def config(key: str) -> str:
        try:
            result = subprocess.run(
                ["git", "config", key],
                cwd=REPO,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
            )
        except OSError:
            die("git is required for capture attribution but could not be run")
        value = result.stdout.strip()
        if result.returncode or not value:
            die(
                f"`git config {key}` is unset — capture attribution is a machine "
                f"fact and cannot be invented (set it with `git config {key} ...`)"
            )
        return value

    return f"{config('user.name')} <{config('user.email')}>"


def next_id(text: str) -> int:
    numbers = []
    for block, _ in iter_blocks(text.splitlines()):
        for line in block:
            match = re.fullmatch(r"id: FN-(\d{4})", line)
            if match:
                numbers.append(int(match.group(1)))
    return (max(numbers) + 1) if numbers else 1


def iter_blocks(lines):
    """Yield (block_lines, opening_line_number) for every fieldnote fence."""
    block, start = None, None
    for number, line in enumerate(lines, 1):
        if block is None:
            if line == FENCE_OPEN:
                block, start = [], number
        elif line == FENCE_CLOSE:
            yield block, start
            block, start = None, None
        else:
            block.append(line)


def capture(argv) -> None:
    kind = "capture"
    if argv and argv[0] == "--kind":
        if len(argv) < 2:
            die("--kind requires a value")
        kind = argv[1].lower()
        if kind not in KINDS_STATABLE:
            die(f"--kind must be one of: {', '.join(KINDS_STATABLE)}")
        argv = argv[2:]
    resolve_only = bool(argv) and argv[0] == "--resolve"
    if resolve_only:
        argv = argv[1:]

    roster = load_roster()
    if not argv:
        print("ERROR: no target given — /fieldnote requires a target as its first word", file=sys.stderr)
        print_targets(roster, sys.stderr)
        print("Nothing was written.", file=sys.stderr)
        sys.exit(1)
    target = argv[0].lower()
    if target not in roster["targets"]:
        print(f"ERROR: unknown target {target!r}", file=sys.stderr)
        print_targets(roster, sys.stderr)
        print("Nothing was written.", file=sys.stderr)
        sys.exit(1)
    ledger_rel = roster["targets"][target]
    ledger = REPO / ledger_rel
    if not ledger.is_file():
        die(f"roster is stale — ledger not found: {ledger}")

    text = ledger.read_text(encoding="utf-8")
    n = next_id(text)
    if resolve_only:
        print(f"target '{target}' -> {ledger_rel} · next id: FN-{n:04d}")
        return

    report = " ".join(argv[1:]).strip()
    if not report:
        die("no report text given — nothing to capture")
    report_lines = report.splitlines() or [""]
    for line in report_lines:
        if line.lstrip().startswith("```"):
            die("report may not contain a code fence line (it cannot round-trip the block format)")

    stamp = datetime.datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    body = "\n".join(("  " + line).rstrip() if line.strip() else "" for line in report_lines)
    block = (
        f"\n{FENCE_OPEN}\n"
        f"id: FN-{n:04d}\n"
        f"ts: {stamp}\n"
        f"author: {git_identity()}\n"
        f"instance: {roster['instance']}\n"
        f"target: {target}\n"
        f"kind: {kind}\n"
        "report:\n"
        f"{body}\n"
        f"{FENCE_CLOSE}\n"
    )
    ledger.write_text(text.rstrip("\n") + "\n" + block, encoding="utf-8")
    print(f"captured: FN-{n:04d} -> {ledger_rel} (immutable machine block; judgment layer is yours, outside it)")


def parse_block(lines, start, file_label, errors):
    def err(msg):
        errors.append(f"{file_label}:{start}: {msg}")

    fields = {}
    index = 0
    for key in KEY_ORDER[:-1]:  # all simple keys, in fixed order
        if index >= len(lines):
            err(f"missing key {key!r}")
            return None
        line = lines[index]
        prefix = f"{key}: "
        if not line.startswith(prefix) or not line[len(prefix):]:
            err(f"expected `{key}: <value>` at block line {index + 1}, got {line!r}")
            return None
        fields[key] = line[len(prefix):]
        index += 1
    if index >= len(lines) or lines[index] != "report:":
        err("expected bare `report:` line after the six value keys")
        return None
    index += 1
    report_lines = []
    for line in lines[index:]:
        if line == "":
            report_lines.append("")
        elif line.startswith("  "):
            report_lines.append(line[2:])
        else:
            err(f"report line not indented by two spaces: {line!r}")
            return None
    while report_lines and report_lines[-1] == "":
        report_lines.pop()
    if not report_lines:
        err("empty report")
        return None

    if not ID_RE.fullmatch(fields["id"]):
        err(f"id {fields['id']!r} is not FN-NNNN")
        return None
    if not TS_RE.fullmatch(fields["ts"]):
        err(f"ts {fields['ts']!r} is not ISO-8601 local time with numeric offset")
        return None
    try:
        datetime.datetime.strptime(fields["ts"], "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        err(f"ts {fields['ts']!r} does not parse as a real timestamp")
        return None
    if not re.fullmatch(r"[^<>]+ <[^<>@ ]+@[^<>@ ]+>", fields["author"]):
        err(f"author {fields['author']!r} is not `Name <email>`")
        return None
    fields["report"] = "\n".join(report_lines)
    fields["file"] = file_label
    return fields


def parse(paths) -> None:
    if not paths:
        die("parse requires at least one ledger file")
    entries = []
    errors = []
    for raw in paths:
        path = Path(raw)
        if not path.is_file():
            errors.append(f"{raw}: not a file")
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{raw}: unreadable: {exc}")
            continue
        in_file = []
        for block, start in iter_blocks(lines):
            entry = parse_block(block, start, str(path), errors)
            if entry:
                in_file.append((start, entry))
        numbers = [int(entry["id"][3:]) for _, entry in in_file]
        if len(set(numbers)) != len(numbers):
            errors.append(f"{raw}: duplicate ids: sequence {['FN-%04d' % n for n in numbers]}")
        elif numbers != sorted(numbers):
            errors.append(f"{raw}: ids not ascending: sequence {['FN-%04d' % n for n in numbers]}")
        entries.extend(entry for _, entry in in_file)
    if errors:
        for line in errors:
            print(f"INVALID: {line}", file=sys.stderr)
        print(f"intake FAILED: {len(errors)} error(s); no JSON emitted (whole-or-nothing)", file=sys.stderr)
        sys.exit(1)
    ordered = [{key: entry[key] for key in ("file",) + KEY_ORDER} for entry in entries]
    print(json.dumps(ordered, ensure_ascii=False, indent=2))
    print(f"intake OK: {len(ordered)} entr{'y' if len(ordered) == 1 else 'ies'} from {len(paths)} file(s)", file=sys.stderr)


def main() -> None:
    argv = sys.argv[1:]
    if argv and argv[0] == "--list":
        print_targets(load_roster(), sys.stdout)
        return
    if argv and argv[0] == "parse":
        parse(argv[1:])
        return
    capture(argv)


if __name__ == "__main__":
    main()
