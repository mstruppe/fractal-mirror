# Fractal Governance Protocol — Claude Series v0.17

**Topic:** The loose-ends pass — Scan #2 ratified as the first canonical review (C-058: reviews are a class; findings ledger); the close-the-loop checklist and auditable handover (C-059); the C-038 drill's **execution record made canonical** (curing scan S2-1.1 — v0.16's "pending" caveats are discharged *here*, in the protocol series, not only in projections); the whole-corpus currency pass executed (19 findings fixed in one close); OQ-23–OQ-27 entered.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.16

---

## 1. Context

Max opened the conversation by commissioning a second whole-project loose-ends scan and declaring it canonical in the same breath — "which automatically makes it a canonical document." The scan ran read-only over the full Claude-era corpus, the live store, the git repository, and the five Project mirrors, against the post-drill state at HEAD `0bd546e`. Its 24 findings (+2 carried from Scan #1) were each verified against source file and line; 24 of Scan #1's 26 findings were confirmed genuinely retired.

The scan's headline: **the corpus is machine-verified exactly where a machine checks it, and was drifting exactly where none does.** `verify.py` PASS to the unit (46 nodes / 179 events, 0 warnings) while eleven prose claims in the projection layer were false — all traceable to one mechanism: the close-the-loop refresh had silently narrowed to a fixed triple (Register, Rule Overview, Local Context; three verbatim-identical refresh lines in the last three Return Packages). Everything outside the triple fell behind by exactly the number of conversations since it was last touched. The 174/176 event-count drift the C-038 drill caught was the first specimen of the class; the scan supplied eleven more.

The scan's second structural finding was reflexive: the C-038 drill conversation — the project's proudest result — closed with a Return Package and **no protocol**, leaving the off-site copy and the green acceptance test recorded only in derived projections, with the Register contradicting v0.16's own caveat lines. And review findings had no cumulative ledger, so Scan #1's findings 1.5 and 2.4 had leaked in exactly the way C-034 was invented to prevent.

Max accepted the full remediation pass, C-058, and the execution delegation explicitly (see §7), and made two further calls mid-pass that this protocol records (§6).

## 2. Questions investigated

1. What loose ends exist across the whole project, and what single mechanism (if any) produces them? *(The scan — `Review_2026-08-14_LooseEnds-Scan-2.md`, the canonical record.)*
2. What does declaring a review "canonical" oblige — identity, minting, status, disposition? *(Scan §7 → C-058.)*
3. How does the refresh habit become a checked duty instead of a memory? *(→ C-059.)*
4. Where do the drill's results live canonically? *(→ §4, the execution record.)*
5. Is the Architecture State still necessary now that the repo itself is the shippable blueprint? *(Max's question mid-pass → §6.1.)*
6. How is the ChatGPT-era Master Index to be weighed by future work, knowing how it was produced? *(Max's question mid-pass → §6.2.)*

## 3. Decisions of record

- **C-058 — Reviews are a canonical class (executed).** Whole-project reviews (the Loose-Ends Scans and successors) are **canonical, sequential, dated artifacts**: dated filename under `Context Packages/Conversations/`, canonical control header, DOC-minted at first commit (C-041), **never revised** — a review is a dated observation; corrections land in later reviews or the ledger. Findings carry stable ids (`S<n>-x.y`); the C-034 mechanism **extends to review findings**: the Decision Register hosts the cumulative review-findings ledger (disposition `open` / `fixed` / `superseded` / `declined`; an item leaves only by recorded disposition). A review's *findings* are verified observations; its *fixes* remain proposals until an ordinary decision adopts them — a canonical review is never a control file. Scan #1 is retro-classed and retro-minted **as-is** (its "not canonical" banner predates the class and stays untouched — the record of what it was when written); its findings 1.5/2.4 seeded the ledger. Resolves S2-3.2.
- **C-059 — Close-the-loop checklist + auditable handover.** The C-004 tail is exercised as a **standing checklist**: every close walks the full living-projection table — Decision Register, Rule Overview, Local Context, Agenda Board (file-first, C-048), Context Index, Global Context, Architecture State, BOOTSTRAP, the Schema→Template coupling, the store tools — marking each **changed** (with new version) or **checked — unchanged**. "Checked, unchanged" is recorded, never implied. Normative home: the Local Context's standing-refresh section (lean filing per the C-047 precedent; escalate to a Settings amendment on observed staleness). Return Packages open their *Next* with the auditable handover — *"previous package queued X; this conversation did Y."* Every conversation closes with a Return Package **and** either a Governance Protocol or a recorded reason none was issued. Addresses S2-3.1 / S2-3.3 / S2-2.5.

## 4. Execution record — the C-038 drill (retroactive; cures S2-1.1)

Recorded here so the protocol series is again the complete history it claims to be. On **2026-08-13**, in the conversation following v0.16's ratification: **C-056 was completed** — private repository `mstruppe/fractal` created at Max's terminal; `origin` bound over SSH after the HTTPS-credential dead end (the C-018 one-URL swap, exercised incidentally); push credential = SSH key (C-057 layer-2/3 conformant); **first push done**; the push rides every C-037 commit since. **The C-038 acceptance test was then exercised green:** a cloud-session clone via a fine-grained, single-repo, read-only token (revoked after the drill) rehydrated per BOOTSTRAP §1 — all referenced paths resolved, history unbroken to the 2026-08-12 baseline, both C-037 author identities present, `verify.py` PASS, byte-parity with the source at HEAD. **Both caveats recorded in v0.16's status line are hereby discharged in the series itself.** The drill also surfaced the first observed projection drift (Local Context headline 174 vs. log 176) — the datum behind OQ-24. The drill conversation numbered no decision, correctly; its omission was the *record*, cured here. Scope boundary of the test now stated in BOOTSTRAP §4: the drill proves structure (rehydration, verification, byte-parity), not prose truth — that is the C-059 duty and, mechanized, OQ-24.

## 5. The currency pass (executed this conversation)

All fixes below were adopted by Max's acceptance of the pass (§7) and executed in one close, one `[GOV]` commit:

- **Architecture State → v0.2** — Schema pointer v0.5, Template v0.4; C-055 one-file log in §2; C-056/C-057 + drill result in §5; role clarification per §6.1. *(S2-1.2)*
- **Context Index → v0.10** — Schema v0.5 (×2), series v0.1–v0.17, Template v0.4; canonical-reviews row added. *(S2-1.3)*
- **BOOTSTRAP → v0.4** — §1 version-pointer dropped for the C-012 stamp-inside rule; §4 test-scope boundary. *(S2-1.4, S2-3.4)*
- **Node Template → v0.4** — companion/parent → Schema v0.5; §C log path → `part-0001.jsonl`; C-059 coupling noted. *(S2-1.5)*
- **Decision Register → v0.15** — C-058/C-059; OQ-23–OQ-27; review-findings ledger seeded (26 items — 20 fixed, 6 open); normative homes version-agnostic; Sources cured; drill/first-push rows marked "execution record per v0.17". *(S2-1.6, S2-2.3, S2-2.4)*
- **Rule Overview → v0.13** — C-058/C-059 rows; ledger caveat updated. **Conversation Settings** — `Reviewed By` completed (v0.4 identity retained; no substantive change). *(S2-2.2)*
- **Knowledge Path Foundation** — status corrected `Draft (Proposal)` → `Ratified (2026-08-12, per v0.7)` (the review pass had ratified C-013–C-020 without flipping the field); §2/Sources protocol-series misattribution corrected to the ChatGPT-era lineage. *(S2-2.1, S1-1.5)*
- **`verify.py` / `mint.py`** — four header comments → Schema v0.5. *(S2-1.7)*
- **`Project Governance/Templates/`** — empty, referenced by nothing since 2026-08-01 — retired to `_to_delete/` (Max empties). *(S1-2.4)*
- **Store** — Scan #1 (retro), Scan #2, and this protocol minted as DOC nodes; eight revise events re-freeze the edited canonicals; **49 nodes / 199 events**; `verify.py` green before commit (C-050).
- **Local Context → v0.20** (carries the first exercised C-059 checklist) · **Agenda Board → v0.20** (file-first, then republished) · **Return Package** `Return_Package_2026-08-14_LooseEnds-Scan-2.md` (first auditable-handover line).

## 6. Calls recorded (no new numbers)

1. **Architecture State — keep, reframed (Max's call).** Max asked whether the document is still necessary, its original purpose — "the blueprint I could give any AI agent without needing to explain FRACTAL" — having been superseded by the shipped repo itself. Recorded: the **blueprint role is superseded by the repository** (a clone + BOOTSTRAP is the blueprint, drill-proven); the document is retained as the **map** — currency, supersession, relation of parts — whose intended reader is the build track (the WS forge, the index server). Banner rewritten accordingly in v0.2. Retirement remains available later as an ordinary decision; nothing hard-binds to keeping it.
2. **Master Index provenance (Max's disclosure, recorded for the WS forge).** The ChatGPT-era Master Index was produced by instructing ChatGPT to "write an extensive list of what to do when building a software, with every detail" — a **generated enumeration**, not a record of Max's decisions, and exhaustive-by-instruction is the opposite of the FRACTAL credo (which is why C-051 declined to resume its 74-chapter plan). Treatment confirmed: pointer-only (C-029), **informs, never governs** (the OQ-22 posture); the future WS forge weighs Parts VI–VIII as raw material, with Max's UI-vision note and observed need leading. Token/ROI note: as a `.docx` behind the pointer-only boundary it costs a filename in a listing; both scans read zero bytes of it.
3. **Genuine transition — not declared.** Offered under OQ-4 (the shipped-and-proven foundation is a strong candidate, and Max's own "we already shipped it" is evidence); Max chose **not yet**. Global Context §2 unchanged; the candidate stands observed; OQ-4's disposition already covers declaration-by-fiat later.
4. **The Return-Package gap is historical fact.** Protocols v0.3, v0.4, v0.5 and v0.12 have no Return Package; the Local Context chain skips v0.3/v0.5/v0.13. Recorded, not reconstructed — fabricating retroactive packages would forge history. C-059's pairing rule prevents recurrence. *(S2-2.5)*
5. **Scan #2's date.** Authored 2026-08-14 over the 2026-08-13 HEAD; the working draft momentarily carried the 13th and was corrected before commit — noted as the first live catch of the pass's own discipline.

## 7. Ratification record (2026-08-14, in-conversation per C-033)

Max's explicit calls, each after a walkthrough: scope — **"Full pass now"** (steps 1–4 in one close); C-058 — **"Accept"** (reviews canonical, sequential, minted; ledger extension; Scan #1 retro-minted); execution — **"I edit + commit, you push"** (Claude edits and commits as the attributed author per C-037; Max reviews and pushes); Architecture State — **"Keep, reframe"**; transition — **"Not yet."** The scan itself was commissioned canonical in Max's opening message. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- **OQ-23 (new):** when is the WS forge triggered? (Ledgered at last — the item C-034's sweep had carried outside the ledger in v0.14/v0.15 §11.) Open — on observed need: the first WS build.
- **OQ-24 (new):** whole-repo verification / projection-drift checking — cadence and mechanization (the version-agreement checker; the natural first build-track item).
- **OQ-25 (new):** restore-drill cadence.
- **OQ-26 (new):** calibrating the C-057 custody ladder against the network horizon.
- **OQ-27 (new):** what "safety" means once other writers exist.
- Standing items carry: OQ-4 (candidate noted again, undeclared), OQ-6, OQ-9, OQ-10 (now adjacent to open finding S2-6.1), OQ-13, OQ-16, OQ-17, OQ-18, OQ-20. Open review findings: S2-5.1, S2-5.2 (→OQ-24), S2-6.1, S2-6.2, S2-6.3 — see the Register's review-findings ledger.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.17 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.17 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.16 |
| Related Documents | Review_2026-08-14_LooseEnds-Scan-2.md (canonical review, C-058); Review_2026-08-12_LooseEnds-Scan.md (retro-minted); Decision Register v0.15; Rule Overview v0.13; Local Context v0.20; Architecture State v0.2; Context Index v0.10; BOOTSTRAP.md v0.4; Node Template v0.4; Conversation Settings v0.4 |
| Document ID | DOC-01KZZPC3G6PZBF25W8ADMC58VQ (minted 2026-08-14, C-041, per this protocol) |
