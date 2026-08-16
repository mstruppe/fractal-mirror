#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — mint guard (C-050).

Makes local duplicate codes IMPOSSIBLE instead of merely forbidden (C-049
prevention layer), and automates "two writes, one truth" (Schema v0.6 §4.5):
one invocation writes both the mint event line and the node stub.

Stdlib-only. Dry-run by default — nothing is written without --write.

Usage:
  python3 mint.py --list -                      # show all roots (the global namespace, C-044)
  python3 mint.py --list PHY.QM                 # show taken codes under a parent (naming options)
  python3 mint.py <facet-token> <CODE> <LABEL> --actor AGENT.X.Y [options]

  python3 mint.py topic PHY.QM.QFT "Quantum field theory" --actor AGENT.HUMAN.MAX
  python3 mint.py topic PHY "Physics" --actor AGENT.HUMAN.MAX --root "root approved by Max, this conversation"
  ... check the preview, then re-run with --write

Options:
  --actor CODE   committing agent (or env FRACTAL_ACTOR); must be a minted AGENT.* code
  --root TEXT    REQUIRED for a root mint (parent-less code): records whose call it was (C-049)
  --note TEXT    free-text rationale for the event's note field
  --write        actually append the event and create the node stub (default: preview only)

After --write: run `python3 verify.py` and commit per C-037.
Reparents (new code for an EXISTING concept) are not this tool's job — follow
Schema v0.6 §5.3 rule 6 (re-mint same subject + redirect alias, one commit).
"""
import sys, os, json, re, time, datetime

C32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
CODE_RE = re.compile(r"^[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?(\.[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?)*$")
HERE = os.path.dirname(os.path.abspath(__file__))

def die(msg, options=None):
    print(f"REFUSED: {msg}")
    if options:
        print(options)
    sys.exit(1)

def ulid(now_ms):
    import os as _os
    r = int.from_bytes(_os.urandom(10), "big")
    enc = lambda v, n: "".join(C32[(v >> (5*i)) & 31] for i in range(n-1, -1, -1))
    return enc(now_ms, 10) + enc(r, 16)

def load_log(evdir):
    events = []
    for fn in sorted(os.listdir(evdir)):
        if fn.endswith(".jsonl"):
            for line in open(os.path.join(evdir, fn), encoding="utf-8"):
                if line.strip(): events.append(json.loads(line))
    events.sort(key=lambda e: (e["ts"], e["id"]))
    return events

def fold(events):
    minted, routes, agents = {}, {}, set()
    for e in events:
        if e["ev"] == "mint":
            minted.setdefault(e["code"], e)          # first mint wins (C-049)
            if e["code"].startswith("AGENT"): agents.add(e["code"])
        elif e["ev"] == "alias" and e.get("kind") == "route":
            routes[e["alias"]] = e["subject"]
    return minted, routes, agents

def siblings(minted, parent):
    if parent is None:
        return sorted(c for c in minted if "." not in c)
    return sorted(c for c in minted if c.rsplit(".",1)[0] == parent and "." in c)

def main():
    args = sys.argv[1:]
    evdir, nodedir = os.path.join(HERE, "_events"), os.path.join(HERE, "nodes")
    events = load_log(evdir)
    minted, routes, agents = fold(events)

    if "--list" in args:
        parent = args[args.index("--list")+1]
        parent = None if parent == "-" else parent
        taken = siblings(minted, parent)
        scope = "GLOBAL ROOT NAMESPACE (one namespace across ALL facets, C-044)" if parent is None \
                else f"children of {parent}"
        print(f"Taken — {scope}:")
        for c in taken:
            e = minted[c]
            print(f"  {c:30s} {e.get('label','')!r}  (facet {e.get('facet')}, {e['ts']})")
        if not taken: print("  (none)")
        print("Pick any name NOT on this list; codes are immutable and never reused (rule 2).")
        return

    def opt(name, default=None):
        if name in args:
            i = args.index(name); v = args[i+1]; del args[i:i+2]; return v
        return default
    root_note = opt("--root")
    note = opt("--note")
    actor = opt("--actor", os.environ.get("FRACTAL_ACTOR"))
    write = "--write" in args
    if write: args.remove("--write")
    if len(args) != 3:
        print(__doc__); sys.exit(1)
    facet_token, code, label = args

    # ---- validations (the guard) ----
    if facet_token not in routes:
        die(f"unknown facet token {facet_token!r}",
            f"Known tokens: {', '.join(sorted(routes))}\n(a facet token is a route alias over a FACET.* concept, C-043)")
    if not CODE_RE.match(code):
        die(f"code {code!r} violates the code grammar (dotted UPPERCASE segments, Schema §5.2)")
    if not actor:
        die("no actor — pass --actor AGENT.X.Y or set FRACTAL_ACTOR (actor = committing agent, C-040)")
    if actor not in agents:
        die(f"actor {actor!r} is not a minted AGENT code",
            f"Minted agents: {', '.join(sorted(agents))}")
    parent = code.rsplit(".",1)[0] if "." in code else None
    if code in minted:
        e = minted[code]
        die(f"code {code} is TAKEN — minted {e['ts']} for {e['subject']} ({e.get('label','')!r}). "
            f"Codes are immutable and never reused (rule 2).",
            "Free alternatives — currently taken under this parent:\n  " +
            "\n  ".join(siblings(minted, parent)) )
    if parent is None:
        roots = siblings(minted, None)
        if root_note is None:
            die(f"{code} is a ROOT mint — legislation in the one global namespace (C-044/C-049). "
                f"Re-run with --root \"<whose call it was>\" to record the decision.",
                "Existing roots (global, across all facets):\n  " + "\n  ".join(roots))
    else:
        if parent not in minted:
            gp = parent.rsplit(".",1)[0] if "." in parent else None
            die(f"parent {parent} is not minted (mint-before-use, rule 1)",
                f"Taken under {gp or 'the root namespace'}:\n  " + "\n  ".join(siblings(minted, gp)))

    # ---- build the two writes ----
    now = time.time()
    now_s = int(now)
    ts = datetime.datetime.fromtimestamp(now_s, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    top_id = "TOP-" + ulid(now_s * 1000)
    evt_id = "EVT-" + ulid(now_s * 1000)
    event = {"ev": "mint", "id": evt_id, "ts": ts, "actor": actor, "subject": top_id,
             "facet": facet_token, "code": code, "parent": parent, "label": label}
    full_note = " · ".join(x for x in (("root mint: " + root_note) if root_note else None, note) if x)
    if full_note: event["note"] = full_note
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
    node_path = os.path.join(nodedir, f"{top_id}--{slug}.md")
    node = (f"---\nid: {top_id}\ntype: TOP\ncreated: {ts}\ncreated_by: {actor}\n"
            f"code: {code}\ntitle: \"{label}\"\nfacet: {facet_token}\n---\n\n"
            f"Concept node for `{code}` in the **{facet_token}** facet. Parentage is carried by the "
            f"code prefix (C-027); this node stores its own coordinate and needs no self-placement.\n")
    # One append-only log file (C-055, resolving OQ-3): append to the single active partition
    # = the lexically last _events/*.jsonl. New partitions are opened only by the roll ceremony
    # (Schema v0.6 §4.1) when verify.py's volume tripwire fires — never automatically per-writer.
    parts = sorted(f for f in os.listdir(evdir) if f.endswith(".jsonl"))
    bucket = os.path.join(evdir, parts[-1] if parts else "part-0001.jsonl")

    print(("WRITING" if write else "PREVIEW (dry-run — re-run with --write to append)") + ":")
    print(f"  event  -> {os.path.basename(bucket)}: {json.dumps(event, ensure_ascii=False)}")
    print(f"  node   -> nodes/{os.path.basename(node_path)}")
    if write:
        with open(bucket, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
        open(node_path, "w", encoding="utf-8").write(node)
        print("Done. Now run `python3 verify.py` and commit per C-037 (one coherent change-set).")

main()
