#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — close-ripple generator.

Finds external canonical DOCs whose bytes have changed, previews their revise
events, and (only with --write) appends those events and synchronizes node
content_hash fields. It can also mint the mechanical store records for a new
canonical DOC, including the C-061 series-pointer ripple when applicable.

Since the C-110/C-112 mechanization it also carries the close's mechanical half:
the dry run (and --walk) pre-fills the C-059 walk table from the hash-diff, flags
the Register as the judgment dirty-bit (C-112), and reads the drag gauge; --stamp
(applied at --write) bumps stale version headers, mints revision-history rows from
each document's --note, and writes store counts at predicted post-ripple totals;
--pack runs the tagging-close gate (clause span, mirror cleanliness, serving-layer
preservation). The judgment half — what a change means, protocol prose,
ratification — stays manual by declared boundary (C-110 proposal 14).

Stdlib-only. Dry-run by default — nothing is written without --write.

Usage:
  python3 close.py [--walk]
  python3 close.py --write [--stamp] [--protocol vX.Y] --note <id-or-path>="<one-line note>" [...]
  python3 close.py [--write] --create <path> --type DOC --title <title> \
      --alias <Fractal_Name> --topic <CODE> [--actor AGENT.X.Y]
  python3 close.py --pack [--mirror <path>] [--mirror-only]

