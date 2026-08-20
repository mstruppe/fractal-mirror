# Flight Record — 2026-08-18 · Scan #5 + Gas Metering (the twenty-fifth session's flight)

> **CANONICAL — flight record (C-108 container class, C-058 preservation rules).** The record of a commissioned ultracode flight: dated artifact, DOC-minted at first commit, never revised. The flight's products are proposals (C-008; landing rules §6): the Scan report stands Draft pending ratification and the slate call; the gas table below is **data, pre-canon** (C-062). This record is authoritative for what the flight did and measured, never for what should be done about it.

**Fractal_Flight_Scan5_Gas** · **Version:** 0.1 · **Status:** Issued (committed at the twenty-fifth session's close, per Protocol v0.59; never revised) · **Document ID:** DOC-01M0B4E3KTA4K5GHZHC7QVDT3K (minted at that close via `close.py --create`; stamped by the paired revise) · **Date:** 2026-08-18 · **Domain:** GOV · **Author:** Claude · **Commissioner:** Max · **Parent:** Fractal_Ultracode_Flight_Protocol_v0.2

---

## 1 · Commission and launch (the compressed sequence, recorded)

Scan #5 was commissioned at the twenty-fourth session (per Protocol v0.58) — the Scan Procedure as the main flown procedure, first `check_scan.py`-gated member, full slate over the sixteen sessions since Scan #4, release-readiness weighted, attention lanes by Max's word: **the diet** and **the adaptive close** (*"features which make FRACTAL a sophisticated system which knows how to counter obstacles"*). At the twenty-fifth session Max added the **gas-metering lane**: *"measure how many tokens were used in the last close cycle, how many when starting this session, and run a simulation of a new project birth cycle with one second start cycle to measure the close and succeeding start. then we can compare how much gas fractal needs empty vs now as reference."*

The game plan was proposed with the full §2 contract (scope, 3 phases, 15 agents derived from roles, per-phase effort, adversarial tier, proposal-only landing, continuous gating); the launch came compressed — **"flight go"**, agreement and go in one word, the DP1-conformant form; the contract was restated as-flown in the launch message. Pre-launch guard state recorded: `verify.py` PASS (784 events · 126 entities · 0 warnings), `check_versions.py` PASS (46 warnings, all known heuristics), HEAD `59e7e2b`, 138 commits.

## 2 · Contract vs as-flown

| Contract field | Declared | As flown |
|---|---|---|
| Phases | Sweep → Verify → Assemble, continuous (one go) | as declared, no gates fired mid-flight |
| Agents | 15 (5 finders + drill + parser + 3 sims / 3 refuters + 1 metering verifier / 1 synthesis) | **15/15 completed, 0 errors, 0 skips** |
| Effort | finders + refuters + synthesis high; drill/parser/sims/verifier medium | enforced per agent by the launch script |
| Verification tier | adversarial (refuter-gated) for the scan slate; independent recomputation for the metering | as declared — every finding carries its refuter verdict; both metering computations independent |
| Landing | proposal-only | held — two Draft files placed uncommitted; no canon touched; no commits |
| Scope | read-only at HEAD `59e7e2b` + 3 declared exceptions (scratch birth, scratch drill clone, transcript reads) | held — no silent scope growth; the repo working tree received only the two landing drafts |
| Cost estimate | ~1.5M tokens (basis: UF1 ≈105k/agent, CB1 ≈93k/agent, capture ≈84k/agent) | **1,624,958 subagent tokens (+8.3%)** · 341 tool uses · ~28 min wall clock. The CB1 2× precedent was not repeated; the estimate's basis held. Orchestrator-loop overhead ran beside the metered figure and is not in it. |

## 3 · The scan lane's landing (summary — the report is the artifact)

Product: `Review_2026-08-18_LooseEnds-Scan-5.md` (Conversations/, **Draft, uncommitted** — pending ratification and the slate call). Pipeline: **38 raw findings → 38 after orchestrator dedupe → 37 survived adversarial refutation (1 refuted, 0 lost) → 35 unique ids** after synthesis merged two cross-territory duplicate pairs (the `AGENTS.md` seven-tool enumeration and the GENESIS §0 count staleness — each found independently by two territories, evidence the territories genuinely overlap at those loci). Headline: **0 High · 16 Med · 19 Low; series 26 → 24 → 8 → 7 → 35** over the widest lens the series has carried (sixteen sessions, five territories). Thesis extended from Scans #3/#4: *the machine now does the work, and the words about the work are the new blind spot* — plus the recurrence lesson: five previously-cured defect classes returned at or near their cured loci; hand-maintained enumerations recur until replaced by class references or machine couplings.

Riding instruments, both green: the **restore drill** 5/5 steps pass (fresh clone, path chain, signers rebind, `99 G · 39 N` zero bad, both checkers green in the clone; boundary note stated) and the **birth test** (§7.3, ridden by the metering lane's scratch birth — the newborn's own checkers green: 19 events · 12 entities · roots AGENT, FACET, LAB). Residue: 10 row-families re-verified — 9 hold; the DF1/CB1/DP1 family's absence became finding S5-1.1. Non-findings recorded: 60. The one refuted candidate (a `/begin` link-rule claim) died against Protocol v0.56 §2(d)'s recorded judgment and is preserved in the report's non-findings.

`check_scan.py` at landing: **FAIL with 36 errors, all of one class** — the 35 missing ledger rows (§10) and the missing Document ID — precisely the two acts that by design happen at the slate call and first commit (the landing order: ratify → mint → stamp → ledger → `check_scan.py` → commit). Every pre-close-checkable duty (filename grammar, control header, state-scanned block, id grammar, seed table) passed. The gate's first live exercise behaved exactly as specified.

## 4 · The gas table — what FRACTAL costs, empty vs now

**Subjects.** *Now:* the mother at 24 closed sessions — the 24th session's close segment (from Max's `/close` to session end, transcript-measured) and the 25th session's opening segment (session start through the orientation report). *Empty:* **Gauge**, a newborn born in scratch by `genesis.py` this flight (route LAB, 44 files, its own checkers green), measured across a real first cycle: birth → first working session with a governed act (P-001) and a full ritual close → a second session opening. Every number below is from actual session transcripts (`message.usage` rows), computed twice independently (parser + verifier) — **all transcript metrics matched exactly**; static word counts matched exactly, char counts within 1% (locale multibyte handling).

