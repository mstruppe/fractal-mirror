# Fractal Client Library

> **CANONICAL — the kernel's catalog of vendor surfaces (C-097).** One entry per client an instance can be worked from: what that client reads, how it behaves, and the adapter template it gets. Set up once, instantiated per instance. Living document: stable filename, version tracked below. **What this library is not:** a second conduct source — every instantiated adapter remains a **C-035 projection of its instance's own Conversation Settings** (C-065), stamped and machine-checked; this library supplies the *skeleton and the client knowledge*, never the rules. **And no runtime API, by doctrine:** an instance calls nothing upstream (the constitution model — updates are offers); this library stays current through the **C-094 field-test loop** — a client changes under real use → `/fieldnote` → ingestion → this file revises. A refresh may *consult* vendor docs as a session act; nothing depends on them at runtime.

**Version:** 0.2 · **Status:** Ratified (2026-08-16, per Protocol v0.42 — C-097; v0.2 field refresh same day, the C-094 loop's first library exercise) · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Conversation Settings (the source all templates project) · **Document ID:** DOC-01M052MNTZCKNK2XTRAD2GT8CN (minted 2026-08-16 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · The universal layer (holds for every client)

- **The word is the command; the slash is one client's shortcut to it.** The kernel's session vocabulary — *orient · close · fieldnote* (and the mother-side *look*) — works as plain words on any surface whose adapter names it. A client's menu mechanism (slash commands, custom prompts) is optional dressing per entry below. (Doctrine forged at fieldnotes entries 32/36; user-readable in the Command Index.)
- **Every entry provides three things:** the **discovery convention** (which file the client auto-reads — the socket, entry 17), the **session-capable adapter template** (orientation rule · source-of-truth · load-only-what-the-task-needs · ask-before-executing · close-the-loop · identity/numbering · the command vocabulary), and the **client mechanics** a user needs (menus, settings, continuation).
- **Adapters are never hand-forked from each other.** Two adapters on one instance (e.g. `CLAUDE.md` + `AGENTS.md`) compress the same Settings; the version stamp in each is the sync check (C-035/C-077).
- **Drone-scoped vs session-capable is a scope choice, not a client property.** The same client can hold both (FRACTAL's own `AGENTS.md` is drone-scoped by C-066; KNet's is session-capable by its owner's choice). An entry's template is session-capable; drone scoping is a deliberate restriction applied per instance.

## 2 · Client: Claude Code (Anthropic) — the reference client

- **Discovery:** auto-reads `CLAUDE.md` at the repo root; auto-discovers `.claude/commands/*.md` into its `/` menu (each file one command; frontmatter `description`; `$ARGUMENTS` for steerable targets).
- **Template:** the live reference implementation is this repo's own `CLAUDE.md` (C-065, `Fractal_Claude_Code_Adapter`) and the child form is written by `genesis.py` at §3.6 with a live-read stamp — **point, don't duplicate** (C-003). Command tier: the Command Index holds the roster; a child starts with `/orient` (tier 0).
- **Mechanics (the entry-7/20 material):** `/model` picker · `/fast` toggle · `claude --continue` / `--resume` · `/help` for the rest; permission layer 2 lives in `/permissions` and the client's own settings file — independent of the constitutional layer (C-008), loosening one never loosens the other.
- **Status:** proven — thirteen governed sessions in the mother, tier-0 closes in the child.

## 3 · Client: OpenAI Codex / ChatGPT desktop

- **The mode seam is dissolved (field-observed 2026-08-16, entry 42 — Max's directive to record it here):** the ChatGPT desktop app carries the agentic (Codex-class) capability *inside the general assistant* — no distinct product boundary is felt in use, and **a full governed loop (orient → work → close) ran from the general app**. Treat "ChatGPT" and "Codex" as **one surface with blended modes**, not two clients. Contrast of record: Anthropic's split stayed hard — Cowork was write-capable (C-072) but never ran a full loop; closes lived on the Code surface (C-089). Strategic corollary: OpenAI has already merged the two-route distribution (CLI + desktop app) that FRACTAL's vision holds as future work — a live datum for the vehicle decision (Workspace Foundation §6).
- **Discovery:** auto-reads `AGENTS.md` (native convention — the ecosystem's emerging vendor-neutral standard, entry 17); does **not** read `.claude/commands/` (entry 36 — the `/` menu stays empty). Optional client-side triggers: Codex's own custom-prompt mechanism can mirror the vocabulary (a per-user act; ask the client session directly what it supports).
- **Template: HARVEST-PENDING (the recorded trigger).** The first session-capable Codex adapter is being field-forged **now** — KNet's first ChatGPT session authors its `AGENTS.md` under the second-client advisory, ratified by the owner. **On ratification, that adapter is harvested upstream into this entry as the template** (the C-094 generator-side move: the field forges, the kernel generalizes). Until then the advisory's §2 brief is the authoritative skeleton: projection of the instance's Settings · no new rules · session-capable (orient, work, close) · **a command-vocabulary section** (the words *orient / close / fieldnote* are commands on this surface — the entry-36 universality fix, born word-universal).
- **Mechanics (as field-observed, entries 30–36):** oriented a governed instance cleanly with zero kernel changes (entry 33); no slash menu from repo files; friction reports flow through the owner (`/fieldnote knet …` on the mother side).
- **Status:** trial in execution — orientation green; **a full governed loop executed from the general app** (entry 42); adapter pending ratification; this entry completes at harvest.

## 4 · Adding a client (the recipe)

1. **Field-forge, never author from theory:** hold a real session on the new surface (an advisory as bootstrap, the KNet pattern); its adapter is drafted there and ratified by the instance's owner.
2. **Harvest:** the ratified adapter generalizes into an entry here — discovery convention, template, mechanics, vocabulary triggers.
3. **Generator:** when demand exists for births onto that client, `genesis.py` gains the client as a parameter and writes the adapter from this entry (GENESIS §3.6 extended — armed, not built; C-021).
4. The **GENESIS §5 shelf row** for this library lands at GENESIS's next reissue (batched, the v0.5 precedent) — recorded here so it is not forgotten.

---

**Refresh triggers:** a client's observed behavior changes under real use (via the C-094 loop); a child ratifies an adapter for a client not yet entered (harvest); the `AGENTS.md` ecosystem convergence completing (entries may merge); a third client arriving.
**Sources:** Conversation Settings v0.8 (the projected source); CLAUDE.md v0.8 + AGENTS.md v0.8 (live adapters, C-065); GENESIS v0.5 §3.6; the Command Index (stamp inside); Site/Fieldnotes_2026-08-15_First-Shipping-Run.md entries 16–17, 30–36 (the multi-client bundle); Site/Upstream_Advisory_2026-08-16_KNet-Second-Client-Trial.md.
**Revision history:** v0.1 (2026-08-16) first issue (C-097, per Protocol v0.42) — the entry-16/17/32/36 bundle resolved into a kernel catalog: the universal word-vocabulary layer stated, Claude Code entered as the proven reference client, Codex/ChatGPT entered with mechanics observed and the template harvest-pending on KNet's ratified adapter; no-runtime-API doctrine recorded; the genesis client parameter armed on need. · v0.2 (2026-08-16) **first field refresh (the C-094 loop working as the currency mechanism, entry 42, Max's directive):** §3 gains the dissolved-mode-seam observation — ChatGPT/Codex are one surface with blended modes; a full governed loop ran from the general app (a first across both vendors here); the two-route-merger corollary recorded for the vehicle decision.
