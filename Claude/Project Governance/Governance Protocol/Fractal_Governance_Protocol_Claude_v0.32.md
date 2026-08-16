# Fractal Governance Protocol — Claude Series v0.32

**Topic:** Post-close doctrine, same conversation. **C-084** — *author is whoever writes; committer is whoever authorized* — amends C-074's declaration that the committer field is mechanical, making it **semantic** while leaving custody with the signature. **C-085** — **live pre-canon**, a class for Max's notebook: tracked for durability, formally non-governing, and excluded from closes by C-084 rather than by any new mechanism. Both raised by Max in response to an attribution error in the v0.31 close, and both generalize the incident rather than patching it.
**Status:** Ratified (2026-08-15 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-15 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.31

---

## 1. Context

The v0.31 close committed with `author = Max Struppe`, which C-037 makes wrong: Claude wrote every byte. The error was reported rather than force-pushed away — the commit was already on `origin`, and C-037 forbids rewriting shared history for a legible blemish.

Max's response was not to fix the commit but to fix the **rule**, which is the more valuable move:

> *"we should clarify this sustainably. In this case I initiated the close, however in any case you execute… whoever actively creates and edits is author. In cases where you execute without explicit permission, because it's already within you permissions, then you are committer as well — by default instructions which are committed by the project owner. Whenever we ratify, I actively ask of command / close, the user or owner is committer."*

He also resolved a second anomaly from the same close in passing: the modified `Vision thought scramble.docx` had no mysterious cause — *"I'm the executioner in your 2. point btw."*

## 2. C-084 — the committer field becomes semantic

**What it settles.** *Author* answers **who made this**; *committer* answers **under whose authority**. The second question previously had no recorded answer, because C-074 had deliberately emptied the field of meaning.

| Situation | Author | Committer |
|---|---|---|
| Claude writes, acting inside permissions already granted (C-064 standing push; anything within the adapter's grant) | Claude | **Claude** |
| Claude writes, Max actively commands or ratifies (`/close`, *go*) | Claude | **Max** |
| Drone executes a brief | Codex | **Codex** — the brief is the grant |
| The governing surface merges a flight | (unchanged — Codex) | whoever authorized the merge |
| Max writes it himself | Max | Max |

**The load-bearing idea** is that standing authority is *still Max's authorization*, given once and not re-asked. That is exactly C-008's promotion mechanism seen from the commit's side: a promotion converts *ask every time* into *authorized in advance*, and the committer field is where that conversion becomes visible in the record. A `/close` is the opposite case — authorization requested and freshly given — and the field says so.

**What is amended, and what is not.** This amends **C-074(a)**, which held that the committer field *"carries no governance meaning — mechanical plumbing recording which configured environment created the commit object."* **C-074(b) stands untouched:** custody is the **signature**, custody-scoped to Max's environment. The two are now orthogonal rather than conflated, and the shape they jointly permit is worth naming because it looks wrong at first glance and is not:

> **author Claude · committer Claude · signature verifies `G` against Max's key** — *Claude wrote it, Claude acted under standing authority, Max's custody vouches for it.*

**Pre-decision committer fields are noise by C-074's own design** and are not retro-fitted; C-037 forbids rewriting shared history, and the noise is harmless. **One consequence worth recording:** the v0.31 close commit was *half correct before the rule existed* — Max typed `/close`, so `committer = Max` was right; only the author field was wrong.

## 3. C-085 — live pre-canon

C-062 labels pre-canon material — *informs, never governs* — but assumed it **frozen**: the ChatGPT-era documents, historical and finished. Max's notebook is a different animal: **live**, continuously edited, a place where ideas are captured and later copied into conversation when he judges the moment right.

Without a name for that class, its edits surfaced as anomalies inside a close — a file changing for no reason the system could account for.

**Disposition (Max's call): tracked and formally non-governing.** Never a source, never orientation-loaded, never cited as authority, outside both checkers' scope, and never part of a close's change-set. **Untracking was rejected** as the worse trade: it would solve a noise problem by discarding version history and off-site durability (C-056), and would make *knowledge is never ignored* take its first deliberate exception — for something that is not knowledge-in-the-system at all.

**The elegant part is that it needs no mechanism.** Under C-084 the notebook's author is Max; a close only ever stages what Claude wrote. The two decisions interlock, and the second is enforced by the first.

## 4. Ratification record (2026-08-15, in-conversation per C-033)

C-084 and C-085 ratified in the conversation that produced them, both stated by Max in his own words (§1). Register → v0.33; Rule Overview → v0.28 (two rows added); `CLAUDE.md` → v0.5 and `AGENTS.md` → v0.6 (**C-077's second exercise** — doctrine touching a surface's rules re-projects in the same close). **Conversation Settings unchanged (v0.6):** the commit convention is a repo ritual (C-037/C-074), not a conduct rule, and no Settings sentence covers it — so no reissue and no restamp cascade.

## 11. Open Questions (TBD)

None opened or closed. **OQ-27** (writers outside Max's custody) gains a clarification rather than a change: C-084 makes the committer field say *under whose authority*, which is a question an outside-custody writer will have to answer explicitly — but the row's scope is unchanged, and federation remains its at-scale case.

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.32 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.32 |
| Status | Ratified (2026-08-15, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-15, this conversation) |
| Date | 2026-08-15 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.31 |
| Related Documents | Decision Register (stamp inside — C-074 row annotated); Rule Overview (stamp inside); `CLAUDE.md` v0.5; `AGENTS.md` v0.6; Local Context (stamp inside); Protocols v0.20 (C-064, the first promotion), v0.28 (C-074 custody), v0.29 (C-077), v0.31 (the close this corrects) |
| Document ID | DOC-01M02H9F6K7X318AMS5FT1CDAV (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise) |
