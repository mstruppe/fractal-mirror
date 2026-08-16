# Fractal Governance Protocol — Claude Series v0.11

**Topic:** The Agenda Board — a standing, stamped interface projection of the active Local Context's agenda (C-047); the C-035 stamped-projection mechanism extended from text to interface
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.10

---

## 1. Context

The conversation opened as an agenda inquiry ("what's next, are next items idle?") answered from the Local Context v0.11. Asked to *show* the agenda, Claude rendered it as a one-page HTML overview; Max then asked to introduce that overview as a **user interface** — a standing at-a-glance view of the queue, so that "I don't have to think about whether I miss something." The board was persisted as the Cowork artifact `fractal-agenda`. That promotion — from one-off view to standing surface — is exactly the moment governance must catch: an ungoverned standing projection is a second source of truth waiting to happen (the failure mode C-003 exists to prevent), and an unrefreshed one silently defeats its own purpose. Max called for the decision to be protocolled and filed in the Decision Register and Rule Overview.

## 2. Questions Investigated

- What *is* the agenda board, governance-wise — a new mechanism, or an existing one in a new medium?
- How is its freshness guaranteed without a new maintenance burden — where does its refresh hook into the existing loop?
- Does the rule need to live in Conversation Settings (and therefore in the Custom-Instructions projection), or is the Rule Overview + Local Context filing sufficient?

## 3. Human Input (Max)

Max asked for the agenda as a persistent interface, made stale-proofing the explicit motive (never having to wonder whether something is missed), and directed that the decision be protocolled and filed in both registries. He raised the custom-instructions question himself mid-conversation. Presented with the C-033 walkthrough, he **ratified C-047 as drafted**, chose the **lean filing** (Rule Overview + Local Context; Conversation Settings v0.3 untouched), and chose the **full canon loop now** (store mint + commit in this conversation).

## 4. AI Input (Claude)

- Identified the board as the **C-035 mechanism in a second medium**: like the Custom-Instructions field, it is a governed projection — a compression of a canonical source, delivered where the reader already is. The same three safeguards transfer verbatim: labelled as derived, version-stamped against its source, never authoritative. No new governance machinery is invented; an existing rule is exercised at a new surface.
- Located the refresh in the **existing close-the-loop step** (C-001/C-004): the board regenerates whenever a conversation's refresh touches the Local Context's agenda — zero standing cost, because the trigger is a step every substantive conversation already performs.
- Recommended the lean filing per the credo (minimal necessary complexity; C-021 build-on-observed-need applied to governance): rule 6's refresh list plus a standing line in the always-loaded Local Context carries the rule; amending Conversation Settings buys marginal self-enforcement at the cost of a Settings revision and a Custom-Instructions update. Escalation path named: amend Settings if the board is ever found stale in practice.
- Noted the safety property worth pinning in the decision text: **nothing lives only in the board** — it is pure projection, so its loss or staleness can never lose project state.

## 5. Jointly Derived Conclusions

1. **A standing interface is a governed projection or it is a liability.** The moment a view outlives its conversation, it either carries a stamp and a refresh hook or it starts to drift into a shadow source of truth. C-035 already solved this for text; the board shows the solution is medium-independent.
2. **Refresh must ride an existing ritual, not create one.** A standing surface with its own maintenance schedule would violate minimal necessary complexity; hooking it to the close-the-loop refresh makes freshness a side effect of discipline already in force.
3. **Filing depth follows observed need.** The rule enters at the lightest layer that carries it (Rule Overview + Local Context); Conversation Settings remains the escalation, not the default.

## 6. Current Decisions

- **C-047 — Agenda Board: standing agenda projection (Working Decision, executed).** The Agenda Board — the Cowork artifact `fractal-agenda` — is a standing **governed projection** of the active Local Context's agenda: the queued *Next*, the sequenced workstreams, parked open questions, standing offers, and completed workstreams. It extends the C-035 mechanism from text to interface: it is a compression, not a copy; it **must open with a version stamp** naming its source Local Context version + date; a stale stamp *is* divergence; it never becomes authoritative (C-003). It joins the **refresh list as a standing item**: any conversation whose close-the-loop step changes the Local Context's agenda regenerates the board in the same step (C-004 tail). Nothing lives only in the board — it is pure projection, so nothing can be lost through it. Filing: Rule Overview + Local Context (lean); Conversation Settings v0.3 untouched; escalate to a Settings amendment only on observed staleness.

