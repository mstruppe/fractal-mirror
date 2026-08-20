#!/usr/bin/env python3
"""FRACTAL corpus — version-agreement checker (OQ-24 -> C-060, per Protocol v0.18;
scan S2-5.2 -> this tool; canonized beside verify.py/mint.py).

THE RITUAL (C-059 close checklist): this script runs BESIDE the store verifier
at every close — that one proves the store's internal consistency; this one
checks the prose layer's external truth: that every "<Document> vX.Y" claim in
the corpus agrees with the named document's own internal stamp, and that every
referenced path exists. It mechanizes the drift class Loose-Ends Scan #2
documented (eleven false present-tense claims in three conversations).

Stdlib-only (zero infrastructure, C-021). Read-only: never writes anything.

Checks:
  A. Self-agreement  — every versioned-series file's internal stamp matches its
                       filename version; every living document has a readable stamp,
                       and no LIVING filename may carry a version token (C-080).
  B. Claim agreement — every attributable "<Doc> vX.Y" claim is resolved:
                       · a version that does not exist anywhere = ERROR, in every
                         source (frozen included) — nothing may cite a phantom.
                       · claim about a LIVING doc in a STRICT source must equal
                         its current internal stamp (mismatch = ERROR).
                       · a STRICT source citing a stale SERIES version without a
                         historical marker ("per", "since", …) = WARN (heuristic);
                         a version range ending short of the newest = WARN.
                       · C-059 checklist table rows ("changed -> vX.Y") are
                         compared against live stamps (mismatch = WARN).
  C. Path existence  — repo-rooted paths and named files referenced in living
                       sources must exist (missing = ERROR); bare relative paths
                       that resolve nowhere = WARN (heuristic).

Source classes (Max's calls, 2026-08-14):
  FROZEN   — exempt from currency, never from existence: everything under
             Context Packages/Conversations/ (Return Packages and canonical
             Reviews, never revised per C-058), superseded series files, and
             store node files (bodies frozen at mint/revise; their
             "Repo-relative path" binding is still existence-checked).
  STRICT   — the pointer surfaces where every claim should be current: Context
             Index, BOOTSTRAP, GENESIS, the root adapters CLAUDE.md + AGENTS.md
             (canonical since C-065/C-066), Architecture State, Global + Local
             Context, Agenda Board, the store README and the three original
             tools (verify.py · mint.py · check_versions.py — the newer tools
             hold TOLERANT currency; growing the set stays an open offer,
             S5-6.4). Living-doc mismatches here are the drift class itself.
  TOLERANT — living documents whose body narrates history (Decision Register,
             Rule Overview, Conversation Settings, the newest file of each
             series): existence-checked everywhere; currency of living-doc
             claims enforced only on a living ledger's "Sources:" line.

Scope: BOOTSTRAP.md + GENESIS.md + the root adapters CLAUDE.md and AGENTS.md (C-065/C-066)
+ all .md/.html under Claude/ + the store tools' .py files.
Excluded: .git, _to_delete/, Archive/ (the pointer-only ChatGPT era lives at
Archive/Foundation with ChatGPT/, C-029/C-063), _events/ (the log is the store
verifier's territory).

Count claims: "N nodes / M events" in living prose must match the store's
actual counts (Scan #4 S4-1.2) — frozen artifacts and versioned files keep
the numbers that were true at their issue (C-040).

Usage:  python3 check_versions.py [<repo-root>] [-v]
        Default repo-root = two levels up from this script (like the verifier).
        -v also lists unattributed version tokens (calibration aid).
Exit 0 = PASS (warnings allowed) · exit 1 = FAIL (at least one error).
"""
import sys, os, re, json

# ---------------------------------------------------------------- registry ---
# The semantic core: how documents are named in prose, and where truth lives.
# LIVING docs: stable filename, version stamped inside (C-012).
# SERIES docs: one file per version (C-040); newest = the current one.

