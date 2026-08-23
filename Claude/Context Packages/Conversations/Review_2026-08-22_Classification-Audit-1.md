# Review — Classification Audit #1 (the rule-corpus update mechanism's first flight; the landing)

> **DERIVED REVIEW RECORD — frozen at issue; PROPOSAL-ONLY (Ultracode Flight Protocol v0.2: the landing binds nothing — every disposition below is Max's).** Commission: Max, the thirty-seventh session, 2026-08-22 — *"the consensus of habits needs to have an update mechanism, such that it iterates checks whether the rules landed in the right classification. It may be that the AI agent may have interpreted something incorrectly, however, it would be very inefficient to go over it one by one. Instead we implement a specific scan flight routine for this."* The routine was built the same session (`Claude/Project Governance/Rule Corpus/` — corpus salvaged from the first flight's journal, `audit.py` the mechanical scoping half, `classification-audit` the named workflow); this record is its **first execution** — and the first flight launched conformant under the two-turn rule drafted from the vendor-collision incident: the contract presented one turn, Max's "go" the next.

**Issued:** 2026-08-22 · **Document ID:** DOC-01M0NBG77CM868HXY1M0GB5EX4 (minted at this close via `close.py --create`) · **Session:** the thirty-seventh (mother) · **Flight shape:** 10 agents, 4 phases (Reconcile 3 · Classify 4 · Adjudicate 2 · Assemble 1), read-only throughout, zero failures · **Gas (§7.2 honesty accounting):** 1,102,259 tokens vs the 0.8–1.2M estimate (within band, ×0.92–1.38; basis: the rule-corpus flight's as-flown 1.71M/14 agents, scoped narrower per agent) · 144 tool calls · ≈46 minutes · **Manifest:** seed 20260822 — 2 dirty · 2 new · 15 disagreement · 12 sample · 365 unreconciled · **Verification tier:** adversarial on every dispute — two opposite-mandate verifiers (refute-the-standing vs refute-the-challenge); a reclassification proposed only where both agree against standing.

---

# Classification Audit — Delta Report

**PROPOSAL-ONLY.** Nothing below is a disposition; every row lands only by the owner's call. Assembled read-only.

---

## 1 · Headline counts

| Metric | Count |
|---|---|
| Corpus version / seed | 0.1 / 20260822 |
| Manifest buckets | 2 dirty · 2 new · 15 disagreement · 12 sample · 365 unreconciled |
| Rows adjudicated adversarially | 16 (15 disagreement rows + 1 sample row escalated: C-098) |
| **Proposed reclassifications** (both verdicts agree, ≠ standing) | **2** |
| **Unsettled** (verdicts split) | **2** |
| **Confirmed** (standing upheld) | **25** (12 adversarial · 11 sample · 2 dirty-resolved) |
| New-rule rows proposed for corpus entry | 2 |
| Family-map entries proposed | 275 (65 merged families · 209 singletons · 1 defective empty residual) |

---

## 2 · Proposed reclassifications

### C-078 — MACHINE → JUDGMENT
Both adversarial verdicts agree standing MACHINE is wrong.
- **Evidence (A):** Register row's own boundary clause — "this decision adopts a *direction and an order*, not a design — each arc opens with its own work and its own decisions." genesis.py enforces C-081/C-083 birth rules (GENESIS §6), not the program decision.
- **Evidence (B):** grep across all eight store tools finds nothing enforcing arc ordering; arc 2's specimen "fixed by Max's call"; arc 3 deferred on the specification-ahead-of-need discipline.
- **Diagnosis (both lanes concur):** the standing class mis-attributed arc-1's *product* (genesis.py) as the *program's* enforcer; strictest-tier keeping then inherited the error. Register-b's original JUDGMENT vote was correct.

### C-090 — MACHINE → HABIT (subclass: accidental)
Both adversarial verdicts agree standing MACHINE is wrong.
- **Evidence (A):** no code executes or verifies the mother-side anchor act (signed tag + OTS + committed receipt); close.py's receipt check (lines 955-964) guards the **mirror's** public chain — C-120's third preservation class, a different repository's duty; check_versions.py never scans Provenance/ (.txt/.ots outside SCAN_EXT). A missing beta-0.8 pair would trip nothing.
- **Evidence (B):** pack_mode ends at "Safe to tag (C-090)" (line 985) — tag, ots stamp, and receipt commit are hand-executed each release; Provenance/beta-0.1..0.7 pairs are ritual products. The C-064 precedent (code never invoked on the governing path) applies exactly.
- **Subclass rationale:** GENERATABLE — the mirror-side receipt-pair check proves the pattern is trivially checkable; a mother-side twin (every local `beta-*` tag must have a tracked `Provenance/<tag>.txt` + `.ots` pair) could ride `--pack` and none does. Likely origin of the standing error: conflation with C-116's tooled cleanliness gate (v0.58).

---

## 3 · Unsettled rows (owner adjudication required; standing class holds meanwhile)

### C-087 — standing MACHINE · A says HABIT-accidental, B says MACHINE
- **A (HABIT):** doctor.py's three-tier secrets scan is real but invoked on **no governing path** — close.py run_gates (line 273) runs only verify.py + check_versions.py (+ check_scan.py conditionally); /close never names doctor.py; no non-sample git hooks. C-064 precedent: present-but-unwired ≠ MACHINE. The .gitignore secrets entries are a structural sliver covering only the env-file path.
- **B (MACHINE):** the tool is the rule's *named* guard (Rule Overview: "Guard: doctor.py"), ratified, roster-configured, genesis-distributed into every newborn (genesis.py lines 48, 801, 929), and actually exercised network-wide 2026-08-22 (91 alarms → 2 real errors) — not the C-064 "never invoked" shape.
- **Crux for the owner:** does MACHINE require per-close wiring, or does ratified + distributed + exercised on-demand suffice? Both lanes note the dispute dissolves if doctor.py is wired into run_gates (the already-banked "doctor.py harvest" item).

### C-116 — standing MACHINE · A says HABIT-accidental, B says MACHINE
- **A (HABIT):** the rider's five executors (curated sync, mirror tag, OTS, push) are conduct under standing authorization — no code in close.py performs any of them; a **wholly-skipped rider passes every --pack check** (a clean stale mirror trips nothing; the new tag is simply absent from own_tags at line 955, so no missing pair). The gate guards quality-of-execution, never occurrence.
- **B (MACHINE):** the v0.58 tooling is real and mandated — pack_mode red-blocks a dirty mirror (lines 900-908), duplicate/iCloud-conflict names (909-920); /close step 3 requires `--pack` green pre-tag plus the `--mirror-only` re-run; the Register row itself records "the check is tooled."
- **Crux for the owner:** occurrence-vs-conformance — the same seam that decided C-090, but here a real gate sits on the path when the ritual runs.
- **Shared wart (both lanes, also seen at REG-custom-never-released):** `--pack`'s default `--mirror` path still points at pre-move `~/Desktop/fractal-mirror`; it fails closed ("mirror not found"), so enforcement is preserved, but the default is stale post-relocation.

---

## 4 · Confirmed rows

### 4a · Adversarially confirmed (both verdicts uphold standing) — 12
| Id | Class | One-line ground |
|---|---|---|
| C-005 | MACHINE | check_versions.py check A blocks stamp/filename disagreement and versioned living filenames at every close; create_mode refuses bad aliases |
| C-029 | STRUCTURAL | ChatGPT era physically fenced at Archive/; SKIP_DIRS + ERA_GUARD make violation require positive new work |
| C-047 | MACHINE | pair_half_gate (FN-0002): stale board stamp = blocking ERROR at every close |
| C-057 | MACHINE | verify.py delivers "evident, never hidden" (fold/chain/hash recompute); layers 1-2 (FileVault, 2FA) honest residue — host facts |
| C-059 | MACHINE | close.py walks the LC row table mechanically (C-110/C-112); judgment half reserved by declared boundary |
| C-066 | JUDGMENT | review-and-merge IS the rule; auto-merging on green would change its meaning |
| C-085 | STRUCTURAL | no personal-class member tracked since the C-098 annex move; a close cannot stage what the repo lacks |
| C-101 | MACHINE | genesis.py writes rail/scaffold/capture door/roster by construction — the artifacts cannot be skipped |
| C-117 | JUDGMENT | adoption sovereignty and the insufficient-green-checkers gate are designed reservation, not drift |
| C-120 | MACHINE | the historically-failing preservation clause (.github/, gh-pages, receipt pairs) red-blocked at --pack |
| C-127 | MACHINE | curated_exclusions reads .gitattributes export-ignore; any leak red-blocks the pack |
| C-098 | HABIT (necessity) | fresh JUDGMENT challenge **defeated 2-0**: the rule is a routing *default* kept in ordinary conduct; the owner's call (C-105 precedent) is the exception path, not the rule's content; "personal-class" too fuzzy for an honest detector |

### 4b · Sample rows — fresh class matched standing (a pass recorded as loudly as a failure) — 11
| Id | Class | Note |
|---|---|---|
| C-007 | STRUCTURAL | era split kept by tree shape; skipping is not checking, but nothing needs checking |
| C-025 | MACHINE | verify.py revise-chain / bijection / fold-equality / hash recompute, on the governing path |
| C-038 | HABIT (accidental) | **live lapse found:** Scan #6 contains no restore-drill section (zero "drill"/"laptop" hits) and check_scan.py has no drill check, so the gate stayed green through the lapse — surfaced for the owner |
| C-046 | MACHINE (MEDIUM) | route-alias layer machine-guarded; carve-out: the Index routing table's currency has no check — stays a hand row of the walk |
| C-048 | STRUCTURAL | since C-089 no non-repo display surface exists; residency cannot be violated by any existing mechanism |
| C-121 | MACHINE | fieldnote.py enforces one-buffer + pressure plug on the real path; ratification write-gate a deliberate judgment carve-out |
| ABF-active-offer | HABIT (necessity) | the trigger is a felt reading of conversation state; an automated nag would change the rule's meaning |
| DOMAIN-DISCIPLINE | HABIT (necessity) | no checker sees conversation content; inputs too fuzzy to mechanize honestly |
| LOOK-REPORT-STOP | JUDGMENT | mechanizing confirmation would make the C-094 ledger record repo state, not the owner's experience; caveat — the no-write perimeter alone is separately sandboxable |
| REG-custom-never-released | MACHINE | export-ignore + the S6-7.3 pack gate, fired at real packs; wart — stale `--mirror` default (fails closed) |
| UDP-felt-need | JUDGMENT | a tool anticipating need would commit the act the rule forbids |

### 4c · Dirty rows resolved — 2 (class unchanged; pin cure proposed)
- **C-026 — MACHINE (confirmed).** Dirty flag resolved: `vocabulary_local.json` is an optional extension hook, absent by design ("Absent file = inherited vocabulary exactly", verify.py:33, handled at :131). Not an enforcement gap. **Proposed pin cure:** evidence pin narrows to verify.py alone, dropping the optional file.
- **C-114 — MACHINE (confirmed).** Same resolution: the missing file is the hook's designed idle state; the gate sits on the only extension path (load_local_vocabulary, :118-150 — the corpus's cited "~130-146" match the live file). **Proposed pin cure:** same narrowing.

