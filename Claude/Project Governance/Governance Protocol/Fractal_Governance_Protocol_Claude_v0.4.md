# Fractal Governance Protocol — Claude Series v0.4

**Topic:** Accepting the node/event format (partial); deferring the facet registry; adding the Decision Register to the context package
**Status:** Ratified (2026-08-12, per Claude Series v0.7) · **Date:** 2026-08-07 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.3

---

## 1. Context

Series v0.3 ratified the KG foundation backlog (C-013–C-021), established the Decision Register (C-028), and fixed the ChatGPT-era lineage as pointer-only (C-029), but deliberately **held** the node/event format decisions (C-022–C-027) pending Max's review. In the following review, Max walked the set decision by decision, accepting the format core and isolating the parts that need their own conversation. He also asked that the Decision Register be promoted into the context package as a standing working guideline. This protocol records those outcomes.

## 2. Questions Investigated

- Which of C-022–C-027 are accepted as-is, which need refinement, and which should be deferred?
- At what granularity does the append-only log record change — every edit, or committed saves?
- Should the event-log partition interval be fixed now?
- Where does the Decision Register belong so it is available as a guideline across conversations?

## 3. Human Input (Max)

- **C-022 accepted** (node file = Markdown + front-matter; identity required, rest optional; foldering is navigation, not identity).
- **C-023 accepted, with a carve-out:** partitioning of the log is approved, but *the interval to divide by* (monthly vs other) is left **TBD**; the verb set is accepted as written.
- **C-025 accepted, with a clarification:** while editing a document, changes are **untraced until committed/saved** — otherwise every spelling correction would count as an event.
- **C-026 deferred:** raised the prior question *what is the facet registry, and what is its purpose?* — assumed to be something like a browsable library / a source-style index (`{title or object name, topic, …}`). Left TBD to be discussed next.
- **C-027 deferred:** to be folded into the C-026 conversation.
- **Register into the context package:** wants the Decision Register available as a standing guideline of work, and noted the governance protocol must be updated to reflect it.

## 4. AI Input (Claude)

- Confirmed C-024 (log-canonical) was accepted in the same review; C-025 is its mechanical consequence and Max's commit-granularity point sharpens it: the log is a record of *committed* facts, mapping cleanly to a git commit (working edits are invisible to history until committed).
- Noted that leaving the partition interval TBD costs nothing now: partitioning-in-principle is fixed, the bracket size is a later, volume-driven tuning.
- Agreed the facet registry's *purpose* is genuinely underspecified and load-bearing enough to deserve its own conversation rather than a rushed seed; §3.3/§5 of the schema are marked provisional until then.
- Recommended treating the register like the other living projections (C-012): stable filename, mirrored into the Project spine and routed in the Context Index, refreshed under the update-ordering rule (C-004).

## 5. Jointly Derived Conclusions

1. The node/event **format core** (C-022, C-023, C-024, C-025) is accepted; FRACTAL's hand-usable format is settled.
2. Two open specifics remain: the log **partition interval** (C-023, TBD) and the whole **facet/role/allocation** layer (C-026 + C-027), the latter blocked on defining what the facet registry is for.
3. The **Decision Register** is part of the context package — a standing, cross-conversation guideline.

## 6. Current Decisions

- **Acceptance of C-022, C-023, C-024, C-025** (node/event format core), promoted from *Proposed* to **decisions of record**, with two amendments carried into the schema:
  - *C-023 amendment* — partitioning of the event log is accepted; the **partition interval is TBD** (monthly is illustrative, not fixed).
  - *C-025 clarification* — an event is recorded at **commit/save**, not per keystroke; in-progress editing (typos, prose revision) is untraced until committed.
- **Deferral of C-026 and C-027.** The facet registry, role vocabulary, weight, and code-allocation rules are **not accepted**; they move to a dedicated next conversation (KG domain) whose opening question is *what the facet registry is and what purpose it serves*. Schema §3.3 and §5 stand as a provisional proposal until resolved.
- **C-030 — Decision Register in the context package.** The `Fractal_Decision_Register` is promoted to a standing context-package guideline: mirrored into the Project spine and routed in the Context Index, maintained as a living projection (C-012) and refreshed per the update-ordering rule (C-004). It remains a derived projection that never overrides its sources (C-003). *(Working Decision.)*

## 7. Alternatives Considered

- **Fix the partition interval (e.g. monthly) now.** Rejected: premature; chosen later from observed volume with no cost to deferring.
- **Seed and accept the facet registry now to finish the format in one pass.** Rejected: its purpose is undefined; accepting a seed by momentum would violate the "keep proposals separate from accepted decisions" discipline. Deferred to its own conversation.
- **Keep the register folder-only.** Rejected: Max wants it as a cross-conversation guideline, which the context-package mirror provides (consistent with C-002 hybrid anchoring).

## 8. Assumptions

- The commit-granularity rule presumes a definable "commit/save" boundary per node/version — to be realised concretely when tooling (git and/or the index Operator) arrives.
- Mirroring the register into the Project keeps it useful only if refreshed on change (C-004).

## 9. Consequences

The node/event format is accepted and hand-usable; the schema is updated with the C-023 and C-025 amendments and marks §3.3/§5 provisional. The register becomes a standing context-package guideline (Project mirror + Context Index pointer). The next KG conversation is defined: the facet registry's purpose, then roles/weight and code allocation (C-026 + C-027).

## 10. Decision Ledger Changes

Accepted C-022, C-023 (partition interval TBD), C-024, C-025 (commit granularity). Deferred C-026 and C-027. Added decision **C-030** (Decision Register in the context package). No change to C-001–C-021, C-028–C-029.

## 11. Open Questions (TBD)

- **What is the facet registry, and what is its purpose?** (opens the next KG conversation; carries C-026 + C-027).
- **Event-log partition interval** (C-023) — chosen later from observed volume.
- Concrete definition of the **commit/save boundary** once git / the index Operator exists.
- "Genuine transition" (C-010) still undefined (carried from v0.3).
- C-015 ID generation algorithm still a Working Hypothesis.

## 12. Next Line of Research

Open the **facet-registry conversation** (KG domain, Operator): define what the registry is and is for, then settle roles/weight (C-026) and code allocation (C-027). Then KG step 2 — the Knowledge Path index MCP server — is triggered on observed need (C-021).

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.4 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.4 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Project Governance — Decision Ledger |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-07 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.3 |
| Related Documents | Fractal Decision Register v0.1; Node & Event Schema v0.1; Local Context — Knowledge Graph; Context Index |
| Revision Trigger | Any change to decisions C-022–C-030, or resolution of the facet-registry conversation |
| Document ID | DOC-01KZVYQFPGJXPJY5H1MG09DGRG (minted 2026-08-12, C-041/C-042, per v0.9) |