After every --write, verify.py and check_versions.py run automatically.
"""
import argparse, datetime, hashlib, json, os, re, subprocess, sys, time
sys.dont_write_bytecode = True   # the checker import must not litter the store tree

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
C32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Z]{2,3}-[0-9A-HJKMNP-TV-Z]{26}$")
PATH_RE = re.compile(r"Repo-relative path: `([^`]+)`")
VERSIONED_RE = re.compile(r"^(.+)_v(\d+\.\d+)\.md$")
COUNTS_RE = re.compile(r"\b(\d+)\s+nodes\s+/\s+(\d+)\s+events\b")
STAMP_RE = re.compile(r"\*\*Version:\*\*\s*v?(\d+\.\d+)")
# Advisory spine word budgets (C-110 proposal 10, ratified as a standing rule —
# tripwire class, C-055's advisory pattern; initial values the DF1 flight's).
BUDGET_WORDS = {"Local Context": 3500, "Context Index": 2000}
SESSION_ROWS_BUDGET = 40


def die(message):
    print(f"REFUSED: {message}")
    raise SystemExit(1)


def sha256(path):
    with open(path, "rb") as source:
        return "sha256:" + hashlib.sha256(source.read()).hexdigest()


def scalar(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
    return value


def parse_node(path):
    raw = open(path, encoding="utf-8").read()
    if not raw.startswith("---\n"):
        die(f"{os.path.basename(path)} has no front-matter")
    end = raw.find("\n---", 4)
    if end < 0:
        die(f"{os.path.basename(path)} has unterminated front-matter")
    front, body = raw[4:end + 1], raw[end + 4:]
    fields = {}
    for line in front.splitlines():
        match = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = scalar(match.group(2).split(" #", 1)[0])
    path_match = PATH_RE.search(body)
    return {
        "file": path,
        "raw": raw,
        "id": fields.get("id"),
        "type": fields.get("type"),
        "content_hash": fields.get("content_hash"),
        "repo_path": path_match.group(1) if path_match else None,
    }


def load_nodes(node_dir):
    nodes = []
    for name in sorted(os.listdir(node_dir)):
        if name.endswith(".md"):
            nodes.append(parse_node(os.path.join(node_dir, name)))
    return nodes


def load_events(event_dir):
    events = []
    for name in sorted(os.listdir(event_dir)):
        if not name.endswith(".jsonl"):
            continue
        with open(os.path.join(event_dir, name), encoding="utf-8") as source:
            for number, line in enumerate(source, 1):
                if not line.strip():
                    continue
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    die(f"{name}:{number}: invalid JSON: {exc}")
    events.sort(key=lambda event: (event["ts"], event["id"]))
    return events


def repo_file(repo_path):
    if os.path.isabs(repo_path):
        die(f"canonical path must be repo-relative: {repo_path}")
    target = os.path.realpath(os.path.join(REPO, repo_path))
    try:
        inside = os.path.commonpath((os.path.realpath(REPO), target)) == os.path.realpath(REPO)
    except ValueError:
        inside = False
    if not inside:
        die(f"canonical path escapes the repository: {repo_path}")
    if not os.path.isfile(target):
        die(f"external canonical file not found: {repo_path}")
    return target


def external_docs(nodes):
    docs = []
    for node in nodes:
        if node["type"] != "DOC" or not node["repo_path"]:
            continue
        old_hash = node["content_hash"]
        if not HASH_RE.match(old_hash or ""):
            die(f"{os.path.basename(node['file'])}: missing or malformed content_hash")
        new_hash = sha256(repo_file(node["repo_path"]))
        if old_hash != new_hash:
            changed = dict(node)
            changed["new_hash"] = new_hash
            docs.append(changed)
    return docs


def ulid_ms(identifier):
    if not ID_RE.match(identifier or ""):
        return 0
    value = 0
    for character in identifier.split("-", 1)[1][:10]:
        value = value * 32 + C32.index(character)
    return value


def ulid(now_ms):
    random_bits = int.from_bytes(os.urandom(10), "big")
    encode = lambda value, length: "".join(
        C32[(value >> (5 * index)) & 31] for index in range(length - 1, -1, -1)
    )
    return encode(now_ms, 10) + encode(random_bits, 16)


class Clock:
    def __init__(self, events, nodes):
        existing = [ulid_ms(event.get("id")) for event in events]
        existing.extend(ulid_ms(node.get("id")) for node in nodes)
        self.next_ms = max(int(time.time() * 1000), max(existing, default=0) + 1)

    def take(self):
        now_ms = self.next_ms
        self.next_ms += 1
        ts = datetime.datetime.fromtimestamp(
            now_ms / 1000, datetime.timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        return now_ms, ts

    def event_id(self, now_ms):
        return "EVT-" + ulid(now_ms)


def latest_hash_events(events):
    latest = {}
    for event in events:
        if event.get("ev") in {"create", "revise"} and event.get("content_hash"):
            latest[event["subject"]] = event["id"]
    return latest


def fold_namespaces(events):
    minted, routes, aliases = {}, {}, {}
    for event in events:
        if event.get("ev") == "mint":
            minted.setdefault(event["code"], event)
        elif event.get("ev") == "alias":
            aliases.setdefault(event["alias"], set()).add(event["subject"])
            if event.get("kind") == "route":
                routes[event["alias"]] = event["subject"]
    return minted, routes, aliases


def parse_notes(values):
    notes = {}
    for value in values:
        if "=" not in value:
            die(f"--note must be TARGET=NOTE, got {value!r}")
        target, note = value.split("=", 1)
        if not target or not note:
            die(f"--note requires a non-empty target and note: {value!r}")
        if "\n" in note or "\r" in note:
            die(f"--note must be one line for {target!r}")
        if target in notes and notes[target] != note:
            die(f"conflicting notes supplied for {target!r}")
        notes[target] = note
    return notes


def note_for(doc, notes):
    matches = [notes[key] for key in (doc["id"], doc["repo_path"]) if key in notes]
    if len(set(matches)) > 1:
        die(f"conflicting id/path notes supplied for {doc['id']} ({doc['repo_path']})")
    return matches[0] if matches else None


def replace_hash(node, new_hash):
    end = node["raw"].find("\n---", 4)
    front, rest = node["raw"][:end], node["raw"][end:]
    updated, count = re.subn(
        r"(?m)^content_hash:\s*sha256:[0-9a-f]{64}\s*$",
        "content_hash: " + new_hash,
        front,
    )
    if count != 1:
        die(f"{os.path.basename(node['file'])}: expected exactly one content_hash field")
    return updated + rest


def replace_repo_path(raw, old_path, new_path):
    old_line = f"Repo-relative path: `{old_path}`"
    new_line = f"Repo-relative path: `{new_path}`"
    if raw.count(old_line) != 1:
        die(f"series node: expected exactly one Repo-relative path line for {old_path}")
    return raw.replace(old_line, new_line)


def active_partition(event_dir):
    parts = sorted(name for name in os.listdir(event_dir) if name.endswith(".jsonl"))
    return os.path.join(event_dir, parts[-1] if parts else "part-0001.jsonl")


def append_events(bucket, events):
    if os.path.exists(bucket) and os.path.getsize(bucket):
        with open(bucket, "rb") as source:
            source.seek(-1, os.SEEK_END)
            if source.read(1) != b"\n":
                die(f"active partition does not end with a newline: {os.path.basename(bucket)}")
    with open(bucket, "a", encoding="utf-8") as target:
        for event in events:
            target.write(json.dumps(event, ensure_ascii=False) + "\n")


def write_files(updates):
    for path, content in updates.items():
        with open(path, "w", encoding="utf-8") as target:
            target.write(content)


def run_gates():
    """verify + check_versions at every close (C-050/C-060); a working
    change-set carrying a Scan report auto-appends check_scan.py on that
    report (S5-6.2 — the Scan Procedure §12 gate cannot be skipped by
    following the ritual verbatim)."""
    runs = [("verify.py", []), ("check_versions.py", [])]
    if os.path.isfile(os.path.join(HERE, "check_scan.py")):
        for rel in sorted(working_changes() or set()):
            if re.search(r"Review_.+LooseEnds-Scan.*\.md$", os.path.basename(rel)):
                runs.append(("check_scan.py", [os.path.join(REPO, rel)]))
    status = 0
    for script, extra in runs:
        print(f"\n$ python3 {script}" + "".join(" " + a for a in extra))
        result = subprocess.run(
            [sys.executable, script, *extra], cwd=HERE, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.returncode:
            status = 1
    return status


# --------------------------------------------------------- mechanization ----
# The C-110/C-112 layer (Group B tool work + the adaptive close, per Protocol
# v0.49; the C-116 cleanliness amendment per v0.56; the C-120 preservation
# duties per v0.57; TF1-4's prefix cure — this tool work is its named trigger).

def git_out(cwd, *argv):
    try:
        result = subprocess.run(["git", "-C", cwd, *argv], text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    except OSError:
        return None
    return result.stdout if result.returncode == 0 else None


def working_changes():
    """Repo-relative paths differing from HEAD — the close commit's future
    content. None when git is unavailable (signal degrades to the hash-diff)."""
    out = git_out(REPO, "status", "--porcelain", "-z")
    if out is None:
        return None
    paths, entries, index = set(), out.split("\0"), 0
    while index < len(entries):
        entry = entries[index]
        if len(entry) > 3:
            paths.add(entry[3:])
            if entry[0] == "R":     # rename: the original path rides as the next entry
                index += 1
        index += 1
    return paths


def head_text(rel):
    return git_out(REPO, "show", f"HEAD:{rel}")


def corpus_env():
    """check_versions.py is the LIVING/SERIES registry's one home (C-092 —
    adopt, don't fork): import it, instance projection applied. None where the
    checker is absent (an instance that adopted close.py alone, GENESIS §6)."""
    sys.path.insert(0, HERE)
    try:
        import check_versions as checker
    except Exception:
        return None
    finally:
        sys.path.remove(HERE)
    _, living, series, _, _, _ = checker.inherited_registry(HERE)
    return checker, living, series


def instance_alias_prefix():
    """TF1-4's cure: the --create alias grammar follows the instance's own name.
    Mother default: Fractal_. An instance's .version-registry (genesis.py's
    projection) names its documents '<Name>_...' — derive the prefix from its
    Global Context override; an explicit alias_prefix key wins."""
    registry = os.path.join(HERE, ".version-registry")
    if not os.path.isfile(registry):
        return "Fractal_"
    try:
        config = json.loads(open(registry, encoding="utf-8").read())
    except (OSError, json.JSONDecodeError):
        return "Fractal_"
    if config.get("alias_prefix"):
        return config["alias_prefix"]
    spec = config.get("living_overrides", {}).get("Global Context", {})
    for alias in spec.get("aliases", []):
        match = re.match(r"^([A-Za-z0-9]+_)Global_Context$", alias)
        if match:
            return match.group(1)
    return "Fractal_"


def board_paths():
    directory = "User Documents"
    full = os.path.join(REPO, directory)
    if not os.path.isdir(full):
        return []
    return [directory + "/" + name for name in sorted(os.listdir(full))
            if name.endswith("_Agenda_Board.html")]


def store_tool_paths():
    directory = "Claude/Knowledge Graph Store"
    return [directory + "/" + name
            for name in sorted(os.listdir(os.path.join(REPO, directory)))
            if name.endswith(".py") or name == "README.md"]


def newest_series_path(checker, series, key):
    spec = series.get(key)
    if not spec:
        return None
    directory = os.path.join(REPO, spec["dir"])
    best = None
    for name in sorted(os.listdir(directory)) if os.path.isdir(directory) else []:
        match = re.match(re.escape(spec["stem"]) + r"_v(\d+\.\d+)\.md$", name)
        if match and (best is None or checker.vkey(match.group(1)) > checker.vkey(best[0])):
            best = (match.group(1), spec["dir"] + "/" + name)
    return best[1] if best else None


def walk_rows(living):
    """The walk table's rows, read from their normative home — the Local
    Context §Standing refresh items (C-059). The row set is maintained in the
    document; this tool only fills the marks."""
    path = os.path.join(REPO, living["Local Context"]["path"])
    if not os.path.isfile(path):
        return []
    text = open(path, encoding="utf-8").read()
    section = re.search(r"^## Standing refresh items.*?$(.*?)(?=^## |\Z)",
                        text, re.M | re.S)
    if not section:
        return []
    rows = []
    for line in section.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cell = line.strip("|").split("|", 1)[0].strip()
        if not cell or cell == "Living projection" or set(cell) <= {"-", " "}:
            continue
        rows.append(cell)
    return rows


def row_paths(row, living, series, checker):
    plain = row.replace("**", "").lower()
    def lp(name):
        return [living[name]["path"]] if name in living else []
    mapping = [
        ("decision register", lambda: lp("Decision Register")),
        ("rule overview", lambda: lp("Rule Overview")),
        ("local context", lambda: lp("Local Context")),
        ("agenda board", board_paths),
        ("context index", lambda: lp("Context Index")),
        ("global context", lambda: lp("Global Context")),
        ("architecture state", lambda: lp("Architecture State")),
        ("bootstrap", lambda: lp("BOOTSTRAP")),
        ("schema", lambda: [p for p in (newest_series_path(checker, series, "schema"),
                                        newest_series_path(checker, series, "template")) if p]),
        ("store tools", store_tool_paths),
        ("conversation settings", lambda: lp("Conversation Settings")),
        ("adapters", lambda: lp("Claude Code Adapter") + lp("Codex Adapter")),
    ]
    for token, resolve in mapping:
        if token in plain:
            return resolve()
    return None


def drag_gauge(living, moment=" at close-open"):
    # The read point is named in the header (S5-5.3): close-open figures
    # understate the committed file by one close's ripple; --stamp --write
    # re-emits post-ripple, and THOSE are the figures a record should carry.
    print(f"\nDrag gauge{moment} (C-110 proposals 9-10 — advisory, never blocking):")
    for name in sorted(living):
        rel = living[name]["path"]
        full = os.path.join(REPO, rel)
        if not os.path.isfile(full):
            continue
        words = len(open(full, encoding="utf-8").read().split())
        head = head_text(rel)
        delta = words - len(head.split()) if head is not None else 0
        line = f"  {name}: {words} words"
        if delta:
            line += f" ({'+' if delta > 0 else ''}{delta} vs HEAD)"
        budget = BUDGET_WORDS.get(name)
        if budget and words > budget:
            line += (f"  YELLOW — over the C-110 budget ({budget}); "
                     "a C-095 compaction is due at the next phase boundary")
        print(line)
    lc = os.path.join(REPO, living["Local Context"]["path"])
    if os.path.isfile(lc):
        section = re.search(r"^## Session record.*?$(.*?)(?=^## |\Z)",
                            open(lc, encoding="utf-8").read(), re.M | re.S)
        if section:
            rows = max(0, len([l for l in section.group(1).splitlines()
                               if l.startswith("|")]) - 2)
            line = f"  Local Context session table: {rows} rows"
            if rows > SESSION_ROWS_BUDGET:
                line += (f"  YELLOW — over the {SESSION_ROWS_BUDGET}-row budget; "
                         "era rows collapse at a phase boundary (C-110 Group C)")
            print(line)


def fieldnote_pressure():
    # The C-121 pressure plug's close-walk surfacing: relay fieldnote.py's
    # depth reading (the single implementation — Format v0.2 §4). Advisory,
    # never blocking; soft-silent where the tool or buffer is absent
    # (a newborn adopts the buffer at genesis, an old instance on migration).
    tool = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fieldnote.py")
    if not os.path.isfile(tool):
        return
    try:
        result = subprocess.run([sys.executable, tool, "--depth"],
                                capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return
    if result.returncode == 0 and result.stdout.strip():
        print(f"\nFieldnote buffer (C-121 pressure plug — advisory, never blocking):")
        print(f"  {result.stdout.strip()}")


def walk_view(nodes, env=None):
    """The adaptive close's read half (C-112): pre-fill + dirty-flag + gauge."""
    env = env or corpus_env()
    if env is None:
        print("\nAdaptive-close view unavailable — check_versions.py "
              "not found beside this tool.")
        return
    checker, living, series = env
    git_changed = working_changes()
    changed = (git_changed or set()) | {d["repo_path"] for d in external_docs(nodes)}
    print("\nC-059 walk pre-fill (C-110 proposal 8 / C-112 — marks are the "
          "mechanical half; judgment on CHANGED rows stays manual):")
    if git_changed is None:
        print("  (git unavailable — change signal is the store hash-diff alone)")
    for row in walk_rows(living) or ["(no walk table found in the Local Context)"]:
        paths = row_paths(row, living, series, checker)
        label = row if len(row) <= 48 else row[:45] + "..."
        if paths is None:
            print(f"  {label}: (no mapping — judge by hand)")
        else:
            hits = sorted(p for p in paths if p in changed)
            if hits:
                print(f"  {label}: CHANGED — " +
                      ", ".join(os.path.basename(h) for h in hits))
            else:
                print(f"  {label}: checked — unchanged")
    register = living.get("Decision Register", {}).get("path")
    print("\nJudgment dirty-flag (C-112 — the Register):")
    if register and register in changed:
        print("  Register CHANGED — decision-shaped session: a Governance "
              "Protocol is due and the judgment walk runs in full.")
    else:
        print("  Register unchanged — the judgment half is trivially clear; "
              "the C-059 recorded-reason line this tool offers:")
        print('    "No Governance Protocol issued — the Decision Register did '
              'not move this session (C-112; execution only)."')
    drag_gauge(living)
    fieldnote_pressure()