**Metric definitions.** WINDOW = input + cache-creation + cache-read at one request (the full prompt). *Window growth* = window_end − window_start over a segment (context genuinely added — churn-immune). *New tokens* = fresh (input + cache-creation) + output (what the API newly processes; fresh is inflated where cache churn re-creates an unchanged prefix — observed in the sim harness — so window growth + output is the robust pair). *Static spine* = the orientation file-set's size (same estimators both sides: chars/4 and words×1.35).

| Metric | Empty (Gauge) | Now (mother, 24 closes) | Ratio |
|---|---|---|---|
| **Static spine weight** (orientation file set, words) | 1,297 w (≈1,750 tok) | 12,137 w (≈16,384 tok) | **≈ 9.4×** |
| **Start: context loaded during orientation** (window growth) | +6,166 | +30,180 | **≈ 4.9×** |
| Start: output (the orientation report) | 3,319 | 3,440 | ≈ 1× |
| Start: requests | 15 | 5 | — |
| **Close: new tokens** (fresh + output) | **11,147** (6,391 + 4,756) | **316,264** (192,815 + 123,449) | **≈ 28×** |
| Close: window growth | +3,274 | +69,155 | ≈ 21× |
| Close: requests | 12 | 70 | ≈ 6× |
| Close: total processed incl. cache re-reads | 614,183 | 20,381,910 | ≈ 33× |

**Context points (mother):** standing load at session open = **52,839 tokens** before any work — ≈33.5k vendor harness prefix (cached) + ≈19.3k FRACTAL-injected layer (adapter, memory, opening command, git status). The 24th session totaled 216 requests / 1.27M fresh / 478k output; the close segment was 70 of those requests (32%) and ≈316k of the ≈1.75M new tokens (≈18%). The close's hot window averaged ≈287k tokens/request (20.4M cache-reads ÷ 70). **Context points (newborn):** a complete birth cost ≈124k new tokens one-time (sim-harness figure, churn-inflated upper bound; window peaked 52.6k); the first working session's *work* half ran 23 requests before the close marker; the newborn's whole kernel tree is 35,248 words across 44 files, of which the living orientation spine is the 1,297 above.

