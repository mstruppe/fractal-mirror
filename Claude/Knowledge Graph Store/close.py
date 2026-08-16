#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — close-ripple generator.

Finds external canonical DOCs whose bytes have changed, previews their revise
events, and (only with --write) appends those events and synchronizes node
content_hash fields. It can also mint the mechanical store records for a new
canonical DOC, including the C-061 series-pointer ripple when applicable.

Stdlib-only. Dry-run by default — nothing is written without --write.

Usage:
  python3 close.py
  python3 close.py --write --note <id-or-path>="<one-line note>" [...]
  python3 close.py [--write] --create <path> --type DOC --title <title> \
      --alias <Fractal_Name> --topic <CODE> [--actor AGENT.X.Y]

After every --write, verify.py and check_versions.py run automatically.
"""
import argparse, datetime, hashlib, json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
C32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Z]{2,3}-[0-9A-HJKMNP-TV-Z]{26}$")
PATH_RE = re.compile(r"Repo-relative path: `([^`]+)`")
VERSIONED_RE = re.compile(r"^(.+)_v(\d+\.\d+)\.md$")
ALIAS_RE = re.compile(r"^Fractal_[A-Za-z0-9_.]+$")


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
    status = 0
    for script in ("verify.py", "check_versions.py"):
        print(f"\n$ python3 {script}")
        result = subprocess.run(
            [sys.executable, script], cwd=HERE, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.returncode:
            status = 1
    return status


def revise_mode(args, nodes, events, bucket):
    changed = external_docs(nodes)
    notes = parse_notes(args.note)
    recognized = {key for doc in changed for key in (doc["id"], doc["repo_path"])}
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
        return 0

    updates = {doc["file"]: replace_hash(doc, doc["new_hash"]) for doc in changed}
    if revisions:
        append_events(bucket, revisions)
        write_files(updates)
        print(f"Synchronized {len(updates)} node content_hash field(s).")
    else:
        print("Nothing to append or synchronize.")
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
    if not ALIAS_RE.match(args.alias):
        die(f"--alias must be a Fractal_Name machine token, got {args.alias!r}")
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
    return parser.parse_args()


def main():
    args = arguments()
    node_dir, event_dir = os.path.join(HERE, "nodes"), os.path.join(HERE, "_events")
    nodes, events = load_nodes(node_dir), load_events(event_dir)
    bucket = active_partition(event_dir)
    if args.create:
        if args.note:
            die("--note is for changed-document revise mode, not --create")
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
