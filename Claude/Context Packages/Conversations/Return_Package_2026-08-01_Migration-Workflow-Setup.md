# Conversation Return Package — 2026-08-01 (rev. 3, final)

> State-transfer object, not a transcript. Read this to resume without reloading the conversation.

**Conversation scope:** FRACTAL — Claude migration, Context Persistence Workflow, and context-model refinement.

**Objective:** Bring Claude up to date, stand up the cross-conversation persistence workflow, and leave the context scaffolding in its refined final shape ready for Knowledge Graph work.

## Completed

- Reviewed the FRACTAL corpus and agreed the persistence workflow (hybrid anchoring, design-before-automate, lean default, `.md`, folder split, ask-before-execute).
- Built the `/Claude/` section and stood up the workflow end-to-end (Governance Protocol v0.1, Global Context, Context Index, Conversation Settings, Return Package).
- **Custom Instructions field confirmed saved** by Max — per-conversation injection is live.
- Refined the context model: **Global (stable: vision + current realisation) vs Local (dynamic: aspect of realisation)**; created the first Local Context; adopted living-document naming; protocolled it as Governance Protocol v0.2.

## Current document set (all `.md`, under `/Claude/`)

- `Context Packages/Global/Fractal_Global_Context_v0.1.md` — **v0.2 internal**: vision + current realisation. Stable filename. Mirrored to Project.
- `Context Packages/Fractal_Context_Index_v0.1.md` — **v0.2 internal**: routing + Active Local Context + naming convention. Mirrored to Project.
- `Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md` — **the load target for the next conversation.**
- `Project Governance/Governance Documents/Fractal_Conversation_Settings_v0.1.md` — conversation rules (pending terminology refresh, see open items).
- `Project Governance/Governance Protocol/Fractal_Governance_Protocol_Claude_v0.1.md` and `…_v0.2.md` — history layer.
- `Context Packages/Conversations/Return_Package_2026-08-01…md` — this package (folder-only).

## Decisions of record

C-001–C-008 (workflow, anchoring, projection integrity, update ordering, stable identity, format, folder split, manual-first automation) · C-009 Global/Local spine · C-010 realisation phasing · C-011 Local opening convention · C-012 living-document naming.

## Carry-forward — the Knowledge Graph conversation

- **Load `Fractal_Local_Context_Knowledge_Graph.md`** (plus Global Context, already in the Project). It states the framing: relate — don't conflate — the semantic identity system (Concept/Document/Version/Relationship IDs) and the retrieval/routing codes; decide whether routing codes derive from identity.
- **Undecided, to design there:** clean-slate new foundation from old material vs. retrofit the graph into old docs; the `/ChatGPT/` archive move depends on this.
- Approach as a **blank page**: most future-proof, simplest feasible code/identity architecture.

## Open governance items

- Conversation Settings to adopt Global/Local terminology and state C-012 normatively (deferred).
- Whether the active Local Context is fed by the prior Return Package (self-updating).
- Whether grandfathered `_v0.1` orientation filenames are eventually normalised.

**Provenance:** FRACTAL migration & context-model conversation, 2026-08-01. Sources in Fractal Global Context.