LIVING = {
    "Global Context":        {"path": "Claude/Context Packages/Global/Fractal_Global_Context.md",
                              "aliases": ["Fractal_Global_Context", "Fractal Global Context",
                                          "Global Context"]},
    "Local Context":         {"path": "Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md",
                              "aliases": ["Fractal_Local_Context (Knowledge Graph)", "Fractal_Local_Context",
                                          "Local Context (Knowledge Graph)", "Local Context"]},
    "Decision Register":     {"path": "Claude/Project Governance/Governance Documents/Fractal_Decision_Register.md",
                              "aliases": ["Fractal_Decision_Register", "Fractal Decision Register",
                                          "Decision Register", "Register"]},
    "Rule Overview":         {"path": "Claude/Project Governance/Governance Documents/Fractal_Rule_Overview.md",
                              "aliases": ["Fractal_Rule_Overview", "Fractal Rule Overview", "Rule Overview"]},
    "Conversation Settings": {"path": "Claude/Project Governance/Governance Documents/Fractal_Conversation_Settings.md",
                              "aliases": ["Fractal_Conversation_Settings", "Fractal Conversation Settings",
                                          "Conversation Settings", "Settings"]},
    "Context Index":         {"path": "Claude/Context Packages/Fractal_Context_Index.md",
                              "aliases": ["Fractal_Context_Index", "Fractal Context Index",
                                          "Context Index", "Index"]},
    "Architecture State":    {"path": "Claude/Architecture/Architecture State/Fractal_Architecture_State.md",
                              "aliases": ["Fractal_Architecture_State", "Fractal Architecture State",
                                          "Architecture State"]},
    "BOOTSTRAP":             {"path": "BOOTSTRAP.md",
                              "aliases": ["Fractal_Bootstrap_Protocol", "BOOTSTRAP.md", "BOOTSTRAP"]},
    # GENESIS joined 2026-08-15 (arc 1 of C-078, per Protocol v0.30): the forward sibling of
    # BOOTSTRAP — a canonical root document, therefore STRICT and guarded like the others.
    "GENESIS":               {"path": "GENESIS.md",
                              "aliases": ["Fractal_Genesis_Protocol", "GENESIS.md", "GENESIS"]},
    "Claude Code Adapter":   {"path": "CLAUDE.md",
                              "aliases": ["Fractal_Claude_Code_Adapter", "Fractal Claude Code Adapter",
                                          "Claude Code Adapter", "Claude Code adapter", "CLAUDE.md"]},
    "Codex Adapter":         {"path": "AGENTS.md",
                              "aliases": ["Fractal_Codex_Adapter", "Fractal Codex Adapter",
                                          "Codex Adapter", "Codex adapter", "AGENTS.md"]},
}

SERIES = {
    "protocol":   {"dir": "Claude/Project Governance/Governance Protocol",
                   "stem": "Fractal_Governance_Protocol_Claude",
                   "aliases": ["Governance Protocol — Claude Series", "Governance Protocol Claude",
                               "Fractal_Governance_Protocol_Claude", "Claude Series",
                               "Governance Protocol", "Protocols", "Protocol", "PROT", "Claude"],
                   "stamp": "title"},   # version lives in the H1 title line
    "schema":     {"dir": "Claude/Architecture/Concepts/Knowledge Graph",
                   "stem": "Fractal_Node_and_Event_Schema",
                   "aliases": ["Fractal_Node_and_Event_Schema", "Fractal Node & Event Schema",
                               "Node & Event Schema", "Node and Event Schema", "Schema"],
                   "stamp": "field"},
    "template":   {"dir": "Claude/Architecture/Concepts/Knowledge Graph",
                   "stem": "Fractal_Node_Template",
                   "aliases": ["Fractal_Node_Template", "Fractal Node Template", "Node Template",
                               "Template"],
                   "stamp": "field"},
    "foundation": {"dir": "Claude/Architecture/Concepts/Knowledge Graph",
                   "stem": "Fractal_Knowledge_Path_Foundation",
                   "aliases": ["Fractal_Knowledge_Path_Foundation", "Fractal Knowledge Path Foundation",
                               "Knowledge Path Foundation"],
                   "stamp": "field"},
    "navigation": {"dir": "Claude/Architecture/Concepts/Knowledge Graph",
                   "stem": "Fractal_Navigation_Contract",
                   "aliases": ["Fractal_Navigation_Contract", "Fractal Navigation Contract",
                               "Navigation Contract"],
                   "stamp": "field"},
}

# Named in prose with versions, but no independently stamped file exists —
# claims are skipped, never guessed at (the Agenda Board's revisions are
# tracked in the Local Context; the Master Index is ChatGPT-era raw material).
UNVERIFIABLE = ["Agenda Board", "Master Index"]

