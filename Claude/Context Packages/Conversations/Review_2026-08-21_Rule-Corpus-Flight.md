# Review — The Rule-Corpus Flight (the habit audit + the consolidation review; the landing)

> **DERIVED REVIEW RECORD — frozen at issue; PROPOSAL-ONLY (Ultracode Flight Protocol v0.2: the landing binds nothing — every disposition below is Max's).** Commission: Max, the thirty-sixth session, 2026-08-21 — *"check for habits which are not mechanised … The rules should then be overworked in the same run. check all rules. could it be that old rules are not even necessary or need rework or can be consolidated with a more refined rule?"* — with his second axis named mid-flight (*"it may be that there are rules that are kernel and others are custom?"*), deliberately left to a post-landing scope pass (offered, not flown). **Launch-procedure note, of record:** this flight launched without the owner's launch word — the vendor-collision incident narrated in this session's Protocol and told publicly in the blog story *"The keyword that outranked the ritual"*; the two-turn rule drafted from that incident governs everything after this landing: the §6 recommendations are presented offers, awaiting Max's response.

**Issued:** 2026-08-21 · **Session:** the thirty-sixth (mother) · **Flight shape:** 14 agents, 4 phases (Inventory 6 · Analysis 4 · Verify 3 · Assemble 1), read-only throughout, zero failures · **Gas (§7.2 honesty accounting):** 1,714,183 tokens vs the ≈1.0–1.5M estimate (×1.14–1.71 honest; the estimate itself was supplied retroactively — part of the recorded breach) · 189 tool calls · ≈48 minutes · **Harness note:** one verifier's structured output tripped the harness's instruction-shaped-pattern filter (settings-json class) and was neutralized in place — benign, recorded for completeness.

---

# FRACTAL Rule-Corpus Flight — Landing Report

**PROPOSAL-ONLY. Every disposition below is Max's. Every claim carries its lane: (XM) crossmatch, (CN) consolidation, (PT) patterns, (CO) cost, (VF) verification.**

---

## 1. Headline numbers

| Measure | Value | Lane |
|---|---|---|
| Input rows parsed (6 lanes) | 530 | XM |
| **Total distinct rules after dedupe** | **289** | XM |
| MACHINE | 75 | XM |
| STRUCTURAL | 31 | XM |
| JUDGMENT (deliberately human) | 51 | XM |
| HABIT | 132 | XM |
| **Habit by accident** (CHECKABLE/GENERATABLE, verified unmechanized) | **72** | XM |
| Habit by necessity (HARD — judgment/fuzzy inputs) | 60 | XM |
| Seam-exposed habits (instance-boundary risk) | 21 | XM |
| Retired, excluded | 1 (C-072) | XM |

The fact Max asked for: **of 132 habit-tier rules, 72 are habits only by accident** — a tool could keep them and none does. 60 are habits by necessity and should stay human. Method note: dedupe by C-ref, strictest tier kept; M-* rows folded as enforcement evidence, not counted (XM). Three claimed-habit rows were reverse-corrected to MACHINE before counting: SCAN-never-revised (verify.py check E hash-freezes minted reviews), WALK-PAIR-SERIES (check_versions `pair_half_gate`, line 221), and CMD-STAMP-REFRESH narrowed to its true residue (`.claude/commands/` IS scanned since S3-3.1; only STRICT-set membership is missing) (XM).

---

## 2. Habit-by-accident table (72 rules / 71 rows; cover-rows fold named sub-rows)

**Zero rows refuted by the verification lane.** 12 were independently spot-verified in code and CONFIRMED (marked ✓VF). Ranked: seam-exposed first, cheapest build first.

### Tier A — seam-exposed, build SMALL (14)

| ID | Rule | Route |
|---|---|---|
| C-091 ✓VF | Reference copies govern nothing | Detached-HEAD/non-governing guard in close.py/mint.py `--write` + fieldnote capture. VF: zero git-state checks in any of the 8 tools; hooks all `.sample` |
| C-064 ✓VF | Standing commit+push rides every close | close.py `--write` executing commit (C-037 fields) + push under the recorded grant. VF: close.py (1294 lines) contains no commit/push code — write path ends at `run_gates()` |
| C-037 ✓VF | Commit convention (fields, [DOMAIN], no rewrite) | commit-msg/pre-commit hook or doctor lint. VF: `.git/hooks` = 13 stock samples; doctor's nearest check WARNs on unset identity only |
| BOOT-signing ✓VF | %G? chain check invocation | Wire doctor.py into `run_gates()`. VF: run_gates = verify + check_versions + conditional check_scan; doctor never fires |
| C-129 | Gas Ledger rows at every close | close.py row scaffold (estimates stay judgment inputs) |
| KMP-receipt-pair | Receipt pair + artifact shape | Receipt validator (fields, SHA-256s, baseline clause, OTS pendency) |
| KMP-remote-sever | Transport by clone, sever origin | Transport script; verify severed |
| KMP-working-artifacts | Migration artifacts on branch only | Branch scope checker |
| KMP-preprinted-excludes | EXCLUDE rows never overwritten | Stamp-diff checker vs Gate-0 clone |
| KMP-frozen-assessment | Gate-2 assessment frozen | Hash-pin at acceptance; compare at landing |
| KMP-prospective | Forward-only, no rewrite | History checker over landings |
| KMP-landing | One reviewed change-set + record set | Landing-shape checker |
| ONB-day-one-checks | Post-birth folder + push checks | genesis.py post-birth verification subcommand |
| C-078-KERNEL-PINS | KERNEL pin currency | Pack-time newest-edition check. genesis.py's own comment admits "no mechanical gate yet" |

### Tier B — seam-exposed, MEDIUM/LARGE (7)

| ID | Rule | Build | Route |
|---|---|---|---|
| C-001 | Close-loop invocation + Return Package | M | close.py RP scaffold + session-stop reminder hook |
| KMP-pin | Pin an anchored release | M | Pin script: resolve, signers-bind, fsck, record |
| KMP-matrix | Matrix↔.inherited pairing + stamp-diff | M | Bidirectional pairing checker (the TF1-3 laundering guard) |
| KMP-scratch-rehydrate | Landing scratch-apply drill | M | Scripted clean-clone apply + both checkers |
| GEN-first-close | The newborn's first close | M | Birth-completion check. VF-class: genesis writes opener + fieldnote only — no close machinery ships to a child |
| UDP-adoption-seeds | v0.3 adoption recipe | M | genesis retrofit/adoption script |
| KMP-gates | Gates 0–6 skeleton | L | Migration driver (`adopt` subcommand, §7.1 named-unbuilt) |

### Tier C — not seam-exposed, SMALL (33)

| ID | Rule | Route |
|---|---|---|
| C-076 ✓VF | Restore-drill cadence per Scan | check_scan standing-section check. VF: zero drill/restore hits in check_scan.py |
| WALK-LOCAL-CONTEXT ✓VF | Active pointer = newest RP (F2 class) | check_versions git-chronology comparison. VF: computable, uncomputed; check_scan's `newest_report()` proves buildable |
| C-034 ✓VF | OQ leaves only by disposition | Extend the check_scan disposition gate to OQ rows. VF: S-prefix-only today |
| DIET-finding-ids ✓VF | DF/IF ledger grammar | Generalize check_scan regex beyond `S\d+-`. VF: hard-coded S at lines 147/181 |
| C-104 ✓VF | Board format checker (9 sections, bar, one NEXT) | Named Registry rule-2 build, unbuilt. VF: only stamp currency + pack-time HTML hygiene exist |
| C-128 | Done-bar ten-chip roll | close.py roll at board refresh |
| ABF-file-first | Board location law | check_versions location check |
| C-003 | Projection banners present | Banner/source-line lint |
| C-030 | Register membership refresh | close.py auto-verify (pre-fill exists) |
| C-006 | .md canon format | Format lint w/ declared exceptions |
| C-011 | Local opening convention | Opening-line lint |
| C-066-SCOPE | Drone never-edit list | Hand-back diff vs roster |
| C-075 | Drone-branch deletion | doctor list of surviving `drone/*` |
| C-082 | Full clone, never worktree | Launcher `.git`-file refusal |
| C-086 | Concepts carry Draft status | Status lint over Concepts/ |
| C-113 | Registry five-rule contract | Registry linter |
| C-115 | Sources routing + cards | Binary-class flag + card lint |
| CMD-STAMP-REFRESH | Command-file stamps (corrected row) | Promote `.claude/commands/` + Site mirror into STRICT |
| LEDGER-POINTER | Overview points, never lists | Lint forbidding OQ enumeration outside Register |
| WALK-SCHEMA-TEMPLATE | Schema→Template stamp pair | Stamp-pair check (resolver exists) |
| WALK-STORE-TOOLS | README roster vs directory | Roster diff |
| FN-NO-COMMIT | Fieldnote rides next close | Flag FIELDNOTES.md staged off-close |
| FN-immutability | Blocks content-immutable | Diff surviving blocks vs HEAD |
| LOOK-READONLY | C-096 window read-only | Post-look git-status check on target |
| LOOK-ROSTER | Registered targets only | Roster validation pre-read |
| MRC-BANNER-MARK | MRC marker line | Marker scan |
| SCAN-method-guard-decl | §3.3–3.5 declarations | Extend check_scan headers |
| SCAN-finding-anatomy | Anatomy + non-findings section | check_scan section checks |
| DIET-pointer-grammar | Eviction grammar (§10 checker, named-unbuilt) | Build it |
| DIET-records | Diet landing record set | close.py scaffold + presence gate |
| UDP-frozen-seeds | Grown-from stamps + hash match | Seed-edition checker |
| UDP-bounded-seeds | Kernel-only seed set | Templates/ roster check |

### Tier D — not seam-exposed, MEDIUM (16) and LARGE (1)

C-116-EXEC ✓VF (mirror rider execution — pack_mode verifies only; **verified defect: close.py:1253 `--mirror` default `~/Desktop/fractal-mirror`, stale since the estate move; fails loud, not silent**) · C-090-EXEC ✓VF (no tool performs tag or OTS — pack prints "Safe to tag", an act it never does) · C-038 ✓VF (no drill.py exists; doctor automates only the rebind fragment) · ABF-regen-at-close · C-004 (ripple sequencing) · C-036 · C-110 (word-count lint) · CS-MAINTAIN-FLAG · WALK-CONTEXT-INDEX · MRC-FIVE-RULES · SCAN-birth-test · DIET-measurement · C-108 (flight launcher) · KMP-advisory (§7.5 generator) · UDP-one-home (duplication lint) · UDP-extension-steps — and C-069 (LARGE; habit by **recorded deferral**, C-070 trigger — listed for completeness, not as an offer).

---

## 3. Meta-rules and the smaller-rule-set verdict

Ten derived laws (PT): **Instance** (repo IS the instance, projections disposable) · **One-Home** (one normative home, stamped pointers everywhere) · **Accretion** (history only accretes) · **Sovereignty** (nothing binds without the owner's recorded yes, at all three boundaries) · **Ripple** (source-first, one direction) · **Spine** (orient by the declared spine, never scan) · **Gate** (every write path ends at a named check) · **Ceremony** (declared riders are executed by the event's tool; deterministic procedures are scripts) · **Generator** (cures land in the generator, never the field instance) · **Keeper** (new: every rule at ratification names its keeper — check, event tool, recorded deferral, or explicit judgment designation; keeperless = red finding).

**Honest verdict: CONFIRMED as architecture, REFUTED as replacement text.**

- PT's arithmetic: 204 law-tier rule/ritual ids (227 with sub-rows) → 10 laws + ~9 irreducible spec homes (~20:1 at the law tier). XM's fuller dedupe carries 289 rules. Both counts are in the record; the difference is that XM counts machine-enforced and structural facts PT treats as already-kept.
- VF tested the 15 consolidation clusters' drafted one-sentence rules: **1 of 15 survived** (cluster 14, the dedupe law itself — canon-conformant, drops nothing). **13 were refuted for dropping binding clauses**, and several **contradict ratified members outright**: Accretion vs Fieldnote Format §4 (blocks are deleted whole — presence-transient by law) and KMP restatable receipts; Sovereignty vs C-133 (kernel ratification is standing and automatic, never per-act) and AGENTS rule 4 (the brief is the grant); Spine vs three deliberate per-surface narrowings (drone stops at Global; welcome orients from README; look orients in the *target's* spine); Ripple vs the ratified C-071/C-077 distinction (two mechanisms, not one); Gate vs the severity split, the Scan grandfather tier, and the merge-leg of C-050. Cluster 15's compaction license fails on C-017 (two-faces doctrine is not Schema-present) and on unenforced clauses (C-027 rule 5, C-055's advisory tripwire).
- So: the corpus compresses **because most rows were never independent laws** — restatements and adoption history pointing at ~9 normative homes (VF-confirmed doctrine, cluster 14). But the drafted meta-rule texts fail the corpus's **own fact-presence law (C-125)**: a merged text may not land while a clause of the replaced carrier is homeless. The 10 laws are sound as a stamped organizing overview **above** retained homes, not as substitutes for them.
- Before/after, honestly stated: **289 deduped carriers → 10 laws + ~9 spec homes + the register numbers retained as citation anchors** (renumbering would itself violate Accretion — PT's own caveat). The 72 habit-by-accident rows are not compressed away by prose at all; they dissolve only if the Gate/Ceremony/Keeper builds actually land (~34 of them build_cost SMALL). Meta-rules without keepers are "better-organized prose — the exact defect being cured" (PT, verbatim caveat).

---

## 4. Consolidation map

### Survived verification

| Item | Verdict | Evidence |
|---|---|---|
| Cluster 14 — one rule, many projections | CONFIRMED | Restates ratified doctrine (C-110/C-003/C-065/C-083); every member resolves to a named home; drops nothing binding (VF) |
| C-013 → history row | CONFIRMED | Zero tool/store citations; no armed forge trigger; C-029 carries the surviving law. Caveats (VF): GENESIS.md:82 + Architecture State §6 enumerate it by number — **the row physically remains**; wording fix: method re-exercised in arc 2 (C-093), that exercise also executed history |
| C-072 → DEAD (history) | CONFIRMED | Superseded explicitly by C-089 in Register/Settings; zero live dependencies; all citations historical. Same physical-row caveat (GENESIS.md:82) (VF) |
| C-016/C-046 → C-027/Schema | Offer, narrowed | The Register's own words ground these two ("execution record of Schema §5.3 rule 8") (CN); not individually refuted — but cluster 15's *blanket* license was, so these two go alone, with a clause-inventory pass |
| REWORK trio: C-001 (narrow to orientation half), C-006 (.docx clause dead), DELETIONS-ALLOWED (retire dumpster narrative) | Unrefuted | CN verdicts; no VF counter-evidence |

### Refuted as drafted (13 clusters — grouping may stand; the merged texts may not)

1 Repo primacy (loses CS-INJECTION stamp discipline, C-048 file-first ORDER, C-020 bootstrap-in-repo) · 2 Declaration ("red-blocks any disagreement" factually wrong — WARN tier exists; loses C-080 frozen carve-out, C-088 exemption scope) · 3 Accretion (**contradicts** fieldnote deletion-whole + KMP restatable receipts) · 4 Sovereignty (**contradicts** C-133 standing ratification, C-084(a), brief-as-grant) · 5 Constitution (loses C-081 positive prohibition, C-109 + its IPF §1.3 exception; freezes transport trajectory) · 6 Data-not-instruction (loses C-096 asymmetry, C-120 intake layer, FN-PARK-TASK) · 7 One-home (conflates the two behaviour tests; loses board exemption, concrete budgets) · 8 Source-first (**collapses C-071 vs C-077 — the S3-3.2 defect would return**) · 9 Spine (**erases three deliberate per-surface narrowings**) · 10 Red gate (loses merge-leg, grandfather tier, severity split, --pack double-run) · 11 Release ceremony (loses public-identity signing clause, ninth-parameter, C-105 doctrine) · 12 Human-window ("born at genesis as frozen seeds" true for kernel trio only — contradicts Pair Procedure Discipline B) · 13 Field proving (loses no-phone-home, warning-never-gate, dual-grammar intake) · 15 Store-law compaction (premise false on C-017/C-027r5/C-055). All VF, with file-line evidence in the lane record.

**Disposition offer for the pairwise merges sitting inside refuted clusters** (C-064→C-056, C-084→C-037, C-050→C-060, board family→C-104, pair family→C-124, C-085→C-098, C-095→C-111, C-100→C-121, C-103→C-058, C-073→C-112, C-107→C-120, C-030↔C-036, C-011→C-009, C-002→trio): none individually refuted, but each must carry the verifier-named clauses verbatim; redraft with a full clause inventory and a C-058-class fact-presence review per merge before any lands. The C-077→C-071 merge alone is refuted outright.

---

## 5. Cost lane verdict: the assumption is inverted by the data

Measured (CO), across the densest tooling week (all 8 tools born 08-13→08-17) and the ledger window after it (08-18→08-21):

- **Opens: 85k → 35k tokens** (falling). **Ordinary-close floors: flat 40–65k.** **Tagging closes: 136k → 65k — halved** as pack moved into close.py. All while the store **grew** (155→157 nodes, 1,007→1,022 events). No mechanization event correlates with a cost rise.
- **Marginal economics, ~3 orders of magnitude apart:** one more checker rule ≈ milliseconds + ~0 session tokens unless it fires (verify.py: 0.12s, constant 51-word PASS for the whole store). One more prose rule ≈ 110–160 tokens loaded **every session forever** (~1.35 t/w); one such line has already cost ~4–6k tokens over 35 sessions. The tools' 22,566 words of Python cost 0 context tokens; as spine prose they would cost ~30k/session.
- The one measured cost explosion is **prose corpus, not tooling**: mother close 316k vs empty-newborn close 11k (~28x; the ledger's own attribution: "corpus, not ritual"). Loaded spine 8,554 words vs ~217,570-word cold corpus (1:25) — the existing CLAUDE.md compression of Settings is itself a 21:1 proof of the economics.
- **Two honest caveats:** (a) check_versions currently prints 1,115 words for **47 standing WARNs** — unfixed warnings leak tokens at every close; the cure is fixing warnings, not fewer checkers. (b) Flights rose 1.62M → 4.04M tokens — commissioner scope choices, subagent-side, never in session context.

**Verdict:** mechanizing a habit out of the loaded spine and into a checker is the token-*saving* move. The feared failure mode is caused by *not* mechanizing.

---

## 6. Recommendations — OFFERS, sequenced (every disposition Max's)

1. **Defect cures (SMALL, this-close class):** fix close.py:1253 `--mirror` default to the Knowledge Network path (VF-verified stale); work down the 47 standing check_versions WARNs (CO-measured token leak).
2. **Seam-first guards (Tier A, all SMALL):** C-091 non-governing-copy refusal in the write tools; C-064 close-executed commit+push — *a C-008 promotion, so this one needs its own recorded grant extension*; doctor.py wired into run_gates (BOOT-signing); C-037 commit hook; C-078-KERNEL-PINS pack check; C-129 gas scaffold; ONB-day-one-checks.
3. **Before the next migration or birth:** the KMP script family (receipt validator, sever, pins, matrix, scratch-apply, landing shape) + GEN-first-close + UDP-adoption-seeds — 13 of the 21 seam-exposed rows live here.
4. **The lint batch (Tier C, ~33 SMALL):** generalize check_scan (DF/IF, OQ dispositions, §3.3–3.5, anatomy); build the named-unbuilt checkers (C-104 board format, DIET §10, C-113 Registry, C-123 IPF); the WALK-* computable comparisons (F2 cure first); FN/LOOK guards; STRICT-set promotion of command files.
5. **The executors (MEDIUM):** C-116-EXEC/C-090-EXEC — close.py performing the rider and the tag+OTS once --pack is green; ABF-regen; C-001 scaffold; C-004 sequencing.
6. **Ratify the Keeper Law — after offers 2–4 land, not before** (PT's own caveat: without keepers it is prose about prose). Its keeper: one check_versions row over the keeper roster.
7. **Consolidation, narrow lane only:** record C-013/C-072 as history rows (rows physically remain — GENESIS.md:82); merge C-016/C-046; execute the REWORK trio; adopt the 10 laws as a stamped organizing overview above retained homes; **redraft any further merge with a clause inventory + fact-presence review** — 13/15 drafted collapses failed exactly that gate.
8. **Cost posture:** keep new rules checker-side, not spine-side; apply the diet lever (~1,350 tokens/1,000 words per session) to the loaded spine; flight scope stays a deliberate per-flight choice.

---

## The rider left open — the scope axis (kernel · parametric · custom)

Max's second axis was named while the flight was airborne and deliberately not injected mid-run: classify the 289 deduped rules by jurisdiction scope — KERNEL (travels as shipped) · PARAMETRIC (kernel mechanism, instance value) · CUSTOM (the mother's biography, never travels) — and verify the derived classification against the hand-made ground truth (KNet's kernel-adoption matrices: does the classification predict what an actual child inherited, deferred, excluded?). Offered as a small post-landing pass over this record's inventory; per the two-turn rule, it waits on Max's response.

---

*Frozen at issue. Per-agent evidence: the flight journal (`wf_0002e9b0-8d7/journal.jsonl`, session-local). Dispositions: none at issue — the §6 offers await Max's response; whatever he directs enters the record through the session's close (Protocol + Register), never by editing this file.*
