# Fractal Governance Protocol — Claude Series v0.22

**Topic:** The multi-agent environment (C-066): a **drone tier** is installed beside the governing surface — OpenAI Codex as the first drone-class writer. Identity `AGENT.AI.CODEX` minted; adapter `AGENTS.md` landed canonical (C-065 class); doctrine fixed: drones execute bounded briefs on `drone/*` branches, never `main`, never governance acts; the two checkers are the model-agnostic acceptance gate. The C-057 signing trigger is formally **armed** — it executes at the drone's first actual write (pending on Max: key custody + host install).
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.21

---

## 1. Context

Same conversation as v0.20/v0.21. Max asked whether ChatGPT/Codex and Claude could work together — Codex as "a drone or co-pilot sent to do specific tasks" — motivated by parallel capacity. The architecture had been waiting for exactly this: C-049/C-050 multi-writer safety, C-057's first-second-writer signing trigger, C-037's one-identity-system attribution, the C-065 adapter class, and OQ-27's standing question about safety once other writers exist. The install was Claude-executable end-to-end except the Codex CLI itself (Max's OpenAI account; `codex` not present on the host at record time) and the C-057 key ceremony (Max's custody).

## 2. Questions investigated

1. Is a second AI writer safe here? *(→ The safety was pre-built: first-mint-wins + `verify.py` (C-049/C-050), append-only log, no-history-rewriting (C-037), and now branch isolation — the drone never touches `main` or the governance layer.)*
2. What is the acceptance test for drone work? *(→ The machine gate: both checkers green on the drone branch before the governing surface merges. Model-agnostic by design — trust the gate, not the model (C-060 philosophy extended from scripts to agents).)*
3. What is the honest capacity claim? *(→ Not "double tokens" of one brain: separate quota pools, parallelism on bounded tasks, and model diversity in review — bought with specification and review overhead, so drones fit mechanically verifiable work best.)*
4. When does signing (C-057) arm? *(→ Now, formally; it executes at the drone's first actual write — the first commit not under Max's and Claude's shared custody. Pending on Max: SSH-key signing config + optional GitHub branch protection for `main`.)*

## 3. Decision of record

- **C-066 — The drone doctrine (multi-agent environment installed; Codex first).** (a) **Class:** drones are bounded-task executors under the governing surface (Claude Code + Max) — never governance actors: no mints, no canonical/living-document edits, no protocols, no register entries (C-008 holds at the top). (b) **Isolation:** drones write only on `drone/<task>` branches — never `main`, never a merge; the governing surface reviews and merges after **both checkers green on the branch** (the machine gate is the acceptance test). (c) **Identity:** `AGENT.AI.CODEX` minted under `AGENT.AI` (first non-Claude AI writer; C-037 attribution extends — author `Codex <codex@fractal.local>`). (d) **Adapter:** `AGENTS.md` at the repo root (Codex's auto-read convention), canonical per the C-065 class — `Fractal_Codex_Adapter` v0.1, DOC-minted, STRICT-scanned; content a drone-scoped C-035 compression of Settings v0.4. (e) **Protection:** the C-057 signing trigger is armed and executes at the drone's first write; GitHub-side `main` protection recorded as Max's optional hardening. (f) **Rationale of record:** parallel capacity on separate quota pools plus model diversity in verification. **OQ-27 gains its first concrete doctrine and stays open** for the full safety story (key custody, drone provenance, revocation). *(Working Decision.)*

## 4. Executed this close (one `[GOV]` commit, C-037; push = Claude, C-064)

- **Store** — `AGENT.AI.CODEX` minted via `mint.py` (C-050 guard); the adapter DOC and this protocol DOC minted (create + route alias + `topic:GOV` + `agent` each); five `revise` events (Register, Rule Overview, Index, BOOTSTRAP, and an Architecture State sources cure riding the ripple); **66 nodes / 292 events**; both checkers green before commit.
- **`AGENTS.md` v0.1 (new, canonical)** — drone rules: brief-only scope with an explicit forbidden-paths list, minimal orientation, `drone/*` branches only, C-037 attribution, the checker gate, hand-back discipline.
- **`check_versions.py`** — scope + STRICT + LIVING gain the Codex adapter (three client-adapter stamps now machine-relevant: two scanned, one vendor-held).
- **Decision Register → v0.20** — C-066 entered; OQ-27 annotated (first doctrine); Sources and revision history.
- **Rule Overview → v0.18** — multi-agent/drone row added; ledger caveat → Register v0.20.
- **Context Index → v0.15** — `AGENTS.md` row in the canonical-documents table; series range → v0.22.
- **BOOTSTRAP → v0.10** — §2 gains the drone-tier entry (Codex adapter, branch rule, armed signing trigger).
- **Local Context → v0.28** — doctrine recorded; checklist walked; board republished (stamp → v0.28); Return Package third postscript.

## 5. Calls recorded (Max, 2026-08-14, this conversation)

1. **The environment:** build it — Codex as a drone/co-pilot for specific tasks ("get started"), motivated by parallel capacity; Claude proposed the doctrine shape (orchestrator/drone, branch isolation, machine gate) and Max's go covered it.
2. **Pending on Max, recorded:** install + authenticate the Codex CLI (his OpenAI account; absent from the host at record time); execute the C-057 key ceremony at or before the drone's first write; optional GitHub branch protection on `main`.

## 6. Ratification record (2026-08-14, in-conversation per C-033)

Max asked whether the two vendors could work together, received the feasibility assessment naming exactly this install as a decide-and-execute session, and said "get started." Claude executed everything Claude-executable — identity, adapter, doctrine, scan scope, ledgers — committed as attributed author (C-037) and pushed per C-064. The first drone flight awaits Max's CLI install. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None opened. **OQ-27 annotated** — first concrete doctrine (C-066); remains open for key custody, drone provenance, and revocation once flights are real. Standing items carry: OQ-4, OQ-6, OQ-9, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. The review ledger stays fully green.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.22 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.22 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.21 |
| Related Documents | AGENTS.md v0.1 (`Fractal_Codex_Adapter`); CLAUDE.md v0.1; Conversation Settings v0.4 (normative source); Decision Register v0.20; Rule Overview v0.18; Context Index v0.15; BOOTSTRAP.md v0.10; Local Context v0.28; Return_Package_2026-08-14_First-Code-Session.md (postscripts) |
| Document ID | DOC-01M00CA1DGGWHC3ENW1FR2P3TX (minted 2026-08-14, C-041, per this protocol) |