# The pointer surfaces held to full currency (see docstring).
STRICT = {
    "BOOTSTRAP.md",
    "GENESIS.md",
    "CLAUDE.md",
    "AGENTS.md",
    "Claude/Context Packages/Fractal_Context_Index.md",
    "User Documents/Fractal_Agenda_Board.html",
    "Claude/Context Packages/Global/Fractal_Global_Context.md",
    "Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md",
    "Claude/Architecture/Architecture State/Fractal_Architecture_State.md",
    "Claude/Knowledge Graph Store/README.md",
    "Claude/Knowledge Graph Store/verify.py",
    "Claude/Knowledge Graph Store/mint.py",
    "Claude/Knowledge Graph Store/check_versions.py",
}

# Claims preceded (in the look-back window) by these are out of scope:
ERA_GUARD = re.compile(r"ChatGPT[ -]era|Master Index", re.I)       # pointer-only era, C-029
EG_GUARD  = re.compile(r"e\.g\.|example|illustrat", re.I)          # illustrative text

# Historical-citation markers: a stale SERIES version cited right after one of
# these records the past rather than claiming the present (no WARN).
HIST_MARKER = re.compile(
    r"(?:\bper\b|\bsince\b|\bsee\b|"
    r"\bParent(?: Protocol)?\b|\bSupersedes\b|\bStatus\b|\bratified\b|\brecorded\b|"
    r"\bresolved\b|\baccepted\b|\bcarried\b|\bapplied\b|\bnew in\b|\bunchanged\b|"
    r"\breceived\b|\bstamped?\b|\bconfirmed\b|\bdischarged\b|\bwas\b|\bformer(?:ly)?\b)"
    r"[^\n]{0,24}$", re.I)

# Known-historical mentions, acknowledged as narrative at this tool's review
# (both entries ratified by Max 2026-08-14, C-060 per Protocol v0.18).
# Format: (source-path-suffix, exact backticked string). Keep this list SHORT —
# every entry is a claim the checker deliberately looks away from.
SUPPRESS = [
    # The frozen v0.5 file narrates the retired monthly bucket by its old
    # path, and names the roll ceremony's *future* partition — deliberate
    # history/foresight, not live references.
    ("Fractal_Node_and_Event_Schema_v0.5.md", "_events/2026-08.jsonl"),
    ("Fractal_Node_and_Event_Schema_v0.5.md", "part-0002.jsonl"),
    # v0.6 carries §4.1 forward verbatim — the same ratified foresight mention
    # of the roll ceremony's future partition (successor of the v0.5 pair).
    ("Fractal_Node_and_Event_Schema_v0.6.md", "part-0002.jsonl"),
    # (the self-scan entry for this file retired at Scan #4 — the filename
    # heuristic no longer reads .py sources at all, S4-3.1)
]

# Files that BY DESIGN exist only in newborn instances, or optionally (the
# S5-6.5 declared class, ratified at the Scan #5 slate — the S4-3.1
# WARN-drowning cure's second round): genesis writes them into a child, or an
# instance opts into them; the mother's documents describe them without
# holding them. INFO, never WARN — the WARN channel stays signal.
INSTANCE_ONLY = {
    "FIELDNOTES.md",          # genesis-written capture door (C-100)
    "First_Loops_Rail.md",    # genesis-written onboarding rail (C-101)
    "vocabulary_local.json",  # optional instance-side vocabulary (C-114)
    "KNet_Fractal_Kernel_Migration_Protocol.md",  # child-jurisdiction file the
                              # migration standard cites (KNet's P-007 record)
}

SCAN_EXT  = {".md", ".html", ".py"}
SKIP_DIRS = {".git", "_to_delete", "Archive", "_events"}
PATH_EXT  = {".md", ".py", ".jsonl", ".html", ".docx", ".txt", ".json"}
PLACEHOLDER = re.compile(r"[<>*{}…]|NNNN|X\.Y|\bvX\b")

errors, warns, infos = [], [], []
err, warn, info = errors.append, warns.append, infos.append
n_suppressed = 0

def vkey(v):  # "0.10" sorts above "0.9"
    a, b = v.split("."); return (int(a), int(b))

def read(p):
    return open(p, encoding="utf-8").read()

def alias_regex(a):
    return re.escape(a).replace(r"\ ", r"[\s_]+")

