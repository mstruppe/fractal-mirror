# Fractal Governance Protocol — Claude Series v0.6

**Topic:** The facet registry — what it is and what it is for (C-026), its code-allocation grammar vs. naming style (C-027), and the first live Knowledge Graph store (C-032)
**Status:** Ratified (2026-08-12, per Claude Series v0.7) · **Date:** 2026-08-12 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.5

---

## 1. Context

This is the deferred conversation the Knowledge Graph Local Context queued as *Next* (C-031 continuity): the Node & Event Schema v0.1 fixed the node/event format and accepted C-022–C-025, but explicitly **deferred** the facet layer (C-026 + C-027) to its own conversation, with the opening question recorded verbatim in the Decision Register — *what is the facet registry, and what is its purpose?* Until now the schema's §3.3 (roles) and §5 (facets + code allocation) stood as a provisional proposal. This protocol records how that question was answered, the one refinement the conversation added, and the first act of using the format on real data.

## 2. Questions Investigated

- What *is* the facet registry — a hand-authored control artifact, or a derived view?
- What is it *for*, in FRACTAL's terms (recursive simplicity; multi-person, long-horizon work)?
- Is the seeded facet set right — in particular, does `agent` earn a facet, and how should human-vs-AI be expressed?
- Must a naming convention be standardised, or does that violate "stay flexible, we don't know what we don't know"?
- How is any of this practically implemented at zero infrastructure?

## 3. Human Input (Max)

- Confirmed the folder-path intuition: a facet code is literally like a file path (Finder / Jupyter), except foldering is interface, not identity.
- Wanted an **encoded standard** — a "sign language for everyone" — so multiple people can share one knowledge system, while keeping it **very simple and flexible**.
- Decided: when Claude generates a document, **Claude is the author** (`by AGENT.…CLAUDE`).
- Asked for a way to **distinguish human vs AI agents generally**, keeping named agents, so one can also filter the two classes.
- Approved **branching the agent facet by kind at its root**.
- Approved standing up the live store, at `Claude/Knowledge Graph Store/`.

## 4. AI Input (Claude)

- Reframed the registry as a **projection, not a control file**: because concepts are `TOP-…` entities like everything else, the registry is just those concept nodes grouped by facet, folded from the event log (consistent with C-019 index-as-derived-cache and C-024 log-canonical). Max's "browsable library / source-style index" is that inverted fold.
- Distilled the **basic requirements** the naming system must meet (a sign means one thing forever; sign ≠ word; multi-homing; decentralised minting without collision; reorganise without erasing history; legible with no tools) and showed each is exactly one of C-027's allocation rules — grounding the grammar in need.
- Resolved the standard-vs-flexible tension as **fix the grammar, grow the dictionary**: a small fixed rule-set generates an unbounded, evolving vocabulary; naming *style* is left as a soft, project-level convention whose job is legibility and reducing duplicate coordinates, never correctness.
- Recommended expressing human/AI by **branching the agent facet** (`AGENT.HUMAN.*` / `AGENT.AI.*`) rather than a parallel `agent-kind` facet: kind is intrinsic to the agent, the filter is one prefix scan, and a separate facet would only duplicate the fact and risk drift.
- Corrected the "3-letter/license-plate" worry: only the entity-type prefix is a short fixed set; coordinates are variable-length dotted words, and uniqueness is only required **under a parent**, so the namespace never exhausts.

## 5. Jointly Derived Conclusions

1. The facet registry is the browsable, log-derived projection of coordinate-concepts grouped by facet — not a separately authored catalog. Its purpose is to give `place` / `trace` / `query-by-facet` one stable, shared coordinate system: consistent placement, cheap prefix-scan retrieval, natural multi-homing, and safe multi-person / long-horizon work through permanent shared signs.
2. The `agent` axis is a facet, branched by kind at its root; human-vs-AI is a prefix filter, not a new facet.
3. Allocation splits into a **universal fixed grammar** and a **soft, project-level naming style**.
4. Implementation at this stage is the by-hand plain-text protocol (C-021 defers the index); it was exercised by bootstrapping the first live store.

## 6. Current Decisions