def history_kind(text):
    if re.search(r"^\|\s*Version\s*\|\s*Date\s*\|", text, re.M):
        return "table"
    if re.search(r"\*\*Revision history:?\*\*", text):
        return "prose"
    return None


def insert_history(text, version, date, note, ofrecord):
    """Mint one revision-history row in the document's own format (C-110
    proposal 6). Table = the Register's | Version | Date | Headline | Of record |;
    prose = the '**Revision history:** ... · vX.Y (date) ...' run. Documents
    with no history block (the diet's compactions) return unchanged."""
    note = note.replace("|", "/").strip()
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if re.match(r"^\|\s*Version\s*\|\s*Date\s*\|", line):
            if len([c for c in line.strip().strip("|").split("|")]) != 4:
                return text, None       # unfamiliar table shape — leave to the hand
            end = index + 1
            while end < len(lines) and lines[end].lstrip().startswith("|"):
                end += 1
            lines.insert(end, f"| v{version} | {date} | {note} | {ofrecord} |\n")
            return "".join(lines), "table"
    match = re.search(r"\*\*Revision history:?\*\*", text)
    if match:
        end = text.find("\n\n", match.end())
        if end < 0:
            end = len(text)
        entry = f" · v{version} ({date}) {note}"
        if not entry.endswith("."):
            entry += "."
        return text[:end].rstrip() + entry + text[end:], "prose"
    return text, None