def registry_copy(registry):
    """Copy the small declarative registry without adding a dependency."""
    return {
        key: {
            field: list(value) if isinstance(value, list) else value
            for field, value in spec.items()
        }
        for key, spec in registry.items()
    }

def inherited_registry(here):
    """Load the birth manifest and its instance-local registry projection.

    FRACTAL has no manifest, so its registry objects are returned untouched. A
    birthed instance carries both files: the manifest defines the INHERITED
    source class; the projection re-points only the names whose truth lives in
    that instance. Removed upstream names remain available as unresolved alias
    targets so citations in inherited biography can be counted, not hidden.
    """
    manifest_path = os.path.join(here, ".inherited")
    if not os.path.isfile(manifest_path):
        return None, LIVING, SERIES, STRICT, [], []

    inherited = set()
    for number, line in enumerate(read(manifest_path).splitlines(), 1):
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        normalized = os.path.normpath(value).replace(os.sep, "/")
        if os.path.isabs(value) or normalized == ".." or normalized.startswith("../"):
            err(f".inherited:{number}: path must be repo-relative: {value!r}")
            continue
        inherited.add(normalized)

    living, series = registry_copy(LIVING), registry_copy(SERIES)
    strict = set(STRICT)
    unresolved_living, unresolved_series = [], []
    registry_path = os.path.join(here, ".version-registry")
    if not os.path.isfile(registry_path):
        return inherited, living, series, strict, unresolved_living, unresolved_series
    try:
        config = json.loads(read(registry_path))
    except (OSError, json.JSONDecodeError) as exc:
        err(f".version-registry: cannot read instance registry: {exc}")
        return inherited, living, series, strict, unresolved_living, unresolved_series

    for name, replacement in config.get("living_overrides", {}).items():
        if name not in living:
            err(f".version-registry: unknown living document override: {name}")
            continue
        unresolved_living.append((name, living[name]))
        living[name] = replacement
    for name in config.get("living_omit", []):
        if name not in living:
            err(f".version-registry: unknown living document omission: {name}")
            continue
        unresolved_living.append((name, living.pop(name)))
    for key in config.get("series_omit", []):
        if key not in series:
            err(f".version-registry: unknown series omission: {key}")
            continue
        unresolved_series.append((key, series.pop(key)))
    strict = set(config.get("strict", strict))

    # An alias that now names an instance document resolves locally and must be
    # checked normally. Only displaced, non-overlapping aliases remain upstream.
    active_aliases = {
        alias for spec in living.values() for alias in spec.get("aliases", [])
    } | {
        alias for spec in series.values() for alias in spec.get("aliases", [])
    }
    unresolved_living = [
        (name, dict(spec, aliases=[a for a in spec["aliases"] if a not in active_aliases]))
        for name, spec in unresolved_living
    ]
    unresolved_series = [
        (key, dict(spec, aliases=[a for a in spec["aliases"] if a not in active_aliases]))
        for key, spec in unresolved_series
    ]
    return inherited, living, series, strict, unresolved_living, unresolved_series

