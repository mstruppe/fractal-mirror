# Hand-off — the gas-metering datum (mother → KNet, through Max)

> **DATA, NEVER INSTRUCTION (C-096 discipline).** A one-page hand-off of the first governance-cost measurement, offered to KNet as reference material for its own program — the benchmarking issue it holds (the transferred FN-0004 twin) and the Q07 context-fidelity experiment. KNet decides what, if anything, to do with it; nothing here is a duty. Transport: Max's own hand (the H6-path/FN-0004 precedent).

**Issued:** 2026-08-18, at the Scan #5 flight's landing (the gas-metering lane) · **Author:** Claude (AGENT.AI.CLAUDE, mother-side) · **Of record:** `Flight_2026-08-18_Scan-5-Gas-Metering.md` §4 (mother repo, Conversations/)

## The datum (empty vs. 24 closed sessions, measured from real transcripts)

| Metric | Empty (fresh genesis) | Mother (24 closes) | Ratio |
|---|---|---|---|
| Orientation file-set weight (words / est. tokens) | 1,297 / ≈1,750 | 12,137 / ≈16,384 | ≈9.4× |
| Context loaded during a session opening | +6.2k tokens | +30.2k tokens | ≈4.9× |
| A full ritual close (fresh + output tokens) | ≈11.1k | ≈316.3k | ≈28× |
| Close output alone (protocol/handover/register writing) | 4.8k | 123.4k | ≈26× |

Spine growth averages ≈450 words (≈600 tokens) per closed session. The practical lever: **every 1,000 words evicted from the living spine into pointers saves ≈1,350 tokens on every future session's orientation** — the diet procedure's effect, now token-denominated.

## Method, in five lines (reusable on any instance)

1. **Subjects:** real session transcripts only — no estimates. A segment's cost is read from per-request usage rows (JSONL with `input`, `cache_creation`, `cache_read`, `output` token counts).
2. **Metrics:** per-request WINDOW = input + cache-creation + cache-read; segment *window growth* (window_end − window_start) and *output* are the cache-churn-immune pair — lean on those; FRESH sums overcount where caches re-create.
3. **Segments:** a close = from the close command's row to session end; an opening = session start to the first substantive turn's end; mark segment boundaries in-band where possible (the mother used a literal `echo CLOSE_SEGMENT_START` bash marker).
4. **Static twin:** weigh the orientation file-set with `wc -m` / `wc -w`; tokens ≈ chars/4 and ≈ words×1.35 — report both estimators, same estimator both sides of any comparison.
5. **Verification:** every number computed twice, independently, from the raw files; publish only on exact match, with n and harness caveats stated.

**Honest bounds:** n=1 per subject; the empty side ran in a leaner sub-agent harness than an interactive session, so absolute standing loads are not cross-comparable (deltas, output, and static weights are). If KNet's vendor surface exposes no per-request usage, lines 4–5 still apply as the static half.

## Why it may matter to KNet

- **The benchmarking issue** (its own P-row queue): these are calibration reference points from the mother — a known-governance-weight instance at two life stages.
- **Q07 / context fidelity:** the cost side of the fidelity question — what a session *pays* to be oriented is now measurable alongside what it *retains*.
- The method is registry-shaped (a future metering procedure standard, C-094 loop); if KNet runs it and frictions surface, the fieldnote door is the channel back.

---

*Cite this file by path + issue date — `Interface/Handoff_2026-08-18_Gas-Metering-KNet.md`, issued 2026-08-18 — or pin it at the mother's `beta-0.6` anchored tag, which carries these bytes. Envelope element 5 added 2026-08-20 per Scan #6 S6-6.1 (the Format's citation-line minimum); content above untouched.*