def bump_minor(version):
    major, minor = version.split(".")
    return f"{major}.{int(minor) + 1}"


def bump_stamp(text, new_version, date):
    text, count = re.subn(r"(\*\*Version:\*\*\s*v?)\d+\.\d+",
                          r"\g<1>" + new_version, text, count=1)
    if count != 1:
        die("stamp bump found no **Version:** field")
    text, _ = re.subn(r"(\*\*Updated:\*\*\s*)\d{4}-\d{2}-\d{2}",
                      r"\g<1>" + date, text, count=1)
    return text


def stamp_plan(env, changed, nodes, events, notes, args):
    """Plan the mechanical prose edits (C-110 proposals 6-7): stamp bumps for
    byte-changed living documents whose header still carries HEAD's version,
    minted history rows carrying each document's --note, and store-count
    refresh to the predicted post-ripple totals — written BEFORE hashing, so
    the recorded hash covers the final bytes (the counts-last lag's cure)."""
    checker, living, series = env
    today = datetime.date.today().isoformat()
    doc_paths = {n["repo_path"] for n in nodes if n["type"] == "DOC" and n["repo_path"]}
    changed_paths = {d["repo_path"] for d in changed}
    # Living projections without DOC nodes (Local Context, Board — derived,
    # deliberately outside the canonical corpus) still restamp at every close:
    # bump eligibility takes the union signal, revise events stay hash-diff-only.
    edited_paths = changed_paths | (working_changes() or set())
    by_path = {d["repo_path"]: d for d in changed}
    living_by_path = {spec["path"]: name for name, spec in living.items()}
    count_scope = sorted({spec["path"] for spec in living.values()} | set(board_paths()))

    n_nodes = len(nodes)
    final_changed = set(changed_paths)
    stale = set()
    for _ in range(4):      # fixpoint: count edits may dirty a DOC, adding a revise
        pred_events = len(events) + len(final_changed & doc_paths)
        stale = set()
        for rel in count_scope:
            full = os.path.join(REPO, rel)
            if not os.path.isfile(full):
                continue
            for m in COUNTS_RE.finditer(open(full, encoding="utf-8").read()):
                if (int(m.group(1)), int(m.group(2))) != (n_nodes, pred_events):
                    stale.add(rel)
                    break
        if final_changed == changed_paths | (stale & doc_paths):
            break
        final_changed = changed_paths | (stale & doc_paths)
    pred_events = len(events) + len(final_changed & doc_paths)

    files, preview, auto_notes, ids = {}, [], {}, {}
    for rel in sorted(final_changed | stale | (edited_paths & set(living_by_path))):
        operations = []
        if rel in by_path:
            ids[rel] = by_path[rel]["id"]
        if living_by_path.get(rel) and rel in edited_paths:
            text = open(os.path.join(REPO, rel), encoding="utf-8").read()
            current = STAMP_RE.search(text)
            head = head_text(rel)
            head_stamp = STAMP_RE.search(head) if head is not None else None
            if current and head_stamp and current.group(1) == head_stamp.group(1):
                new_version = bump_minor(current.group(1))
                operations.append(("bump", new_version))
                preview.append(f"  {rel}: stamp v{current.group(1)} -> v{new_version}, "
                               f"Updated -> {today} (annotation text kept — review by hand)")
                if history_kind(text):
                    operations.append(("history", new_version))
                    preview.append(f"  {rel}: revision-history {history_kind(text)} row "
                                   f"minted from its --note (v{new_version}, {today})")
            elif current and head_stamp:
                preview.append(f"  {rel}: stamp already moved by hand "
                               f"(v{head_stamp.group(1)} -> v{current.group(1)}) — "
                               "bump and history row left to the hand")
        if rel in stale:
            operations.append(("counts",))
            preview.append(f"  {rel}: store counts -> {n_nodes} nodes / "
                           f"{pred_events} events (predicted post-ripple)")
            if rel not in changed_paths and rel in doc_paths:
                auto_notes[rel] = ("mechanical ripple: store counts refreshed "
                                   "to post-ripple totals (C-110)")
        if operations:
            files[rel] = operations
    return {"files": files, "preview": preview, "auto_notes": auto_notes,
            "ids": ids, "totals": (n_nodes, pred_events), "today": today,
            "ofrecord": args.protocol or "(this close)"}


