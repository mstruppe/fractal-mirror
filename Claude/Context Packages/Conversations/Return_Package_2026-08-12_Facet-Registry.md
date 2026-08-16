# Conversation Return Package — 2026-08-12 (Facet Registry)

> State-transfer object, not a transcript. Read this to resume without reloading the conversation.

**Conversation scope:** FRACTAL — Knowledge Graph domain (KG). The deferred facet-registry conversation queued by the Local Context's *Next* (C-031 continuity). Opening question, verbatim from the register: *what is the facet registry, and what is its purpose?* Resolves C-026 + C-027, and — because implementation was exercised — stands up the first live store (new C-032).

**Parent:** Fractal Node & Event Schema v0.1 (§3.3 roles, §5 facets/allocation, previously provisional). **Objective:** fix what the facet registry is and is for, settle the seeded vocabularies and code-allocation rules, then make it real.

## State at close

The facet layer is **accepted and running**. The Node & Event Schema is now **Accepted** (was Draft/Proposal); its §5 provisional banner is replaced, the agent-branch and grammar-vs-style are folded in, and §4.5 is marked accepted (C-024). A new **Governance Protocol — Claude Series v0.6** ratifies C-026, C-027 and C-032. The **live store** exists at `/Claude/Knowledge Graph Store/` (`nodes/` + `_events/2026-08.jsonl` + README), seeded by minting the agent-kind branch and the `KG`/`GOV` topic roots, then creating + placing the first real document. Three by-hand traces verified end-to-end: AI-authorship prefix filter (`AGENT.AI.*`), topic filter (`KG`), and the placements-fold from the log (C-024). FRACTAL has crossed from *specified* to *running with real data*.

## What the facet registry is (the answer of record)

The facet registry is the **browsable, log-derived projection of the coordinate-concepts (`TOP-…`) grouped by facet** — a projection, not a hand-authored control file (consistent with C-019 index-as-derived-cache and C-024 log-canonical). Two tiers: a small **facet set** (independent axes) and an open, minted **coordinate vocabulary** within them; Max's "browsable library / source-style index" is the inverted fold over these. **Purpose:** give `place` / `trace` / `query-by-facet` one stable shared coordinate system — consistent placement, cheap prefix-scan retrieval, natural multi-homing, and safe multi-person / long-horizon work through permanent shared signs.

## Decisions of record (accepted this session, Governance Protocol v0.6)

- **C-026** — Facet registry = log-derived projection of `TOP` coordinate-concepts by facet. Facets `{topic, method, source-type, time, agent}`; **agent facet branched by kind** (`AGENT.HUMAN.<name>` / `AGENT.AI.<name>`); roles `{about, in, cites, by, member-of, is-a, derived-from}`; `weight ∈ [0,1]`. Vocabularies are seeds, extended on observed need. *(Working Decision.)*
- **C-027** — Allocation splits into **grammar** (universal, fixed: mint-before-use; immutable & never reused; unique-under-parent; label separate; honest-depth+weight; reparent-by-redirect; parentage = code prefix; routes from identity) and **naming style** (spelling/abbreviation = recommended project convention, not a mandated rule). *(Working Decision.)*
- **C-032** — Knowledge Graph Store established at `/Claude/Knowledge Graph Store/` (`nodes/` + `_events/`); FRACTAL hand-usable with zero infrastructure; index deferred to observed need (C-021). *(Working Decision.)*

## Key reasoning carried

- **Fix the grammar, grow the dictionary** — resolves standard-vs-flexible: a small fixed rule-set generates an unbounded, evolving vocabulary; that is why naming style is soft.
- **Agent is a facet, branched by kind** — authorship is the `by` *role*; the facet is the browsable *who*; human/AI is a prefix filter, not a parallel `agent-kind` facet (kind is intrinsic; a separate axis would duplicate and drift).
- **Not license plates** — only the entity-type prefix is a short fixed set; coordinates are variable-length dotted words, and uniqueness is only required under a parent, so the namespace never exhausts.
- **Mint on observed need** — the bootstrap minted only the seven coordinates the first document required; no pre-built taxonomy.

## Assumptions

- Foldering is navigation, not identity (C-022) — the store location is movable without breaking references.
- Genesis self-reference (first `mint` events' `actor` naming a code minted in the same batch) is acceptable under the zero-infra clause; true by end of batch.
- Hand-written store; the `place`/`trace`/`query-by-facet` index is built only when tracing-by-grep gets slow.

## Open questions

- Log **partition interval** (C-023) — chosen later from observed volume.
- Whether `time` placements auto-derive from `created` — carried, non-blocking.
- Whether standing up a live hand-store counts as a "genuine transition" for the Global current-realisation line (C-010).

## Dependencies

- Must stay consistent with `Fractal_Node_and_Event_Schema_v0.1.md` (now Accepted) and the Foundation.
- The deferred Knowledge Path index (step 2) will consume exactly this format and store.
- Connected folder `Desktop/FRACTAL/` is canonical; the Project is a projection.

## Change summary (files written this session)

- **NEW** `Claude/Knowledge Graph Store/` — live store: `_events/2026-08.jsonl`, 8 node files (agent-kind branch + `KG`/`GOV` + the first `DOC`), `README.md`.
- **UPDATED** `Claude/Architecture/Concepts/Knowledge Graph/Fractal_Node_and_Event_Schema_v0.1.md` — status → Accepted; §5 banner, agent branch, grammar-vs-style; §4.5 accepted; §7 C-026/C-027 accepted.
- **NEW** `Claude/Project Governance/Governance Protocol/Fractal_Governance_Protocol_Claude_v0.6.md` — ratifies C-026, C-027, C-032.
- **UPDATED** `Claude/Project Governance/Governance Documents/Fractal_Decision_Register.md` → v0.2 (C-026/C-027 accepted; C-032 added; OQ-2 closed).
- **UPDATED** `Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md` → v0.6.
- **UPDATED** `Claude/Context Packages/Fractal_Context_Index_v0.1.md` → v0.4 (store routed).
- **NEW** `Claude/Context Packages/Conversations/Return_Package_2026-08-12_Facet-Registry.md` — this package.
- **MIRRORED** Decision Register, Local Context, Context Index refreshed to the Claude Project spine; the Register artifact in the desktop sidebar updated.

## Refresh list (not done this session — next)

1. **Max to review** the Draft protocols (v0.3–v0.6) to move statuses from Draft to final.
2. **On observed need (step 2)** — build the Knowledge Path index MCP server (`place`/`trace`/`query-by-facet`) as a derived cache over the store.
3. Begin **placing real FRACTAL content** into the store (existing docs as nodes) as usage warrants.
4. Confirm the log **partition interval** (C-023) from observed volume.
5. Consider whether "store is live" warrants a Global Context current-realisation note (C-010).
6. Author the **bootstrap/rehydrate protocol**; decide ChatGPT-era migration into this format.

## Provenance

FRACTAL Facet-Registry conversation, 2026-08-12 (Claude + Max). Sources in each doc's "Sources" line; decisions ratified in Governance Protocol — Claude Series v0.6.