- **Ratification record (2026-08-13, in-conversation per C-033).** Max ratified C-047 after the walkthrough, choosing the lean filing and the full canon loop explicitly.

## 7. Alternatives Considered

- **Leave the board ungoverned** (a convenience artifact outside the registries). Rejected: a standing surface without a stamp is a drift risk by construction — the exact gap C-035 closed for the Custom-Instructions field.
- **Amend Conversation Settings now** (rule 6 board line → v0.4 + Custom-Instructions re-projection). Defensible, offered, declined by Max's call: the lean filing carries the rule through machinery already loaded into every conversation; Settings amendment stands as the named escalation if staleness is ever observed.
- **Give the board a `Fractal_<Name>` artifact identity (C-005).** Rejected: the board is not an exported artifact but a rendered projection surface, the same category as the Custom-Instructions field — governed by stamp (C-035 pattern), not by artifact identity.
- **Defer the store mint to next touch** (C-041 allows "shortly after first commit"). Offered, declined by Max's call: the loop closes completely today.

## 8. Assumptions

- The Cowork artifact `fractal-agenda` persists in Max's artifact gallery across sessions and can be regenerated by any future conversation with desktop access; if the surface ever disappears, the projection is rebuilt from the Local Context at zero loss (pure-projection property).
- The stamp convention transfers unchanged from C-035: *"Projection of Fractal_Local_Context (Knowledge Graph) v<X>, <date>"*; sync-check = stamp vs. the loaded Local Context's version.
- Board regeneration is in-scope for any conversation that updates the Local Context's agenda, regardless of that conversation's declared domain (it is a close-the-loop mechanic, not domain work).

## 9. Consequences

- Decision Register → **v0.7**: C-047 added; no OQ resolves; no new OQ opens.
- Rule Overview → **v0.5**: Agenda Board row added to §2 (governance rules); refresh-trigger note.
- Local Context → **v0.12**: standing refresh item (the board) added; this conversation recorded; agenda otherwise unchanged — E remains the queued *Next*.
- The board itself carries its first stamp: *Projection of Fractal_Local_Context (Knowledge Graph) v0.12, 2026-08-13.*
- Knowledge Graph Store: **+1 node (36), +6 events (124)** — this protocol's DOC mint (create, route alias, two placements) and the two living-doc revisions (Register, Rule Overview). Committed per C-037.
- Conversation Settings v0.3 and the Custom-Instructions projection: **unchanged** (lean filing).

## 10. Decision Ledger Changes

Added **C-047** (Agenda Board — standing stamped projection of the Local Context's agenda; refresh rides close-the-loop; lean filing). No prior decision content changed; C-035 gains its first cross-medium exercise. No OQs resolve; no new OQs open.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None new. Standing items carry unchanged: workstream E (OQ-19; scan 5.3), workstream F (scan 2.1/2.2; OQ-12; C-046 residual), OQ-3, OQ-4, OQ-18, OQ-21.
- Watch-item (not an OQ): if the board is ever found stale despite the refresh-list line, escalate the filing to Conversation Settings (§7, alternative 2).

## 12. Next Line of Research

Unchanged from v0.10: workstream **E** (multi-writer safety) is the queued *Next*; **F** follows; the repo-resident skill stands as an offer. This protocol is a governance interlude, not a workstream — the agenda it governs is the one it leaves in place.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.11 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.11 |
| Status | Ratified (2026-08-13, in-conversation per C-033) |
| Domain | Project Governance — Conversation Operation / Interfaces |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.10 |
| Related Documents | Fractal Decision Register v0.7; Fractal Rule Overview v0.5; Fractal Conversation Settings v0.3 (unchanged); Fractal Local Context — Knowledge Graph v0.12 |
| Revision Trigger | Any change to C-047, the board's stamp convention, or its refresh hook |
| Document ID | DOC-01KZX8P0PHESF55S5PJZFANW72 |
