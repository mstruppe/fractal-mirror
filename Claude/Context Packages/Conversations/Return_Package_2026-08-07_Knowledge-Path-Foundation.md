# Conversation Return Package — 2026-08-07 (Knowledge Path Foundation)

> State-transfer object, not a transcript. Read this to resume without reloading the conversation.

**Conversation scope:** FRACTAL — Knowledge Graph domain (KG). Design the "Knowledge Path": a simple, robust, portable mechanism to give every piece of information a stable identity and trace it within context across domains; decide the technical substrate and the portability model.

**Parent:** Fractal Global Context · **Objective:** turn the blank-page KG aspect into a decided, externalised clean-era foundation.

## State at close

A canonical foundation document exists (`Fractal_Knowledge_Path_Foundation_v0.1.md`, Draft/Proposal). The Local Context is refreshed to v0.2 (blank page → designed). Load-bearing decisions were accepted-in-conversation with Max; scheme specifics remain Working Hypothesis / TBD.

## Decisions of record (this session)

- **C-013** Forge a clean Claude-era foundation *from* ChatGPT-era material (not retrofit).
- **C-014** Essential core = two relations (Identity + Placement) recorded in one Event Log; the eight KG components are blocks added back.
- **C-015** Persistent Object ID = opaque `TYPE-ULID` for living entities; content-hash per version; names/codes are aliases (git choosing rule).
- **C-016** Facets are independent namespaces; routing codes **derive from** identity (resolves prior open question).
- **C-017** Shells = two faces of one node — Galaxy (container) / Operator (application); an Operator's run appends provenance edges.
- **C-018** Substrate **B** — FRACTAL is a thin layer over git + files + MCP + Skills; vendor surfaces (Projects/Memory/Claude Code) are swappable clients.
- **C-019** Canonical data is plain text in git; the index DB is a derived, disposable cache.
- **C-020** Portability doctrine — the repository *is* FRACTAL; bootstrap protocol ships in-repo; "laptop in the ocean" acceptance test.

## Assumptions

- MCP remains the portable tool interface across Claude and ChatGPT.
- Git is an acceptable substrate for identity/integrity/provenance/replication (no bespoke store needed).
- Architecture State ONT (Galaxy/Operator) is still open design space, not a locked spec.

## Open questions

- Final ID generation algorithm; event/edge schema (roles, weights, supersede); Concept-code allocation & reparenting.
- Bootstrap/rehydrate protocol contents; migration of ChatGPT-era documents.
- Confirm the ULID-vs-hash split as accepted (currently Working Hypothesis).

## Dependencies

- Inherits Knowledge Graph Architecture v0.1 principles; must be reconciled against Architecture State v0.1 Parts IV–V.
- Connected folder `Desktop/FRACTAL/` is the canonical store; Project is a projection.

## Provenance

FRACTAL Knowledge Path design conversation, 2026-08-07 (Claude). Sources in the Foundation doc §"Sources".

## Change summary (files written this session)

- **NEW** `Claude/Architecture/Concepts/Knowledge Graph/Fractal_Knowledge_Path_Foundation_v0.1.md` — canonical foundation.
- **UPDATED** `Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md` → v0.2.
- **NEW** `Claude/Context Packages/Conversations/Return_Package_2026-08-07_Knowledge-Path-Foundation.md` — this package.
- **MIRRORED** refreshed Local Context to the Claude Project spine.

## Refresh list (not done this session — next conversation)

1. Reconcile Galaxy/Operator into **Architecture State** (ONT, Parts IV–V).
2. Bump **Context Index** KG row to point at the Knowledge Path Foundation as canonical.
3. Prototype the **Knowledge Path index MCP server** (`place` / `trace` / `query-by-facet`).
4. Draft the **event/edge schema** and the **bootstrap protocol**.
5. Promote foundation decisions C-013–C-020 from Proposal to accepted in a Governance Protocol entry once confirmed.
