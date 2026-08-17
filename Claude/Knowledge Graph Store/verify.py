#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — fold verifier (C-050).

THE RITUAL (Schema v0.6 §5.5): this script must run and PASS before every
store-touching commit and after every merge that touches the store (the C-037
commit boundary). Git merges JSONL appends textually; the semantic merge check
is this script, never git.

Stdlib-only (zero infrastructure, C-021). Read-only: never writes to the store.

Checks, over the full store:
  A. Log integrity   — every line parses; verbs & required fields; ULID coherence
                       (id prefix decodes into the recorded ts/created second);
                       event-id uniqueness; ts ordering; the C-055 volume tripwire
                       (advisory WARN when a partition exceeds 50,000 events —
                       time for the roll ceremony, Schema v0.6 §4.1).
  B. Mint grammar    — code shape; parent = code prefix; mint-before-use; sibling
                       uniqueness; GLOBAL ROOT UNIQUENESS (C-044); the COLLISION
                       TRIPWIRE with first-mint-wins / cured discrimination (C-049);
                       post-pin root mints must carry a note naming whose call.
  C. References      — placement targets exist; roles & weights; alias kinds;
                       route-token uniqueness; redirect wiring (C-045); revise chains.
  D. Fold vs nodes   — every node file matches the fold of the log for its id:
                       identity fields, TOP code/facet, title (newest-label rule,
                       C-045 grandfather), aliases, placements (redirect-resolved),
                       content_hash chain. Log <-> nodes bijection.
  E. Hashes          — store-node body hashes recompute; external canonical-file
                       hashes recompute against the repo (Schema v0.6 §3.7).

Instance vocabulary: an optional vocabulary_local.json beside the store extends
the placement-role set governedly (each role names its adopting decision — see
Fractal_Vocabulary_Extension_Procedure v0.1; roles only, the interchange layer
stays frozen). Absent file = inherited vocabulary exactly.

Usage:  python3 verify.py [<store-dir>] [<repo-root>]
        Defaults: store-dir = this script's directory; repo-root = two levels up.
Exit 0 = PASS (warnings allowed) · exit 1 = FAIL (at least one error).

