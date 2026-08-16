# Fractal Governance Protocol — Claude Series v0.3

**Topic:** Ratifying the Knowledge-Graph foundation backlog; establishing the Decision Register; fixing the ChatGPT-era lineage rule
**Status:** Ratified (2026-08-12, per Claude Series v0.7) · **Date:** 2026-08-07 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.2

---

## 1. Context

Between Claude Series v0.2 and now, a run of load-bearing decisions was taken *in conversation* while designing the Knowledge Graph — the two-relation core, the identity scheme, the substrate and portability doctrine (C-013–C-020), and the build-sequencing rule (C-021). They were accepted with Max but never written into a governed protocol, so the decision ledger drifted out of step with the actual state of the project. Separately, a question — "is there one overview of C-001 → C-n?" — surfaced that **no consolidated decision index existed**, and that the `C-` numbering's origin was unclear. Investigating it confirmed the numbering is Claude-era (opened at C-001 in Series v0.1) and that the ChatGPT-era used a different notation. This protocol closes the ratification gap, records the register created to answer it, and fixes how the ChatGPT-era lineage is treated going forward.

## 2. Questions Investigated

- Which conversationally-accepted decisions (C-013–C-021) should be promoted to decisions of record, and with what type nuances preserved?
- Where does the `C-` ledger originate, and is there a single index of all decisions?
- How should the ChatGPT-era decision lineage relate to the Claude-era C-series — merge, renumber, or point?
- What is the status of the freshly-proposed KG format decisions (C-022–C-027) and the register decision (C-028)?

## 3. Human Input (Max)

- Requested a governance protocol to formalise the outstanding decisions.
- **ChatGPT-era = old foundation, pointer only.** "We may use it as source later, but for now this is the old foundation; we're building a new heritage." The pre-Claude material is referenced, not renumbered or merged into the C-series.
- Flagged that **"genuine transition" (C-010) is itself undefined** and must be marked TBD rather than treated as settled — "we don't know what we don't know" yet.
- Noted the register topic crept into a KG-scoped conversation; accepted continuing here but wanted the KG and GOV threads kept separate.

## 4. AI Input (Claude)

