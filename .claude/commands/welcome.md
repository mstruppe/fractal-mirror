---
description: First contact — what FRACTAL is, where you are standing, and the two paths out
---
Welcome a newcomer to FRACTAL. This is the scripted first contact (fieldnotes entry 6: the opening of the first session is part of the product). Follow these steps in order:

1. **Determine where this session is standing** (one command: `git status` + `git describe --tags --always`, read-only):
   - **A distribution clone** (detached HEAD, a release tag, or any copy that is not the governing working repo) → you are a **reference surface** (Settings rule 9, C-091): you may read, explain, and assist a birth — you never close, never edit canon, never push. Say so in one friendly sentence, not as a wall of rules.
   - **The governing repository itself** (a working branch with its own live history) → say so, and point at `/fractal` for a working session instead. The rest of this command still works as a tour.
2. **Explain FRACTAL in one short paragraph, for a user, not an evaluator:** an operating system for structured knowledge — your project gets a memory that survives every session: decisions recorded with their reasoning, work handed over so any future session picks up cold, all of it plain text in git that you own. The AI works inside rules you can read; nothing is hidden in chat history.
3. **Offer exactly two paths** and follow the user's pick:
   - **"Start my own project"** → run the **onboarding interview**: say *begin* (or `/begin`) and follow `Fractal_Onboarding_Protocol.md` (Governance Documents) — five real questions, the birth via `genesis.py` (dry-run first, always), the handoff into their own repo. The product is a **new repository** — their instance, their rules, their empty ledger. Onboarding ends at their first close, not at birth; the guidance fades by design.
   - **"Show me around"** → orient them from `README.md` and `Claude/Context Packages/Global/Fractal_Global_Context.md`, and answer from the corpus (cite what you read; load only what the question needs).
4. **Answer the questions first users actually ask, briefly and only if asked:** what the clone contains vs. what an instance inherits (GENESIS §0 — the whole corpus ships, only the rules are inherited; the rest is citable literature) · which version to use (GENESIS §7 — latest tag for births, own repo for own work) · what minting means (repo = library shelf, store = catalog; minting = the catalog card — defer penalty-free until something in the graph must point at the document) · the two permission layers (the constitution's ask-before-execute vs. the client's own tool gates — independent by design).

Never scan the repo to orient (rule 1); never run the mother's rituals from a copy (rule 9).

---
*Stamped-procedure projection (C-035 class, per Protocol v0.38 — the phase-5 ingestion, fieldnotes entry 6): scripts the first-contact moment the shipping run found unscripted. Sources: Conversation Settings v0.8 rules 9–10 (C-091/C-092) + GENESIS.md §0/§2/§7 + README.md quickstart + Fractal_Onboarding_Protocol v0.1 (the start-my-own-project path). Re-stamped 2026-08-16 (the flip-preparation session — path A routes through the interview). Refresh triggers: a Settings reissue touching rules 9–10, a GENESIS or Onboarding Protocol reissue moving the referenced sections, or a C-059 walk finding this stamp stale.*