**Honest caveats (n=1 per subject).** The sim agents run a leaner harness than an interactive session (standing 34.6k vs 52.8k) — absolute standing loads are not comparable across subjects; the deltas, output, and static weights are. The mother's 24th close was the mechanized close's first live run; the newborn's close was a tier-0 manual walk — both are the honest current shapes of their tiers. `fresh` overcounts where cache churn re-creates unchanged prefixes; ratios quoted on window growth + output are the conservative ones.

**Reading.** Empty FRACTAL is cheap: the whole governance ritual of a newborn's close costs ≈11k new tokens, and its spine loads in under 2k. Twenty-four sessions on, the spine weighs ≈9× more (≈452 words/session average growth), orientation ≈5× more, and the close ≈21–28× more — with the close's mass sitting in *output* (the protocol, the return package, the register rows — 123k of the 316k) and in re-reading a heavy hot window, not in the ritual's mechanics. The two over-budget living projections the diet lane flagged (LC at 6,305 words, +5.3% beyond its recorded YELLOW — S5-5.3) are the single largest lever on both the spine and the start cost. This is **OQ-28's first quantitative mother-side datum** and the first executed instance of the context-rot metrology vision (`general` lane FN-0001); the diet's budgets now have a token-denominated meaning: every 1,000 words evicted from the spine saves ≈1,350 tokens × every future session's orientation.

## 5 · Byproducts and hand-over (the commissioner's triage)

1. **Sim ambiguity slate — genesis/onboarding feedback from a real newborn cycle** (improvisation-on-ambiguity, recorded not fixed): commit granularity at the first close (one commit or two — read minimally as two); committer identity undefined in the newborn's adapter (author only — the inherited git config would have decided silently); `check_versions.py` ships in the kernel but no newborn document invokes it (only `verify.py` named in the close ritual); no revision-history convention for version bumps; "both root protocols" undefined by name; return-package topic naming free. Plus the second start's three: the P-001 measurement unit unfixed; the measurement datum's home unrouted; the `/gauge` opener named by the rail (the command file exists — the sim read files directly instead).
2. **The newborn Gauge stands intact in scratch** (`…/scratchpad/gauge/Gauge`, 3 commits, checkers green) for inspection; the drill clone likewise. Both vanish with the session's scratchpad unless kept.
3. **Fieldnote candidates** (Max's call, C-094): the gas datum → `general` lane (context-rot metrology's first executed measurement, OQ-28 data); the recurrence lesson (five cured classes returned) → candidate for the same lane.
4. **What did not move:** no canon, no store event, no commit, no push; the repo working tree carries exactly two new uncommitted Draft files (the Scan report, this record); the two landing acts that remain are the commissioner's — the ratification + slate call, then the close (ledger rows, DOC mints, `check_scan.py` green, commit).

## 6 · Deviations

None material. Recorded for completeness: the close-segment boundary in the sim transcript was identified by the `CLOSE_SEGMENT_START` bash marker's *invocation* row (the marker string also appears in the agent's own briefing — the parse used the tool call, not the prompt mention); the second-start sim oriented by direct file reads rather than the `/gauge` command file (noted in its ambiguities; the file exists).

---

**Sources:** the flight's journal and per-agent transcripts (`…/subagents/workflows/wf_8d4c6935-408/`); the two session transcripts measured (24th: `6919560a…`, 25th: `bcf1183e…`); `Review_2026-08-18_LooseEnds-Scan-5.md` (Draft, this flight's scan product); Fractal_Ultracode_Flight_Protocol_v0.2; Fractal_Scan_Procedure_v0.1; Protocol v0.58 (the commission); the twenty-fifth session's launch exchange (the metering addition; "flight go").
**Revision history:** v0.1 (2026-08-18) first issue — the flight's landing record, written at landing by the orchestrating session; Draft until the close commits it.