def apply_stamp(plan, notes):
    for rel, operations in plan["files"].items():
        full = os.path.join(REPO, rel)
        text = open(full, encoding="utf-8").read()
        for op in operations:
            if op[0] == "bump":
                text = bump_stamp(text, op[1], plan["today"])
            elif op[0] == "history":
                note = notes.get(rel) or notes.get(plan["ids"].get(rel)) \
                    or plan["auto_notes"].get(rel)
                if note:
                    text = insert_history(text, op[1], plan["today"],
                                          note, plan["ofrecord"])[0]
            elif op[0] == "counts":
                text = COUNTS_RE.sub(
                    f"{plan['totals'][0]} nodes / {plan['totals'][1]} events", text)
        with open(full, "w", encoding="utf-8") as target:
            target.write(text)


def pack_mode(args):
    """The tagging-close gate (--pack) — the checks owed once per release:
    the Migration Procedure's clause-span rule (C-117 §7.3), the mirror's
    post-rebuild cleanliness (the C-116 amendment, per v0.56), and the
    serving-layer preservation duties (C-120). Red block: exit 1 on failure."""
    failures = []
    scope = "mirror half only (S5-6.1 post-rebuild re-run)" if args.mirror_only \
        else "C-117 §7.3 · C-116 cleanliness · C-120 preservation"
    print(f"Pack-time gate ({scope}):")

    if not args.mirror_only:
        genesis = os.path.join(REPO, "GENESIS.md")
        env = corpus_env()
        register_rel = env[1].get("Decision Register", {}).get("path") if env else None
        if not os.path.isfile(genesis):
            failures.append("GENESIS.md not found — the clause-span check needs it")
        elif not register_rel or not os.path.isfile(os.path.join(REPO, register_rel)):
            failures.append("Decision Register not found — the clause-span check needs it")
        else:
            genesis_text = open(genesis, encoding="utf-8").read()
            clause = re.search(r"decisions C-001[–-]C-(\d+)", genesis_text)
            numbers = re.findall(r"\bC-(\d{3})\b",
                                 open(os.path.join(REPO, register_rel), encoding="utf-8").read())
            register_max = max(int(n) for n in numbers) if numbers else 0
            if not clause:
                failures.append("GENESIS §3.4: inheritance clause span not readable "
                                "(expected 'decisions C-001–C-NNN')")
            elif int(clause.group(1)) != register_max:
                failures.append(f"GENESIS §3.4 clause spans C-001–C-{clause.group(1)} but the "
                                f"Register runs to C-{register_max:03d} — reissue the clause "
                                "before tagging (Migration Procedure §7.3)")
            else:
                print(f"  clause-span: OK — GENESIS §3.4 and the Register agree at "
                      f"C-{register_max:03d}")
            zero = re.search(r"(\d+) at this writing", genesis_text)
            if not zero:
                failures.append("GENESIS §0: the 'N at this writing' count not readable "
                                "(S5-7.2 — the gate covers §0 alongside the clause)")
            elif register_max and int(zero.group(1)) != register_max:
                failures.append(f"GENESIS §0 counts {zero.group(1)} decisions but the "
                                f"Register runs to C-{register_max:03d} — cure §0 with "
                                "the clause reissue (S5-7.2; the CAP1-PROD-1/TF1-11 class)")
            elif register_max:
                print(f"  §0 count: OK — GENESIS §0 and the Register agree at {register_max}")

    mirror = os.path.expanduser(args.mirror)
    if not os.path.isdir(os.path.join(mirror, ".git")):
        failures.append(f"mirror not found at {mirror} — pass --mirror "
                        "(the C-116/C-120 checks run there)")
    else:
        porcelain = git_out(mirror, "status", "--porcelain")
        if porcelain is None:
            failures.append("mirror: git status failed")
        elif porcelain.strip():
            failures.append(f"mirror working tree not clean post-rebuild "
                            f"({len(porcelain.splitlines())} entries — C-116 "
                            "cleanliness check, per v0.56)")
        else:
            print("  mirror cleanliness: OK — working tree clean")
        tracked = (git_out(mirror, "ls-files") or "").splitlines()
        duplicates = [f for f in tracked
                      if re.search(r" \d+\.[A-Za-z0-9]+$", os.path.basename(f))
                      or "conflicted copy" in f.lower()
                      or re.search(r" \(\d+\)\.", f)]
        if duplicates:
            failures.append(f"mirror carries {len(duplicates)} duplicate-pattern file(s) "
                            "(the iCloud-conflict class): "
                            + ", ".join(duplicates[:5])
                            + ("..." if len(duplicates) > 5 else ""))
        else:
            print("  mirror duplicates: OK — no conflict-pattern names among tracked files")
        if any(f.startswith(".github/") for f in tracked):
            print("  mirror intake layer: OK — .github/ tracked")
        else:
            failures.append("mirror: .github/ intake layer missing from the tracked "
                            "tree (C-120 preservation)")
        gh_pages = git_out(mirror, "show-ref", "--verify", "refs/heads/gh-pages") \
            or git_out(mirror, "show-ref", "--verify", "refs/remotes/origin/gh-pages")
        if not gh_pages:
            failures.append("mirror: no gh-pages ref — the serving branch (C-120)")
        else:
            print("  mirror gh-pages: OK — serving branch present")
            cname = git_out(mirror, "show", "gh-pages:CNAME") \
                or git_out(mirror, "show", "origin/gh-pages:CNAME")
            if cname and cname.strip():
                print(f"  mirror CNAME: OK — {cname.strip()}")
            else:
                print("  mirror CNAME: none on gh-pages (informational — the gate "
                      "repo carries the domain; pull-before-push still applies)")

    if failures:
        print(f"\nFAIL — {len(failures)} pack-time failure(s). "
              "Cure before tagging (C-090/C-116/C-120).")
        for message in failures:
            print("  ERR:", message)
        return 1
    print("\nPASS — the pack-time gate is green. Safe to tag (C-090).")
    return 0


