#!/usr/bin/env python3
"""FRACTAL fieldnote tool — capture, depth, and intake for field observations (C-094, C-121).

The machine half of /fieldnote. v0.2 (the RAM redesign, C-121): the fieldnote
is temporary memory — ONE buffer per instance, no routing at capture, worked
off soon. Solving dissolves an entry into the project (a decision, a document
update, a transfer) and deletes it whole from the buffer; the citation plus
git history is the trace. Ids never rewind (the header's high-water line).

CAPTURE — appends one content-immutable machine-format block (Fractal
Fieldnote Format v0.2: six keys, no target) to the buffer named in the config.
The raw report lands verbatim; the derived reading and categorisation proposal
are judgment-layer, written by the AI surface AFTER the user's ratification
(the write gate is conduct — Format §5; this tool is only the writer).

DEPTH — the pressure plug (C-121): depth = surviving blocks + unchecked
`- [ ]` work-down rows; over the header's budget line → YELLOW advisory.
Warning, never a gate: a full buffer still captures.

PARSE — the intake half: validate files and emit entries as JSON,
whole-or-nothing. Accepts BOTH grammars — v0.2 six-key blocks and v0.1
seven-key blocks (frozen ledgers, v0.1-kernel children) — emitting `target`
only where a block carried it.

Config authority lives in `fieldnote_roster.json` beside this tool (historic
filename kept; v0.2 shape): {"instance": "<Name>", "buffer": "<path>"}.

Usage:
  python3 fieldnote.py <report text ...>            append a capture block
  python3 fieldnote.py --kind friction <text ...>   capture with a stated kind
  python3 fieldnote.py --depth                      print depth vs budget, write nothing
  python3 fieldnote.py parse <file> [<file> ...]    validate + emit entries as JSON

Where this tool and Fractal_Fieldnote_Format_v0.2.md disagree, the document
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
CONFIG_FILE = HERE / "fieldnote_roster.json"

KINDS_STATABLE = ("friction", "green", "vision", "question", "capture")
ID_RE = re.compile(r"^FN-(\d{4})$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{4}$")
KEY_ORDER = ("id", "ts", "author", "instance", "kind", "report")          # v0.2
V01_KEY_ORDER = ("id", "ts", "author", "instance", "target", "kind", "report")
FENCE_OPEN = "```fieldnote"
FENCE_CLOSE = "```"
BUDGET_RE = re.compile(r"^\*\*Budget:\*\* (\d+) entries", re.M)
HIGHWATER_RE = re.compile(r"^\*\*Id high-water:\*\* FN-(\d{4})", re.M)
OPEN_ROW_RE = re.compile(r"^- \[ \]", re.M)


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    print("Nothing was written.", file=sys.stderr)
    sys.exit(1)


def load_config() -> dict:
    if not CONFIG_FILE.is_file():
        die(f"config file not found: {CONFIG_FILE.name} (expected beside this tool)")
    try:
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        die(f"config file unreadable: {exc}")
    if isinstance(config, dict) and "targets" in config:
        die(
            "config carries the retired v0.1 target roster — the v0.2 shape is "
            '{"instance": "<Name>", "buffer": "<path>"} (Format v0.2 §6; '
            "migration: the lanes freeze, one buffer replaces them)"
        )
    if (
        not isinstance(config, dict)
        or not isinstance(config.get("instance"), str)
        or not config["instance"]
        or not isinstance(config.get("buffer"), str)
        or not config["buffer"]
    ):
        die('config file must be {"instance": "<Name>", "buffer": "<path>"}')
    return config


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


def block_ids(text: str):
    numbers = []
    for block, _ in iter_blocks(text.splitlines()):
        for line in block:
            match = re.fullmatch(r"id: FN-(\d{4})", line)
            if match:
                numbers.append(int(match.group(1)))
    return numbers


def buffer_state(text: str):
    """(depth, budget, high_water) — the §4 machine facts."""
    depth = len(block_ids(text)) + len(OPEN_ROW_RE.findall(text))
    budget_match = BUDGET_RE.search(text)
    budget = int(budget_match.group(1)) if budget_match else None
    hw_match = HIGHWATER_RE.search(text)
    high_water = int(hw_match.group(1)) if hw_match else None
    return depth, budget, high_water


def pressure_line(depth: int, budget) -> str:
    line = f"buffer depth: {depth}/{budget if budget is not None else '—'}"
    if budget is not None and depth > budget:
        line += ("  YELLOW — over the budget (C-121 pressure plug, advisory): "
                 "work the buffer down soon (solve = dissolve into the project, Format v0.2 §4)")
    return line


def resolve_buffer(config) -> Path:
    buffer = REPO / config["buffer"]
    if not buffer.is_file():
        die(f"config is stale — buffer not found: {buffer}")
    return buffer


def depth_view() -> None:
    config = load_config()
    text = resolve_buffer(config).read_text(encoding="utf-8")
    depth, budget, _ = buffer_state(text)
    print(f"{config['instance']} · {config['buffer']} · {pressure_line(depth, budget)}")


def capture(argv) -> None:
    kind = "capture"
    if argv and argv[0] == "--kind":
        if len(argv) < 2:
            die("--kind requires a value")
        kind = argv[1].lower()
        if kind not in KINDS_STATABLE:
            die(f"--kind must be one of: {', '.join(KINDS_STATABLE)}")
        argv = argv[2:]

    config = load_config()
    buffer = resolve_buffer(config)
    text = buffer.read_text(encoding="utf-8")

    report = " ".join(argv).strip()
    if not report:
        die("no report text given — nothing to capture")
    report_lines = report.splitlines() or [""]
    for line in report_lines:
        if line.lstrip().startswith("```"):
            die("report may not contain a code fence line (it cannot round-trip the block format)")

    depth, budget, high_water = buffer_state(text)
    if high_water is None:
        die(
            "buffer header lacks the Id high-water line "
            "(`**Id high-water:** FN-NNNN`) — ids must never rewind past "
            "deletions (Format v0.2 §2 rule 3); restore the line before capturing"
        )
    n = max([high_water] + block_ids(text)) + 1

    stamp = datetime.datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    body = "\n".join(("  " + line).rstrip() if line.strip() else "" for line in report_lines)
    block = (
        f"\n{FENCE_OPEN}\n"
        f"id: FN-{n:04d}\n"
        f"ts: {stamp}\n"
        f"author: {git_identity()}\n"
        f"instance: {config['instance']}\n"
        f"kind: {kind}\n"
        "report:\n"
        f"{body}\n"
        f"{FENCE_CLOSE}\n"
    )
    text = HIGHWATER_RE.sub(f"**Id high-water:** FN-{n:04d}", text, count=1)
    buffer.write_text(text.rstrip("\n") + "\n" + block, encoding="utf-8")
    print(f"captured: FN-{n:04d} -> {config['buffer']} (block is the fact layer; "
          f"the ratified derived reading goes beneath it) · {pressure_line(depth + 1, budget)}")


def parse_block(lines, start, file_label, errors):
    def err(msg):
        errors.append(f"{file_label}:{start}: {msg}")

    # Grammar sniff (Format v0.2 §3): position five decides — `target:` = v0.1.
    v01 = len(lines) > 4 and lines[4].startswith("target: ")
    key_order = V01_KEY_ORDER if v01 else KEY_ORDER

    fields = {}
    index = 0
    for key in key_order[:-1]:  # all simple keys, in fixed order
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
        err("expected bare `report:` line after the value keys")
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
    fields["_keys"] = ("file",) + key_order
    return fields


def parse(paths) -> None:
    if not paths:
        die("parse requires at least one buffer/ledger file")
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
    ordered = [{key: entry[key] for key in entry["_keys"]} for entry in entries]
    print(json.dumps(ordered, ensure_ascii=False, indent=2))
    print(f"intake OK: {len(ordered)} entr{'y' if len(ordered) == 1 else 'ies'} from {len(paths)} file(s)", file=sys.stderr)


def main() -> None:
    argv = sys.argv[1:]
    if argv and argv[0] == "--depth":
        depth_view()
        return
    if argv and argv[0] == "parse":
        parse(argv[1:])
        return
    capture(argv)


if __name__ == "__main__":
    main()
