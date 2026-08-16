# Conversation Return Package — 2026-08-07 (Node & Event Schema)

> State-transfer object, not a transcript. Read this to resume without reloading the conversation.

**Conversation scope:** FRACTAL — Knowledge Graph domain (KG). Step 1 of the build sequence (C-021): spec the plain-text on-disk **format** — node front-matter, the append-only event-log line format, and the facet-code allocation rules — so FRACTAL is hand-usable at zero infrastructure (placing and tracing done by reading the folder). No code, no index, no UI.

**Parent:** Fractal Knowledge Path Foundation v0.1 · **Objective:** turn the Foundation's two-relation core into a concrete, writable format + a copy-paste template.

## State at close

Two canonical documents exist under `/Claude/Architecture/Concepts/Knowledge Graph/`: `Fractal_Node_and_Event_Schema_v0.1.md` (the spec) and `Fractal_Node_Template_v0.1.md` (templates + the nuclear-paper worked example). Both are Draft (Proposal). The format was verified internally against the Foundation (identity/context separation, one append-only log, log-canonical fold, independent facets, routes-derive-from-identity, portability) and the nuclear-paper example traces end-to-end including reclassification-by-supersede. Nothing accepted yet beyond authoring — decisions below are proposed for Max's confirmation.

## Decisions of record (proposed this session)

- **C-022** Node file = UTF-8 Markdown + YAML front-matter; required identity `{id, type, created, created_by}`; optional `{content_hash, version_of, title, aliases, code, placements}`. Filename `<id>[--slug].md`; physical foldering is navigation, not identity.
- **C-023** Event log = append-only JSONL, one event/line, monthly partitions `_events/YYYY-MM.jsonl`; verbs `{create, place, unplace, mint, alias, revise, run}`; events are addressable (`EVT-ULID`).
- **C-024** *(load-bearing — needs explicit accept)* Canonical-source rule: the **event log is authoritative**; node `placements:` is a **materialized fold** of the log. Alternative (front-matter-primary, log-as-journal) recorded but rejected as default.
- **C-025** Supersede semantics: no edit/delete; correction is a new event with `supersedes`; current state = fold in `ts` order.
- **C-026** Facet registry (v0.1) `{topic, method, source-type, time, agent}` with reserved roots; role vocabulary `{about, in, cites, by, member-of, is-a, derived-from}`; weight ∈ [0,1] distinguishes central vs tagged.
- **C-027** Facet-code allocation: mint-before-use, immutable & never reused, unique under parent, label separate, honest-depth+weight, reparent-by-redirect, routes derive from identity. Concept **parentage is the code prefix** (no separate edge); a `TOP` node stores its own `code`.

## Assumptions

- ULID-based `TYPE-ULID` identity (Foundation §4) stands; hand-written ULIDs are illustrative until a generator exists.
- Monthly log partitioning is an acceptable realisation of "one log" (git-merge friendliness); global order is by `ts`.
- Lazy mint (place first, mint the concept shortly after) is tolerable at pure zero-infra.

## Open questions

- **Confirm C-024** (log-canonical vs front-matter-primary) — this shapes every future write and the index.
- Confirm the seeded **role** and **facet** vocabularies (extend only on observed need).
- `mint` collision policy across concurrent git branches beyond "unique under parent, merge surfaces clashes"; whether `time` placements auto-derive from `created`.

## Dependencies

- Derives from and must stay consistent with `Fractal_Knowledge_Path_Foundation_v0.1.md` (two relations, one log; §§3–5).
- The deferred Knowledge Path index (step 2) will consume exactly this format; the Galaxy UI (step 3) reads the same fold.
- Connected folder `Desktop/FRACTAL/` is the canonical store; the Project is a projection.

## Provenance

FRACTAL Node & Event Schema design conversation, 2026-08-07 (Claude). Sources in each doc's "Sources" line.

## Change summary (files written this session)

- **NEW** `Claude/Architecture/Concepts/Knowledge Graph/Fractal_Node_and_Event_Schema_v0.1.md` — the format spec.
- **NEW** `Claude/Architecture/Concepts/Knowledge Graph/Fractal_Node_Template_v0.1.md` — templates + worked example.
- **UPDATED** `Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md` → v0.4 (step 1 done; step 2 now the NOW-on-need).
- **NEW** `Claude/Context Packages/Conversations/Return_Package_2026-08-07_Node-and-Event-Schema.md` — this package.
- **MIRRORED** refreshed Local Context to the Claude Project spine.

## Refresh list (not done this session — next conversation)

1. **Max to accept/decide C-022–C-027**, especially **C-024** (canonical-source rule).
2. Bump **Context Index** KG row to also point at the Node & Event Schema as canonical format.
3. **DEFERRED (step 2, on observed need)** — build the Knowledge Path index MCP server (`place` / `trace` / `query-by-facet`) as a derived cache over exactly this format.
4. Author the **bootstrap/rehydrate protocol**; decide **ChatGPT-era migration** into this format.
5. Reconcile **Galaxy/Operator** into Architecture State (ONT, Parts IV–V).
6. Promote confirmed decisions (C-013–C-020, C-021, C-022–C-027) into a **Governance Protocol** entry.