def revise_mode(args, nodes, events, bucket):
    changed = external_docs(nodes)
    notes = parse_notes(args.note)

    env, plan = None, None
    if args.stamp:
        env = corpus_env()
        if env is None:
            die("--stamp needs check_versions.py beside this tool "
                "(the registry's one home)")
        plan = stamp_plan(env, changed, nodes, events, notes, args)
        print(("Applying" if args.write else "Would apply")
              + " the --stamp pass (C-110 proposals 6-7):")
        for line in plan["preview"]:
            print(line)
        if not plan["preview"]:
            print("  (nothing to stamp)")
        print(f"  predicted post-ripple store totals: {plan['totals'][0]} nodes / "
              f"{plan['totals'][1]} events")
        if args.write and plan["files"]:
            # Notes are validated BEFORE any byte moves — a refused run must
            # leave the tree untouched (C-008's spirit at the file layer).
            missing = [f"{doc['id']} ({doc['repo_path']})" for doc in changed
                       if not note_for(doc, notes)]
            if missing:
                print("REFUSED: missing --note for changed document(s):")
                for item in missing:
                    print("  " + item)
                return 1
            apply_stamp(plan, notes)
            nodes = load_nodes(os.path.join(HERE, "nodes"))
            changed = external_docs(nodes)     # re-hash: the stamp edits are in
            for rel, note in plan["auto_notes"].items():
                notes.setdefault(rel, note)

    recognized = {key for doc in changed for key in (doc["id"], doc["repo_path"])}
    if plan:
        recognized |= set(plan["files"])       # notes may feed stamp-plan rows too
    unused = sorted(set(notes) - recognized)
    if unused:
        die("note target(s) match no changed document: " + ", ".join(unused))

    print(f"Changed documents ({len(changed)}):")
    for doc in changed:
        print(f"  {doc['id']}  {doc['repo_path']}")
        print(f"    {doc['content_hash']} -> {doc['new_hash']}")
    if not changed:
        print("  (none)")

    missing = [f"{doc['id']} ({doc['repo_path']})" for doc in changed if not note_for(doc, notes)]
    if args.write and missing:
        print("REFUSED: missing --note for changed document(s):")
        for item in missing:
            print("  " + item)
        return 1

    latest = latest_hash_events(events)
    clock = Clock(events, nodes)
    revisions = []
    for doc in changed:
        if doc["id"] not in latest:
            die(f"{doc['id']} has no create/revise event carrying content_hash")
        now_ms, ts = clock.take()
        revisions.append({
            "ev": "revise", "id": clock.event_id(now_ms), "ts": ts,
            "actor": args.actor, "subject": doc["id"],
            "content_hash": doc["new_hash"], "supersedes": latest[doc["id"]],
            "note": note_for(doc, notes) or "<required with --write>",
        })

    action = "Appending" if args.write else "Would append"
    print(f"{action} revise events ({len(revisions)}) to _events/{os.path.basename(bucket)}:")
    for event in revisions:
        print("  " + json.dumps(event, ensure_ascii=False))
    if not args.write:
        if args.stamp:
            print("  (revise hashes above are pre-stamp bytes — "
                  "--write re-hashes after the stamp pass)")
        walk_view(nodes, env)      # the adaptive close's read half (C-112)
        return 0

    updates = {doc["file"]: replace_hash(doc, doc["new_hash"]) for doc in changed}
    if revisions:
        append_events(bucket, revisions)
        write_files(updates)
        print(f"Synchronized {len(updates)} node content_hash field(s).")
    else:
        print("Nothing to append or synchronize.")
    if args.stamp and env is not None:
        drag_gauge(env[1], " post-ripple (S5-5.3 — record these figures)")
    return run_gates()


