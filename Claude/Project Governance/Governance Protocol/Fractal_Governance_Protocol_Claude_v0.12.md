# Fractal Governance Protocol — Claude Series v0.12

**Topic:** The Agenda Board becomes repo-resident (C-048, amending C-047): the board's file is a living projection in the Context Packages; the Cowork artifact is demoted to a display surface republished from it
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.11

---

## 1. Context

Hours after C-047 ratified the Agenda Board, its §8 persistence assumption was falsified by observation: a fresh conversation on the same machine found no `fractal-agenda` artifact and had to regenerate the board from the Local Context. The safety property held exactly as designed — zero loss, because nothing lives only in the board — but the regeneration was *improvised*: with no standardised source file, every rebuilding conversation renders its own board. Max caught the structural gap immediately: a standing projection whose only concrete form is a vendor-side artifact has no canonical home in the repo, unlike every other projection in the context package.

## 2. Questions Investigated

- Where does a rendered interface projection live in the repo's taxonomy — and is the Context Packages root (beside the Context Index) the right shelf?
- What is the relationship between the repo file and the Cowork artifact once both exist?
- Does an HTML file need a C-006 exception, and does it get minted as a DOC node?

## 3. Human Input (Max)

Max reported the observation from the fresh conversation and asked the structural question himself ("I thought there would be a standardised, canonical document within the context package?"). Offered the lean path (accept-in-conversation, protocol later) and the full loop, he chose the **full ceremony now**, and **ratified C-048 as drafted** after the walkthrough.

## 4. AI Input (Claude)

- Read the incident as a successful failure-mode test that nonetheless exposed the gap: C-047 pinned stamp and refresh but left storage artifact-only; portability doctrine (C-020 — the repository *is* FRACTAL) was never applied to the board.
- Located the file at the Context Packages root beside the Context Index: both are standing, whole-project projections rather than Global/Local/Conversation-scoped ones.
- Proposed the demotion framing: repo file = the projection; artifact = display surface, republished from the file, never a source. Artifact loss becomes cosmetic by construction.
- Flagged the two format pins: HTML as a declared C-006 exception (rendered surface, not governed text), and no DOC mint (projection category, C-042 mint-on-reuse — same as Local Context and Return Packages).

## 5. Jointly Derived Conclusions

1. **A standing projection must have a repo-resident source or it isn't portable.** C-020's "laptop in the ocean" test applies to interfaces too: anything that must survive a machine change lives in the repository, and vendor surfaces are rehydrated from it — the C-018 swappable-clients doctrine exercised on the board.
2. **Improvised regeneration is silent drift.** Without a standardised file, each rebuild renders a subtly different board; the stamp guards content-freshness but not form. The repo file closes both.
3. **Assumptions in protocols are testable claims.** C-047 §8 was falsified within hours and cured within the day — the observed-need loop (C-021) working at governance speed.

## 6. Current Decisions

- **C-048 — Agenda Board is repo-resident (Working Decision, executed; amends C-047).** The board's rendered file is a **living projection in the repo**: `Claude/Context Packages/Fractal_Agenda_Board.html` — stable filename (C-012), stamp inside, at the package root beside the Context Index. The C-047 close-the-loop refresh now means: **regenerate this file first, then republish the Cowork artifact `fractal-agenda` from it**. The artifact is a display surface only and is never the source of anything; its loss is cosmetic by construction. Subsidiary pins: **(a)** authoring format is HTML — a declared exception to C-006 (the board is a rendered surface, not a governed text); **(b)** the file is **not** minted as a DOC node — projection category, C-042 mint-on-reuse, same as the Local Context and Return Packages. Retires C-047 §8's falsified persistence assumption (observed 2026-08-13).

- **Ratification record (2026-08-13, in-conversation per C-033).** Max chose the full loop and ratified C-048 as drafted after the walkthrough.

## 7. Alternatives Considered

- **Lean filing** (accept-in-conversation, record in the next protocol). Offered, declined by Max's call — the full loop closes today.
- **Leave the board artifact-only and accept improvised regeneration.** Rejected: the pure-projection property makes loss safe but not *standard* — form drifts, and the board has no existence under C-020 portability.
- **Mint the board file as a DOC node.** Rejected: it is a projection, not a canonical document; minting it would blur the very line C-003 draws. Mint-on-reuse stands available if the board is ever cited as a source (which it should never be).
- **A new `Board/` subfolder in Context Packages.** Rejected as premature structure (minimal necessary complexity): one file sits fine at the root beside the Index; a subfolder is warranted when a second board exists.

## 8. Assumptions

- Republishing the artifact from the file is available to any conversation with desktop access; conversations without it simply update the file — the artifact catches up at the next opportunity, and the stamp exposes any lag.
- The board file's stamp tracks the Local Context version it projects (v0.13 at this writing); file and artifact carry the same stamp when in sync.

## 9. Consequences

- **New:** `Claude/Context Packages/Fractal_Agenda_Board.html` (living projection, stamped v0.13).
- Decision Register → **v0.8**: C-048 added; amendment note on C-047.
- Rule Overview → **v0.6**: Agenda Board row updated (file-then-artifact order; artifact = display surface).
- Local Context → **v0.13**: standing refresh item rewritten to the file-first order.
- The Cowork artifact `fractal-agenda` republished from the repo file.
- Knowledge Graph Store: **+1 node (37), +6 events (130)** — this protocol's DOC mint (create, route alias, two placements) and the two living-doc revisions (Register, Rule Overview). Committed per C-037.

## 10. Decision Ledger Changes

Added **C-048** (repo-resident board; artifact demoted to display; HTML exception to C-006; no DOC mint). **C-047 amended:** §8 persistence assumption retired; refresh semantics now file-first. No OQs resolve; no new OQs open.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None new. Standing items carry unchanged: workstream E (OQ-19; scan 5.3), workstream F (scan 2.1/2.2; OQ-12; C-046 residual), OQ-3, OQ-4, OQ-18, OQ-21; C-047's Settings-escalation watch-item.

## 12. Next Line of Research

Unchanged: workstream **E** (multi-writer safety) is the queued *Next*; **F** follows; the repo-resident skill stands as an offer. Like v0.11, this is a governance interlude — a one-decision cure for an observed gap.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.12 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.12 |
| Status | Ratified (2026-08-13, in-conversation per C-033) |
| Domain | Project Governance — Conversation Operation / Interfaces |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.11 |
| Related Documents | Fractal Decision Register v0.8; Fractal Rule Overview v0.6; Fractal Local Context — Knowledge Graph v0.13; Fractal_Agenda_Board.html (the projection this governs) |
| Revision Trigger | Any change to C-048, the board file's location, or the file→artifact republish order |
| Document ID | DOC-01KZXAG032XR1MG4QBPGNWJYQJ |
