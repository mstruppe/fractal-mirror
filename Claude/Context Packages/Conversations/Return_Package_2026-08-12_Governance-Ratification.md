# Conversation Return Package — 2026-08-12 (Governance Ratification — Workstream A)

> State-transfer object, not a transcript. Read this to resume without reloading the conversation.

**Conversation scope:** FRACTAL — Project Governance domain (GOV). The queued opening of the consolidation & hardening phase (scan-derived agenda, workstream A: governance ratification & hygiene). Objective: define the review act, clear the perpetual-Draft backlog, fix the Register legend, establish the cumulative open-question ledger, and stamp the Custom-Instructions projection.

**Parent:** Loose-Ends Scan 2026-08-12 (findings 1.1, 4.3, 7.1, 7.2); Decision Register v0.2; Governance Protocols — Claude Series v0.1–v0.6.

## State at close

**Workstream A is complete.** The review act is defined (C-033: in-conversation acceptance after a walkthrough → ratification entry in the next protocol → status flips). The **first review pass ran in this conversation**: Max ratified Governance Protocols v0.1–v0.6 and Conversation Settings in bulk, with two recorded caveats. Every decision C-001–C-035 is now fully **Ratified** under a legend that is no longer self-contradictory. The Register (v0.3) is the cumulative open-question ledger (C-034, OQ-1–OQ-20) — the lost v0.1/v0.2 §11 items are swept in with dispositions. Conversation Settings is reissued as v0.3 (governed-projection + stamp wording, C-035), and **Max has pasted the stamp line into the Project's Custom Instructions field** — the sync check is now decidable.

## Decisions of record (this session, Governance Protocol v0.7 — ratified in-conversation per C-033)

- **C-033 — The review act.** Act: explicit in-conversation acceptance after a walkthrough. Record: ratification entry in the next Governance Protocol. Effect: `Draft → Ratified (date, per protocol)`. Trigger: pending items presented at the next governance conversation at the latest. Field convention: `Review Owner: Max` until reviewed; `Reviewed By: Max (date, per protocol)` after.
- **Ratification pass (first exercise of C-033).** v0.1–v0.6 + Conversation Settings ratified 2026-08-12. *Caveat 1:* the C-015 ID **scheme** remains a Working Hypothesis (OQ-14, workstream C). *Caveat 2:* v0.6's multi-person safety is a **goal**; the store is **single-writer** until OQ-19 (workstream E).
- **C-034 — Cumulative open-question ledger.** The Register's OQ section is the single ledger; every protocol §11 item enters with a disposition; items leave only by recorded disposition.
- **C-035 — Stamped Custom-Instructions projection.** The field is a governed projection (compression, not verbatim) of Conversation Settings and must open with a version stamp; sync-check = stamp comparison. Conversation Settings → v0.3.

## Key reasoning carried

- **One root defect:** all four workstream-A items traced to the undefined review act; defining it cheaply (lean tie-breaker, C-008 manual-first) made the rest mechanical.
- **Caveats over silence:** ratifying with recorded caveats avoids repeating the scan's claimed-as-achieved pattern.
- **Stamps over adjectives:** projections stay honest by carrying a version stamp, not by asserting "verbatim."

## New thread opened (not yet in the ledger): shipping FRACTAL

Max raised distribution: shipping FRACTAL requires **effortless setup**, so updating the per-client instruction surface must eventually live inside the architecture — ideally via sandbox-style AI packaging (GPTs-like), not new software. Direction sketched (consistent with C-018 substrate-B / C-020 repo-is-FRACTAL): the rules live in the repo (Conversation Settings is the governed source); each vendor surface gets a thin, stamped **adapter projection**. Claude-side tiers: a repo-resident **skill** (most FRACTAL-native; would dissolve OQ-16), a **plugin** (skill + MCP bundle, the true GPTs analog, distributable via marketplaces), and shared **Projects** (current, least portable). Cross-vendor: custom GPTs / Gems = other clients' adapter slots. **Consequence for workstream B:** the bootstrap/rehydrate protocol should include an "install the client adapter" step, and a repo-resident skill is the natural first automation candidate under C-008. → Queued in Local Context v0.8, agenda item H.

## Open questions

- Full ledger now lives in the Register v0.3 (OQ-1–OQ-20, C-034). Touched this session: OQ-1 resolved (review act + pass); OQ-16 gains an interim mechanism (stamp) and a candidate dissolution path (repo-resident skill, see above).

## Dependencies

- Workstream B (next): `git init` + commit convention + bootstrap protocol — now explicitly including the client-adapter step.
- Workstream C consumes Caveat 1 (C-015 confirm-vs-grandfather); workstream E consumes Caveat 2 (single-writer until collision policy).
- Connected folder `Desktop/FRACTAL/` is canonical; the Project is a projection.

## Change summary (files written this session)

- **NEW** `Claude/Project Governance/Governance Protocol/Fractal_Governance_Protocol_Claude_v0.7.md` — C-033–C-035 + the ratification pass (itself Ratified in-conversation).
- **UPDATED** protocols v0.1–v0.6 — `Status: Draft` → `Ratified (2026-08-12, per v0.7)`; `Reviewed By: Max` → dated.
- **UPDATED** `Claude/Project Governance/Governance Documents/Fractal_Conversation_Settings_v0.1.md` → **v0.3** (governed-projection + stamp, §3/§5/§6; ratified).
- **UPDATED** `Claude/Project Governance/Governance Documents/Fractal_Decision_Register.md` → **v0.3** (legend fixed; all statuses flipped; cumulative OQ ledger OQ-1–OQ-20; C-033–C-035; status = Living projection).
- **UPDATED** `Claude/Context Packages/Local/Fractal_Local_Context_Knowledge_Graph.md` → v0.8 (A closed; B queued; H extended with shipping/adapter thread).
- **NEW** `Claude/Project Governance/Governance Documents/Fractal_Rule_Overview.md` — one-page rule-book projection (five layers, all rules traced to C-numbers); mirrored to the Project. Created after the initial close, at Max's request.
- **NEW** `Claude/Context Packages/Conversations/Return_Package_2026-08-12_Governance-Ratification.md` — this package.
- **MIRRORED** Decision Register + Local Context refreshed to the Claude Project spine.
- **MAX (done):** stamp line pasted into the Project Custom Instructions field (C-035).

## Refresh list (not done this session — next)

1. **Workstream B** (queued next): `git init` the FRACTAL repo (C-018/019/020, C-025 commit binding); define the commit convention; author or trigger-define the bootstrap/rehydrate protocol **including the client-adapter step**.
2. Workstreams C–F per the scan agenda (Local Context v0.8 carries the full list).
3. Consider the repo-resident FRACTAL skill as the first automation candidate (C-008 boundary; dissolves OQ-16) — design conversation when Max takes it up.
4. OQ-3 (partition interval) and OQ-4 (genuine transition) remain by Max's call.
5. One-line protocol entry in the next GOV conversation: record the Rule Overview's creation and decide whether it joins the context package (cf. C-030).

## Provenance

FRACTAL Governance-Ratification conversation, 2026-08-12 (Claude + Max). Decisions recorded and ratified in Governance Protocol — Claude Series v0.7; ledger state in Decision Register v0.3.