def series_pointer(create_path, alias, nodes, aliases):
    name = os.path.basename(create_path)
    match = VERSIONED_RE.match(name)
    if not match:
        return None
    series_name = match.group(1)
    if alias != name[:-3]:
        die(f"versioned --alias must match the filename stem exactly: {name[:-3]}")
    directory = os.path.dirname(create_path)
    version_path_re = re.compile(r"^" + re.escape(series_name) + r"_v\d+\.\d+\.md$")
    related = [
        node for node in nodes
        if node["repo_path"]
        and os.path.dirname(node["repo_path"]) == directory
        and version_path_re.match(os.path.basename(node["repo_path"]))
    ]
    if not related:
        return None
    subjects = aliases.get(series_name, set())
    candidates = [node for node in related if node["id"] in subjects]
    if len(candidates) > 1:
        die(
            f"existing versioned series {series_name} has {len(candidates)} identifiable "
            "series pointers; expected at most one"
        )
    # Zero pointers is a legitimate class: the protocol series is per-version
    # only (C-061 kept series pointers for the specs) — nothing to revise.
    return candidates[0] if candidates else None


def node_stub(doc_id, ts, actor, content_hash, title, alias, topic, repo_path):
    return (
        f"---\nid: {doc_id}\ntype: DOC\ncreated: {ts}\ncreated_by: {actor}\n"
        f"content_hash: {content_hash}\ntitle: {json.dumps(title, ensure_ascii=False)}\n"
        f"aliases: [{json.dumps('route:' + alias, ensure_ascii=False)}]\nplacements:\n"
        f"  - {{facet: topic, code: {topic}, role: about, weight: 1.0}}\n"
        f"  - {{facet: agent, code: {actor}, role: by, weight: 1.0}}\n---\n\n"
        f"DOC node for the canonical document **{alias}** (C-041 identity bridge).\n\n"
        f"Repo-relative path: `{repo_path}`\n"
        "`content_hash` = sha256 of that file's committed bytes at minting (Schema v0.6 §3.7). "
        "The\n`placements:`/`aliases:` blocks are a materialized fold of the log — the log is "
        "canonical (C-024).\n"
    )


