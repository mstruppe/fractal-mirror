# Flight Record — 2026-08-17 · The Diet Flight (the Ultracode Flight Protocol's first conformant launch)

> **CANONICAL FLIGHT RECORD (C-058 class via Fractal_Ultracode_Flight_Protocol_v0.1 §6.3) — dated, frozen at issue, never revised.** Findings carry stable ids `DF1-…`; the whole slate lands **banked, untriaged** (Max's call: the new session works it). Fixes and products are proposals until ordinary decisions adopt them.

**Identity:** `Fractal_Flight_Record_Diet_1` · **Version:** 1.0 (frozen) · **Domain:** GOV · **Author:** Claude (orchestrator) · **Date:** 2026-08-17 (post-close of the seventeenth session) · **Commissioned by:** Max — *"test thoroughly if we can put any working process on a diet … whether there is stuff piling up over time which makes the system heavy, whether the load can be mitigated"* · **Document ID:** DOC-01M07RD1Y69E9EX1Z8CMTMMZ93 (minted at first commit via `close.py --create`; stamped by the post-mint revise)

## 1 · Commissioning contract vs. as-flown — the first conformant launch

**The launch sequence ran clean for the first time:** game plan proposed → Max's agreement ("start flight 1") → the armed declaration with the effort checkpoint → his "go". **Contract:** 8 agents, 4 phases (Measure ×4 parallel at low effort → Diagnose ×1 at high → Mitigate ×2 default → Verify ×1 default); verification tier work-over single-pass with mechanical reproducibility (every number carries its command); read-only; proposal-only landing. **As flown:** 8 agents, ~446k tokens, ~15 min, 0 failures, no deviations.

## 2 · Findings — the weight-class map

- **DF1-1 [High · superlinear] Register ledger accretion.** 19 KB → 200 KB in 5 days (10.5×), doubled in the last 2 days (~3.8 KB/close). Engines: the **Revision history** block (32 KB, 5.9× since 08-14 — every close appends a prose re-narration of a protocol that already exists frozen) and the **OQ ledger** (58 KB — rows annotated in place; OQ-28's row alone 3.9 KB). C-095 named the Register a candidate "at its own observed-drag trigger" — **this measurement is that trigger, fired.**
- **DF1-2 [High · linear] Spine refill.** The append mechanisms C-095 compacted still run: the Local Context session table (~150–250 words/row) and the Index's per-session Sources narrative (+460 words/day) refill the compacted files. (Verifier's fair note: arguably Med — the spine sits at 43.5% of the OQ-28 baseline, so this is trajectory, not present overload.)
- **DF1-3 [Med · episodic] Doctrine re-telling fan-out.** One decision lands as full prose in ~6 living places (C-105: ~525 words across six); the corpus's own counter-pattern exists (the beta-0.4 pack: ~60 living words, pointer-style).
- **DF1-4 [Med · flat] Manual close-walk stamping tax.** ~7 of 12 living docs hand-bumped per close; the ritual itself is not growing.
- **DF1-5 [Low · linear] Off-spine bulk** (Agenda Board, Architecture State) — not in the opening spine; the board's growth is content, not chip pileup.
- **DF1-6 [process finding — Max's mid-flight question, sharpened by his post-landing point]** The Flight Protocol §2 lacks a **gating-mode field**, and the gate's real function is the **effort-adjustment point**: *gated* = each phase its own launch, effort/speed/scope adjustable at every gate (the capture pattern); *continuous* = one go, one landing, **effort locked at launch for the whole program** — the commissioner must size effort for the hardest phase before the go. Per-phase effort declarations in the contract (this flight's Measure-low/Diagnose-high) are the continuous mode's only substitute, and work only because they precede launch. Fix shape: §2 gains the gating-mode field + this trade stated; the effort-immutability clause and the gating mode are two halves of one rule. (The verifier had struck the original "lighter gating mode" clause as unattested — it now has its history.)

**Non-findings (checked, demonstrably NOT heavy):** the C-059 checklist flat at 12 rows since canonization · CLAUDE.md flat at 1,548 words through six re-projections (the adapter compression works) · Global Context flat at 632 words · the frozen tier (protocol series, 48 files / 488 KB) is the record by design, not drag · close.py already absorbs the highest-risk mechanics · the C-095 compaction held losslessly · the opening spine at 10,052 words ≈ 13.6k tokens = 43.5% of the OQ-28 baseline.

## 3 · The mitigation slate — 14 proposals, banked untriaged

**Compaction (C-095 — the trigger fired by this flight's data):**
1. Register Revision-history block → pointer table (~27 KB / ~4,100 words saved).
2. Register OQ + findings ledgers → status + current-shape clause + protocol pointers (~31 KB). *Pre-condition from the verifier: ~5 OQ rows and ~12 history entries lack explicit protocol pointers — add them before compacting, or the compaction is not lossless.*
3. Rule Overview §2/§3 rows → ≤40-word norm + refs, history as pointers (~29 KB).
4. Architecture State revision-history line → pointer table (~7 KB); the body accepted (current architecture is its product).
5. Context Index: retire the per-session Sources narrative to a two-line pointer (~780 words off the spine; kills the +460 words/day trajectory).

**Mechanization (close.py / check_versions.py):**
6. History rows minted mechanically at `--write` (close.py already knows date, protocol number, changed-doc set).
7. A `--stamp` pass: version headers + store counts from the live log (absorbs the counts-last manual step).
8. The C-059 walk table pre-filled from close.py's own hash-diff (the mark-and-stamp half of 12 rows).
9. A **drag gauge** in check_versions.py: per-file size deltas, advisory yellow — the C-095 trigger measured instead of felt.
10. Spine word budgets (advisory tripwire — e.g. Local Context ≤3,500 words, Index ≤2,000, session table ≤40 rows). *Needs ratification (new standing rule).*

**Structural (precedent NONE — need ratification):**
11. The **pointer-weight re-telling rule**: one normative home carries the full statement; every other living surface ≤ ~40 words + refs (the beta-0.4 pattern promoted to rule; ~300–500 living words saved per future decision).
12. Session-row grammar cap (~20-word headline + of-record pointer; era-rows collapse at phase closes).

**Acceptance-with-reason:**
13. The Agenda Board — its content is the product for its declared audience; trigger stays armed.
14. The judgment half of the close — after 6–8 land, what remains is the reasoning of record; ratify that as the mechanization program's **boundary**, closing DF1-4.

**Estimated total if the compaction slate lands:** ~94 KB ≈ 14,000 words off the living tier; the spine ~1.5k words lighter; the mechanical close-half roughly halved.

## 4 · Verification (declared tier: work-over single-pass)

**PASS with minor corrections.** 20+ load-bearing numbers re-run at HEAD and reproduced exactly. 8 issues, none High: four off-by-one/anatomy slips in the re-telling measurement; one overstated lossless claim (→ the pre-condition on proposal 2); two cherry-pick notes (DF1-2's severity; the protocol series' designed growth should be stated explicitly as accepted — it is, in the non-findings); one doctrine note (proposals 10–12 correctly need ratification, not routine adoption). Full issue list in the workflow record (`wf_845a5692-bff`).

## 5 · Unchanged, with reasons

Nothing in canon moved — the flight was read-only by contract; every proposal awaits Max's triage. The frozen tier's volume is accepted as the record. The spine's present weight is within budget; the flight's subject was trajectory.

---
*Sources: workflow run `wf_845a5692-bff` (8 agents; per-agent returns in the session's workflow journal); measured at HEAD `bbd72f3`; comparison commits a9daa6f (08-12) · a57f592 (08-14) · 8db3142 (08-15). Frozen at issue.*