# ------------------------------------------------------------------- main ----
def main():
    global n_suppressed
    here = os.path.dirname(os.path.abspath(__file__))
    args = [a for a in sys.argv[1:] if a != "-v"]
    verbose = "-v" in sys.argv
    repo = os.path.abspath(args[0]) if args else os.path.normpath(os.path.join(here, "..", ".."))
    inherited, living, series, strict_sources, unresolved_living, unresolved_series = \
        inherited_registry(here)

    # -- scope files (checked) + basename index (everything that exists)
    scope, basenames = [], set()
    for base, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in (".git", "_to_delete")]
        for f in files:
            basenames.add(f)
            rel = os.path.relpath(os.path.join(base, f), repo).replace(os.sep, "/")
            if any(part in SKIP_DIRS for part in rel.split("/")): continue
            if os.path.splitext(f)[1].lower() not in SCAN_EXT: continue
            # .claude/commands/ joined the walk 2026-08-15 (Scan #3 S3-3.1, per Protocol v0.29):
            # the command tier is a tracked behavioral surface — its paths and claims are guarded.
            if rel in ("BOOTSTRAP.md", "GENESIS.md", "CLAUDE.md", "AGENTS.md") or rel.startswith("Claude/") \
               or rel.startswith(".claude/commands/"):
                scope.append(rel)

    # -- store actuals for the count-claim rule (S4-1.2)
    _nodes_dir = os.path.join(repo, "Claude", "Knowledge Graph Store", "nodes")
    _events_dir = os.path.join(repo, "Claude", "Knowledge Graph Store", "_events")
    store_nodes = len([f for f in os.listdir(_nodes_dir) if f.endswith(".md")]) \
        if os.path.isdir(_nodes_dir) else None
    store_events = sum(
        sum(1 for ln in open(os.path.join(_events_dir, f), encoding="utf-8") if ln.strip())
        for f in sorted(os.listdir(_events_dir)) if f.endswith(".jsonl")
    ) if os.path.isdir(_events_dir) else None

    # -- protocol DOC coverage (S5-2.1 tripwire): the C-041 per-version mint
    # lapsed silently for v0.50–v0.54 and resumed silently at v0.55. Every
    # Governance Protocol series file must be named in the event log (its
    # create/alias events carry the version-labeled name); WARN, never ERR —
    # a retro mint is a governed act, not a mechanical one.
    _proto_dir = os.path.join(repo, "Claude", "Project Governance", "Governance Protocol")
    if os.path.isdir(_proto_dir) and os.path.isdir(_events_dir):
        _log_text = "".join(
            open(os.path.join(_events_dir, f), encoding="utf-8").read()
            for f in sorted(os.listdir(_events_dir)) if f.endswith(".jsonl"))
        for _pf in sorted(os.listdir(_proto_dir)):
            if _pf.startswith("Fractal_Governance_Protocol_") and _pf.endswith(".md") \
               and _pf[:-3] not in _log_text:
                warn(f"Governance Protocol/{_pf}: no store event names this file — "
                     "the C-041 per-version DOC mint is missing (S5-2.1 tripwire)")

    # -- living stamps
    stamps = {}
    for name, spec in living.items():
        p = os.path.join(repo, spec["path"])
        if not os.path.exists(p):
            err(f"registry: living document missing on disk: {spec['path']}"); continue
        # C-080 (2026-08-15): a LIVING document's filename may never carry a version
        # token. C-012 puts the version INSIDE a living document and keeps the filename
        # stable; a version in the name is a claim that goes stale the moment the
        # document is revised. Three grandfathered exceptions existed until C-080
        # retired the grandfathering wholesale — this check makes the violation
        # impossible to reintroduce rather than merely discouraged (OQ-13 closed).
        if re.search(r"_v\d+(\.\d+)?(?=\.[A-Za-z0-9]+$)", os.path.basename(spec["path"])):
            err(f"registry: LIVING document carries a version token in its filename: "
                f"{spec['path']} — living documents stamp the version inside and keep "
                f"a stable filename (C-012/C-080). Rename it, or register it as a SERIES.")
        t = read(p)
        m = (re.search(r"\*\*Version:\*\*\s*v?(\d+\.\d+)", t)
             or re.search(r"\|\s*Version\s*\|\s*v?(\d+\.\d+)\s*\|", t))
        if not m: err(f"{spec['path']}: no readable internal version stamp (living doc, C-012)")
        else: stamps[name] = m.group(1)

    # -- series files: enumerate + self-agreement
    series_versions = {}
    for key, spec in series.items():
        d, found = os.path.join(repo, spec["dir"]), {}
        for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            m = re.match(alias_regex(spec["stem"]) + r"_v(\d+\.\d+)\.md$", f)
            if not m: continue
            v, rel = m.group(1), spec["dir"] + "/" + f
            found[v] = rel
            t = read(os.path.join(repo, rel))
            if spec["stamp"] == "field":
                s = re.search(r"\*\*Version:\*\*\s*v?(\d+\.\d+)", t)
            else:
                s = re.search(r"^#.*?v(\d+\.\d+)\s*$", t, re.M)
            if not s: err(f"{rel}: series file carries no internal version stamp")
            elif s.group(1) != v:
                err(f"{rel}: internal stamp v{s.group(1)} != filename version v{v} (self-agreement)")
        if not found: err(f"registry: no files found for series '{key}' under {spec['dir']}")
        series_versions[key] = found
    newest = {k: max(v, key=vkey) for k, v in series_versions.items() if v}

    # grandfathered stable pointers: the filename's version is a name, not a claim (C-012)
    grandfathered = {os.path.basename(s["path"]) for s in living.values()}
    living_paths = {s["path"] for s in living.values()}
    # alias-stems that may survive masking as a filename prefix ("BOOTSTRAP.md" -> "BOOTSTRAP")
    stem_prefixes = sorted({a for s in living.values() for a in s["aliases"] if " " not in a}
                           | {s["stem"] for s in series.values()}, key=len, reverse=True)

    # -- alias table, longest-first, one combined regex
    alias_rx = []
    for name, spec in living.items():
        for a in spec["aliases"]: alias_rx.append((a, "living", name))
    for key, spec in series.items():
        for a in spec["aliases"]: alias_rx.append((a, "series", key))
    for name, spec in unresolved_living:
        for a in spec["aliases"]: alias_rx.append((a, "unresolved living", name))
    for key, spec in unresolved_series:
        for a in spec["aliases"]: alias_rx.append((a, "unresolved series", key))
    for a in UNVERIFIABLE: alias_rx.append((a, "unverifiable", a))
    alias_rx.sort(key=lambda x: -len(x[0]))
    alias_pat = re.compile("|".join("(" + alias_regex(a) + ")" for a, _, _ in alias_rx))
    def classify(s):
        for a, kind, key in alias_rx:
            if re.fullmatch(alias_regex(a), s): return kind, key
        return None, None

    def is_frozen(rel):
        if "Context Packages/Conversations/" in rel: return True
        if "/nodes/" in rel: return True
        base = os.path.basename(rel)
        if base in grandfathered: return False
        for key, spec in series.items():
            m = re.match(alias_regex(spec["stem"]) + r"_v(\d+\.\d+)\.md$", base)
            if m: return m.group(1) != newest.get(key)
        return False

    def suppressed(rel, s):
        return any(rel.endswith(suf) and s == txt for suf, txt in SUPPRESS)

    # -- scan every scope file
    n_claims = n_agree = n_paths = n_inherited = 0
    unattributed = []
    VTOK  = re.compile(r"\bv(\d+\.\d+)\b")
    COUNTS = re.compile(r"\b(\d+)\s+nodes\s+/\s+(\d+)\s+events\b")
    FNAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-]*\.(?:md|py|jsonl|html|docx|txt|json)\b")
    CHAIN = re.compile(r"^[ \t]*(?:[–—\-/,+&→]|->|\.\.\.|…|and\s|to\s|through\s)[ \t]*")

    for rel in sorted(scope):
        raw = read(os.path.join(repo, rel))
        text = re.sub(r"<[^>]+>", lambda m: "\x00" * len(m.group(0)), raw) if rel.endswith(".html") else raw
        frozen, strict = is_frozen(rel), rel in strict_sources
        inherited_source = inherited is not None and rel in inherited
        node_file = "/nodes/" in rel
        masked = list(text)
        def mask(a, b):
            token = text[a:b]
            keep = next((len(p) for p in stem_prefixes if token.startswith(p)), 0)
            for i in range(a + keep, b): masked[i] = "\x00"

        # ---- C. backticked paths (existence)
        for m in re.finditer(r"`([^`\n]+)`", text):
            s = m.group(1).strip()
            if PLACEHOLDER.search(s): continue
            is_pathlike = "/" in s and os.path.splitext(s)[1].lower() in PATH_EXT
            is_dirlike = s.rstrip("/").endswith(("Governance Documents", "Governance Protocol",
                          "Context Packages", "Knowledge Graph Store", "Architecture State",
                          "Conversations", "Claude", "nodes", "_events", "Knowledge Graph"))
            if not (is_pathlike or is_dirlike): continue
            mask(m.start(1), m.end(1))
            if frozen and not node_file: continue
            if node_file and "Repo-relative path" not in text[max(0, m.start()-40):m.start()]:
                continue
            n_paths += 1
            cand = s.lstrip("/")
            if cand.startswith("FRACTAL/"): cand = cand[len("FRACTAL/"):]
            rooted = cand.split("/")[0] in ("Claude", "Archive", "_to_delete") \
                     or cand == "BOOTSTRAP.md"
            tries = [os.path.join(repo, cand),
                     os.path.join(repo, "Claude", cand),
                     os.path.join(repo, os.path.dirname(rel), s),
                     os.path.join(repo, "Claude", "Knowledge Graph Store", s)]
            if any(os.path.exists(t) for t in tries): continue
            if suppressed(rel, s): n_suppressed += 1; continue
            if inherited_source:
                n_inherited += 1
                continue
            if rooted or node_file:
                err(f"{rel}: referenced path does not exist: `{s}`")
            else:
                warn(f"{rel}: relative path resolves nowhere: `{s}` (heuristic)")

        # ---- bare filename mentions: existence by basename; masked either way
        for m in FNAME.finditer(text):
            s = m.group(0)
            if masked[m.start()] == " ": continue
            mask(m.start(), m.end())
            if frozen or PLACEHOLDER.search(s) or re.match(r"^\d", s): continue
            if rel.endswith(".py"):
                continue    # code assembles filenames from string fragments —
                            # not prose claims; half the WARN channel was this
                            # one noise class (Scan #4 S4-3.1)
            if s in grandfathered or any(b == s or b.endswith(" " + s) for b in basenames):
                continue
            ln = text.splitlines()[text.count("\n", 0, m.start())]
            if re.search(r"candidat|until built|planned|would|not yet|future|retired|unbuilt", ln, re.I):
                continue    # named as a future or deliberately-unbuilt artifact,
                            # not a claim (retired|unbuilt added at Scan #4
                            # S4-3.1 — living docs correctly narrate C-083
                            # retiring SKILL.md unbuilt)
            n_paths += 1
            if suppressed(rel, s): n_suppressed += 1; continue
            if inherited_source:
                n_inherited += 1
                continue
            if s in INSTANCE_ONLY or os.path.basename(s) in INSTANCE_ONLY:
                info(f"{rel}: instance-only/optional artifact {s} — lives in "
                     "newborns or by opt-in, not the mother (S5-6.5 declared class)")
                continue
            warn(f"{rel}: named file exists nowhere in the repo: {s} (heuristic)")

        # ---- A9. store-count claims (S4-1.2): "N nodes / M events" was the one
        # numeric claim class no rule read — Scan #1's 174-vs-176 drift recurred
        # at Scan #4 (85/454 written before the close's own store acts). Living
        # prose only: frozen artifacts and versioned files keep the numbers that
        # were true at their issue (C-040 — they supersede, never drift).
        if store_nodes is not None and not frozen and not inherited_source \
           and not re.search(r"_v\d+\.\d+\.[a-z0-9]+$", rel):
            for m9 in COUNTS.finditer(text):
                cn, ce = int(m9.group(1)), int(m9.group(2))
                if (cn, ce) != (store_nodes, store_events):
                    err(f"{rel}: claims {cn} nodes / {ce} events — the store holds "
                        f"{store_nodes} nodes / {store_events} events")

        text2 = "".join(masked)
        lines = text2.splitlines(keepends=True)
        line_at, off = [], 0
        for ln in lines: line_at.append((off, ln)); off += len(ln)
        def line_of(pos):
            lo, hi = 0, len(line_at) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if line_at[mid][0] <= pos: lo = mid
                else: hi = mid - 1
            return line_at[lo][1]

        # ---- B1. C-059 checklist table rows: "| <Doc> | ... changed -> vX.Y"
        if strict and rel.endswith(".md"):
            for m in re.finditer(r"^\|\s*([^|\n]+?)\s*\|[^\n]*?(?:→|->)\s*v(\d+\.\d+)",
                                 text2, re.M):
                cell, v = m.group(1), m.group(2)
                am = alias_pat.search(cell)
                if not am: continue
                kind, key = classify(am.group(0))
                if kind == "living" and stamps.get(key) and v != stamps[key]:
                    warn(f"{rel}: checklist row marks {key} → v{v} — its internal stamp "
                         f"says v{stamps[key]} (currency heuristic)")

        # ---- B2. version-claim tokens
        for m in VTOK.finditer(text2):
            v, start = m.group(1), m.start()
            window = text2[max(0, start - 56):start]
            guard_win = re.split(r"[\n|;]", text2[max(0, start - 80):start])[-1]
            if ERA_GUARD.search(guard_win) or EG_GUARD.search(guard_win): continue

            kind = key = None
            if re.search(r"\bper\s+$", window):                 # adjacent "per vN"
                kind, key = "series", "protocol"
            else:
                hit = None
                for am in alias_pat.finditer(window):
                    gap = window[am.end():]
                    if ("\n" not in gap and "·" not in gap and "|" not in gap
                            and ";" not in gap and not re.search(r"\d", gap)
                            and len(gap) <= 24):
                        hit = am
                if hit:
                    kind, key = classify(hit.group(0))
            if kind is None:
                unattributed.append((rel, (window[-28:] + "v" + v).replace("\n", " "))); continue

            # consume a chained run ("v0.3/v0.4", "v0.1–v0.14") as one range claim
            claims, tail = [v], text2[m.end():]
            while True:
                cm = CHAIN.match(tail)
                if not cm: break
                nm = VTOK.match(tail[cm.end():])
                if not nm: break
                claims.append(nm.group(1)); tail = tail[cm.end() + nm.end():]
            is_range = len(claims) > 1
            line = line_of(start)
            sources_line = bool(re.match(r"\s*(?:\*\*)?(?:Sources|State scanned|Baseline)\s*:", line))
            normative_line = "Normative home" in line
            history_line = bool(re.match(r"\s*(?:\*\*)?Revision history\s*:", line)
                                or "**Status:**" in line)

            for i, cv in enumerate(claims):
                n_claims += 1
                if kind == "unverifiable": continue
                if kind.startswith("unresolved"):
                    if inherited_source:
                        n_inherited += 1
                    else:
                        err(f"{rel}: cites {key} v{cv} — named document resolves nowhere")
                    continue
                if kind == "living":
                    cur = stamps.get(key)
                    if cur is None:
                        if inherited_source:
                            n_inherited += 1
                        continue
                    if cv == cur: n_agree += 1; continue
                    if frozen or history_line: n_agree += 1; continue       # historical record
                    if is_range and i < len(claims) - 1:
                        n_agree += 1; continue                               # range: history up to now
                    if strict or ((sources_line or normative_line) and rel in living_paths):
                        err(f"{rel}: claims {key} v{cv} — its internal stamp says v{cur}")
                    else: n_agree += 1                                       # tolerant narration
                else:  # series
                    have = series_versions.get(key, {})
                    if cv not in have:
                        if inherited_source:
                            n_inherited += 1
                            continue
                        err(f"{rel}: cites {key} v{cv} — no such version exists "
                            f"(series runs to v{newest.get(key)})")
                        continue
                    n_agree += 1
                    stale = cv != newest.get(key)
                    if not stale or frozen: continue
                    if not strict and not normative_line: continue
                    if history_line or sources_line: continue
                    if is_range:
                        if i == len(claims) - 1:
                            warn(f"{rel}: version range ends at {key} v{cv} — series runs "
                                 f"to v{newest.get(key)} (currency heuristic)")
                    elif not HIST_MARKER.search(window):
                        warn(f"{rel}: cites {key} v{cv} without a historical marker — "
                             f"newest is v{newest.get(key)} (currency heuristic)")

    # ---- report
    print(f"FRACTAL version-agreement checker — repo: {repo}")
    info(f"{len(scope)} files scanned · {n_claims} version claims attributed "
         f"({n_agree} agree) · {n_paths} path/file references checked · "
         f"{len(unattributed)} tokens unattributed"
         + (f" · {n_suppressed} suppressed (known-historical)" if n_suppressed else ""))
    info("living stamps: " + " · ".join(f"{k} v{stamps[k]}" for k in sorted(stamps)))
    info("series newest: " + " · ".join(f"{k} v{newest[k]}" for k in sorted(newest)))
    if inherited is not None:
        info(f"{n_inherited} upstream citations exempted (INHERITED, C-088)")
    for msg in infos: print("  ·", msg)
    if verbose and unattributed:
        print("  unattributed version tokens (calibration aid):")
        for rel, ctx in unattributed: print(f"    - {rel}: …{ctx}")
    for msg in warns: print("  WARN:", msg)
    if errors:
        print(f"\nFAIL — {len(errors)} error(s). The corpus disagrees with itself; "
              f"cure before closing (C-059).")
        for msg in errors: print("  ERR:", msg)
        sys.exit(1)
    print(f"\nPASS — every attributable version claim agrees "
          f"({len(warns)} warning(s)). Safe to close (C-059).")

if __name__ == "__main__":       # close.py imports this module for the LIVING/SERIES
    main()                       # registry — one registry home (C-092, the C-110 tool work)