def create_mode(args, nodes, events, bucket):
    if args.type != "DOC" or not args.title or not args.alias or not args.topic:
        die("--create requires --type DOC, --title, --alias, and --topic")
    for label, value in (("title", args.title), ("alias", args.alias)):
        if "\n" in value or "\r" in value:
            die(f"--{label} must be one line")
    if '"' in args.title:
        die('--title cannot contain a double quote (node front-matter parser limitation)')
    prefix = instance_alias_prefix()      # TF1-4: instance-derived, mother default Fractal_
    if not re.match(r"^" + re.escape(prefix) + r"[A-Za-z0-9_.]+$", args.alias):
        die(f"--alias must be a {prefix}Name machine token, got {args.alias!r}")
    create_path = os.path.normpath(args.create).replace(os.sep, "/")
    target = repo_file(create_path)
    if any(node["repo_path"] == create_path for node in nodes):
        die(f"canonical path already has a DOC node: {create_path}")

    minted, routes, aliases = fold_namespaces(events)
    if args.actor not in minted or not args.actor.startswith("AGENT"):
        die(f"actor {args.actor!r} is not a minted AGENT code")
    if args.topic not in minted:
        die(f"topic code {args.topic!r} is not minted")
    if "topic" not in routes or "agent" not in routes:
        die("topic and agent facet route tokens must both exist")
    if args.alias in routes:
        die(f"route alias is already bound: {args.alias}")

    pointer = series_pointer(create_path, args.alias, nodes, aliases)
    latest = latest_hash_events(events)
    if pointer and pointer["id"] not in latest:
        die(f"series pointer {pointer['id']} has no hash-bearing create/revise event")

    content_hash = sha256(target)
    clock = Clock(events, nodes)
    create_ms, create_ts = clock.take()
    doc_id = "DOC-" + ulid(create_ms)
    create_event = {
        "ev": "create", "id": clock.event_id(create_ms), "ts": create_ts,
        "actor": args.actor, "subject": doc_id, "type": "DOC",
        "content_hash": content_hash, "title": args.title,
    }
    events_to_add = [create_event]
    now_ms, ts = clock.take()
    events_to_add.append({
        "ev": "alias", "id": clock.event_id(now_ms), "ts": ts,
        "actor": args.actor, "subject": doc_id, "alias": args.alias, "kind": "route",
    })
    for facet, code, role in (
        ("topic", args.topic, "about"), ("agent", args.actor, "by")
    ):
        now_ms, ts = clock.take()
        events_to_add.append({
            "ev": "place", "id": clock.event_id(now_ms), "ts": ts,
            "actor": args.actor, "subject": doc_id, "facet": facet,
            "code": code, "role": role, "weight": 1.0,
        })
    if pointer:
        now_ms, ts = clock.take()
        events_to_add.append({
            "ev": "revise", "id": clock.event_id(now_ms), "ts": ts,
            "actor": args.actor, "subject": pointer["id"],
            "content_hash": content_hash, "supersedes": latest[pointer["id"]],
            "note": f"series pointer advanced to {args.alias}",
        })

    slug = re.sub(r"[^a-z0-9]+", "-", args.alias.lower()).strip("-")
    node_path = os.path.join(HERE, "nodes", f"{doc_id}--{slug}.md")
    stub = node_stub(
        doc_id, create_ts, args.actor, content_hash, args.title,
        args.alias, args.topic, create_path,
    )
    updates = {node_path: stub}
    if pointer:
        revised_pointer = replace_hash(pointer, content_hash)
        revised_pointer = replace_repo_path(revised_pointer, pointer["repo_path"], create_path)
        updates[pointer["file"]] = revised_pointer

    action = "WRITING" if args.write else "PREVIEW (dry-run — ids below are ILLUSTRATIVE and are regenerated at --write; re-run with --write)"
    print(action + ":")
    for event in events_to_add:
        print(f"  event -> _events/{os.path.basename(bucket)}: " + json.dumps(event, ensure_ascii=False))
    print(f"  node  -> nodes/{os.path.basename(node_path)}")
    if pointer:
        print(f"  series pointer -> {pointer['id']}: {pointer['repo_path']} -> {create_path}")
    if not args.write:
        return 0

    append_events(bucket, events_to_add)
    write_files(updates)
    print(f"Appended {len(events_to_add)} event(s) and synchronized {len(updates)} node file(s).")
    status = run_gates()
    # Printed last, after the gates, so the minted identity is the final line on screen —
    # the dry-run preview shows different, illustrative ids (they are regenerated here).
    print(f"MINTED: {events_to_add[0]['subject']}  (alias {args.alias}) — stamp THIS id into the document")
    return status


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="append events and update node files")
    parser.add_argument("--note", action="append", default=[], metavar="TARGET=NOTE")
    parser.add_argument("--actor", default="AGENT.AI.CLAUDE")
    parser.add_argument("--create", metavar="PATH")
    parser.add_argument("--type", choices=("DOC",))
    parser.add_argument("--title")
    parser.add_argument("--alias")
    parser.add_argument("--topic")
    parser.add_argument("--stamp", action="store_true",
                        help="mechanical prose pass at --write: stamp bumps, history rows, post-ripple counts (C-110)")
    parser.add_argument("--protocol", metavar="vX.Y",
                        help="of-record pointer for minted history rows (e.g. 'Protocol v0.58')")
    parser.add_argument("--walk", action="store_true",
                        help="print only the adaptive-close view: walk pre-fill, Register flag, drag gauge (C-112)")
    parser.add_argument("--pack", action="store_true",
                        help="run the tagging-close gate: clause span, mirror cleanliness, preservation (C-117/C-116/C-120)")
    parser.add_argument("--mirror", default="~/Desktop/fractal-mirror",
                        help="the public mirror's working copy for --pack (default: ~/Desktop/fractal-mirror)")
    parser.add_argument("--mirror-only", action="store_true",
                        help="with --pack: run only the mirror half — the cheap post-rebuild re-run "
                             "before the mirror tag (S5-6.1; the C-116 check must see the NEW rebuild)")
    return parser.parse_args()


def main():
    args = arguments()
    if args.mirror_only and not args.pack:
        die("--mirror-only accompanies --pack")
    if args.pack:
        if any((args.create, args.note, args.stamp, args.walk, args.write)):
            die("--pack runs alone (the tagging-close gate)")
        raise SystemExit(pack_mode(args))
    node_dir, event_dir = os.path.join(HERE, "nodes"), os.path.join(HERE, "_events")
    nodes, events = load_nodes(node_dir), load_events(event_dir)
    bucket = active_partition(event_dir)
    if args.walk:
        if any((args.create, args.note, args.stamp, args.write)):
            die("--walk is a read-only view and runs alone")
        walk_view(nodes)
        raise SystemExit(0)
    if args.create:
        if args.note:
            die("--note is for changed-document revise mode, not --create")
        if args.stamp:
            die("--stamp is for changed-document revise mode, not --create")
        status = create_mode(args, nodes, events, bucket)
    else:
        if any((args.type, args.title, args.alias, args.topic)):
            die("--type, --title, --alias, and --topic require --create")
        minted, _, _ = fold_namespaces(events)
        if args.actor not in minted or not args.actor.startswith("AGENT"):
            die(f"actor {args.actor!r} is not a minted AGENT code")
        status = revise_mode(args, nodes, events, bucket)
    raise SystemExit(status)


if __name__ == "__main__":
    main()