On a COLLISION error (two mints of one code, different subjects): the earlier
mint holds the code (C-049 first-mint-wins). Cure in the next commit, append-only:
re-mint the losing subject under a fresh code (note citing the collision and the
winning event id), then re-point the placements that intended the losing concept
(unplace + place) — this script lists every placement against the contested code.
"""
import sys, os, json, re, hashlib, datetime

C32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
ULID_RE = re.compile(r"^[0-9A-HJKMNP-TV-Z]{26}$")
CODE_RE = re.compile(r"^[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?(\.[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?)*$")
ID_RE = re.compile(r"^[A-Z]{2,3}-[0-9A-HJKMNP-TV-Z]{26}$")
ROLES = {"about","in","cites","by","member-of","is-a","derived-from"}
VERBS = {"create","place","unplace","mint","alias","revise","run"}
KINDS = {"label","route","redirect"}
COMMON = ("ev","id","ts","actor","subject")
# C-045: newest-label fold rule applies from v0.3 forward; earlier labels grandfathered.
GRANDFATHER_TS = "2026-08-13T00:00:00Z"
# Bootstrap batch: actor semantics pinned later (C-040) — created_by drift is a warning there.
BOOTSTRAP_END = "2026-08-12T18:56:59Z"
# C-049 pin: root mints at/after this instant must carry a note naming whose call it was.
C049_PIN = "2026-08-13T12:00:00Z"

errors, warns, infos = [], [], []
err, warn, info = errors.append, warns.append, infos.append

def ulid_sec(u):
    v = 0
    for ch in u[:10]: v = v*32 + C32.index(ch)
    return v // 1000

def check_coherence(eid, ts, what):
    u = eid.split("-",1)[1]
    if not ULID_RE.match(u): err(f"{what} {eid}: not a 26-char Crockford ULID"); return
    want = int(datetime.datetime.strptime(ts,"%Y-%m-%dT%H:%M:%SZ")
               .replace(tzinfo=datetime.timezone.utc).timestamp())
    if ulid_sec(u) != want:
        err(f"{what} {eid}: ULID prefix decodes to {ulid_sec(u)}, recorded ts/created says {want} ({ts})")

def parse_scalar(v):
    v = v.strip()
    if v in ("~","null",""): return None
    if v.startswith('"') and v.endswith('"'): return v[1:-1]
    return v

def parse_node(path):
    raw = open(path, encoding="utf-8").read()
    if not raw.startswith("---\n"): err(f"{os.path.basename(path)}: no front-matter"); return None
    end = raw.find("\n---", 4)
    fm, body = raw[4:end+1], raw[end+4:]
    if body.startswith("\n"): body = body[1:]
    d = {"placements": [], "aliases": [], "_body": body}
    cur = None
    for line in fm.splitlines():
        if not line.strip() or line.strip().startswith("#"): continue
        s = line.strip()
        if s.startswith("- ") and cur == "placements":
            inner = s[2:].strip()
            if inner.startswith("{") and inner.endswith("}"):
                p = {}
                for part in inner[1:-1].split(","):
                    k, v = part.split(":", 1)
                    p[k.strip()] = parse_scalar(v)
                if p.get("weight") is not None: p["weight"] = float(p["weight"])
                d["placements"].append(p)
            else: err(f"{os.path.basename(path)}: unparsed placement line: {s}")
        elif re.match(r"^[A-Za-z_]+:", s):
            k, v = s.split(":", 1)
            k = k.strip(); v = v.split(" #")[0].strip()
            if k == "placements" and v == "": cur = "placements"
            elif k == "aliases":
                cur = None
                if v.startswith("["):
                    d["aliases"] = [] if v == "[]" else [parse_scalar(x) for x in v[1:-1].split(",")]
            else:
                cur = None
                d[k] = parse_scalar(v)
    return d

ROLE_TOKEN_RE = re.compile(r"^[a-z][a-z0-9-]*[a-z0-9]$")

def load_local_vocabulary(store):
    """Instance vocabulary extension (Fractal_Vocabulary_Extension_Procedure v0.1, RF1-2).

    An instance may extend the placement-role vocabulary without forking this
    checker: vocabulary_local.json beside the store, {"roles": {"<token>":
    "<adopting decision + one-line meaning>"}}. Every role must name the
    decision that adopted it — vocabulary never grows silently. Roles only:
    verbs and alias kinds are interchange-layer and stay frozen (§1 of the
    procedure). Absent file = inherited vocabulary exactly.
    """
    path = os.path.join(store, "vocabulary_local.json")
    if not os.path.exists(path): return
    try:
        vl = json.load(open(path, encoding="utf-8"))
    except Exception as ex:
        err(f"vocabulary_local.json: unreadable ({ex})"); return
    extra = vl.get("roles")
    if not isinstance(extra, dict):
        err("vocabulary_local.json: 'roles' must be a map of token -> adopting-decision rationale"); return
    added = []
    for tok, ref in sorted(extra.items()):
        if not ROLE_TOKEN_RE.match(tok):
            err(f"vocabulary_local.json: role {tok!r} is not a lowercase-hyphen token")
        elif tok in ROLES:
            err(f"vocabulary_local.json: role {tok!r} collides with an inherited role (extension, never redefinition)")
        elif not (isinstance(ref, str) and ref.strip()):
            err(f"vocabulary_local.json: role {tok!r} carries no adopting decision ref (the gate: no silent vocabulary growth)")
        else:
            ROLES.add(tok); added.append(tok)
    if added:
        info(f"local vocabulary: {len(added)} role(s) adopted by recorded decision — {', '.join(added)}")

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    store = sys.argv[1] if len(sys.argv) > 1 else here
    repo = sys.argv[2] if len(sys.argv) > 2 else os.path.normpath(os.path.join(store, "..", ".."))
    evdir, nodedir = os.path.join(store,"_events"), os.path.join(store,"nodes")
    load_local_vocabulary(store)

    # ---------- A. log integrity ----------
    events, seen_ids, per_file = [], set(), {}
    for fn in sorted(os.listdir(evdir)):
        if not fn.endswith(".jsonl"): continue
        for n, line in enumerate(open(os.path.join(evdir,fn), encoding="utf-8"), 1):
            if not line.strip(): continue
            try: e = json.loads(line)
            except Exception as ex: err(f"{fn}:{n}: JSON parse failure: {ex}"); continue
            e["_where"] = f"{fn}:{n}"
            for f in COMMON:
                if f not in e: err(f"{fn}:{n}: missing required field '{f}'")
            if e.get("ev") not in VERBS: err(f"{fn}:{n}: unknown verb {e.get('ev')!r}")
            if e.get("id") in seen_ids: err(f"{fn}:{n}: duplicate event id {e['id']}")
            seen_ids.add(e.get("id"))
            if ID_RE.match(e.get("id","")) and e["id"].startswith("EVT-"):
                check_coherence(e["id"], e["ts"], "event")
            else: err(f"{fn}:{n}: event id {e.get('id')!r} is not EVT-<ULID>")
            events.append(e)
            per_file[fn] = per_file.get(fn, 0) + 1
    events.sort(key=lambda e: (e["ts"], e["id"]))   # C-049: fold order = ts, ULID tie-break

    # C-055 volume tripwire (OQ-3 resolution): the log is ONE append-only file; a partition
    # this large calls for the roll ceremony — a deliberate, recorded commit on MERGED state
    # that closes the active file and opens the next (part-NNNN.jsonl). Advisory, never fatal.
    TRIPWIRE_EVENTS = 50000
    for fn, cnt in sorted(per_file.items()):
        if cnt > TRIPWIRE_EVENTS:
            warn(f"{fn}: {cnt} events exceeds the {TRIPWIRE_EVENTS}-event tripwire (C-055) — "
                 f"schedule the roll ceremony (close this partition, open the next in one "
                 f"recorded commit on merged state; append-only, the closed file never changes)")

    # ---------- B+C. replay (the fold) ----------
    minted, node_state, routes, subjects_born = {}, {}, {}, {}
    collisions = []   # (code, winner_subject, loser_subject, where)
    def state(sid): return node_state.setdefault(sid, {"aliases":[],"placements":{},"codes":[],
                        "title":None,"hash":None,"created":None})
    for e in events:
        w, ev, sid = e["_where"], e["ev"], e.get("subject","")
        if ev == "mint":
            code, parent, facet = e.get("code"), e.get("parent"), e.get("facet")
            if not code or not CODE_RE.match(code): err(f"{w}: bad code shape {code!r}"); continue
            expect_parent = code.rsplit(".",1)[0] if "." in code else None
            if parent != expect_parent: err(f"{w}: parent {parent!r} does not match code prefix of {code}")
            if parent is not None and parent not in minted:
                err(f"{w}: parent {parent} minted nowhere before {code}")
            if parent is None and e["ts"] >= C049_PIN and not e.get("note"):
                err(f"{w}: ROOT MINT WITHOUT RECORDED CALL — {code} (C-049: post-pin root mints "
                    f"carry a note naming whose decision it was; use mint.py --root)")
            if code in minted:
                prev = minted[code]
                if prev["subject"] != sid:
                    collisions.append((code, prev["subject"], sid, w))
                    # first mint wins (C-049): the code stays bound to prev; this mint does not bind,
                    # but the losing subject's mint list records it (cure discrimination below).
                else: warn(f"{w}: duplicate mint of {code} for same subject")
            else:
                minted[code] = {"subject": sid, "ts": e["ts"], "where": w, "facet": facet}
            st = state(sid); st["codes"].append(code); st["facet"] = facet
            if st["created"] is None:
                st.update(created=e["ts"], created_by=e["actor"], type=sid.split("-")[0])
                if e.get("label"): st["title"] = st["title"] or e["label"]
            subjects_born.setdefault(sid, w)
        elif ev == "create":
            if sid in subjects_born: err(f"{w}: {sid} created twice")
            subjects_born[sid] = w
            st = state(sid)
            st.update(created=e["ts"], created_by=e["actor"], type=e.get("type"))
            if e.get("title"): st["title"] = e["title"]
            if e.get("content_hash"): st["hash"], st["hash_ev"] = e["content_hash"], e["id"]
            if e.get("type") != sid.split("-")[0]: err(f"{w}: create type {e.get('type')} != id prefix of {sid}")
            if sid.split("-")[0] != "EVT": check_coherence(sid, e["ts"], "node")
        elif ev == "place":
            if sid not in subjects_born: err(f"{w}: place for unborn subject {sid}")
            code, facet, role, wt = e.get("code"), e.get("facet"), e.get("role"), e.get("weight",1.0)
            if role not in ROLES: err(f"{w}: unregistered role {role!r}")
            if not (isinstance(wt,(int,float)) and 0 <= wt <= 1): err(f"{w}: weight {wt!r} outside [0,1]")
            if ID_RE.match(code or ""):
                if facet: err(f"{w}: entity-target placement must omit facet")
                if code not in subjects_born: err(f"{w}: entity target {code} does not exist")
            else:
                if code not in minted: err(f"{w}: placement against unminted code {code}")
                elif minted[code]["ts"] > e["ts"]: err(f"{w}: placement before mint of {code}")
            state(sid)["placements"][(facet, code, role)] = wt
        elif ev == "unplace":
            key = (e.get("facet"), e.get("code"), e.get("role"))
            if key not in state(sid)["placements"]: err(f"{w}: unplace of absent placement {key}")
            else: del state(sid)["placements"][key]
        elif ev == "alias":
            al, kind = e.get("alias"), e.get("kind")
            if kind not in KINDS: err(f"{w}: unknown alias kind {kind!r}")
            if sid not in subjects_born: err(f"{w}: alias on unborn subject {sid}")
            if kind == "route":
                if al in routes and routes[al] != sid:
                    err(f"{w}: ROUTE COLLISION — token {al!r} bound to {routes[al]} and {sid}")
                routes[al] = sid
            if kind == "redirect":
                if al not in minted: err(f"{w}: redirect names never-minted code {al}")
                elif minted[al]["subject"] != sid: err(f"{w}: redirect on {al} whose subject differs")
            st = state(sid); st["aliases"].append((kind, al, e["ts"]))
            if kind == "label" and e["ts"] >= GRANDFATHER_TS: st["title"] = al
        elif ev == "revise":
            if sid not in subjects_born: err(f"{w}: revise of unborn subject {sid}")
            sup = e.get("supersedes")
            if not sup or sup not in seen_ids: err(f"{w}: revise.supersedes {sup!r} is not a known event id")
            h = e.get("content_hash","")
            if not re.match(r"^sha256:[0-9a-f]{64}$", h): err(f"{w}: malformed content_hash {h!r}")
            st = state(sid)
            if st.get("hash_ev") and sup != st["hash_ev"]:
                err(f"{w}: revise chain break — supersedes {sup}, expected {st['hash_ev']}")
            st["hash"], st["hash_ev"] = h, e["id"]
        elif ev == "run":
            for x in e.get("inputs",[]) + e.get("outputs",[]):
                if x not in subjects_born: err(f"{w}: run references unknown entity {x}")

    # collision verdicts (C-049): cured iff the losing subject's newest code moved off the contested one
    for code, winner, loser, w in collisions:
        cured = node_state.get(loser,{}).get("codes",[])[-1:] != [code]
        if cured:
            warn(f"{w}: cured collision on {code} — first mint ({winner}) holds it; "
                 f"{loser} re-minted at {node_state[loser]['codes'][-1]}")
        else:
            placed = [f"{ev2['_where']} ({ev2['subject']})" for ev2 in events
                      if ev2["ev"] == "place" and ev2.get("code") == code]
            err(f"{w}: CODE COLLISION on {code} — first mint wins: {winner} holds it (C-049); "
                f"CURE REQUIRED: re-mint {loser} under a fresh code, then re-point its intended "
                f"placements. All placements against {code}: {placed or 'none'}")

    agent_codes = {c for c in minted if c.startswith("AGENT")}
    for e in events:
        if e.get("actor") not in agent_codes:
            err(f"{e['_where']}: actor {e.get('actor')!r} is not a minted AGENT code")

    facet_tokens = {t for t,s in routes.items()
                    if any(c == "FACET" or c.startswith("FACET.") for c in node_state.get(s,{}).get("codes",[]))}
    used_tokens = {e.get("facet") for e in events if e.get("facet")} - {None}
    for t in sorted(used_tokens - facet_tokens):
        err(f"facet token {t!r} used in events but resolves to no FACET.* concept")

    def canonical(code):
        seen = set()
        while code in minted and code not in seen:
            seen.add(code)
            cur = node_state[minted[code]["subject"]]["codes"][-1]
            if cur == code: return code
            code = cur
        return code

    roots = sorted(c for c in minted if "." not in c)
    info(f"{len(events)} events · {len(subjects_born)} entities · {len(minted)} codes · "
         f"roots: {', '.join(roots)} · {len(routes)} route tokens · "
         f"{sum(1 for e in events if e['ev']=='alias' and e.get('kind')=='redirect')} redirects · "
         f"{len(collisions)} collision(s) in history")

    # ---------- D. fold vs node files ----------
    by_id = {}
    for f in sorted(x for x in os.listdir(nodedir) if x.endswith(".md")):
        node = parse_node(os.path.join(nodedir, f))
        if not node: continue
        nid = node.get("id")
        fid = f.split("--")[0].replace(".md","")
        if nid != fid: err(f"{f}: filename id {fid} != front-matter id {nid}")
        if nid in by_id: err(f"{f}: duplicate node id {nid}")
        by_id[nid] = (f, node)
        check_coherence(nid, node.get("created",""), "node")
    log_ids = {s for s in subjects_born if not s.startswith("EVT-")}
    for missing in sorted(log_ids - set(by_id)): err(f"log entity {missing} has no node file")
    for extra in sorted(set(by_id) - log_ids): err(f"node file {by_id[extra][0]} has no birth event in the log")

    for nid,(f,node) in sorted(by_id.items()):
        st = node_state.get(nid)
        if not st: continue
        if node.get("type") != nid.split("-")[0]: err(f"{f}: type != id prefix")
        if node.get("created") != st["created"]: err(f"{f}: created {node.get('created')} != log {st['created']}")
        if node.get("created_by") != st.get("created_by"):
            (warn if (st["created"] or "9") <= BOOTSTRAP_END else err)(
                f"{f}: created_by {node.get('created_by')} != birthing actor {st.get('created_by')}"
                + (" (bootstrap batch, pre-C-040 pin)" if (st["created"] or "9") <= BOOTSTRAP_END else ""))
        if nid.startswith("TOP-"):
            if node.get("code") != (st["codes"][-1] if st["codes"] else None):
                err(f"{f}: code {node.get('code')} != newest mint {st['codes'][-1:]}")
            if node.get("facet") != st.get("facet"): err(f"{f}: facet {node.get('facet')} != mint facet {st.get('facet')}")
        if st.get("title") and node.get("title") != st["title"]:
            err(f"{f}: title {node.get('title')!r} != fold title {st['title']!r}")
        # materialization convention: label aliases are bare; route/redirect carry a kind prefix
        want_aliases = {a if k == "label" else f"{k}:{a}" for (k,a,_) in st["aliases"]}
        have_aliases = set(node.get("aliases") or [])
        if want_aliases != have_aliases:
            err(f"{f}: aliases {sorted(have_aliases)} != fold {sorted(want_aliases)}")
        want_pl = {(fc, canonical(c) if not ID_RE.match(c or "") else c, r): wt
                   for (fc,c,r),wt in st["placements"].items()}
        have_pl = {(p.get("facet"), p.get("code"), p.get("role")): p.get("weight",1.0)
                   for p in node["placements"]}
        if want_pl != have_pl:
            err(f"{f}: placements differ\n    node: {sorted(have_pl.items())}\n    fold: {sorted(want_pl.items())}")
        if st.get("hash") and node.get("content_hash") != st["hash"]:
            err(f"{f}: content_hash != newest revise/create hash in log")

        # ---------- E. hash recompute ----------
        if node.get("content_hash"):
            m = re.search(r"Repo-relative path: `([^`]+)`", node["_body"])
            if m:
                p = os.path.join(repo, m.group(1))
                if os.path.exists(p):
                    h = "sha256:" + hashlib.sha256(open(p,"rb").read()).hexdigest()
                    if h != node["content_hash"]:
                        err(f"{f}: external file hash mismatch for {m.group(1)}")
                else: warn(f"{f}: external file {m.group(1)} not found under repo root (skipped)")
            else:
                h = "sha256:" + hashlib.sha256(node["_body"].encode()).hexdigest()
                if h != node["content_hash"]: err(f"{f}: body hash does not recompute")

    # ---------- report ----------
    print(f"FRACTAL fold verifier — store: {store}")
    for m in infos: print("  ·", m)
    for m in warns: print("  WARN:", m)
    if errors:
        print(f"\nFAIL — {len(errors)} error(s). Do NOT commit store changes until cured (C-050).")
        for m in errors: print("  ERR:", m)
        sys.exit(1)
    print(f"\nPASS — all checks hold ({len(warns)} warning(s)). Safe to commit (C-037 boundary).")

main()
