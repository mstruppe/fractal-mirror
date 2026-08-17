# Fractal Scan Procedure v0.1

> **CANONICAL SPECIFICATION — the loose-end-finding procedure (C-058's canonical review, the defect-hunting variant), distilled from history per C-108.** Versioned artifact (C-040 class): this version is frozen at issue; any substantive change is a new version/file. Nothing here is invented: every rule below is extracted from the four executed Loose-Ends Scans (2026-08-12, 2026-08-14, 2026-08-15 ×2) and the decisions that governed them — "already provided by history, it only needs to be implemented as such" (Max's ruling of record, C-108). A Scan is a **procedure** in the C-108 taxonomy: a pluggable component that an ultracode flight composes, and that also runs standalone — as all four instances of record did.

**Version:** 0.1 · **Status:** Ratified (2026-08-17, in-conversation per C-033 — Max: "full slate", including the §12 checker gate as written: Scan #5 does not close without the conformance checker) · **Reviewed By:** Max (2026-08-17, per C-033) · **Domain:** GOV · **Author:** Claude · **Date:** 2026-08-17 · **Provenance:** C-108 (the flight tier and the registry release), seventeenth Code session — a standards-and-skills registry entry, distilled for beta-0.5 · **Document ID:** DOC-01M06JKXG00P9TT8TE3RJVMC6K (minted 2026-08-17 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · What a Scan is

A **Scan** is a whole-project adversarial review for loose ends *not explicitly stated* — contradictions, dangling references, present-tense claims that are false, undefined-but-relied-upon mechanisms, and drift in whatever the machine guards do not reach (the four instances' shared self-description; the moved-frontier thesis stated across Scans #2–#4: *drift lives in the checkers' declared blind spots*).

Its class is fixed by **C-058**: a Scan is a **canonical, sequential, dated artifact** — dated filename under `Context Packages/Conversations/`, canonical control header, DOC-minted at first commit (C-041), **never revised**. A review is a dated observation; revising it would destroy the record of what was true when (Scan #2 §7, the reasoning C-058 adopted). Corrections to a frozen Scan land in later Scans or in the Register's review-findings ledger — "frozen records stand; this row is their correction" (the S3-1.1 disposition, naming this the C-058 pattern).

A Scan is authoritative for **what was observed at its HEAD**, never for what should be done about it: findings are verified observations; fixes are proposals until an ordinary decision adopts them. A canonical review is never a control file (C-058, restating the C-019/C-024 discipline; every Scan banner carries this sentence).

## 2 · Commissioning

1. **A Scan is commissioned, never scheduled.** Every instance of record was fired by the commissioner's explicit request — "run at Max's request" (Scan #1), "declared canonical by him in the same breath" (Scan #2), "let's do the 3rd scan" (Scan #3), "run scan #4 now" (Scan #4). No calendar cadence exists anywhere in the history, and C-076 made the posture doctrine for the drill that rides the Scans: the trigger is owned by a commissioned ritual, "never a watched date (the S2-3.1 lesson applied forward)."
2. **The commission may carry a declared mandate.** Scan #4 was commissioned with one the series had not carried before — the pre-pack gate — and the mandate reshaped the instrument set (it brought the birth test, §7). A mandate is recorded in the banner; absent one, the Scan is the plain defect hunt.
3. **The commissioner chooses the executing surface.** Scans #1–#2 ran on an external read-only sandbox; Scans #3–#4 ran on the governing surface by Max's explicit call ("should we send codex or fable?" — Scan #3 banner). The choice is part of the commission and is recorded in the provenance line.

## 3 · Scope and method declaration

Every Scan declares, in its header block, the following — each item practiced since it first became declarable (Scan #1 predates the repository, the checkers, and the exclusion practice; the declarations accreted across the series):

1. **Baseline** — the previous Scan by filename and date (Scans #2–#4; Scan #1, having none, named its corpus instead).
2. **State scanned** — the version of every major living document, the store counts, the commit count, and the **HEAD hash** the observations bind to. "Line numbers refer to the files as of HEAD `…`" (Scan #2 method; repeated in #3 and #4).
3. **Method** — read-only over the full corpus, the live store, and the git repository; any exception recorded explicitly (Scan #4 recorded two: the in-session fix slate and the scratch-only births/drill).
4. **In-flight exclusions** — known mid-session state is enumerated up front and excluded from findings (Scan #4's *In-flight* note: the already-moved Global §2 and its known checker lags "enumerated below and excluded from findings").
5. **Guard state at start** — both checkers' status at scan start is recorded, so the findings are legible as what the machines did not catch. (Scan #3: "green at scan start and stayed green throughout"; Scan #4 ran its checkers *knowing the mid-session state* — two known hash-lags and known citation drift, enumerated as in-flight exclusions. Both shapes are conformant: the duty is recording the state, not being green.)

## 4 · Finding identity

Findings carry **stable ids `S<n>-x.y`** — `n` the Scan ordinal, `x` the section, `y` the finding within it (C-058: "findings carry stable ids (`S<n>-x.y`)"; practiced from Scan #2 onward; Scan #1 predates the grammar and was retro-classed as-is, its findings cited as `S1-x.y`). The id is minted in the Scan and never reused; it is the key under which the finding lives in the Register's ledger and by which later Scans, protocols, and decisions cite it (e.g. C-059 "addresses scan S2-3.1 / S2-3.3 / S2-2.5"). Sibling review series use their own prefixes in the same ledger (`CAP1-…` per the ledger's stable-ids header; `ST1-…` established by the Stranger Test #1 review banner and its ledger rows — the header itself lagged both `S4-` and `ST1-` until the seventeenth session's fix).

## 5 · Severity

Three grades, **High / Med / Low**, one per finding, stated inline with the finding. History defines them by consistent practice, not by definition; the practiced boundaries are:

- **High** — a load-bearing claim is false or a governance mechanism is broken: nothing is actually Ratified (S1-1.1), the substrate does not exist (S1-5.1), a projection overrides its source (S2-1.1), the close ritual has silently narrowed (S2-3.1), findings have no ledger (S2-3.2).
- **Med** — a living or authoritative surface is wrong, or a defect class has a structural cause with contained consequence: the custody flagship claim false as stated (S3-1.1), the generator lagging the document it executes (S4-2.1), the authoritative-for-supersession document carrying a superseded idea (S3-2.1).
- **Low** — presentation, hygiene, or prose currency where nothing load-bearing is false. The Scans argue their Lows explicitly and the standard adopts the argument as the test: "prose currency, not a broken path" (S3-3.3), "no custody guarantee is false" (S4-1.5), "presentation, not substance" (S4-1.4).

The headline reports the count by severity, in series context ("eight findings, none High (Scan #1: 26; Scan #2: 24)" — Scan #3; the series arc 26 → 24 → 8 → 7 is the trajectory every summary states).

## 6 · Evidence discipline

1. **Every finding is verified against its cited source file and line — never against any document's claim about it** (Scan #2 method, repeated verbatim in #3 and #4; the residue checks apply the same rule: "verified against sources, not against the ledger's claims," Scan #3 §6).
2. **Findings that do not reproduce are dropped** — and a disproved suspicion may be recorded as a non-finding instead (Scan #3 method: the suspected OQ-16 drop, "disproved by history — recorded as a non-finding").
3. **Each finding carries:** the id and a one-sentence claim in bold; **Severity**; **Where** (file, line); **Evidence** (live command output where the claim is about repo state); the **mechanism** — including *why the machine missed it* wherever a checker exists (the standing analysis of Scans #3–#4); and a **Fix** — a proposal, marked "landed" only when the slate call adopted it in-pass (§8).
4. **Non-findings are recorded.** Every Scan closes its observation half with a "Non-findings checked (verified consistent)" section — what was checked and found sound, stated as precisely as the defects (all four instances).

## 7 · The riding instruments

1. **The restore drill rides every Scan** (C-076: "a standing section of every canonical Loose-Ends Scan," plus an ad-hoc trigger on any custody or host change; no calendar cadence). The section reports the drill as a step/result table — clone, path-chain resolution, signers rebind, signature shape (`%G?` counts, per the S3-1.1 fix), both checkers in the fresh clone (Scan #3 §4, Scan #4 §4).
2. **The drill's scope boundary is stated in the section:** it proves the corpus rehydrates, verifies, and matches — structure and version-claim agreement — "it does not read prose for truth; that remains the Scans' half" (Scan #3 §4, the S2-3.4 boundary rule).
3. **Where a Scan gates a ship boundary, the birth test joins the drill as a standing section** — the drill proves the corpus *restores*; the birth proves it *reproduces* (Scan #4 §5, adopted with the full slate; its first run caught S4-2.1, which no checker could see).

## 8 · Dispositions and the fix slate

1. **The disposition set is `open` / `fixed` / `superseded` / `declined`** (C-058). A finding leaves the ledger **only by recorded disposition, never by omission** (C-058, extending C-034).
2. **Forward commitments stay Open.** A disposition whose fix contains a forward commitment ("at next reissue," "at next touch") stays **Open with that named trigger** — never Fixed on the promise; Fixed marks only what is done (the ledger practice note of record, adopted 2026-08-15 from the S3-2.2 class: a Fixed disposition's pending forward half regressed silently at exactly its named trigger).
3. **Grouped rows are permitted for Medium/Low volume** with per-row evidence in the frozen artifact; an item leaves a grouped row only by entering its own row with a disposition (the CAP1-MED practice in the same ledger).
4. **The fix slate is the commissioner's call.** At the Scan's close the proposed fixes are put to the commissioner; adoption may be per-item or whole ("Full slate" — Max's calls of record at Scans #3 and #4, in each case with any deliberately-held item recorded: S3-2.2 "open on its named trigger"). Fixes adopted in-pass land before the document freezes and their rows enter **Fixed in-pass**; everything not adopted enters **Open**. A third exercised mode sits between them (Scan #3): the slate adopted *at close* — the frozen seed table records its rows **Open**, the fixes land per the session's protocol after the document freezes, and the rows turn **Fixed in the Register's ledger only**; conformance is judged against the ledger, never against the frozen seed alone. An in-pass slate is recorded as a declared exception to the read-only method (Scan #4 method note).

## 9 · The report document

Distilled from the four instances, a Scan report is one file:

- **Filename:** `Review_<YYYY-MM-DD>_LooseEnds-Scan-<n>.md` under `Claude/Context Packages/Conversations/` (the series of record; Scan #1's un-numbered filename is grandfathered).
- **Identity:** `Fractal_LooseEnds_Scan_<n>`, v0.1, never revised; **Status** recording the in-conversation ratification and the slate call verbatim; **Reviewed By** Max with his calls quoted; **Document ID** minted at first commit via the close tooling (Scans #3–#4: `close.py --create`).
- **Banner:** class statement (canonical per C-058), commission quote, mandate if any, authority scope ("authoritative for what was observed … not for what should be done about it"), method summary, guard state at start.
- **Baseline / State-scanned block** (§3 above).
- **Summary:** the series trajectory, the headline severity counts, what held, and the thesis the findings share — said plainly, the good news first ("that is a real result and it should be said plainly before the findings below," Scan #2).
- **Thematic finding sections** (§6 grammar), ordered by theme, not severity.
- **The riding-instrument sections** (§7).
- **Worked analysis (optional):** a standing question carried to a decision-ready option set — explicitly *analysis, not a finding*; its disposition is the commissioner's call (Scan #3 §5, OQ-13 worked to options — the exercised precedent).
- **Residue:** every prior Scan's dispositions re-verified at their loci against sources (Scan #3 §6, Scan #4 §6 — this is how S2-2.2's silent regression was caught).
- **Non-findings checked.**
- **Disposition ledger seed** — the findings tabulated `ID | Finding | Sev | Disposition`, offered as the rows that enter the Register (every instance since Scan #2).
- **Footer:** Sources (exhaustive, at the scanned HEAD), Method (with recorded exceptions), Provenance (commission, surface, riding instruments), Revision history.

## 10 · Ledger integration

Every finding enters the Register's **cumulative review-findings ledger (C-058)** with a disposition, and leaves only by recorded disposition. The frozen Scan is the evidence; the ledger is where the finding *lives*: dispositions, corrections to frozen records, and held-open reasoning are ledger content, not document edits. The **next Scan verifies the ledger against reality** — residue rows are checked at their loci, and a regressed Fixed re-enters as a new finding (S2-2.2 → S3-2.2, the exercised precedent).

## 11 · Relationship to the flight container

Per **C-108**, the Scan is a **procedure** — a pluggable component of the ultracode flight, the container for governed programs of multiple coordinated flights. A Scan may run **standalone** (all four instances of record did, commissioned directly in-session) **or as a flight component**; in a flight, the flight standard's commissioning contract governs the container, and the Scan keeps every duty above — its own report, its ids, its ledger entry, its riding instruments where its mandate calls them. Conduct guards carry over unchanged: read-only method (C-091 class on reference surfaces), no silent scope growth, proposal-only landings (C-008; C-108's landing rules).

## 12 · The checker half

Per the Knowledge Network Foundation's rule (§5, welded limit 3: *"a standard without a checker is a norm, not a gate"*; §6: both halves, prose and checker, or it is a recommendation), registry entries ship prose + checker, versioned together (the C-040 coupling pattern). This entry ships **prose-first with the checker's trigger named**, as C-108 provides for the registry release. The checker's job, when built: validate a Scan report's conformance (filename grammar, control header fields, state-scanned block, id grammar, disposition-seed table present) and its ledger integration (every `S<n>-x.y` id in the report has a Register ledger row; no row left without a disposition). **Trigger: the first close that lands a Scan after this standard's ratification — Scan #5 does not close without it.** Design and canonization follow the C-060 lineage (a `check_versions.py`-family tool, red blocks).

---

**Refresh triggers (for the series, not this frozen version):** Scan #5's first execution under this standard contradicting a rule here; a change to the C-058 class or the C-076 cadence; the flight standard's ratification requiring a composition-mechanics update (§11).
**Sources:** Decision Register (C-058, C-076, C-108, C-034, C-041, C-040, C-091, C-008; the review-findings ledger header and its 2026-08-15 practice note); `Review_2026-08-12_LooseEnds-Scan.md`; `Review_2026-08-14_LooseEnds-Scan-2.md` (§7 — the class question C-058 answered); `Review_2026-08-15_LooseEnds-Scan-3.md`; `Review_2026-08-15_LooseEnds-Scan-4.md`; Fractal_Knowledge_Network_Foundation §5 limit 3 + §6 (the prose+checker rule); Max's ruling of record, seventeenth session (C-108: distilled from history, never invented).
**Revision history:** v0.1 (2026-08-17) first issue — the seventeenth session's registry distillation: the Scan procedure extracted from its four executed instances and their governing decisions; checker half named, not built.
