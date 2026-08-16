# Return Package — 2026-08-15 · The Instantiation Program (C-078–C-080; arc 1 opened, OQ-13 closed permanently)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Local Context v0.45; Decision Register v0.31; Governance Protocol — Claude Series v0.30; Architecture State v0.11; `GENESIS.md` v0.1; `verify.py` + `check_versions.py` runs of this close (both PASS).

**Parent:** Return_Package_2026-08-15_LooseEnds-Scan-3.md · **Local Context:** v0.40 → **v0.45**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** nothing — the G offers and H roadmap stood open. **This conversation did:** Max opened with a **frame, not a task** — *"I think we're getting close to the finish line where we can ship fractal… I want to throw in my vision and you can tell me how far we are away."* The vision was assessed against the corpus (tools and specs read directly, not narrated from prose), adopted as **C-078 — the instantiation program**, and **arc 1 was opened and half-delivered in the same session**. Then Max named a standing irritant — OQ-13 — and it was closed permanently as **C-080**. Fifth Code session; opened by `/fractal`; the C-031 discipline held throughout (every decision was Max's call, offered with a recommendation).

## 2. Acts of record

- **C-078 — the instantiation program.** FRACTAL becomes *governable-from*, in three ordered arcs: **kernel extraction → the portfolio live tracker as first foreign instance → federation** (deferred until two instances exist). Adopts **a direction and an order, never a design**. Roadmap H absorbed, not displaced. **Global §2 deliberately untouched** (Max: *"Not yet"*) — the realisation line moves when FRACTAL first governs a project that is not itself, which is now OQ-4's named **second candidate** and the condition under which that row is expected to *resolve*.
- **C-079 — the kernel is tiered.** Raised by Max's question *"KG search/index is also still open. Something we may want to fix before the kernel extraction?"* Answered **no — decide its tier membership instead**, at the cost of one decision rather than an arc. FRACTAL ships a **specification** for reads, not an implementation: the Navigation Contract is kernel, tier 0 is the grep ritual, tier 1 is the index server on its unfired C-068 trigger. Recorded honestly: arc 1 completes the **skill** packaging tier, not the **plugin** tier.
- **Arc 1, deliverable 1 — the partition measured.** Walking all 79 decisions found **three classes, not two**: kernel **~64**, **parameterized 7**, instance **14**. The parameterized class was not anticipated and is the operationally important one — a kernel *rule* carrying an instance *value*, and precisely the input form a genesis tool must ask for. **FRACTAL is ~80% kernel**, superseding the ~40 estimate C-078 and Architecture State §6 both shipped with; that estimate was flagged as awaiting measurement and is corrected in both loci.
- **Arc 1, deliverable 2 — `GENESIS.md` v0.1 issued** (canonical root document, DOC-minted `DOC-01M0270TWM1YPA2Z8MTHBT6AW0`, joined the `check_versions.py` LIVING registry + STRICT scope + walk). BOOTSTRAP's forward sibling: one rehydrates *this* instance, the other births a *new* one; §0 of each now bounds the other's scope. Its load-bearing contribution is the **inheritance-clause pattern** — a new instance's Register opens with *one clause*, never 64 copied rows.
- **C-080 — the `_v0.1` grandfathering retired; OQ-13 closed permanently.** Max: *"it feels like a duct tape fix. Can we eliminate the issue for once?"* The three orientation files renamed (`git mv`, history preserved, 93–99% similarity), C-012's grandfathering clause and the Index's naming paragraph **retired**, and the class **closed mechanically** — `check_versions.py` now errors on any LIVING filename carrying a version token, unit-tested against all three retired names, all ten current living documents, and two synthetic violations. **OQ-13 has no remaining trigger.**
- **Drone flight 3 launched** — `genesis.py` briefed to `AGENT.AI.CODEX` on `drone/genesis-tool`, in an isolated git worktree so the flight cannot collide with this close. Spec = `GENESIS.md` §1–§3 + Architecture State §6; model = `close.py` (C-073 precedent); gate = both checkers green **inside a birthed scratch instance**, not merely in this repo.

## 3. Change summary (three `[GOV]` commits, Claude-authored per C-037; push at close per C-064)

`feb7db8` C-078 + C-079 + Protocol v0.30 · `47a302e` arc 1's partition + `GENESIS.md` · `8db3142` C-080. **New:** `GENESIS.md` v0.1 (minted) · Protocol v0.30 (minted, `DOC-01M026CTV62CS0FSH96SXNJQ8F`) · this package. **Living docs:** Architecture State → **v0.11** (new §6) · Register → **v0.31** · Rule Overview → **v0.26** · BOOTSTRAP → **v0.15** · `CLAUDE.md` → **v0.4** · `AGENTS.md` → **v0.5** · Context Index (renamed; GENESIS rows) · Local Context → **v0.45** · Board regenerated. **Renamed (C-080):** `Fractal_Global_Context.md` · `Fractal_Context_Index.md` · `Fractal_Conversation_Settings.md`. **Tools:** `check_versions.py` — `GENESIS.md` registered, plus the new LIVING-filename version guard. **Store:** +18 events (2 creates with alias + placements, 14 revises) — **79 nodes / 407 events**. **Unchanged:** Global Context v0.3 (deliberately) · Conversation Settings v0.6 · Schema v0.6 / Template v0.4 / Navigation Contract v0.1.

## 4. Refresh list

The C-059 checklist was walked — see Local Context v0.45 §Standing refresh items. Two rows are worth reading rather than skimming: **Rule Overview** fired on a *retirement* for the first time (its trigger reads "rule added **or** retired"), and the **client-adapter row** records `CLAUDE.md`/`AGENTS.md` as **path currency, not re-projection** — a rename is not a doctrine change, and the distinction is preserved so the C-077 walk keeps seeing it. Both checkers green before every commit.

## 5. Unresolved / carried

- **Arc 1 is open — two of four deliverables.** Remaining: `genesis.py` (**in flight** on `drone/genesis-tool`) and the **skill packaging unit**, which forces **OQ-16**. The skill is explicitly *not* drone-able: C-066 bars drones from governance acts, and a `SKILL.md` carrying conduct rules is a C-065-class canonical adapter.
- **Open review findings:** one — **S3-2.2** (`Reviewed By` on Schema v0.6 + Navigation Contract v0.1), on its named trigger. Noted this session: both are **kernel** documents, so arc 1 should close it for free if it reissues either, and otherwise leave it open **deliberately** rather than by accident.
- **Standing OQs:** OQ-4 (second candidate named; fires *and should resolve* at arc 2) · OQ-9 · OQ-16 (forcing event named: arc 1's packaging decision) · OQ-17 · OQ-18 · OQ-20 · OQ-23 · OQ-27 (federation = its at-scale case) · **new:** OQ-28 (weight dial) · OQ-29 (code as governed artifact) · OQ-30 (secrets — decide before the first key exists) · OQ-31 (federation namespace + trust). **OQ-13 is closed permanently.**
- **Pending on Max: nothing.** Branch protection stays dormant (C-075).
- **Live risk of record:** OQ-28. A kernel too heavy to instantiate fails the vision more quietly than one missing features — the counterweight to this whole program, and it resolves from arc 2's lived experience, not from arc 1's design.

## 6. Next — review the flight, then finish arc 1

Open with **`/fractal`** (loads Global + Local v0.45 + this package). **First act: review `drone/genesis-tool`** — read the hand-back, run the gate yourself (both checkers *inside a birthed scratch instance*, not just in this repo), merge or send back, then **delete the branch, local and remote (C-075)**. Then the real acceptance test: **birth an instance and close a session in it** — that test *is* the tool's value; a genesis tool that looks correct but produces a subtly broken instance is worse than none, because the first to find out would be a stranger following `GENESIS.md` §6. Then **OQ-16** with the tool in hand — the skill should package the *automated* path, which is why it was sequenced second.

---

*Author: Claude (AGENT.AI.CLAUDE) · Conversation surface: Claude Code, in-repo — fifth session on the default surface, opened by `/fractal`; frozen at issue (C-058-class handover record, not minted — C-042 mint-on-reuse).*
