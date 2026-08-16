# Fractal Governance Protocol — Claude Series v0.31

**Topic:** **Arc 1 completed.** The genesis tool reviewed, gated and merged; the flight branch retired (C-075). Then the two things arc 1 was actually for: **an instance was birthed and a session was closed inside it — twice**, the second run a control proving the first run's findings cured at the source. Three decisions of record: **C-081** — `verify.py` alone is the genesis gate, with the kernel's inherited biography *measured* (9 registry errors + **67 upstream citations**) and deliberately left unresolved; **C-082** — a drone flight runs in a full clone, never a linked worktree, after that isolation choice made flight 3's commit duty impossible; **C-083** — **OQ-16 resolved by retiring an artifact rather than building one**: the packaging unit is the adapter plus its commands, and the queued `SKILL.md` is retired unbuilt because it would reopen the drift class C-067 closed. Node Template → v0.5 (pointer currency), C-040's coupling amended to check pointers as well as content, S3-2.2 held open deliberately on Max's call.
**Status:** Ratified (2026-08-15 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-15 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.30

---

## 1. Context

Sixth Claude Code session, opened by `/fractal` on the v0.30 handover, whose *Next* named the first act precisely: **review `drone/genesis-tool` — read the hand-back, run the gate yourself inside a birthed instance, merge or send back, delete the branch per C-075.** Max's opening restated it and added two standing watch-items:

> *"S3-2.2 sits on two kernel specs, so it closes for free if the arc reissues either and otherwise should be left open deliberately; and OQ-28, the weight dial, remains the honest counterweight to this whole program — a kernel too heavy to instantiate fails the vision more quietly than one missing features."*

Both were honoured, and both changed shape under evidence — the first resolved *against* the free close, the second acquiring its first two numbers.

**The session opened on a false premise, and catching it was the first act's real content.** The handover recorded the flight as launched, which was true; it did not record that the drone was *still flying*. `drone/genesis-tool` carried **zero commits**, no `HANDBACK.md`, and only a brief and a log — while the process was alive and its log growing 75 KB in 20 seconds. Reviewing it then would have been reviewing an empty branch. The drone landed at 10:43, mid-conversation, having spent its first ~3,600 log lines reading before writing a line of code — itself an OQ-28 datum (see §3).

## 2. Evidence of record

**The hand-back was honest, and both of its failures were the governing surface's, not the drone's.**

1. **The commit was impossible by construction (→ C-082).** Flight 3 was launched in a *linked git worktree* so it could not collide with the concurrent close. A linked worktree's index lives in the **parent** repository at `.git/worktrees/<name>/`, outside the drone's sandbox (`workdir`, `/tmp`, `$TMPDIR`). The drone reported it verbatim: `fatal: Unable to create '.../index.lock': Operation not permitted`. The isolation choice and `AGENTS.md` rule 4 were mutually exclusive; the drone could not have complied. Confirmed by contrast — the same `git add` succeeded immediately from an unsandboxed shell.

2. **The acceptance test was mis-specified by the governing surface (→ C-081).** The brief demanded `check_versions.py` PASS inside the birthed instance. Reproduced independently: **76 errors**, and the taxonomy is the finding. Only **9** are the registry hard-coding FRACTAL's living-document names — the drone's own diagnosis, correct but 12% of the story. The other **67** are *inherited kernel documents citing FRACTAL's own history*: the Rule Overview names Protocols v0.1–v0.30, the Schema names its superseded versions, the Settings name the protocols that ratified them. Marking the inherited kernel *frozen* does not help — the checker's rule B is deliberately strict (*nothing may cite a phantom, frozen sources included*). And `GENESIS.md` §6 **already said `verify.py`**: the brief contradicted the document it was automating.

**The tool itself is sound**, verified by the governing surface in an instance birthed *independently* of the drone's own acceptance run: `verify.py` PASS (21 events / 13 entities, 0 warnings); dry-run writes nothing; re-run into an existing target, malformed routes and root collisions all REFUSE with legible reasons; all seven tier-0 copies byte-identical; instance history reaches its own initial commit; no source paths leak; no generated spine filename carries a version token (C-080 holding on the first instance ever built).

**A prediction confirmed by machine.** Before the drone landed, a dig into S3-2.2 found `Fractal_Node_Template_v0.4.md` pointing at Schema **v0.5** in three places while the Schema stood at v0.6 — invisible in FRACTAL, where v0.5 exists as history. The birthed instance, whose tier-0 set holds only v0.6, returned it as a hard error: `cites schema v0.5 — no such version exists`. *Stale here, dangling there* — the C-080 lesson in a second file, and the argument that carried the Template to v0.5.

## 3. Decisions of record

| ID | One-line |
|---|---|
| **C-081** | `verify.py` alone is the genesis gate; `check_versions.py` is tier-1 and must never be demanded of a newborn. The kernel's inherited biography is **measured** (9 / 67) and **deliberately unresolved** — both real dispositions (an `INHERITED` source class; stripping revision histories on copy) write machinery ahead of observed need, against C-079's grain. |
| **C-082** | A drone flight runs in a **full clone**, never a linked worktree, whenever the brief requires a commit. Corollary: a flight's hand-back must be *verified*, never assumed — this is the **second consecutive flight** whose launch had a defect only inspection caught. |
| **C-083** | **OQ-16 resolved.** The packaging unit is the **adapter + `.claude/commands/`**; `genesis.py` writes both at §3.6. The queued `SKILL.md` is **retired unbuilt**. The vendor-held half of OQ-16 stays open behind OQ-9. |

**OQ-28 gained its first two measurements.** The tier-0 kernel is **~167 KB / ~23,100 words**, of which **~20,000 are mandatory prose** — roughly 100 minutes of reading, ~30k tokens of context, before a newcomer writes a line. Observed the same day on a live agent: the drone read for ~3,600 log lines before producing code, so the dial measures *cost to act inside*, not only cost to read. The second number is C-081's 67. Neither is a verdict — arc 2 supplies that — but the row now has baselines instead of an intuition.

## 4. Arc 1's remaining deliverables, executed

**4a · The flight merged and retired.** `genesis.py` landed on `main` as a linear commit authored `Codex <codex@fractal.local>`, committed mechanically (C-074), signature verifying `G` — matching the flight-1 and flight-2 precedent of a Codex commit followed by a governance record. Branch deleted **local and remote**; worktree removed; the brief, hand-back and 1.2 MB transcript preserved as the flight record. **C-075 lifecycle complete.**

**4b · The acceptance test — run twice, the second as a control.** GENESIS §0 names it: *a competent stranger can birth a working instance and close their first session in it.* It had never been run.

*Lyra* (first instance) closed green — spine written, `P-001` recorded, handover issued, `verify.py` PASS. **The loop survives instantiation.** `P-001` is the load-bearing specimen: it *binds* the inherited tier-0 rule (C-079) rather than re-deriving it, citing FRACTAL's constitution without copying a row, with `P-` and `C-` never colliding — the inheritance-clause pattern working exactly as GENESIS predicted.

Lyra also reported three gaps between the tool and the document it automates: **no `Conversations/` home** (though §3.8 requires a handover at every close), **no client adapter** (though §1 lists one and §3.6 is a step — `genesis.py` implemented §3.1–§3.5 and §3.7 and stopped, its own Register template hedging *"client adapter (when installed)"*), and a **genesis commit authored by a dotted code** rather than a writer (C-037).

*Nova* (second instance, born after the fixes) closed green **creating no scaffolding by hand** — all three cured at the source, verified at birth. Fixing the generator and testing on a *fresh* instance, rather than patching Lyra, is what makes this a control.

**4c · C-083 — the packaging unit, resolved by subtraction.** The third finding was not a bug: the tool correctly declined to install a unit nobody had decided. BOOTSTRAP §2.2 had queued a `SKILL.md` *"carrying the conversation rules and orientation as one installable unit."* Building it would place a **second** compressed projection of Conversation Settings beside `CLAUDE.md` on the same surface — two projections of one normative source, drifting independently. That is the class **C-067** retired (the Project-spine mirrors, *"the last un-mechanizable refresh duty"*), and C-065's header already forbids it. Meanwhile the tier had *landed slice by slice* — `/fractal`, `close.py`, `/close` — without being named done.

`genesis.py` now writes a parameterized adapter and a tier-0 `/orient` command. **Tiering falls out of C-079 rather than needing a new rule:** `/orient` needs nothing but the repo; `/close` drives `close.py` and so ships only where that tier-1 tool does.

**One implementation detail is the session's quiet lesson.** The adapter's stamp is **read live from the Conversation Settings file at birth**, never hardcoded — a frozen stamp in the generator would have gone stale exactly as the Template's spec pointer did, the same defect cured three hours earlier in a different place. The refusal-first design proved itself here too: the first attempt at that read used a wrong pattern, and the tool **refused** (`REFUSED: could not read a version stamp`) rather than shipping an unstamped adapter.

**4d · Currency cures.** Node Template → **v0.5** (companion/parent/Sources → Schema v0.6), with `genesis.py`'s KERNEL tuple updated in the same pass — the version coupling firing on its first opportunity, as its own commit message predicted. **C-040's coupling amended:** the Schema→Template walk checks **pointers, not only content** — Protocol v0.24's *"Template v0.4 coupling checked — unchanged"* was right about content and silent about pointers. And `Fractal_Conversation_Settings.md` still described its own filename as *"grandfathered, C-012"* — a leftover C-080's 13-file sweep missed, in a **kernel** document that ships to every instance; cured as C-080 execution remainder, no rule change.

## 5. Calls recorded (Max, 2026-08-15, this conversation)

| Call | Verbatim | Executed as |
|---|---|---|
| The session's frame | *"read the hand-back, run the gate yourself inside a birthed instance rather than trusting the branch being green here"* | The gate re-run independently; the empty branch caught before review |
| The four items | *"go"* | Merge + C-075; the gate correction; C-082; the Template pass |
| Kernel biography | *"Defer — ratify GENESIS §5"* | **C-081** — measured, recorded, unresolved by choice |
| Spec currency | *"Template pointer only; S3-2.2 stays open"* | Template → v0.5; **S3-2.2 held open deliberately**, grounds recorded |
| OQ-16 | *"Adapter + commands; no SKILL.md"* | **C-083** |
| The remainder | *"fix all three, start with OQ-16"* | §4c then §4b's control run |

**S3-2.2, held open deliberately (not by drift).** Two grounds recorded: `Reviewed By: Max` asserts that Max reviewed the document — it cannot be supplied by the author on his behalf, which is *why* the row exists; and reissuing two kernel specs for a header field adds ceremony exactly where C-081's measurement says weight is the live risk. Trigger unchanged, with a likely occasion now named: arc 2's instantiation.

## 6. Ratification record (2026-08-15, in-conversation per C-033)

C-081, C-082 and C-083 ratified in the conversation that produced them; each traces to an explicit call in §5. No decision was taken on Max's behalf. Register → v0.32; both checkers green before commit; push per C-064.

## 11. Open Questions (TBD)

**Resolved here:** OQ-16's packaging half (C-083). **Newly measured, still open:** OQ-28 (two baselines, verdict deferred to arc 2). **Open, unchanged:** OQ-4 (fires and should resolve at arc 2) · OQ-9 (now carries OQ-16's vendor-held remainder) · OQ-17 · OQ-18 · OQ-20 · OQ-23 · OQ-27 · OQ-29 · OQ-30 · OQ-31. **Review ledger:** one open finding — S3-2.2, held open deliberately. **The inherited-biography question** (an `INHERITED` source class vs stripping revision histories on copy) is recorded in C-081 and GENESIS §5 without an OQ number, deliberately: it is arc 2's to raise when an instance's corpus wants the tool.

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.31 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.31 |
| Status | Ratified (2026-08-15, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-15, this conversation) |
| Date | 2026-08-15 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.30 |
| Related Documents | `GENESIS.md` v0.2 (§0 tool-executable, §1 adapter + handover home, §5 the 9/67 measurement, §6 the positive gate rule); `genesis.py` (the fifth store tool, drone-built, gated); `BOOTSTRAP.md` (stamp inside — §2.2 rewritten for C-083); Node Template v0.5; Decision Register (stamp inside); Architecture State (stamp inside — §6); Rule Overview (stamp inside); Local Context (stamp inside); Context Index (stamp inside); Agenda Board; Protocols v0.22 (C-066), v0.23 (C-067), v0.24 (C-070 + the coupling walk amended here), v0.28 (C-074/C-075), v0.30 (C-078–C-080) |
| Document ID | DOC-01M02GB3Y3RMCWRZJDJGS0AVHQ (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise, the v0.27–v0.30 precedent) |