- Traced the numbering: the `C-` ledger opened at C-001 in Series v0.1 (2026-08-01), which explicitly opened a new series and closed the ChatGPT-era patch sequence (…v0.11). The ChatGPT era used sequential protocol patches, not numbered decisions.
- Compiled the first consolidated **Decision Register** (C-001–C-028) as a derived projection that cites its sources and never overrides them (C-003).
- Recommended **not** renumbering ChatGPT-era decisions into the C-series: it would collide with the existing C-001+ and violate identity stability (C-005). Pointer-only preserves both lineages cleanly.
- Recommended ratifying C-013–C-021 while preserving their type nuances (e.g. C-015's ID *scheme* stays a Working Hypothesis even as the separation principle is load-bearing), and **holding** C-022–C-027 as proposals until Max reviews them, because C-024 (canonical-source rule) is load-bearing and must not be accepted by default.

## 5. Jointly Derived Conclusions

1. The KG load-bearing decisions (C-013–C-021) are accepted and are now decisions of record.
2. The Claude-era C-series is the single going-forward decision ledger; the Decision Register is its index.
3. The ChatGPT-era lineage is preserved as the *old foundation* — pointed to, not merged; usable as a source later.
4. "Genuine transition" (C-010) is an open definition (TBD), to be fixed from observed cases.
5. The KG format decisions (C-022–C-027) remain proposals pending Max's explicit acceptance; the register decision (C-028) is adopted.

## 6. Current Decisions

- **Ratification of C-013–C-021.** The decisions taken in the Knowledge Path Foundation conversation (C-013–C-020) and the build-sequencing decision (C-021) are promoted from *accepted-in-conversation* to **decisions of record**, as catalogued in the Decision Register. Type nuances are preserved verbatim from their source: notably **C-015** — the separation of identity from context is a *Principle*; the specific `TYPE-ULID`/content-hash *scheme* remains a *Working Hypothesis* until confirmed. *(This protocol is the ratification vehicle; it takes effect on Max's review.)*
- **C-028 — Decision Register.** The `Fractal_Decision_Register` is established as the canonical decision-index projection: every numbered decision is listed with its type, ratification status, and source document; the register never supersedes its sources (C-003). Stable filename, internal version (C-012). *(Working Decision.)*
- **C-029 — ChatGPT-era lineage is pointer-only.** The pre-Claude decision lineage (sequential protocol patches …v0.11; ChatGPT-era Governance Protocol v0.1–v0.2) is the *old foundation*. It is referenced by pointer from the register, **not** renumbered into or merged with the Claude-era C-series. It may be cited as a source if specific material is later reused, but the Claude-era C-series is the sole active going-forward ledger — the "new heritage." *(Working Decision.)*

## 7. Alternatives Considered

- **Renumber / merge ChatGPT-era decisions into the C-series.** Rejected (C-029): collides with existing C-001+ and violates C-005 identity stability; the old lineage would lose its clean provenance boundary (C-007).
- **Catalogue ChatGPT-era decisions under a separate prefix (e.g. `P-xx`) now.** Deferred: unnecessary until specific pre-Claude decisions are actually reused; pointer-only suffices for now.
- **Ratify C-022–C-027 in this protocol.** Rejected: C-024 is load-bearing and unreviewed; ratifying by default would violate the "keep proposals separate from accepted decisions" discipline. Held for a focused KG acceptance.
- **Define "genuine transition" (C-010) now.** Rejected: too few phase transitions exist to generalise a criterion; better defined from observed cases (kept TBD).

## 8. Assumptions

- Max's in-conversation acceptance of C-013–C-021 is faithfully captured by the Foundation and Local Context sources the register cites.
- The register, as a projection, stays honest only if statuses are updated when sources change (per C-004 ordering).

## 9. Consequences

The decision ledger is now consistent with the project's actual state for C-013–C-021. The Decision Register (C-001–C-029) is the single index of decisions. The ChatGPT-era lineage has a fixed, pointer-only relationship to the Claude-era series. C-022–C-027 remain visibly pending, so the KG format is not treated as settled until reviewed. The Context Index should gain a pointer to the register (housekeeping, below).

## 10. Decision Ledger Changes

Ratified C-013–C-021 (promoted to decisions of record). Added decisions **C-028** (Decision Register) and **C-029** (ChatGPT-era pointer-only lineage). No change to C-001–C-012. C-022–C-027 remain *Proposed*.

## 11. Open Questions (TBD)

- **Definition of a "genuine transition" (C-010).** Undefined; to be fixed from observed realisation-phase transitions. Belongs in Series v0.2 §11 when settled.
- **Acceptance of C-022–C-027** (KG node/event format), especially the load-bearing **C-024** canonical-source rule and the seeded role/facet vocabularies — pending Max's review in a KG-domain decision.
- **C-015 ID algorithm** remains a Working Hypothesis until the generation scheme is confirmed.
- Whether ChatGPT-era decisions are ever individually indexed (`P-xx`) if reused — deferred; default remains pointer-only.

## 12. Next Line of Research

Accept or amend C-022–C-027 in a focused KG review (Operator), starting with C-024. Then KG step 2 — the Knowledge Path index MCP server — is triggered on observed need (C-021). Housekeeping: add a register pointer to the Context Index; when a "genuine transition" criterion emerges, record it in Series v0.2 §11.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.3 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.3 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Project Governance — Decision Ledger |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-07 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.2 |
| Related Documents | Fractal Decision Register v0.1; Knowledge Path Foundation v0.1; Node & Event Schema v0.1; Local Context — Knowledge Graph; Context Index |
| Revision Trigger | Any change to decisions C-013–C-029, or ratification of C-022–C-027 |
| Document ID | DOC-01KZVYQBSGW3YHXHY14CVN2NAY (minted 2026-08-12, C-041/C-042, per v0.9) |
