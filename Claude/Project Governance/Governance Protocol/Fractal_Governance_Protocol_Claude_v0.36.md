# Fractal Governance Protocol — Claude Series v0.36

**Topic:** The beta-pack close (ninth Code session). Max opened on the milestone read — *"we have achieved the first big milestone … run a scan, then we're ready to pack fractal and consider it the first shippable beta version we can check and also build an identity around it"* — and one concern: *"anyone could simply copy the repo and claim it theirs … How can it be verifiably my invention? we need to consider a legal concept."* The session answered all of it: **C-090 — the legal identity layer** (releases are provenance-anchored; license and trademark postures recorded beside it); the **first realisation transition** — Global Context §2 moved v0.3 → v0.4 by Max's fiat, becoming **OQ-4's first declared datum**; **Scan #4 executed as the pre-pack gate** (7 findings, 0 High — the series' smallest; full slate fixed in-pass); and **the pack itself**: the close commit tagged **beta-0.1**, signed, with C-090's first anchor riding it.
**Status:** Ratified (2026-08-15 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-15 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.35

---

## 1. Context

The session opened by `/fractal` onto a completely clear runway — the punch-list close had left nothing pending. Max's first act closed the last cosmetic tail (vendor-side Cowork deletion confirmed done, C-089); his second declared the milestone and its consequence — scan, pack, identity — and raised the ownership question that became this close's doctrine. The discussion split the risk in two: losing **ownership** is a legal question, losing **recognition** a brand question, and they have different defenses. On ownership the corpus turned out to be its own best evidence — FRACTAL's founding thesis (*preserve the reasoning process, not just results*) means a copier holds a snapshot while Max holds the causal history, nine sessions deep, cross-referenced and third-party-corroborated (GitHub push records). The one gap: internal evidence is self-asserted. The fix became C-090.

## 2. C-090 — the legal identity layer (releases are provenance-anchored)

**The rule:** every shipped release tag is externally anchored at pack time — an **OpenTimestamps attestation** of the tag's hashes (free, Bitcoin-anchored, verifiable by anyone without trusting the author or the host), the **receipt committed into the repo**, so the repo carries its own proof. Optional escalations at need: an eIDAS qualified timestamp (EU court-grade presumption), US Copyright Office registration (statutory damages where US enforcement matters). Ownership itself was never the gap — copyright arises at creation (Berne) — the gap was **proof of priority**, and after the first anchor any copier's earliest provable date is later, forever. The mechanism is a **kernel rule**; the anchor-authority set is an **instance value** — **the ninth parameterized decision** (GENESIS §2 row 9).

**Recorded beside it, un-numbered by design (the v0.35 posture pattern):**
- **License posture** — Max's intent verbatim: *"I want fractal to be used freely out there, it should have easy access"* — free use with attribution preserved (sketch of record: CC BY for the document corpus, Apache-2.0 for the tools); the C-079 open-core ladder stays available for tier 1; the verification architecture is the value to keep building (*"the crucial components … ready and flexible for solutions"*). The license text is chosen at the flip; until then the private default (all rights reserved) is the interim state.
- **Trademark posture** — the compound name chosen at the flip is registered as a mark; copyright protects the corpus, the mark protects the identity. Rides the recorded naming posture (v0.35: the bare word is crowded; qualify/compound at the flip).
- **Patent path declined knowingly** — EU novelty dies at publication, and publication is itself the defense: a timestamped public corpus is prior art in Max's name. Staying private is the riskier posture for idea-theft; the anchor makes publication safe.

## 3. The first realisation transition (Global v0.4 — OQ-4's first declared datum)

Max asked whether the milestone triggers the Global §2 update; the Register held the answer in OQ-4's own text: *"Max may declare a transition by fiat, and that case becomes the first datum."* His call — *"the global context issue being a prio 1 case I want to fix immediately"* — exercised exactly that provision, grounded in **executed fact, not intent**: arc 1 complete and the punch list closed, the foundation phase *finished*. Global Context moved v0.3 → v0.4 the same hour: *building its foundational architecture* → **"shipping its completed foundation and proving it beyond itself."** The arc-2 candidate stands untouched as the expected **second** datum, and OQ-4's resolution expectation is unchanged — the term is defined when the second case forces comparison. The phase-level history (C-010) now has its first recorded transition.

## 4. Scan #4 — the pre-pack gate (full slate fixed in-pass)

Commissioned by Max ("run scan #4 now") with a mandate the series had not carried: gate the pack. **Seven findings — 3 Med, 4 Low, 0 High — the smallest slate of the series** (26 → 24 → 8 → 7), and the thesis extended by one generation: *each new capability era is born outside the guard perimeter* — this era's findings sat exactly in its additions (the ship surface, the generator, the guard's own output, the close's own act-ordering). Canonical record: `Review_2026-08-15_LooseEnds-Scan-4.md`, minted at this close.

- **S4-2.1 (the sharpest):** `genesis.py` carried a private copy of the §3.4 inheritance clause, frozen at C-083 while GENESIS moved to C-089 — every newborn opened with an under-inclusive constitution clause. Invisible to every checker; caught by the series' **first birth test**. Cure by subtraction: the tool's copy **deleted** — `genesis.py` reads the blockquote from GENESIS.md at run time (GENESIS §0's rule decided the direction: *the document wins*, so the document became the only copy). **Re-gated:** a second scratch birth, clause string-equal to the document, both checkers green, 0 warnings.
- **S4-1.2:** store-count claims were stale at birth — the v0.35 close wrote "85/454", then its own mints and revises made the store 86/468. Cure: `check_versions.py` gains the **count rule** (living count prose must match the store — first run caught both live instances), and `/close` gains the **counts-last** step.
- **S4-1.1:** README one flight behind with its own §2-transition refresh trigger fired — refreshed (six tools, ship framing). **S4-1.3:** frozen "next: Scan #3" parentheticals dropped (BOOTSTRAP §4, Rule Overview §5). **S4-1.4:** OQ-30's cell re-headed Resolved. **S4-1.5:** push wording harmonized to rides-every-close (C-064) in AST §5 and the Rule Overview. **S4-3.1:** the WARN channel de-noised — 28 standing warnings were 79% two stable noise classes; heuristics refined (`.py` fragment skip; `retired|unbuilt` context), the SUPPRESS list *shrank* by one, the channel now 9 and all genuine.
- **Riding executions, both green:** the restore drill (second Scan-riding run — all 12 §1 paths; **the first machine-executed §4 rebind**, `doctor.py --write` on the fresh clone; signature shape exact; both checkers PASS in the clone) and the **birth test** (adopted with the slate as a standing section wherever a Scan gates a ship boundary — the drill proves the corpus *restores*, the birth proves it *reproduces*).
- **Reissues in the pass:** GENESIS → **v0.4** (the ninth parameter; clause and ledger numbers current) · Rule Overview → **v0.31** (the anchor row) · Architecture State → **v0.14** (parameterized 9) · BOOTSTRAP → **v0.17** · Register → v0.38 (S4 rows, all Fixed) · README refreshed · `/close` amended.

## 5. The pack — beta-0.1, C-090's first execution

Executed at this close's tail, in order: the close commit (this protocol, the scan mint, the full C-059 walk) is tagged **`beta-0.1`** — an annotated, **signed** tag (custody, C-074); a **Provenance** folder at the repo root receives the tag's attestation file (tag and commit hashes, identity, date) and its **OpenTimestamps receipt**; the anchor commit lands directly on the tag's heels; the close push (C-064) carries commit, tag, and anchor together. The OTS pipeline was **pre-tested in session scratch before this protocol froze** (client installed to the user environment — tooling is environment, not repo content; four calendar servers answered). An OTS receipt is complete-but-pending at issue and upgrades to its Bitcoin-final form at any later session — mechanical, no decision. From this act forward, *"verifiably my invention"* is mathematics: the beta's exact corpus provably existed under Max's custody no later than today.

## 6. What this close deliberately does not do

Arc 2 does not open — it stays the queue's head **on Max's word**, with the specimen question his (tracker vs research project; recommendation of record: birthed beside the repo). The flip-time bundle stays postured, not decided: license text, compound name + mark, flip-vs-mirror, branch protection — all fire at the public boundary, now with the legal layer beneath them. Conversation Settings is untouched (a release ritual is a repo ritual, not a conduct rule — the C-084 precedent); `AGENTS.md` is untouched (drones cannot release). S3-2.2 stays open on its unchanged grounds. No route is minted; the Knowledge Network Foundation is untouched; OQ-4 is *not* resolved — it gained its first datum, nothing more.

## 11. Open Questions (TBD)

- **OQ-4 annotated:** first declared datum recorded (the foundation-complete transition, by fiat per the row's own provision); the arc-2 second-datum expectation and the resolve-at-arc-2 forecast both stand.
- **OQ-28 annotated:** the kernel gained its ninth parameter (C-090) — one more small, deliberate increment on the weight dial; arc 2 remains the verdict's source.
- The C-090 escalations (eIDAS, US registration) are instance values exercised at need, not open questions; the OTS receipt upgrade is mechanical and rides any later session.
- Nothing new opened. Nine OQs stand, every one on a named trigger or an arc.

## Ratification record (2026-08-15, in-conversation per C-033)

Max's calls of record, in sequence: the milestone read and scan commission (*"I suggest to run a scan, then we're ready to pack fractal …"*); the legal-layer adoptions — *"I like that, we need to hold on to that"* (the anchor, item 3 of the discussion), *"also 5. is an important consideration"* (trademark), *"6. I agree, I actually want fractal to be used freely out there, it should have easy access, the verification within are the crucial components"* (license posture + defensive publication); the transition — *"the global context issue being a prio 1 case I want to fix immediately, let's quickly document those items, then fix the global context"*; the scan — **"run scan #4 now"**; the slate — **"full slate"**; the close and pack — **`/close`** on the runway stated and restated (close → tag beta-0.1 → anchor → push). Ripple: Global Context → **v0.4** · Register → **v0.37/v0.38/v0.39** (C-090 entered, S4 rows, ratification + first-execution mark) · Rule Overview → **v0.31** · Architecture State → **v0.14** · BOOTSTRAP → **v0.17** · GENESIS → **v0.4** · `CLAUDE.md` → **v0.7** (C-077's fourth exercise — the C-090 release-ritual line; Settings unchanged at v0.7, so the stamp holds) · `AGENTS.md` unchanged (v0.7) · Context Index → **v0.26** · Local Context → **v0.51** · board regenerated · `/close` counts-last step · `genesis.py` + `check_versions.py` amended per the slate · Scan #4 minted · **tag beta-0.1 + the Provenance anchor + push**.

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.36 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.36 |
| Status | Ratified (2026-08-15, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-15, this conversation) |
| Date | 2026-08-15 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.35 |
| Related Documents | Global Context (stamp inside — v0.4 this close); Decision Register (stamp inside); Rule Overview (stamp inside); Architecture State (stamp inside); BOOTSTRAP.md + GENESIS.md (stamps inside); CLAUDE.md + AGENTS.md (stamps inside); Context Index (stamp inside); Local Context (stamp inside); Review_2026-08-15_LooseEnds-Scan-4.md (minted this close) |
| Document ID | DOC-01M03564WQKA6RHGKBZP08JR5V (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise) |
