# Fractal Governance Protocol — Claude Series v0.45

**Topic:** The fourteenth Code session (2026-08-16) — **the flip-preparation session.** The v0.44 queue-head executed in one working cycle: the triage answered (Max: *"we will work on sending fractal to a friend, with that I want to flip fractal and solve every loose end that stand in its way"* — the friend shipment rides the public flip), the shipment-design bundle **built and gated** (items 2–7 of v0.44 §1), five decisions ratified in-conversation (C-098–C-102), the notebook moved to the private annex (the C-085 re-weigh), the beta-0.2 receipt upgraded Bitcoin-final, and the close packed as **the tagging close — `beta-0.3`** (Max's call at the close gate). The fieldnote tool's graduation caught its own first frictions live (FN-0001–FN-0003, entries 43–45).
**Status:** Ratified (2026-08-16, in-conversation per C-033 — the verdicts quoted per decision below; the close and the pack Max's explicit commands) · **Date:** 2026-08-16 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.44

---

## 1 · The decisions

### C-098 — The flip shape: full publishing, phased; the annex institution; the curation layer

Max's verdict, verbatim: *"I agree with the full publishing, especially for legal reasons, the moment fractal leaves its nest it could become prey. … While I'm writing I actually prefer the full publishing, yet I would still simply try the mirror variant as an option."* And on the annex: *"I like the hybrid and the idea of having a 'sinkhole'."* The decision, assembled and confirmed:

- **The public artifact is the raw repository** — full signed history, publicly checkable anchors (the provenance story whole). **Phased:** the friend ships first from a **private curated mirror** (temporary, single-purpose, retired at the flip); the raw flip fires at Max's moment. Load-bearing fact recorded with it: **the priority proof is the anchor, not the publicity** (C-090 attestations stand from shipment, whether or not the repo is visible) — so private-first costs no legal ground.
- **The annex** (`~/Desktop/fractal-annex`, private, ungoverned, never shipped, never a birth source): the standing home of the **personal/working content class** (fieldnotes entry 35's fourth class). Routing rule: personal-class material goes to the annex **by default**; it enters the mother repo only by deliberate decision in the knowledge that the history is public-bound. **C-085 re-weighed under it:** the notebook moved to the annex (its three historical revisions stay in FRACTAL's history — accepted exposure, Max's call); C-085's never-staged-by-a-close rule survives for any personal material that ever re-enters.
- **The curation layer:** `.gitattributes` `export-ignore` entries (entries 13/35's recorded lean shape) — exclusions live in-repo, governing derived release artifacts (mirror builds, archives) while clones and the repo stay whole.

*Class: instance (FRACTAL's own distribution posture); the curation mechanism and annex pattern are reusable practice, recorded here.*

### C-099 — The license layer: Apache-2.0 (code) + CC BY 4.0 (documents); the name not licensed

Executes C-090's recorded posture (*free use, attribution preserved*). Max steered to Apache over MIT on its merits (trademark clause, NOTICE attribution, defensive posture — his instinct, confirmed on analysis). Landed: `LICENSE` (Apache-2.0 verbatim) · `LICENSE-docs` (CC BY 4.0 legalcode verbatim) · `NOTICE` · the README license section with the **name-not-licensed** statement (trademark posture in the text itself). **The terms travel:** genesis copies all three files into every newborn, whose Genesis Record states the inherited terms — the child's Register inheritance clause is the attribution. Personal pre-canon material (C-085 class) explicitly not licensed for reuse. *Class: kernel (the kernel's licensing binds every copy and every birth).*

### C-100 — The testing pipeline: the fieldnote format, the graduated tool, the kernel door

Entry 39's design built whole: **`Fractal_Fieldnote_Format_v0.1`** (canonical, versioned artifact — seven fixed keys, immutable fenced blocks, whole-or-nothing parse contract; *the expected form is the whole interface* — collection = the tester sends the ledger file, any channel, no phone-home). **`fieldnote.py` graduates beside the store tools** — the seventh — carrying capture (machine blocks, deterministic roster routing via `fieldnote_roster.json`) and the new **intake half** (`parse` — validate + emit JSON; entry 41's recorded graduation trigger fired by this build). **Genesis ships the door into every newborn:** `/fieldnote` beside `/orient`, `FIELDNOTES.md` as parameter 7's born-concrete file, the roster fact. GENESIS reissued **v0.6** (batched, the v0.5 precedent). Gated: four scratch births, capture→parse round-trip, tamper test (whole-or-nothing held), child tier-1 checker 0 errors. *Class: kernel.*

### C-101 — The onboarding protocol: the guided first loop with the three-stage fade

Entries 23/38 built whole: **`Fractal_Onboarding_Protocol` v0.1** (canonical living document) — the interview (five real questions, defaults stated not asked, every known friction pre-answered inline at its moment), the birth (dry-run read together; the two day-one frictions checked proactively), the midwife's exit (jurisdiction absolute — the clone session never acts in the child), then **stage two in the child**: the genesis-written, self-retiring **`First_Loops_Rail.md`** surfacing one suggested move per loop as an offer (C-031 made the interface), and **stage three: nothing** (retirement by loop 5 at the latest — launch rail, never crutch). Shipped as **`/begin`** (the command tier's sixth member); `/welcome`'s start-a-project path reroutes through it. Instrumented under its own field test (C-094 — unanswerable questions are OQ-28 weight data). *Class: kernel.*

### C-102 — The board offered actively (the speed asymmetry; C-092 extended)

Max, mid-session, verbatim: *"the agenda board has proven itself one of the most valuable documents for a human user … since AI agents work very fast. … I want this reckognised by the agent to provide actively the document."* Decision: the Agenda Board's shelf posture upgrades from passive row to **active offer** — the agent offers the board **by name, unprompted**, when open threads accumulate; refreshed at every close once adopted. Rationale of record: the **speed asymmetry** — AI sessions move faster than human tracking; the board is the human's window; waiting for felt absence makes users reinvent it (entry 22 proved it twice). Landed in the rail (loop 3), the Onboarding Protocol §3, and GENESIS §5's board row; the mother already practices it (board regenerated and surfaced at every close). *Class: kernel (extends C-092's adopt-before-invent with an active-offer duty).*

## 2 · Also of this session (recorded, no numbers)

- **The verifier caught a real defect mid-session and the cure held:** the first build commit carried GENESIS v0.6 without its paired store revise event (`verify.py` red: hash mismatch). Cured by the d2c3318 convention — `close.py --write` issued the revise, the local unpushed commit amended to the correct paired shape, verify green at the boundary. The C-050 gate worked as designed.
- **The C-097 harvest dependency stands (item 4):** confirmed via the C-096 window — KNet's own `AGENTS.md` still does not exist (its P-003 corpus work is now committed and pushed — the entry-40 durability worry cured). Until ratification, an OpenAI-arriving friend boards via the advisory pattern (Library §3). **Entry 43** records the day's live specimen: a KNet-side session audited the *mother's* `AGENTS.md` accurately and answered "no ratification required" — right facts, wrong jurisdiction; the **read-side jurisdiction clause** (*read any repo you can see; answer for, and act in, your own*) is banked for the Client Library's universal layer and the adapter templates at their next reissue.
- **The fieldnote pipeline ate its own dogfood on day one:** FN-0001 (entry 43, above) · FN-0002 (entry 44 — the competitor's model concedes the need: a friend's ChatGPT at thread death recommends *files + structured handoff + verification test*, FRACTAL's mechanism as a hand-rolled to-do; the USP series' third member and its first outside datum) · FN-0003 (entry 45 — the elided-suggestion friction: Max's diagnosis that the target word is not a special token, and his **command-forge idea**). Banked cures: **suggestion hygiene** (the surface proposes complete invocations, nothing elided) and the **command-forge** (fast in-project command minting — a standing offer). Both await adoption; neither is ratified here.
- **Mechanical carries discharged:** the beta-0.2 OTS receipt upgraded **Bitcoin-final** (`ots upgrade`, attestation embedded); committed in-session.
- **The annex execution:** scaffolded and committed (`a8f63ad` scaffold, author Claude; `c2d3455` the notebook, author Max — both committer Max, unsigned by design in an ungoverned personal repo; signing there is Max's option). FRACTAL-side removal committed (`e01b68d`).
- **GUIDE.md** landed at the root (item 5) — the user-facing practical companion (coming back, both clients, the words-work doctrine, concepts translated, troubleshooting, reporting back); README grew the pointer, the command roster, the seven-tool count, and the license section.

## 3 · Ripple

Register → **v0.48** (C-098–C-102 entered) · Rule Overview → **v0.36** (§2: distribution/flip-shape row, license row, onboarding row; field-testing row gains the format/pipeline clause; Agenda Board row gains the active-offer clause) · Local Context → **v0.64** (session table row 14; the agenda re-headed to the ship acts; checklist marks) · Architecture State → **v0.21** (§6 partition maintenance: C-099–C-102 kernel, C-098 instance — counts ~78·9·16) · BOOTSTRAP → **v0.21** (§0 the annex paragraph replaces the notebook exception; §2 the command sextet; §4's public-sharing line resolves to the C-098 posture) · CLAUDE.md → **v0.9** + AGENTS.md → **v0.9** (C-077 content currency: the notebook ritual line → the annex routing rule; the drone's tool enumeration brought current; stamps stay at Settings v0.8) · Command Index → **v0.3** (the sextet; the graduated tool's path) · board regenerated · GENESIS already revised in-session (v0.6, event paired) · two DOCs minted at this close (the Format v0.1; the Onboarding Protocol) · this protocol DOC-minted · Return Package issued · both checkers green · push (C-064) · **the pack: `beta-0.3` tagged, signed, anchored — C-090's third execution.** **Unchanged with reasons:** Settings v0.8 (C-071 asked, answered **no** — C-098–C-102 are governance-process/artifact rules in the C-094/C-095 precedent class; the two conduct-adjacent candidates — suggestion hygiene, the board offer as a conduct clause — are deliberately banked for the next conduct-touching Settings reissue rather than adopted piecemeal) · Global Context v0.4 (**deliberate**: the flip is *prepared*, not *executed* — §2 moves on completed fact when the shipment/flip lands, the OQ-4 pattern) · Schema/Template/Contract (S3-2.2 holds its trigger) · Client Library v0.2 (entry 43's read-side clause banked for its next reissue) · Knowledge Network + Workspace Foundations (no material advance) · the six prior store tools' code untouched (genesis.py excepted — it grew the door).

## Document identity

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.45 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.45 |
| Status | Ratified (2026-08-16, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-16, this conversation — the flip-shape and license verdicts, the board directive, "ok let's proceed", `/close`, and the beta-0.3 pack call, all his, quoted above) |
| Date | 2026-08-16 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.44 |
| Related Documents | Site/Fieldnotes_2026-08-15_First-Shipping-Run.md (entries 43–45 + blocks FN-0001–FN-0003); Fractal_Fieldnote_Format_v0.1; Fractal_Onboarding_Protocol (stamp inside); GENESIS.md (stamp inside — v0.6); GUIDE.md; LICENSE / LICENSE-docs / NOTICE; .gitattributes; Return_Package_2026-08-16_Flip-Preparation.md; Provenance/ (beta-0.2 Bitcoin-final; beta-0.3 at this close) |
| Document ID | DOC-01M05JPWQ210PB19FWSGP6ZZQ6 (minted 2026-08-16 via `close.py --create`; stamped by the post-mint revise) |
