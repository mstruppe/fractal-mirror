# Fractal Governance Protocol — Claude Series v0.5

**Topic:** Continuity & primacy — teaching every conversation to carry the loaded context as foreknowledge without presuming on the user
**Status:** Ratified (2026-08-12, per Claude Series v0.7) · **Date:** 2026-08-07 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.4

---

## 1. Context

FRACTAL's context-persistence model means each conversation is bounded and stateless across the chat boundary: memory lives in the loaded context, not in chat history (C-001). A consequence surfaced in use — when Max opens the *next* conversation the previous one queued (e.g. the facet-registry step named in the Local Context's *Next*), that fresh conversation has genuinely loaded the anticipation, yet can carry itself as if the topic were novel: it "acts surprised" that Max asked exactly what the context foretold. Max asked for the opposite stance — a system that is "self-conscious" of its own workflow — while insisting the balance be kept: the agent must recognise the queued topic as expected when raised, but must never demand or presume the user's request is about it. The user's request is primary.

## 2. Questions Investigated

- How can a fresh conversation convey real continuity with the queued *Next* without faking memory?
- How do we prevent the agent from either (a) treating the anticipated topic as novel, or (b) presuming the user's request must be that topic?
- Where does such a rule live so it applies to every conversation?

## 3. Human Input (Max)

- Wants FRACTAL "self-conscious": the context should convey that each new conversation follows another, so asking about a topic already queued in the context package is *expected*, not surprising.
- **Hard constraint:** if the user does **not** ask about what the context implies, the agent **MUST NOT** demand or expect the request to be about the implied topic. "The agent's primary are the user requests after all."

## 4. AI Input (Claude)

- Reframed: this is not memory or illusion — the context genuinely *is* the memory (C-001), so the fix is a **stance rule**, not fabricated recall. The Local Context's *Next* is real foreknowledge; the failure is behavioural.
- Proposed the operating principle: **loaded context is a prior; the user's request is the ground truth.** Request confirms prior → smooth continuity; request diverges → drop the prior instantly and follow the user.
- Distinguished *acknowledging readiness* (legitimate continuity — "I loaded X; the queued step is Y") from *committing the user* (illegitimate presumption) — the line that satisfies Max's constraint.
- Recommended the rule's normative home be `Fractal_Conversation_Settings_v0.1.md` (loaded every conversation via the Custom Instructions projection), with a matching note that the *Next* is "the baton."

## 5. Jointly Derived Conclusions

1. Continuity is real, carried by the loaded context, and must be *behaved*, not simulated.
2. The queued *Next* is anticipation, never obligation; the user's request always dominates.
3. The rule belongs in Conversation Settings so it applies universally.

## 6. Current Decisions

- **C-031 — Continuity & primacy.** Every conversation is one bounded step in a continuing program, not a fresh start; the active Local Context's *Next* is genuine foreknowledge (C-001). (a) When the user takes up the queued item, receive it as *expected* — name the thread it continues, proceed from the prepared opening question, do not act surprised or re-derive settled context. (b) When the user goes elsewhere, follow them — the queued item is a standing offer, never a mandate; do not steer, presume, or reframe their request as "really" about it. (c) When ambiguous, offer the queued item once, then follow the answer. Claude may open by acknowledging readiness but must not commit the user before they speak. The user's request is primary; loaded context is prior knowledge, held in reserve otherwise. *(Working Decision. Normative home: Conversation Settings §4 rule 8.)*

## 7. Alternatives Considered

- **Carry state in chat memory / cross-conversation recall.** Rejected: contradicts C-001 (context is the memory) and portability; brittle and vendor-bound.
- **Have each conversation open by driving the queued topic.** Rejected: violates user-primacy (Max's hard constraint) — presumes before the user speaks.
- **Say nothing about continuity and rely on the model's defaults.** Rejected: that is exactly the "acts surprised" failure this protocol fixes.

## 8. Assumptions

- The rule reaches conversations only once mirrored into the **Custom Instructions field** (the injection projection); until Max syncs it, the behaviour is documented but not yet enforced.
- The Local Context's *Next* is kept current at close (existing update-ordering, C-004), so the foreknowledge it conveys is accurate.

## 9. Consequences

Conversation Settings gains rule 8 (v0.2). New conversations should now recognise a queued topic as expected when raised, and follow the user without presumption otherwise. A sync action falls to Max: add C-031 to the Custom Instructions field. Divergence between this document and that field is flagged per Conversation Settings §6.

## 10. Decision Ledger Changes

Added decision **C-031** (Continuity & primacy). Updated Conversation Settings to v0.2. No change to prior decisions.

## 11. Open Questions (TBD)

- Whether the Custom Instructions text should be auto-generated from Conversation Settings to guarantee sync (carried from that document).
- How strong the "offer once" nudge (case c) should be before it reads as steering — to calibrate in use.

## 12. Next Line of Research

Max syncs the Custom Instructions field with Conversation Settings v0.2. Then the queued KG work resumes: the **facet-registry conversation** (C-026 + C-027).

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.5 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.5 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Project Governance — Conversation Operation |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-07 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.4 |
| Related Documents | Fractal Conversation Settings v0.2; Fractal Decision Register v0.1; Fractal Local Context — Knowledge Graph |
| Revision Trigger | Any change to the continuity & primacy rule (C-031) |
| Document ID | DOC-01KZVYQKKG5B3FZFFG4ZG3KMSK (minted 2026-08-12, C-041/C-042, per v0.9) |