- **C-026 — Facet registry (Accepted).** The facet registry is the browsable, log-derived projection of coordinate-concepts (`TOP-…`) grouped by facet — a projection, not a control file. Facets `{topic, method, source-type, time, agent}`; the **agent facet is branched by kind** (`AGENT.HUMAN.<name>` / `AGENT.AI.<name>`); role vocabulary `{about, in, cites, by, member-of, is-a, derived-from}`; `weight ∈ [0,1]` marks central vs merely tagged. Vocabularies are seeds, extended on observed need. *(Working Decision.)*
- **C-027 — Facet-code allocation (Accepted).** The **grammar** is universal and fixed: mint-before-use; immutable & never reused; unique-under-parent; label separate from code; honest depth + weight; reparent-by-redirect (never delete); parentage carried by the code prefix; routing codes derive from identity. The **naming style** (how segments are spelled/abbreviated) is a *recommended project-level convention, not a mandated rule*. *(Working Decision.)*
- **C-032 — Knowledge Graph Store established (Accepted).** The live plain-text store exists at `/Claude/Knowledge Graph Store/` with `nodes/` and `_events/`. Seeded by minting the agent-kind branch and the `KG`/`GOV` topic roots, then creating and placing the first real document. FRACTAL is now hand-usable with zero infrastructure; the `place`/`trace`/`query-by-facet` index remains deferred to observed need (C-021). *(Working Decision.)*

## 7. Alternatives Considered

- **A hand-authored registry / curated catalog.** Rejected: demotes the event log below C-024 and duplicates what the fold already gives; the registry is a projection.
- **A separate `agent-kind` facet (HUMAN/AI as its own axis).** Rejected: kind is intrinsic to the agent; a parallel axis duplicates the fact, risks drift, and needs a join to filter where the branch needs one grep.
- **Mandating a naming convention up front.** Rejected as premature specification; correctness never depends on spelling, so style stays a soft project convention.
- **Pre-seeding a full taxonomy.** Rejected: mint on observed need; the bootstrap minted only the seven coordinates the first document required.

## 8. Assumptions

- Foldering is navigation, not identity (C-022), so the store location is movable without breaking references.
- Genesis self-reference (the first `mint` events' `actor` naming a code minted in the same batch) is acceptable under the zero-infra clause; it is true by the end of the batch.

## 9. Consequences

- Node & Event Schema v0.1 status Draft (Proposal) → **Accepted**; §5 provisional banner replaced; agent-branch and grammar-vs-style folded into §5; §4.5 marked accepted (C-024).
- Decision Register → v0.2: C-026/C-027 promoted to Accepted, C-032 added, open-question 2 closed.
- Local Context (KG) → v0.6 and Context Index → v0.4 refreshed; the live store is now routed.
- FRACTAL crosses from *specified* to *running with real data* — a candidate phase note for the Global Context if Max judges it a genuine transition (C-010), though a hand-store may not yet qualify.

## 10. Decision Ledger Changes

Accepted **C-026** and **C-027** (previously Deferred); added **C-032** (Knowledge Graph Store established). No change to prior decisions.

## 11. Open Questions (TBD)

- Log **partition interval** (C-023) — chosen later from observed volume.
- Whether `time` placements should auto-derive from `created` — carried, non-blocking.
- Whether standing up a live hand-store counts as a "genuine transition" for the Global current-realisation line (C-010).

## 12. Next Line of Research

Begin placing real FRACTAL content into the store as usage warrants; build the `place`/`trace`/`query-by-facet` index only when tracing-by-grep gets slow (C-021 step 2).

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.6 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.6 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Knowledge Graph — Facet Registry |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-12 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.5 |
| Related Documents | Fractal Node & Event Schema v0.1; Fractal Decision Register v0.2; Fractal Local Context — Knowledge Graph v0.6; Fractal Context Index v0.4; Knowledge Graph Store (live) |
| Revision Trigger | Any change to the facet registry (C-026), the allocation grammar/style (C-027), or the store definition (C-032) |
| Document ID | DOC-01KZVYQQGGYJ0WZYZG3RY02W57 (minted 2026-08-12, C-041/C-042, per v0.9) |
