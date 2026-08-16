# Fractal Governance Protocol — Claude Series v0.7

**Topic:** Defining the review act (C-033); the first ratification pass (Claude Series v0.1–v0.6 + Conversation Settings); the cumulative open-question ledger (C-034); the Custom-Instructions projection stamp (C-035)
**Status:** Ratified (2026-08-12 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-12 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.6

---

## 1. Context

The whole-project Loose-Ends Scan (2026-08-12) surfaced a systemic governance defect: every Claude-era Governance Protocol (v0.1–v0.6) and the Conversation Settings standard carried `Status: Draft — pending Max's review`, while nothing defined what that review *is*, where its record lands, or what triggers it. By the Decision Register's own legend ("**Ratified** = recorded in a *reviewed* Governance Protocol"), nothing in the project was actually Ratified — yet downstream artifacts (the accepted Schema, the live store, immutable identities) were building on those decisions. Two further hygiene defects followed from the same root: earlier protocols' §11 open questions vanished without disposition (no cumulative ledger), and the Custom-Instructions projection was claimed "verbatim" while being an unstamped paraphrase. This protocol — the opening act of the consolidation & hardening phase (workstream A of the scan-derived agenda) — closes all four items.

## 2. Questions Investigated

- What should "Max's review" formally consist of — its act, its record, its trigger, its effect?
- Should protocols v0.1–v0.6 be ratified now, in bulk, and with what caveats?
- Where do open questions live so they can no longer leak between protocols?
- How does the Custom-Instructions projection become verifiably in-sync rather than asserted-verbatim?

## 3. Human Input (Max)

- **Review = lightweight and in-conversation.** Chose the leanest mechanism: an explicit acceptance in conversation after a walkthrough, recorded as a ratification entry in the next Governance Protocol, flipping the document's status. Consistent with the lean tie-breaker (v0.1) and manual-first governance (C-008).
- **Ratify all, now, with caveats.** Chose bulk ratification of v0.1–v0.6 plus Conversation Settings v0.2 in this conversation, with the two scan-derived caveats recorded (see §6) rather than silently absorbed.

## 4. AI Input (Claude)

- Diagnosed the four workstream-A items as one root defect: the undefined review act. Once review is defined and exercised, the legend contradiction, the perpetual Drafts, and the "Reviewed By" misnomer resolve mechanically.
- Presented the per-protocol walkthrough (decisions + scan findings against each) as the review material; flagged that ratifying v0.3 does **not** confirm the C-015 ID scheme, and that v0.6's multi-person-safety language claims as achieved what is still a design goal.
- Recommended: a *dispositioned* cumulative ledger (an item leaves only by recorded disposition, never by omission), and a stamped projection (sync becomes a decidable comparison instead of an assertion).

## 5. Jointly Derived Conclusions

1. Review is an act that must be cheap enough to actually happen and recorded enough to be citable; the in-conversation walkthrough + protocol entry satisfies both.
2. This conversation constitutes the first review pass; the ratification backlog is cleared with caveats made explicit, not dropped.
3. Open questions are a ledger, not a per-protocol snapshot; the Decision Register is that ledger's home.
4. Projections are kept honest by version stamps, not adjectives.

## 6. Current Decisions

- **C-033 — The review act (Working Decision).** *Max's review* of a governance document consists of: (a) **act** — an explicit in-conversation acceptance by Max, following a walkthrough of the document's decisions and any findings held against it; (b) **record** — a ratification entry in the next Governance Protocol, naming the documents reviewed and any caveats; (c) **effect** — the document's status flips `Draft → Ratified (date, per recording protocol)`; (d) **trigger** — any document pending review is presented at the next governance-domain conversation at the latest. Field convention: a document not yet reviewed carries **`Review Owner: Max`**; on ratification the field becomes **`Reviewed By: Max (date, per protocol)`** — the field never asserts a review that has not occurred.

- **Ratification pass (first exercise of C-033).** Governance Protocols — Claude Series **v0.1, v0.2, v0.3, v0.4, v0.5, v0.6** and **Conversation Settings** are **Ratified** as of 2026-08-12, recorded here. Consequently every decision C-001–C-032 attains full **Ratified** status under the Register's legend. Two caveats are part of the record:
  - *Caveat 1 (C-015):* ratification of v0.3 does **not** confirm the C-015 identity scheme — the `TYPE-ULID`/content-hash *scheme* remains a **Working Hypothesis**. The live store has hardened it de facto (scan finding 4.2); its confirmation or grandfathering is a queued workstream-C decision.
  - *Caveat 2 (multi-person safety):* v0.6/§5.1's "safe multi-person work" is ratified as a **design goal**, not an achieved property. Until a mint-collision policy and fold-verification ritual exist (workstream E), the Knowledge Graph Store is **single-writer**; a second writer requires out-of-band coordination.

- **C-034 — Cumulative open-question ledger (Working Decision).** The Decision Register's open-questions section is the project's **single cumulative ledger** of open questions. Every Governance Protocol §11 item is swept into it with a **disposition** (`open`, `resolved (where)`, or `superseded (by what)`); an item leaves the ledger only by recorded disposition, never by omission. Protocol §11 sections remain as historical snapshots; the ledger is the live index. The lost v0.1/v0.2 §11 items are swept in with this protocol (see Register v0.3).

- **C-035 — Stamped Custom-Instructions projection (Working Decision).** The Project's Custom Instructions field is a **governed projection** of Conversation Settings — a compression, not a verbatim copy. It **must** open with a version stamp naming its source and date (e.g. *"Projection of Fractal_Conversation_Settings v0.3, 2026-08-12"*). The §6 sync-check duty becomes decidable: compare the stamp against the current Conversation Settings version; divergence = stale stamp. Conversation Settings is reissued as **v0.3** with §3/§5 reworded accordingly (the word "verbatim" no longer describes the projection).

## 7. Alternatives Considered

- **Solo read + sign-off, or checklist review.** Rejected by Max for the default: heavier, and the Draft state stays open until scheduled effort happens; the in-conversation act can still be escalated to a checklist for contentious documents.
- **Ratify without caveats.** Rejected: silently absorbing the C-015 and multi-person findings would repeat the exact claimed-as-achieved pattern the scan flagged.
- **Hold v0.6 until workstreams C/E land.** Rejected: its decisions (C-026/C-027/C-032) are sound; the concerns attach to *claims around* them and are carried as explicit caveats instead.
- **A separate open-questions document.** Rejected: the Register already aggregates decision state and is mirrored into the Project (C-030); one more standing document violates leanness.

## 8. Assumptions

- The walkthrough presented faithfully summarised each protocol; ratification relies on those summaries plus Max's prior familiarity with the sources he co-authored.
- Ratifying this protocol *in the conversation it records* is a genesis self-reference of the same kind accepted in v0.6 §8 — true by the end of the act.

## 9. Consequences

- Protocols v0.1–v0.6: `Status → Ratified (2026-08-12, per v0.7)`; control-table field `Reviewed By: Max` → `Reviewed By: Max (2026-08-12, per v0.7)`.
- Conversation Settings reissued as **v0.3** (verbatim→governed-projection wording, stamp rule) and ratified in the same pass.
- Decision Register → **v0.3**: legend now consistent with reality; all statuses flipped; open-questions section becomes the cumulative ledger (C-034) with the v0.1/v0.2 §11 sweep; C-033–C-035 added; Register status set to *Living (derived projection)* — a projection tracks its sources and is not itself Draft/Ratified.
- Max pastes the stamped Custom-Instructions text (drafted this conversation) into the Project settings.
- The perpetual-Draft bottleneck (scan 7.1), the legend contradiction (1.1), the open-question leak (7.2), and the verbatim claim (4.3) are closed. Workstream A is complete.

## 10. Decision Ledger Changes

Added **C-033** (review act), **C-034** (cumulative open-question ledger), **C-035** (stamped Custom-Instructions projection). Ratified Claude Series v0.1–v0.6 and Conversation Settings; C-001–C-032 attain Ratified status (C-015 scheme caveat: still a Working Hypothesis; v0.6 multi-person caveat recorded). No decision content changed.

## 11. Open Questions (TBD)

*(Per C-034 these are also entered in the Register's cumulative ledger.)*

- Whether the Custom-Instructions text should eventually be auto-generated from Conversation Settings (carried; automation boundary C-008).
- Whether the review act needs a heavier variant (checklist) for load-bearing decisions — calibrate in use.
- C-015 confirmation vs grandfathering (queued, workstream C).
- Mint-collision policy + fold-verification ritual to retire Caveat 2 (queued, workstream E).

## 12. Next Line of Research

Workstream **B** (substrate realization): `git init` the FRACTAL repository so C-018/C-019/C-020 and C-025's commit granularity are enforced by the substrate rather than discipline; define the commit convention; give the bootstrap/rehydrate protocol a named trigger or author its minimal version.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.7 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.7 |
| Status | Ratified (2026-08-12, in-conversation per C-033) |
| Domain | Project Governance — Review & Decision Ledger |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, this protocol) |
| Date | 2026-08-12 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.6 |
| Related Documents | Fractal Decision Register v0.3; Fractal Conversation Settings v0.3; Loose-Ends Scan (2026-08-12); Governance Protocols — Claude Series v0.1–v0.6 |
| Revision Trigger | Any change to C-033–C-035, or a change to the review act |
| Document ID | DOC-01KZVYQVDGR9JD7E2JTJWYZGRM (minted 2026-08-12, C-041/C-042, per v0.9) |
