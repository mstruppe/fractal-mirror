# Fractal Governance Protocol — Claude Series v0.2

**Topic:** Context Model Refinement — the Global/Local spine, current-realisation framing, and living-document naming
**Status:** Ratified (2026-08-12, per Claude Series v0.7) · **Date:** 2026-08-01 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.1

---

## 1. Context

After the Context Persistence Workflow was stood up (Claude Protocol v0.1), Max refined the context model. The original Global Context mixed stable material (vision, philosophy) with more dynamic material (architecture map, workflow). Max proposed separating the stable and dynamic poles cleanly, and clarified what the stable pole should contain. Protocolling this update was requested explicitly.

## 2. Questions Investigated

- What belongs in the stable Global Context versus the dynamic Local Context?
- How should the project's current stage of realisation be represented, and where?
- How can a version bump of an always-loaded orientation document avoid breaking the Custom-Instructions pointer that injects it?

## 3. Human Input (Max)

- **Global Context is stable and contains the vision *plus* a simple breakdown of how the project is currently realised** — right now, "by building the foundational architecture." As the project realises into a new form (e.g., an interactive interface), that realisation is updated in the Global Context.
- **Local Context is dynamic and concerns a specific aspect of the current realisation**, following the vision.
- Requested that this governance update be recorded as a protocol.

## 4. AI Input (Claude)

- Mapped the proposal to a **stable/dynamic spine**: Global = stable pole (vision + current realisation); Local = dynamic pole (an aspect of the current realisation). Domain/Task/Return remain the scopes and mechanics by which a Local Context is worked and handed off — not a competing scheme.
- Noted the structure is **nested and fractal** (Vision → Realisation → Aspect ≈ why → what-form-now → which-part-now), so a Local Context cannot drift from the vision.
- Noted a **free phase-level changelog**: because the current-realisation line changes only at true transitions, the sequence of those changes records how the vision materialised.
- Proposed an **opening convention**: every Local Context names which aspect of the current realisation it addresses.
- Surfaced a naming problem: version-bumping an always-loaded orientation document changes its filename and breaks the injected pointer. Proposed treating orientation projections as **living documents with stable filenames**, tracking version internally.

## 5. Jointly Derived Conclusions

1. The context spine is Global (stable) vs Local (dynamic).
2. Global Context = vision + current realisation; it is updated only at realisation-phase transitions.
3. Local Context = an aspect of the current realisation and opens by naming that aspect.
4. Orientation projections are living documents; filenames are stable pointers and versions are tracked inside.

## 6. Current Decisions

- **C-009 — Global/Local spine.** Global Context is the stable pole (vision + current realisation); Local Context is the dynamic pole (an aspect of the current realisation). Domain/Task/Return are scopes and mechanics of Local. *(Principle.)*
- **C-010 — Realisation phasing.** The Global Context's current-realisation statement changes only at genuine transitions in how the project is embodied; the ordered sequence of these changes is the project's phase-level history. *(Principle.)*
- **C-011 — Local opening convention.** Every Local Context begins by naming which aspect of the current realisation it addresses. *(Working Decision.)*
- **C-012 — Living-document naming.** Living projections (Global Context, Context Index, Conversation Settings, Architecture State, Local Contexts) use a stable filename with the version tracked internally; historical/sequential artifacts (Protocols, Return Packages) carry versioned or dated filenames. Existing `_v0.1` orientation filenames are grandfathered as stable pointers, preserving the Custom-Instructions pointer. *(Working Decision.)*

## 7. Alternatives Considered

- Keep vision, philosophy, and architecture map together in one Global Context. Rejected: mixes stable and dynamic content and reintroduces bloat.
- Bump orientation-document filenames on each revision. Rejected: breaks the injected Custom-Instructions pointer (violates identity stability, C-005).

## 8. Assumptions

- Realisation transitions are rare relative to conversation-level work, so the Global Context stays cheap to load.
- Local Contexts may be numerous over time; each stays scoped to one aspect.

## 9. Consequences

Global Context restructured to v0.2 (vision + current realisation) with a stable filename. First Local Context created for the Knowledge Graph aspect. Context Index updated with an Active-Local-Context section and the C-012 naming convention. The Custom-Instructions pointer is unaffected.

## 10. Decision Ledger Changes

Added decisions C-009 through C-012.

## 11. Open Questions (TBD)

- Whether the active Local Context should be *fed* by the previous Return Package (a self-updating "where we are"), or authored independently.
- When Conversation Settings adopts the Global/Local terminology and states C-012 normatively (deferred to its next revision).
- Whether remaining `_v0.1` orientation filenames are eventually normalised to versionless names (currently grandfathered).

## 12. Next Line of Research

The Knowledge Graph conversation: blank-page design of the code/identity system, loading `Fractal_Local_Context_Knowledge_Graph.md`.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.2 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.2 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Project Governance — Context Model |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-01 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.1 |
| Related Documents | Fractal Global Context (v0.2); Fractal Local Context — Knowledge Graph; Fractal Context Index; Fractal Conversation Settings |
| Revision Trigger | Any change to the context-model spine or the naming convention |
| Document ID | DOC-01KZVYQ7WGDW49X5EDF4KMQVM2 (minted 2026-08-12, C-041/C-042, per v0.9) |
