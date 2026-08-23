# FRACTAL — Knowledge Graph Store

Live plain-text store for the FRACTAL Knowledge Graph. Hand-usable with zero infrastructure
(C-021). Format spec: **Node & Event Schema v0.7** (what is written) + **Navigation Contract v0.2**
(how it is read — the C-070 companion), both in `../Architecture/Concepts/Knowledge Graph/`.

## Layout
- `_events/part-0001.jsonl` — the append-only event log, one event per line. **Canonical (C-024).**
  **One file (C-055):** the single active partition; `verify.py` warns past 50,000 events per file,
  and only the **roll ceremony** (one recorded commit on merged state) ever opens the next partition.
- `nodes/<id>[--slug].md`  — one file per entity (YAML front-matter + optional body).
  A node's `placements:` block is a human-readable *fold* of the log; where they disagree, the log wins.
- `verify.py` / `mint.py` / `check_versions.py` / `close.py` — the canonized tools (C-050, C-060, C-073):
  fold verifier, mint guard, version-agreement checker, and close-ripple generator (dry-run by default;
  judgment never delegated). Stdlib-only; code artifacts (C-006 exception), not DOC-minted.
  Since the C-110/C-112 mechanization, `close.py` also carries the close's mechanical half: the dry
  run (and `--walk`) pre-fills the C-059 walk table from the hash-diff + git signal, flags the
  Register as the judgment dirty-bit (C-112 — unchanged Register ⇒ the recorded-reason line offered
  mechanically), and reads the drag gauge (advisory word budgets, C-110 proposal 10); `--stamp`
  (applied at `--write`) bumps stale version headers, mints revision-history rows from each
  document's `--note`, and writes store counts at predicted post-ripple totals *before* hashing;
  `--pack` runs the tagging-close gate — the GENESIS §3.4 clause-span + §0 count checks (Migration
  Procedure §7.3; S5-7.2), the AST §6 partition-seat check (S6-7.1 — every shipped decision classified),
  the mirror's post-rebuild cleanliness + duplicate scan (the C-116 amendment), the serving-layer
  preservation checks (`.github/` · `gh-pages` · the mirror's own `-public` receipt pairs, C-120 —
  `CNAME` reported informationally, the gate repo carries the domain), and the composition checks
  (S6-7.3 curated-exclusion absence · S6-7.4 shipped-HTML hygiene). The `--create`
  alias grammar's prefix follows the instance's own `.version-registry` (TF1-4's cure; mother
  default `Fractal_`). Judgment on what a change *means* stays manual (C-110 proposal 14).
  `check_versions.py` carries the **`INHERITED` source class (C-088)**: in a birthed instance, a
  `.inherited` manifest + `.version-registry` projection exempt inherited kernel documents' upstream
  citations (counted, never hidden); with no manifest — this repo — behavior is unchanged. **The
  manifest grows only by governed adoption** (the Kernel Migration Procedure): every newly adopted
  kernel file is appended in the same change-set, each line paired to an adoption-matrix row;
  instance-authored files never enter it — an exemption without a pairing is itself a finding, and
  the manifest is never a way to silence the checker. (Mechanics: the manifest lives beside
  `check_versions.py` as `.inherited`, one repo-relative path per line, `#` comments permitted.)
- `check_scan.py` — the Scan conformance checker (C-118, the Scan Procedure's §12 gate): validates a
  Scan report (filename/header/state-block/id grammar/seed table) and its C-058 ledger integration;
  red-blocks Scan #5 onward, historical scans grandfathered WARN-only. Same family rules as above.
- `genesis.py` — dry-run-first executor that births a separate FRACTAL-governed repository from the
  tier-0 kernel, parameterized spine, and a new instance ledger; `--write` creates and commits it.
  Since flight 4 it also writes the newborn's `.inherited` manifest, its checker-registry projection,
  and the C-087 secrets-layer `.gitignore` entries.
- `doctor.py` — the sixth tool (flight 4, per Protocol v0.35): diagnoses repository posture by tier —
  identity, allowed-signers binding (`--write` rebinds), signing shape, tier detection (absence of a
  tier-1 component is information, never failure — C-081), the C-087 secrets guard (ignore entries +
  tracked-file secret scan, values redacted), remote, and privileged-posture instructions.
- `fieldnote.py` — the seventh tool (C-100, the flip preparation; the RAM model since C-121): the
  capture, depth, and intake halves of the testing pipeline — one buffer per instance via the
  single-buffer config `fieldnote_roster.json` (targets retired), content-immutable machine-format
  blocks (Fieldnote Format v0.2), the `--depth` pressure reading (budget + high-water in the buffer
  header), and `parse` for whole-or-nothing intake — both grammars accepted (v0.1 child ledgers).
- `postman.py` — the ninth tool (C-139, the connection doctrine — Interface Place Format v0.2 §7):
  the interface place's machine half — `poll` (the connections block as the reading list; header-diff
  notifications against the reader-side cursor `postman_cursor.json`; connection-requests quarantined),
  `post` / `receipt` (envelope + index row + high-water, refusing addressed posts to non-connections;
  author resolved instance-locally, never the machine-global git identity), `spent` / `dissolve` (the
  §6.1 closing acts, grammar-checked, the commit-before-dissolve duty warned), and `check` — the index
  parser that *is* the format's checker. Ships to newborns via `genesis.py` (born v0.2-connected,
  CN-0001 = the mother). Suite: `test_postman.py` (39). Stdlib-only, same family rules.