---

## 5 · New-rule rows proposed for corpus entry

- **C-032 — STRUCTURAL** (establishment/milestone row, flagged as such per the audit brief). Persisting content: the store's existence and two-directory shape (nodes/ + _events/), kept by file layout + git; tools self-anchor the layout (verify.py:153-156). The integrity discipline riding it is machine-kept **under C-049/C-050/C-055's own rows** — crediting verify.py here would double-count.
- **C-052 — STRUCTURAL** (history row — a one-time recording act, complete). The supersession record of the ChatGPT-era two-shell-classes model stands in Register:159 + Architecture State §3 + the frozen Archive corpus. The live face-doctrine belongs to C-017, already carried separately.

---

## 6 · Family-map summary

- **275 entries proposed: 65 merged families (157 member rows) + 209 singletons + 1 defective residual** — `GEN-no-biography` appears with an empty member list while its id rides the C-078 family; the empty row should be dropped at landing.
- **Checksum note:** member ids tally to 366 against the manifest's 365 unreconciled rows — a one-id tension the landing should re-verify mechanically before adoption (this assembly is hand-counted).
- **Largest families:** C-047 (5: the board's projection/stamp/regen clauses + walk row) · five 4-member families: C-027 (facet mint/immutability/prefix), C-066 (drone tier), C-078 (kernel birth + inheritance clause), C-091 (reference-copy + standing checks), C-131 (seed-tree) · fourteen 3-member families (incl. ORIENT-FIRST, C-037, C-050/C-060, C-059, C-064, C-076, C-116, C-121, C-127).
- **Adjudicated A/B disagreements (24):** merges decided **for** — CLOSE-6-REPORT→C-059, CLOSE-3-STAMP→C-073, GEN-adapter-commands→C-083, GEN-no-biography→C-078, FN-TOOL-WRITE→C-100, MRC-SCOPE-BIND→C-132, KMP-semantic-checks→C-117, ABF-derived→C-047 (not C-003), WELCOME/BEGIN-STANDING→C-091, BEGIN-HANDOFF→ONB-jurisdiction (not ONB-handoff), ORIENT-FIRST canonical over C-001. Merges decided **against** (kept singleton) — C-001 (umbrella spans several rules), C-084 (own decision; compound row rides C-037), C-066-STOP, CS-INJECTION, CLOSE-1-JUDGE (vs C-033), WALK-BOOTSTRAP (vs C-038), WALK-ARCH-STATE (vs C-051), SCAN-commissioned (vs C-108), REG-sovereign-adoption (vs C-113), DIET-fact-presence (vs C-125), WELCOME-RESTRAINT (spans two families), and C-123's four IPF rows (canonization-vs-internals treatment applied consistently with C-104/C-111/C-113/C-100).
- **Forced-merge check: pass with one defect.** No family fuses distinct rules — umbrella rows (C-001), compound rows (C-037/C-084, C-116/C-120, C-050/C-060) and per-jurisdiction principle instances (data-not-instruction ×3, felt-need cluster, sovereign-adoption pair) all kept separate on stated grounds. The one defect is the empty GEN-no-biography residual above.

---

## 7 · What did not move, and why

- **The 25 confirmed rows** — standing classes untouched; C-026/C-114 keep their class with only an evidence-pin narrowing proposed.
- **C-087 and C-116** — unsettled rows never move; standing MACHINE holds for both until the owner adjudicates the occurrence-vs-conformance seam. Both come with a cheap dissolution path (wire doctor.py into run_gates; script the rider or add an occurrence check).
- **C-098** — the fresh JUDGMENT challenge lost 2-0; HABIT-necessity stands. Reclassifying on the exception path would hollow the HABIT/JUDGMENT boundary for every flag-on-doubt rule.
- **The family map** — binds nothing; every merge/singleton is a proposal, including the 24 adjudications.
- **Findings surfaced but not disposed** (owner's call, per the always-flag practice): the Scan #6 restore-drill lapse + check_scan.py's missing drill-section check (C-038); the stale `--pack --mirror` default (fails closed, so enforcement preserved); the C-026/C-114 pin narrowing.

---

## Landing verification (mechanical, run at freeze — the assembler's own request)

The report's §6 checksum note ("member ids tally to 366 against the manifest's 365 — re-verify mechanically before adoption") was executed at landing: **366 member ids = 365 corpus rows + C-072** (the retired row, absorbed by a family though the manifest excludes it — disposition open) · **zero duplicates** across families · **zero corpus rows unassigned** · the **empty `GEN-no-biography` entry confirmed** as the map's single structural defect (its id rides the C-078 family; drop proposed). The family map lands as `Claude/Project Governance/Rule Corpus/family_map_proposal.json` (Draft, proposal-only), the verification result recorded in its provenance block.

---

*Frozen at issue. Per-agent evidence: the flight journal (`wf_18ab3e9f-409/journal.jsonl`, session-local). Dispositions: none at issue — the proposed reclassifications (C-078, C-090), the unsettled rows (C-087, C-116 — the occurrence-vs-conformance seam), the pin cures (C-026/C-114), the new rows (C-032, C-052), the family map, and the surfaced findings (the Scan #6 restore-drill lapse · the stale `--pack --mirror` default) all await Max's response; whatever he directs enters the record through the session's close, never by editing this file. Ratified deltas update `rule_corpus.json` with a version bump — the update loop's second half.*
