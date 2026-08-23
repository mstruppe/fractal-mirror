# Review — The Scope-Axis Flight (the manifest's raw material; the landing)

> **DERIVED REVIEW RECORD — frozen at issue; PROPOSAL-ONLY (Ultracode Flight Protocol v0.2: the landing binds nothing — every disposition below is Max's).** Commission: Max, the thirty-seventh session, 2026-08-22 — the beta-0.8 chain's link 2, launched on his "go" after the contract's presentation (the two-turn rule honored): sort every rule family on the scope axis (KERNEL travels as shipped · PARAMETRIC mechanism travels, value local · CUSTOM never travels) and the Kernel-Layer Doctrine's layer bit (ENGINE swap-freely · CONTRACT break-is-major), ground-truthed against the network's only real adoption records — KNet's two migrations and PR's birth tree.

**Issued:** 2026-08-22 · **Document ID:** DOC-01M0NBGK14NYXWGSPG9JFT4SGN (minted at this close via `close.py --create`) · **Session:** the thirty-seventh (mother) · **Flight shape:** 11 agents, 4 phases (Sort 6 · Ground-truth 2 · Refute 2 · Assemble 1), read-only throughout — C-091/C-096 conduct in the children's trees — zero failures · **Gas (§7.2 honesty accounting):** 1,478,761 tokens vs the 0.9–1.3M estimate (**×1.14 over the upper bound** — the overrun honest and recorded; basis was the audit flight's 1.10M/10 agents, and the ground-truth verifiers' full-tree reads in two child jurisdictions cost more than the scoped audit reads) · 215 tool calls · ≈49 minutes · **Verification tier:** ground-truth crossmatch (550 verdicts) + adversarial pair with opposite mandates over all 54 disputes.

**The data of record:** the complete 275-row sort, all 550 ground-truth verdicts, and both adversarial verdict sets land beside the corpus as `Claude/Project Governance/Rule Corpus/scope_axis_sort.json` (Draft, proposal-only) — including the ~95 undisputed rows beyond the assembler's input slice, per the report's own §7 instruction that they be appended verbatim before the ratification pass. The report below is the assembled reading; the JSON is the complete inventory.

---

# Scope-Axis Flight — Landing Report (PROPOSAL-ONLY)

**Status:** Every disposition below is a proposal for the owner. Nothing here binds any jurisdiction — not the mother's, not KNet's, not PR's. This is the raw material of the birth-state manifest (Birth-State Proposal item 3) plus the Kernel-Layer Doctrine's layer bit.

**Coverage note (data honesty):** the assembler's input slice carried the sorted rows through `C-131` (90 KB boundary) and the ground-truth rows through `KMP-receipt-artifact` (40 KB boundary). All 54 disputed families arrived complete via the adversarial pair, so every dispute is fully adjudicated below. Of the 275 sorted families, **180 are enumerable in this report** (134 sorted rows in full + 46 dispute-only rows beyond the slice); the remaining ~95 undisputed rows (the `CS-*`, `FN-*`, `GEN-*`, `IPF-*`, `KMP-*`, `CLOSE-1/3`, `C-132/C-133`, `DRONE-*`, `FACET-*` blocks and kin) land at the sorter's call per the rules and ride complete in the flight's `sorted` return value; their ground-truth annotations, where visible, are folded into §4 and §7.

---

## 1 · Headline counts

| Bucket | Count (enumerable set, n=180) |
|---|---|
| KERNEL | **84** (79 CONTRACT · 5 ENGINE) |
| PARAMETRIC | **14** (11 CONTRACT · 2 ENGINE · 1 layer-open) |
| SPLIT (members land differently; traveling halves in §2) | **18** |
| CUSTOM (never travels) | **48** |
| **UNSETTLED** (adversaries disagree — owner's call) | **16 scope + 1 layer-only** |

**Dispute pipeline:** 54 families disputed (ground-truth contradictions + low-confidence rows) → adversarial pair agreed on 37 (**33 sorter upheld, 4 sorter corrected**) → 17 items left unsettled.

**The four corrections the pair agreed on (proposal: adopt):**
- `C-073` flat KERNEL/ENGINE → **SPLIT** (close-mechanics doctrine KERNEL/CONTRACT via the born RO row + §3.4 clause; close.py tier-1 ENGINE, shelf-adopted, never birth-shipped)
- `C-118` flat KERNEL/ENGINE → **SPLIT** (the §12-gate doctrine KERNEL/CONTRACT via the byte-born RO row; check_scan.py ENGINE travels only with Scan adoption)
- `CLOSE-0-ORIENTED` KERNEL/ENGINE → **CUSTOM** (close.md exists only mother-side; /close deliberately not shipped, GENESIS §3.6)
- `LOOK-ORIENT-TARGET` KERNEL/ENGINE → **CUSTOM** (look.md mother-only, skill tier, not tier-0; the read-don't-scan substance travels separately as adapter rule 1)

---

## 2 · THE MANIFEST DRAFT

The packing list genesis and the KMP will consume. Path legend: **GOV** = `Claude/Project Governance/Governance Documents/`, **KG** = `Claude/Architecture/Concepts/Knowledge Graph/`, **STORE** = `Claude/Knowledge Graph Store/`, **TPL** = `Templates/`, root files as named.

### 2.1 KERNEL / CONTRACT

| Family | Carrier files | Pinned edition | Note |
|---|---|---|---|
| ABF-adoption | GOV Agenda_Board_Format_v0.3, TPL Board_Seed_v0.0, STORE genesis.py | ABF v0.3; Seed v0.0 | adoption-by-own-decision half is the rule's own text |
| ABF-bar | GOV ABF v0.3, TPL Board Seed | ABF v0.3 | |
| ABF-next-card | GOV ABF v0.3, TPL Board Seed | ABF v0.3 | |
| ABF-section-grammar | GOV ABF v0.3, TPL Board Seed | ABF v0.3 | |
| C-001 | GOV Conversation_Settings, GOV Rule_Overview, genesis.py | Settings stamp read live (v0.8 today) | close.py mechanization deliberately tier-1 |
| C-003 | Settings, Rule_Overview, STORE check_versions.py, genesis.py | — | |
| C-004 | Settings, Rule_Overview | — | remembered discipline, unenforced everywhere |
| C-006 | GENESIS.md, genesis.py | — | thin carrier: clause-inherited only |
| C-008 | Settings, genesis.py | — | child born fully ask-first, zero standing authorizations |
| C-009 | genesis.py, Settings | — | spine by construction |
| C-011 | genesis.py, GENESIS.md, Settings | — | |
| C-012 | check_versions.py, genesis.py, Settings | — | checker adoption stays the child's decision (C-081) |
| C-014 | KG Schema_v0.7, STORE verify.py | Schema v0.7 | |
| C-015 | Schema, verify.py, genesis.py | Schema v0.7 | |
| C-016 | Schema, verify.py, genesis.py | Schema v0.7 | facet structure minted at birth |
| C-017 (MEDIUM) | Schema, GENESIS.md | Schema v0.7 | thin: AST §3 home does not travel |
| C-018 | Rule_Overview, genesis.py | — | |
| C-019 | Rule_Overview, verify.py | — | |
| C-020 | genesis.py, Rule_Overview | — | |
| C-022 | Schema, KG Node_Template_v0.5, verify.py | Schema v0.7; Template v0.5 | |
| C-023 | Schema, verify.py, STORE mint.py | Schema v0.7 | |
| C-024 | Schema, verify.py, genesis.py | Schema v0.7 | baseline re-bound to child's genesis commit |
| C-025 | Schema, verify.py | Schema v0.7 | |
| C-026 | verify.py, Schema | Schema v0.7 | vocabulary_local.json absent-by-design at birth |
| C-027 | mint.py, verify.py, Schema | Schema v0.7 | |
| C-028 | genesis.py, GENESIS.md | — | Register born at P-001 |
| C-031 | Settings, genesis.py | — | report-stop law template-instantiated |
| C-033 | Rule_Overview, GENESIS.md, Settings | — | review act generalizes to the instance owner |
| C-034 | Rule_Overview, GENESIS.md | — | |
| C-041 | Schema, verify.py | Schema v0.7 | mechanization half tier-1 |
| C-042 | Rule_Overview, GENESIS.md | — | judgment-class everywhere |
| C-043 | Schema, verify.py, mint.py, genesis.py | Schema v0.7 | |
| C-044 | Schema, verify.py, mint.py | Schema v0.7 | |
| C-045 | Schema, verify.py, mint.py | Schema v0.7 | |
| C-048 | ABF v0.3, Board Seed, genesis.py | ABF v0.3; seed v0.0 | |
| C-049 | Schema, verify.py, mint.py, genesis.py | Schema v0.7 | |
| C-055 | Schema, verify.py, mint.py, genesis.py | Schema v0.7 | roll ceremony human by design |
| C-057 (MEDIUM) | Rule_Overview, verify.py, STORE doctor.py, GENESIS.md | — | custody values owner-environment facts |
| C-061 (MEDIUM) | Schema, verify.py, GENESIS.md | Schema v0.7 | executing ripple tier-1 |
| C-065 | genesis.py, Settings, check_versions.py | Settings stamp live | |
| C-066 (MEDIUM) | Rule_Overview, Settings, GENESIS.md | — | apparatus §5 shelf |
| C-067 | genesis.py, Settings, Rule_Overview | — | true by construction |
| C-068 | KG Navigation_Contract_v0.2, genesis.py | NC v0.2 (pins release-relative — PR lawfully carries v0.1) | |
| C-069 | Navigation_Contract | NC v0.2 | contract only, no implementation ships anywhere |
| C-070 | Schema + Navigation_Contract | Schema v0.7 + NC v0.2 | |
| C-071 | Settings, check_versions.py, genesis.py | — | |
| C-075 (MEDIUM) | Rule_Overview, Settings, GENESIS.md | — | binds on drone-tier adoption |
| C-076 (MEDIUM) | Rule_Overview, genesis.py, GENESIS.md | — | drill fires by commission only |
| C-077 | genesis.py, Settings, check_versions.py | — | |
| C-079 | genesis.py, GENESIS.md, Navigation_Contract | — | tier-0 birth, add on felt absence |
| C-080 | check_versions.py, genesis.py | — | |
| C-082 (MEDIUM) | Settings, Rule_Overview, GENESIS.md | — | binds at drone launch |
| C-083 | genesis.py, GENESIS.md | — | no SKILL.md class exists |
| C-084 | genesis.py, Settings, Rule_Overview | — | writer values are C-037's parameter |
| C-085 | Rule_Overview, Settings, genesis.py | — | |
| C-086 | Rule_Overview, Settings | — | class rule travels; tissue grows locally |
| C-091 | Settings, Rule_Overview, GENESIS.md | — | constitutional, not mechanical, by design |
| C-092 | Settings, Rule_Overview, Registry/README.md | — | |
| C-094 | Rule_Overview | — | |
| C-095 | Rule_Overview | — | measuring trigger tier-1 |
| C-096 | Rule_Overview | — | /look script mother-surface, not shipped |
| C-099 | LICENSE, LICENSE-docs, NOTICE | Apache-2.0 (tools) + CC BY 4.0 (docs) | name/marks deliberately unlicensed |
| C-102 | ABF v0.3, Rule_Overview | ABF v0.3 | |
| C-103 (MEDIUM) | Rule_Overview | — | thin: method's full shape lives in mother precedent |
| C-104 | ABF v0.3, Board Seed | ABF v0.3 | |
| C-108 | Rule_Overview; Flight_Protocol_v0.2 + Scan_Procedure_v0.1 via shelf | UFP v0.2 · SP v0.1 | standards ride pinned release/Registry, not the genesis copy set |
| C-109 | Rule_Overview | — | structural wherever exercised |
| C-110 | Rule_Overview | — | SPINE-BUDGETS tool half tier-1 |
| C-113 | Rule_Overview; Registry/README.md via pinned release | — | sovereign-adoption clause is content, not a gap |
| C-117 | Rule_Overview, GENESIS.md; KMP_v0.1 via shelf | KMP v0.1 | |
| C-122 | GOV Pair_Procedure_v0.3 | UDP v0.3 | |
| C-123 | GOV Interface_Place_Format_v0.1, genesis.py | IPF v0.1 | Interface/ born at IF-0000 |
| C-124 | Pair_Procedure_v0.3, genesis.py | UDP v0.3 | trio's user halves born |
| C-125 | Pair_Procedure_v0.3, Rule_Overview | UDP v0.3 | |
| C-126 | Pair_Procedure_v0.3 §2, genesis.py | UDP v0.3 | |
| C-128 | ABF v0.3, Rule_Overview | ABF v0.3 | |
| C-131 | TPL README + four v0.0 seeds, genesis.py, UDP v0.3 | seeds v0.0 (frozen editions) | genesis dies on missing Templates/ |
| WS-OPEN | Rule_Overview | — | settled by adversarial agreement |
| LEDGER-POINTER | Rule_Overview; genesis.py (Active-Return pointer, four template sites at HEAD) | — | PR's missing pointer is pre-F2-cure release lag, not kernel truth — cure at PR's next migration |

### 2.2 KERNEL / ENGINE

| Family | Carrier files | Note |
|---|---|---|
| C-050 | verify.py, genesis.py | mandatory from birth; genesis runs it at write_plan |
| C-081 | genesis.py, GENESIS.md | verify.py alone gates a newborn; check_versions never demanded |
| C-088 | check_versions.py, genesis.py | .inherited manifest written at every birth |
| C-121 | fieldnote.py, Fieldnote_Format_v0.2 (CONTRACT half rides beside), TPL Buffer_Seed_v0.0 | settled upheld; KNet's conduct CONFLICTs are a pre-doctrine child's sovereign divergence, not a transport fact |
| ONB-rail | genesis.py (first_loops_rail + opener step 4) | settled upheld; self-retiring birth apparatus; name/opener fills are ordinary §2 values riding a kernel template |

### 2.3 PARAMETRIC (mechanism travels, value bound at birth)

| Family | Instance value | Layer | Carrier files |
|---|---|---|---|
| C-005 | name prefix | CONTRACT | check_versions.py, Settings, genesis.py, GENESIS.md |
| C-037 | writer identities/emails | CONTRACT | genesis.py, Settings, Rule_Overview, GENESIS.md |
| C-038 | bootstrap content | CONTRACT | genesis.py, GENESIS.md |
| C-046 | route/domain codes | CONTRACT | genesis.py, GENESIS.md, Schema, verify.py |
| C-056 | remote (or none) | CONTRACT | genesis.py, GENESIS.md, Rule_Overview |
| C-059 | close-checklist rows | CONTRACT | genesis.py, GENESIS.md, Settings, Rule_Overview |
| C-062 | pre-canon set (FIELDNOTES.md born first member) | CONTRACT | genesis.py, GENESIS.md, Buffer_Seed v0.0, Settings |
| C-087 | credential inventory | CONTRACT | genesis.py, doctor.py, GENESIS.md |
| C-090 | anchor-authority set (parameter 9) | CONTRACT | Rule_Overview, GENESIS.md — enforcement half (close.py --pack) mother tier-1 |
| C-060 | .version-registry / .inherited projections | ENGINE | check_versions.py, genesis.py |
| C-074 (MEDIUM) | custody/signing values | ENGINE | doctor.py, Rule_Overview, GENESIS.md |
| LOOK-RATIFY-MAX | owner value | CONTRACT | Rule_Overview (C-096 row) — settled |
| LOOK-REPORT-STOP | owner value | CONTRACT | Rule_Overview + shipped fieldnote apparatus — settled |
| LOOK-ROSTER | roster rows | **layer UNSETTLED** (§5) | Rule_Overview |

### 2.4 SPLIT families (traveling halves belong in the manifest)

| Family | Split (one line) |
|---|---|
| C-010 | rule + global-shape → KERNEL (RO §2 + genesis global_context); WALK-GLOBAL-CONTEXT → PARAMETRIC (parameter-6 row) |
| C-030 | Register-as-spine-member → KERNEL; WALK-REGISTER → PARAMETRIC (parameter-6 row) |
| C-035 | Settings + live-stamp adapter machinery → KERNEL; CMD-STAMP-REFRESH → does not travel (mother habit) |
| C-036 | Rule_Overview byte-ships → KERNEL; WALK-RULE-OVERVIEW → child's own binding |
| C-040 | format pins machine-enforced → KERNEL (Schema v0.7 + Template v0.5); WALK-SCHEMA-TEMPLATE → not shipped |
| C-047 | Board Format + seed + stamp walk → KERNEL/CONTRACT; WALK-AGENDA-BOARD → mother wiring |
| C-050/C-060 | **settled upheld:** verify half birth-mandatory KERNEL/ENGINE; check_versions half ships adoption-gated (C-081); CLOSE-4-GATES mother tier-1. KNet's B07-07 "never byte-copy" is the pre-C-088-cure state — superseded by the externalized .version-registry |
| C-058 | class doctrine + hash-freeze (verify check E) → KERNEL; Scan Procedure + check_scan → shelf |
| C-073 | **corrected to SPLIT:** doctrine KERNEL/CONTRACT (RO close-mechanics row); close.py tier-1 ENGINE shelf |
| C-078 | C-078 row + pin-currency habit → CUSTOM; GEN-kernel-copy + GEN-no-biography → KERNEL/ENGINE (genesis.py + GENESIS §1/§4) |
| C-100 | fieldnote.py KERNEL/ENGINE; Formats v0.2+v0.1 KERNEL/CONTRACT; fieldnote_roster.json PARAMETRIC |
| C-101 | Onboarding Protocol + /begin + genesis.py = release-copy birth ENGINE (never in the child); stage-two rail = PARAMETRIC genesis instantiation |
| C-106 | named opener PARAMETRIC/ENGINE (value = instance name, fallback /orient); one-loop rule KERNEL/CONTRACT |
| C-111 | Diet Procedure standard KERNEL/CONTRACT via shelf; procedures blog CUSTOM |
| C-112 | adaptive-close doctrine KERNEL/CONTRACT; close.py + close.md tier-1 ENGINE shelf |
| C-114 | verify.py hook KERNEL/ENGINE; vocabulary_local.json PARAMETRIC (designed idle = absent); Procedure doc via shelf |
| C-118 | **corrected to SPLIT:** §12-gate doctrine KERNEL/CONTRACT (RO row byte-born); check_scan.py ENGINE shelf-only |
| C-127 | five-category taxonomy KERNEL/CONTRACT; pack-gate enforcement mother tier-1 ENGINE |

*(Beyond the slice, the ground record marks `C-132` "Exact SPLIT match" — its full sorted row rides the flight's return value, as do the undisputed `CS-*`, `FN-*`, `GEN-parameters`/`GEN-remote`, `IPF-*`, `KMP-*` rows, all ground-AGREEd where visible.)*

---

## 3 · The CUSTOM roster (never travels)

**Mother biography — decision rows, history, eras:** C-002, C-007, C-013, C-021 (philosophy travels re-expressed via RO/GENESIS §5), C-029, C-032 (shape lands as C-022/23/24 law, row never does), C-051, C-052, C-089, C-093, C-107.

**Mother distribution/public posture:** C-064 (standing push — a child's promotion is its own P-decision), C-098 (annex), C-105 (mirror-as-home), C-116 (mirror rider), C-119/C-120 (site, go-live), C-129 (Gas Ledger), C-130 (site sections).

**Mother apparatus that never enters a child tree (adversarially settled):** BEGIN-COLD-ARRIVAL, CLOSE-0-ORIENTED, LOOK-ORIENT-TARGET, ONB-inline-preanswers, ONB-instrumentation, ONB-jurisdiction, ONB-never-fork, ONB-one-question, ONB-perform, ONB-real-first-loop (outputs travel via the parametric channel: --vision/--focus/--human-email).

**Shelf-standard clauses whose only carrier is a not-birth-shipped document (adversarially settled):** DIET-measurement, DIET-provenance-note, DIET-slate-classes; all sixteen SCAN-* families (birth-test, commissioned, conduct-guards, drop-unreproduced, evidence-verify, finding-anatomy, forward-open, id-grammar, mandate-surface, method-guard-decl, non-findings, report-format, residue, severity, slate-call, state-block). A child reaches these only by its own recorded shelf adoption — the CUSTOM parenthetical's origin-reference channel, which is exactly how knet holds them.

---

## 4 · Ground-truth scorecard

Of the ground rows that reached the assembler (~200, KNet's adoption record in full, PR's birth record partially):

- **AGREE ≈ 111** (KNet half alone) — the sort predicted KNet's real dispositions with striking fidelity: every EXCLUDE the sort called CUSTOM (C-093, C-098, C-105, C-107, C-116, C-119, C-120, C-129, C-130), every SPLIT matched exactly (C-100, C-106, C-111, C-114, C-132 "exact SPLIT match"), and the parameter class behaved as parameters (C-037 writers, C-056 remote, C-059 checklist, C-087 inventory, C-090 anchor, GEN-parameters "the binding maps ARE the parameter class living per-jurisdiction").
- **CONTRADICT = 12 visible** (C-050/C-060, C-115, C-118, C-121, eight DIET rows) plus the PR-side challenges that drove the rest of the 54-family dispute set.
- **SILENT ≈ 75** — overwhelmingly the pre-C-091 birth-span block (§7).

**Contradictions refuted (sorter vindicated, 33):** C-050/C-060 (KNet's "never byte-copy" dated from before the C-088 registry-externalization cure), C-121 (KNet's conduct CONFLICTs are a pre-doctrine child's lawful divergence; PR, the post-doctrine newborn, was born with the full apparatus), the three settled DIET rows and all sixteen SCAN rows (`.inherited` residence is Registry §1.5 *adoption*, not birth transport — the challenge's ".inherited row → travels" inference was refuted by the Registry's own text), WS-OPEN, LEDGER-POINTER (PR's gap dates the F2 cure rather than refuting the classification), the seven ONB rows, ONB-rail, the three LOOK conduct rows (scope).

**Contradictions cured (sorter corrected, 4):** C-073, C-118, CLOSE-0-ORIENTED, LOOK-ORIENT-TARGET — all four the same defect class: a flat KERNEL/ENGINE label on machinery that GENESIS §3.6/§5 deliberately keeps on the tier-1 shelf while only the doctrine text is born.

**Contradictions unresolved:** 16 + 1 layer → §5.

---

## 5 · Unsettled families — for the owner

Seventeen items, but only **four underlying questions**. Deciding each question once disposes of its whole block.

**Q1 — When a Rule Overview row restates a shelf standard's norm, is the family SPLIT-kernel or CUSTOM?** *(9 families)*
`DIET-behaviour-test, DIET-commissioned, DIET-fact-presence, DIET-gauge, DIET-pointer-grammar` · `REG-checker-named, REG-growth-by-decision, REG-honest-status, REG-sovereign-adoption`
- Position A (anti-sort): SPLIT — the norm is byte-born in every child via RO rows 51/52/62 (and Pair Procedure v0.3 §3.4 for the diet norms); only the full clause text is shelf-tier. For REG-sovereign-adoption the residence machinery (genesis-written .inherited + shipped check_versions) is additionally born.
- Position B (pro-sort): CUSTOM — the RO carriage belongs to the sibling families already sorted kernel (C-095/C-110/C-111/C-113/C-092); counting it again here double-books one carrier, and the clause documents demonstrably do not ship (absent from the KERNEL tuple and from PR).
- The owner's call is really a *bookkeeping convention*: whether a norm's kernel carriage is credited to the family that names the clause or to the family that owns the carrier row. Either answer is internally consistent; mixing them is not.

**Q2 — Are the genesis-hard-coded default checklist rows KERNEL template text or PARAMETRIC parameter-6 values?** *(3 families)*
`WALK-BOOTSTRAP, WALK-CONTEXT-INDEX, WALK-LOCAL-CONTEXT`
- Position A: PARAMETRIC/CONTRACT — one template line in `decision_register()` writes all the rows; GENESIS §2 row 6 declares the row set an instance value; the sort already labels this line's row-mates PARAMETRIC, and splitting one line across two scopes is refuted by the single template site.
- Position B: KERNEL/CONTRACT — no CLI flag exists, nothing is filled at birth; the rubric's PARAMETRIC requires a birth-filled value, and a post-birth re-binding right is just sovereignty over inherited law. If there is an inconsistency it indicts the PARAMETRIC line-mates.
- Note: both adversaries agree the *line-mates must land together* — the owner is choosing which side of the sort's own internal inconsistency to cure.

**Q3 — Rules whose only full text lives in unshipped mother projections (AGENTS.md) but whose substance is inherited law:** *(2 families)*
`C-066-STOP` (A: CUSTOM, no born carrier; B: KERNEL/CONTRACT — the general C-066/C-084 reservation is byte-born and the rule re-materializes at any drone-adapter forging) · `C-084-DRONE` (same shape; the sorter's own LOW confidence flagged it).

**Q4 — Doctrine-kernel vs document-shelf on flat labels:** *(2 families)*
`C-097` (A: SPLIT — RO doctrine row born, but Fractal_Client_Library.md is not in the KERNEL tuple and absent from PR; B: flat KERNEL/CONTRACT stands, the carriage observation was already in the sorted row and the RO wording defect is a blemish, not a misclassification) · `C-115` (A: SPLIT — materials rule kernel, Convention shelf-tier per RO row 67's own words and KNet's DEFER/CONFLICT; B: flat KERNEL/CONTRACT with the class-kernel/members-shelf caveat already recorded).

**Layer-only:** `LOOK-ROSTER` — scope settled PARAMETRIC; A says CONTRACT (what travels is rule-book text, no look engine ships), B says ENGINE (the roster-config class genesis demonstrably parameterizes, e.g. fieldnote_roster.json).

---

## 6 · Where the two children's records disagree between themselves — the seam signal

1. **check_versions.py portability.** KNet's beta-0.5 record says "contains mother paths … never byte-copy" (B07-07); PR's birth shows the identical bytes running clean against a genesis-generated `.version-registry`. Not a contradiction of fact but of **date**: the C-088 registry-externalization cure landed between the two records. Seam signal: *a child's frozen assessment can outlive the defect it describes* — the KMP has no mechanism to expire superseded findings, and a future migration advisory could re-assert a cured objection.
2. **The Active-Return pointer (LEDGER-POINTER).** KNet's Local Context was re-pointed at the F2 cure (this close's own act); PR, born one day pre-cure, has no pointer at all. Both lawful; the seam is **release lag as a standing class** — every kernel cure creates a window where the newest child is behind HEAD, and nothing but the child's next migration closes it.
3. **Fieldnote conduct (C-121).** PR is born on Format v0.2 whole; KNet lawfully retains v0.1 conduct with recorded CONFLICTs. The network now runs two fieldnote conduct regimes by birth-date — sovereign, but a cross-instance reader must know which regime governs which ledger.
4. **Shelf holdings diverge by channel.** knet holds Diet, Scan, Onboarding, Registry, Client Library, KMP, Vocabulary, and the Convention via `.inherited` adoption; PR holds none of them. Same law, different exposure — exactly what the adoption channel predicts, but it means "does a child have document X" is never evidence about the kernel without asking *which channel* delivered it. This single confusion drove all sixteen SCAN and eight DIET ground contradictions.
5. **Navigation Contract pins.** PR carries v0.1, the mother now ships v0.2 (F8 cure) — pins are release-relative by design; noted so nobody reads it as drift.

---

## 7 · What did not move / silent families

- **The pre-C-091 birth-span block (~60 families, C-001 through C-089's odd rows):** KNet predates the migration-matrix era for these — its record simply has no rows. PR's tree confirms them by construction wherever the birth verifier looked. Silence here is expected, not evidentiary weakness; the sorter's calls stand ground-annotated as SILENT.
- **Conduct practiced but never dispositioned by number:** C-004 ordering, C-025 commit boundaries, C-071 source-first, CLOSE-3-PACK (KNet writes its own Return Packages — the practice is live child-side, the family row silent), KMP practice rows exercised twice without ever being C-numbered dispositions.
- **Mother-only apparatus no child record could see:** DRONE-HANDBACK, DRONE-ORIENT, FACET-HONEST-WEIGHT, FACET-LABEL-SEP, FN-NO-COMMIT, DELETIONS-ALLOWED, DOMAIN-DISCIPLINE, GEN-clause-seed/first-close/manual-normative/no-federation/root-rationale/tiering/version-relationship, DIET-finding-ids, DIET-records.
- **The ~95 undisputed rows beyond the assembler's input slice** (CS-*, FN-*, IPF-*, KMP-*, C-132/C-133 and kin): land at the sorter's call per the rules; every visible ground verdict on them is AGREE (the FN, IPF, and KMP blocks agreed wholesale, FN-config "Exactly PARAMETRIC", KMP exercised twice end-to-end). Their full sorted rows ride the flight's `sorted` return value and should be appended verbatim to this manifest draft before the owner's ratification pass.

---

*Proposal-only. The manifest draft (§2) is the packing list; the four corrections (§1) and seventeen unsettled items (§5) are the owner's queue; the five seam signals (§6) are candidates for the fieldnote buffer at the owner's discretion.*

---

*Frozen at issue. Dispositions: none at issue — the four agreed corrections, the seventeen unsettled families (four questions + one layer call, §5), the manifest draft (§2), and the five seam signals (§6) all await Max's response; whatever he directs enters the record through the session's close, never by editing this file. The ratified sort becomes the birth-state manifest's authoring input (Birth-State Proposal item 3 + the Kernel-Layer Doctrine's layer bit) — the beta-0.8 chain's link 3.*