- `stats.py` — **a convenience utility, not a canonized tool** (the first drone flight's drill
  artifact, 2026-08-14): a read-only fold counter whose output cross-checks `verify.py`'s totals.
  Canonization on observed need; it carries no invariant of its own.

## Rules in force (C-022–C-027, C-043–C-046, C-049–C-050, C-055)
- Identity = `TYPE-ULID`, immutable. Names/codes are aliases (kinds: `label` / `route` / `redirect`).
- To change anything you **append a new event** — never edit or delete (supersede, C-025).
- Mint a coordinate before placing against it; codes are immutable, unique-under-parent;
  **root codes are unique globally, across all facets (C-044)** — `python3 mint.py --list -` shows the namespace.
- Parentage is the code prefix; the label is separate from the code (C-027).
- **Facets are minted concepts** under the `FACET` root, meta-facet token `facet` (C-043);
  event-field tokens (`topic`, `agent`, …) are `route` aliases over `FACET.*` nodes.
- **Reparent = re-mint on the same subject + `alias(kind: redirect)` on the old code (C-045).**
  The fold resolves codes through redirect chains; log lines are never touched.
- Agent facet is branched by kind: `AGENT.HUMAN.<name>`, `AGENT.AI.<name>`.
- **Collisions resolve first-mint-wins (C-049):** if a merge lands two mints of one code, the
  earlier event (`ts`, ULID tie-break) holds it; the later subject is re-minted under a fresh
  code and its intended placements re-pointed — append-only, listed by `verify.py`.
- **Root mints are deliberate (C-049):** from 2026-08-13 a root mint requires `mint.py --root
  "<whose call>"` — the note records the decision; `verify.py` errors on bare post-pin roots.

## Minting (use the guard)
- `python3 mint.py --list <PARENT|->` — see what's taken (naming options) before choosing.
- `python3 mint.py <facet-token> <CODE> "<Label>" --actor AGENT.X.Y` — validates everything
  (grammar, parent, uniqueness incl. global roots, actor), previews the event + node stub;
  add `--write` to append both in one move ("two writes, one truth" automated).
- Fallback ULID one-liner (never hand-write a ULID; prefix must decode to the recorded second, C-040):
  python3 -c "import os,time;C='0123456789ABCDEFGHJKMNPQRSTVWXYZ';t=int(time.time()*1000);r=int.from_bytes(os.urandom(10),'big');e=lambda v,n:''.join(C[(v>>(5*i))&31] for i in range(n-1,-1,-1));print(e(t,10)+e(r,16))"

## Verify (THE RITUAL, C-050 — a duty, not an option)
- `python3 verify.py` — replays the whole log and checks every invariant: parse, ULID coherence,
  mint grammar, global roots, the collision tripwire, alias/route/redirect wiring, every node's
  fold against the log, and every content hash (body + external canonical files).
- **Run it before every store-touching commit and after every merge that touches the store**
  (the C-037 commit boundary). Git merges JSONL textually — the semantic merge check is this
  script, never git. Red verifier = do not commit until cured.
- `python3 check_versions.py` — the corpus-side ritual (C-060): every `<Document> vX.Y` claim in
  the prose layer resolved against the named document's internal stamp, plus path existence.
  **Runs beside verify.py at every close (C-059)** — red from either blocks the close.

## Multi-writer status
Multi-writer safe since C-049/C-050 (2026-08-13; retires the C-032 single-writer caveat, OQ-19):
duplicates are **prevented** locally (`mint.py`), collisions from concurrent clones are
**detected** at the merge boundary (`verify.py`) and **cured** append-only (first-mint-wins).

## Trace by hand (until an index is worth building)
The ritual below is the **zero-infra tier of the Navigation Contract** (C-070) — the read-side
canonical this store is navigated by; the contract governs (`resolve`/`enter`/`trace`/`history`,
ranking, redirects), these greps implement.
- Moved codes (check FIRST if a scan comes up short): grep '"kind": "redirect"' _events/*.jsonl
- Everything *authored* by an AI: grep '"role": "by"' _events/*.jsonl | grep '"code": "AGENT.AI.'
  (matching `AGENT.AI.` alone also catches mints *of* AI agents by others — role `by` is authorship)
- Everything about the KG — subtree prefix scan (no closing quote): grep -n '"code": "KG' _events/*.jsonl
  · exact node only: grep -n '"code": "KG"' _events/*.jsonl
- All facets: grep '"code": "FACET' _events/*.jsonl (prefix scan FACET.*)
- A document's placements: read its node file, or fold its `place` lines from the log.
