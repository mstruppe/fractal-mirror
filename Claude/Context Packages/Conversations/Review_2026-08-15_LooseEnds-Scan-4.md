# FRACTAL — Loose-Ends Scan #4 (the pre-pack gate)

> **CANONICAL — Claude-era review document (C-058 class).** A whole-project adversarial scan for loose ends *not explicitly stated*, commissioned by Max in the ninth Code session ("run scan #4 now") with a declared mandate the series has not carried before: **the pre-pack gate** — the sweep that stands between the completed foundation and the first shippable beta (his framing at session open: *"we have achieved the first big milestone … run a scan, then we're ready to pack fractal"*). Executed on the governing surface. It is authoritative for **what was observed on 2026-08-15 over the mid-session state at HEAD `395f414`**; it is not authoritative for what should be done about it — findings are observations, fixes proposals, and the fix slate below became binding through Max's in-conversation call (**"full slate"**), which landed all seven cures in the same session, before this document froze. Read-only over the full Claude-era corpus, the live store, the git repository, a fresh clone of the off-site copy (§4, the second Scan-riding restore drill per C-076), and — new to the series, the pre-pack mandate's own instrument — **two live births through `genesis.py`** (§5), the second the re-gate of the first's finding.
>
> **Second scan under full machine guard, first under a moved Global §2:** both checkers were run at scan start knowing the mid-session state (the C-090 documentation pass had already moved Global Context v0.3 → v0.4 and Register v0.36 → v0.37, so `verify.py` carried two known hash-lags and `check_versions.py` the known citation drift — enumerated in *In-flight* below and excluded from findings). Everything below was found where the machines do not look.

**Fractal_LooseEnds_Scan_4** · **Version:** 0.1 · **Status:** Ratified (2026-08-15, in-conversation per C-033/C-058 — commission "run scan #4 now"; slate call **"full slate"**, all seven cures landed in-session) · **Reviewed By:** Max (2026-08-15 — the "full slate" call) · **Updated:** 2026-08-15 · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Global Context · **Document ID:** DOC-01M03565AVDKG9DMRNXY9ZRY71 (minted 2026-08-15 via `close.py --create`, C-041/C-058; stamped by the post-mint revise)

**Baseline:** Scan #3 (`Review_2026-08-15_LooseEnds-Scan-3.md`, same day — sessions 5–9 all landed between the two) · **State scanned:** Protocol series v0.35 · Register v0.37 (mid-session; v0.36 at session open) · Rule Overview v0.30 · Conversation Settings v0.7 · Schema v0.6 · Template v0.5 · Navigation Contract v0.1 · Index v0.25 · Global **v0.4** (moved this session — the first realisation transition, OQ-4's first declared datum) · Local Context v0.50 · Architecture State v0.13 · BOOTSTRAP v0.16 · GENESIS v0.3 · `CLAUDE.md` v0.6 · `AGENTS.md` v0.7 · board stamp v0.50 · store 86 nodes / 468 events · 69 commits, HEAD `395f414`, tree clean, origin one commit behind (mid-session by design, C-064).

---

## Summary

Scan #3, this same morning, found eight findings and named the thesis: *drift lives in the checkers' declared blind spots.* Five sessions later — the instantiation program adopted and arc 1 executed, genesis and doctor landed, the punch list closed, the Cowork surface retired, the legal identity layer adopted — this scan finds **seven findings, none High** (the series: 26 → 24 → 8 → 7), and every one of Scan #3's cures holding. The eldest guard classes produced **zero** findings: ledgers arithmetically complete (C-001 → C-090, OQ-1 → OQ-32, no gaps, every row dispositioned), custody shape exact to the commit (30 `G` / 39 `N`, zero bad — the 38 pre-signing plus flight 4's one dated exception `598a21c`, its attestation the signed merge `17636e1` directly above it), no Cowork residue on any living surface, both checkers green in a fresh clone of the off-site copy, and the restore drill green at every step with a first: **the §4 rebind was machine-executed by `doctor.py --write`** — the sixth tool doing on a real clone exactly what it was built for, six hours after it merged.

The thesis therefore extends by one generation: **each new capability era is born outside the guard perimeter, and what drifts is precisely the artifacts the newest era added.** This era added a ship surface, a generator, and a legal layer — and the findings sit exactly there: the README one flight behind with its own refresh trigger fired unserved (S4-1.1); the close's own act-ordering writing store counts the close itself then falsifies (S4-1.2); and the sharpest specimen, **S4-2.1** — `genesis.py` carrying a private copy of the inheritance clause that froze at C-083 while `GENESIS.md` §3.4 moved to C-089, so that every newborn opened with a constitution clause under-claiming the very content its kernel documents carry. No checker could see it; the **birth test** (§5) caught it on the first run. The cure honors GENESIS §0's own rule — *where the two ever disagree this document wins* — by deleting the tool's copy entirely: the clause is now read from the document at run time, and the class (tool lags document) is structurally dead. The guard's own output was the last blind spot: 28 standing warnings, 22 of them stable noise, training every reader to skip the channel (S4-3.1) — cured by refining the heuristics, with the SUPPRESS list *shrinking* by one entry rather than growing by four.

Nothing found is dangerous; nothing is lost; every finding was cured in-session on the "full slate" call. The pre-pack verdict this scan was commissioned to render: **the foundation is ship-shape** — the kernel births clean instances, the off-site copy restores, custody verifies, and the corpus now carries one more rule than it did this morning for each way it was caught drifting.

---

## 1 · Currency drift — in the machine's blind spots

**S4-1.1 The README — the repo gate — is one flight behind, and its own refresh trigger fired unserved.**
**Severity:** Medium. **Where:** `README.md` map row ("the five tools (`verify.py`, `mint.py`, `check_versions.py`, `close.py`, `genesis.py`)"), the instantiation bullet ("`genesis.py`, the store's fifth tool"), and the stamp line, whose first-listed refresh trigger — *"a Global §2 realisation transition"* — fired this very session (Global v0.4).
**Evidence:** `doctor.py` merged as the sixth store tool at `17636e1` (the punch-list close); the README predates it by one session and was not touched at that close. The stamp's trigger fired hours before the scan with no refresh.
**Why the machine missed it:** the README is a derived projection outside the STRICT registry, and "five tools" is a *count*, not a version claim — the checker reads neither.
**Fix (landed, "full slate"):** one README pass — six tools in the map row; the ordinal dropped from prose (*ordinals are drift magnets* — the map row carries the inventory, prose should not); "where it stands" aligned to the new §2 (the first recorded realisation transition: ship it); the stamp records the same-day refresh.

**S4-1.2 Store-count claims were stale at birth: the close wrote the counts, then falsified them with its own store acts.**
**Severity:** Medium. **Where:** Local Context v0.50 §Current state and the Agenda Board (stamp v0.50) — both: "85 nodes / 454 events". **Actual at the same HEAD:** 86 nodes / 468 events (`stats.py`, `verify.py`, and `wc -l` agree).
**Mechanism:** the v0.35 close refreshed the Local Context (writing the counts), *then* minted the Protocol v0.35 DOC and appended the close's revise events — 14 events and one node after the number was written. The claim was false the moment the close commit landed. This is Scan #1's 174-vs-176 class recurring inside the machine-guarded era, because counts were the one numeric claim class no checker rule read.
**Fix (landed):** (a) `check_versions.py` gains the **count rule** — any "N nodes / M events" in living prose must match the store; frozen artifacts and versioned files are exempt by construction (their numbers were true at issue, C-040 — they supersede, never drift). First run caught both live instances (the checker's second first-run live catch, after C-060's own). (b) `/close` step 3 gains **counts last**: count claims are brought to `close.py --write`'s post-ripple totals, never written in step 2. (c) The live instances cure at this close's refresh — now under mechanical enforcement.

**S4-1.3 Frozen forward-pointers: two documents still said the drill's "next execution: Scan #3."**
**Severity:** Low. **Where:** BOOTSTRAP §4 ("(next execution: Scan #3)") · Rule Overview §5 ("(next: Scan #3)"). Scan #3 ran this morning; its drill rode it green.
**Why the machine missed it:** "Scan #3" is neither a version claim nor a path — a forward-naming parenthetical is invisible to every rule, and it froze the moment it was written (the S3-1.2 tolerant-zone family, one shade further out).
**Fix (landed):** both parentheticals dropped. The cadence is the rule (C-076); the Scans' own series is the execution record; naming the next instance invites exactly this staleness.

**S4-1.4 OQ-30's ledger cell still heads "Open —" — the resolution is appended at the tail.**
**Severity:** Low. **Where:** Register, OQ ledger — the cell opens "**Open — must be decided *before* the first key exists…**" and closes, six annotations later, "**RESOLVED (2026-08-15, C-087, per v0.35)**". Sibling rows resolved the same day (OQ-16/17/18) head with the resolution.
**Evidence of harm:** this scan's own first parse — a head-of-cell read — miscounted the standing OQs as ten; a human scanning the column does the same. The C-034 recorded-disposition rule is *satisfied* (the resolution is in the cell); the finding is presentation, not substance — which is why it is Low and was worth thirty seconds to fix.
**Fix (landed):** head re-marked **Resolved**, the original head preserved inside the cell as history.

**S4-1.5 Push-phrasing drift: two loci say the push rides "every commit"; the practiced, promoted ritual is push-at-close.**
**Severity:** Low. **Where:** Architecture State §5 ("the push riding every commit (C-056)") · Rule Overview off-site row ("every commit ends with `git push`"). C-064's promotion and ~15 sessions of practice: the push rides the **close**; mid-session commits sit unpushed by design — demonstrated at scan time by origin standing one commit behind. BOOTSTRAP §4 already carries the resolving clause ("executed … at close under standing authorization").
**Why it matters at Low:** no custody guarantee is false — the off-site copy is current at every close, which is the actual protection contract — but the S3-1.1 lesson is that custody prose must match the evidence exactly.
**Fix (landed):** both loci harmonized to rides-every-close, with the mid-session clause stated.

## 2 · The generator seam — the tool lagged the document it executes

**S4-2.1 `genesis.py`'s inheritance clause froze at C-083; GENESIS §3.4 says C-089; the ledger says C-090.**
**Severity:** Medium — the scan's sharpest specimen, and the one with ship-gate consequence.
**Where:** `genesis.py` `decision_register()` — a private string: *"…decisions C-001–C-083 … excluding the instance class (… C-078) and with the parameterized seven …"*. `GENESIS.md` §3.4 (v0.3, current at scan start): *"…C-001–C-089 … (… C-078, C-089) … the parameterized eight …"*.
**Evidence:** the §5 birth test. The newborn's Register opened with the C-083 clause: an under-inclusive range (its own copied kernel documents carry C-084–C-089 content — the Rule Overview's attribution row, the secrets row — that its constitution clause did not claim), an exclusion list missing C-089, and a parameter count two behind. The tool was written at flight 3, when the ledger ran to C-083; flight 4's brief touched genesis for manifests and registries but had no reason to touch the clause; two GENESIS reissues later, nothing had ever compared them.
**The structural finding:** the ledger numbers lived in **three places** — Register (source), GENESIS §3.4 (document), `genesis.py` (tool) — and the third had no currency tripwire of any kind: not the checker (a Python string is not a prose claim), not the close walk (the store-tools row fires on schema moves and tool changes, not on ledger growth), not the flights (a brief scopes what it names).
**Fix (landed, and re-gated):** the tool's copy is **deleted**. `genesis.py` reads the §3.4 blockquote from `GENESIS.md` at run time and refuses to birth if it cannot find it — GENESIS §0 already held the rule that decides the direction (*"where the two ever disagree this document wins"*), so the document is now the only copy, and the class (tool lags document) is structurally dead rather than patrolled. GENESIS reissued to v0.4 in the same pass (clause → C-090, the ninth parameter row, ledger numbers current — folding the C-090 ripple this close already owed it). **Re-gate executed (§5):** a second scratch birth after the fix — the newborn's clause is string-equal to the document's, `verify.py` PASS, `check_versions.py` PASS, 0 warnings.

## 3 · The guard's own output — the tolerated channel

**S4-3.1 The WARN channel was drowning in its own tolerance: 28 standing warnings, 22 of them two stable noise classes.**
**Severity:** Low. **Where:** `check_versions.py` output at scan start — **14** "named file exists nowhere" hits on `genesis.py` (code assembling filenames from string fragments: `_Global_Context.md`, `_Context_Index.md`, …); **8** "SKILL.md exists nowhere" hits on four living documents (BOOTSTRAP, Architecture State, Local Context, Board) that *correctly narrate* C-083 retiring the file **unbuilt** — named precisely because it must never exist. Plus ~6 genuine close-cured currency nudges, drowned.
**Why it matters:** warnings that never block and are 79% noise train every reader — human and machine-side alike — to skip the channel; the checker's own output had become a blind spot. (Scan #3 §non-findings read the channel and reported the count without reading the composition — this finding is that omission's correction.)
**Fix (landed; suppress handling per the "full slate" call):** the filename heuristic no longer reads `.py` sources at all (a code fragment is not a prose claim); the future-artifact line-context gains `retired|unbuilt` (a file narrated as deliberately never-built is history, not a claim) — and BOOTSTRAP §2.2's one keyword-less sentence now names the retirement inline. Net: the C-060 SUPPRESS list **shrank** by its one newly-dead entry instead of growing by four; the channel after the fix: **9 warnings**, all genuine and close-cured.

## 4 · The restore drill (standing section, C-076 — second Scan-riding execution)

Executed 2026-08-15 from a clean scratch directory against a fresh clone of `git@github.com:mstruppe/fractal.git`. **Result: green, every step.**

| Step | Result |
|---|---|
| Clone (SSH, custody credential) | **OK** — full history, HEAD `d844555` = origin (source one commit ahead mid-session, by design — C-064: the push rides the close) |
| BOOTSTRAP §1 chain + root protocols + `.allowed_signers` | **all 12 paths resolve** (11 at Scan #3; `GENESIS.md` has since joined the chain) |
| `doctor.py` report on the raw clone | **correctly ERRs** — repo-local signers binding unset, expected path printed |
| §4 rebind | **first machine execution:** `doctor.py --write` performed the rebind (BOOTSTRAP §4's hand command now has a tool executor); binding verified bound to the clone's own `.allowed_signers` |
| Signature verification in the clone | **29 `G` / 39 `N`, zero `B`/`E`/`U`** — source-at-that-HEAD exactly; the flight-4 dated exception (`598a21c` `N`) in shape, its custody attestation the signed merge above it |
| `verify.py` in the clone | **PASS** — 468 events / 86 entities / 0 collisions / 0 warnings |
| `check_versions.py` in the clone | **PASS** — 27 warnings (the pre-fix noise composition; the S4-3.1 cure landed after the drill ran and rides the close push) |

Datum for the record: the drill now exercises the sixth tool's core purpose on every future clone — `doctor.py` diagnosing and repairing the fresh-clone state it was built for, on the day it first could.

## 5 · The birth test (new section — the pre-pack mandate's instrument)

The mandate asked whether the kernel a stranger receives actually works. The only honest instrument is the one GENESIS §0 names as its acceptance test: **birth an instance and check it**. Executed twice.

**Birth 1 (`Probe`, pre-fix):** `genesis.py --write` into session scratch. Newborn complete — kernel copies, parameterized spine, empty store with root mints (19 events / 12 entities / roots `AGENT`, `FACET`, `PRB`), `.inherited` manifest + `.version-registry` (the C-088 machinery), secrets-layer `.gitignore` (C-087), adapter + `/orient` command (C-083 unit), initial commit authored and committed by the operating AI (C-084 — the operator's instruction is the grant). **Gates:** `verify.py` PASS (the C-081 gate); `check_versions.py` PASS with **116 upstream citations exempted (INHERITED, C-088)** — the first independent re-execution of the flight-4 machinery since its gate, green. **And the catch:** the inheritance clause read **C-001–C-083** → finding S4-2.1.

**Birth 2 (`Probetwo`, the re-gate):** after the fix — clause string-equal to GENESIS §3.4 (C-001–C-090, exclusions current, "the parameterized nine"), `verify.py` PASS, `check_versions.py` PASS, **0 warnings**.

**Proposal adopted with the slate:** where a Scan gates a ship boundary, the birth test joins the drill as a standing section — the drill proves the corpus *restores*; the birth proves it *reproduces*. Two different survivals, and the second is the one a stranger meets first.

## 6 · Residue, and the in-flight state (recorded, not findings)

**Scan #3 slate:** all 7 Fixed dispositions verified holding at their loci (BOOTSTRAP §4 `%G?` drill shape · Rule Overview §5 version-agnostic · store README six tools + Contract pointer · AST §4 C-068 posture · commands stamped, `.claude/commands/` walked · AGENTS never-edit list current at v0.7 · BOOTSTRAP §2 command tier). **S3-2.2 stands open by design** — unchanged trigger (each spec's next real reissue), untouched by this scan on its own recorded grounds.

**In-flight at scan close, cured by the session's close by design:** 6 `verify.py` hash-lags (Global, Register, Rule Overview, AST, BOOTSTRAP, GENESIS — this session's edits awaiting their `close.py --write` revises); the Local Context's citation/count/checklist drift against this pass's reissues (26 checker errors, all one class — the v0.51 refresh rewrites them, the count rule now enforcing two of them); the Register's C-090 group header naming its protocol ahead of issuance (cures when the protocol lands at close); origin one commit behind (the close push carries everything). **Transient, no action:** one `~$` Word owner-file at root — the notebook is open in Word; gitignored, vanishes on close (the S2-6.3 class, correctly latent).

**Non-findings checked (verified consistent):** OQ-30 is genuinely resolved — the cell's tail carries the full C-087 disposition (the head was S4-1.4); the Site (`Site/fractal-site.html`) is claim-light by design — no tool arithmetic, no count claims, `verify.py`-as-gate correct per C-081; ledgers arithmetically complete (C-001 → C-090 no gaps; OQ-1 → OQ-32 all dispositioned, **nine standing** + OQ-4 carrying its first declared datum from this session; review ledger fully dispositioned but S3-2.2); committer patterns conformant per C-084 including the recorded `da75638` authorship error (C-084's own origin — history unrewritten, by design); `doctor.py` PASS on the source repo (secrets guard: ignore entries present, no likely values in tracked files); Knowledge Network Foundation v0.1 conformant to its C-086 class (Draft, non-binding, provenance line); Conversation Settings v0.7 coherent with the C-089 scope; `.gitignore` carries the C-087 secrets layer; no `drone/*` branches (C-075 holding); Index v0.25 rows current (six tools, GENESIS v0.3-at-scan-start — moves with the close).

## Disposition ledger (seed — entered in the Register at v0.38, all rows Fixed in-pass)

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| S4-1.1 | README one flight behind; its own §2-transition refresh trigger fired unserved | Med | **Fixed** in-pass ("full slate") |
| S4-1.2 | Store-count claims stale at birth (85/454 vs 86/468); close wrote counts before its own store acts | Med | **Fixed** in-pass — count rule + counts-last step; live instances cure at this close under enforcement |
| S4-1.3 | Frozen "next: Scan #3" parentheticals (BOOTSTRAP §4, Rule Overview §5) | Low | **Fixed** in-pass |
| S4-1.4 | OQ-30 cell heads "Open —", resolution at tail | Low | **Fixed** in-pass |
| S4-1.5 | Push wording "every commit" vs practiced push-at-close (AST §5, Rule Overview) | Low | **Fixed** in-pass |
| S4-2.1 | `genesis.py` inheritance clause frozen at C-083 vs GENESIS §3.4 at C-089 (ledger C-090); three copies, no tripwire | Med | **Fixed** in-pass — tool copy deleted, run-time read of the document; GENESIS → v0.4; re-gated by birth 2 |
| S4-3.1 | WARN channel 79% stable noise (28 standing, 22 in two classes) | Low | **Fixed** in-pass — heuristics refined, SUPPRESS shrank; channel at 9, all genuine |

---

**Sources:** the full Claude-era corpus at `Desktop/FRACTAL/` as of 2026-08-15, HEAD `395f414` — every document named in the State-scanned line, read at that state; the live Knowledge Graph Store and fresh runs of `verify.py`, `check_versions.py` (pre- and post-fix), `stats.py`, `doctor.py` (source repo, raw clone, and `--write` on the clone); the git repository (status, branches, remote, full log with `%G?` under the repo's `.allowed_signers` binding); `.claude/commands/fractal.md` + `close.md`; `.gitignore`; `README.md`; `Site/fractal-site.html`; BOOTSTRAP v0.16→v0.17; GENESIS v0.3→v0.4; the §4 drill's fresh clone of `mstruppe/fractal`; the §5 births (`Probe`, `Probetwo`) in session scratch.

**Method:** read-only over the repository, with two deliberate exceptions recorded here: (1) the ratified fix slate (Max: "full slate") landed in-session before this document froze — the reissues are enumerated in the Register v0.38 entry; (2) the §5 births and the §4 drill wrote only to the session scratchpad and a fresh clone, never to `Desktop/FRACTAL/`. Every finding was verified against its cited source at HEAD `395f414` and against live command output; the OQ-30 head misread was caught by re-reading the full cell and demoted from a resolution-integrity finding to the presentation finding S4-1.4 — recorded as the method working, not the ledger failing.

**Provenance:** FRACTAL whole-project loose-ends scan #4, 2026-08-15, commissioned by Max in the ninth Code session ("run scan #4 now") as the pre-pack gate; executed by the governing surface (Fable), carrying the second Scan-riding restore drill (C-076) and the series' first birth test (§5). Canonical per the C-058 class: sequential, dated, DOC-minted at commit, never revised.

**Revision history:** v0.1 (2026-08-15) first issue — 7 findings (3 Medium, 4 Low, 0 High; the series' smallest) across ship-surface currency, the generator seam, and the guard's own output; full slate fixed in-pass on Max's call; second Scan-riding drill green with the first machine-executed §4 rebind (`doctor.py --write`); first birth test executed (catch → fix → re-gate green, 116 INHERITED exemptions verified); Scan #3 residue 7/7 holding, S3-2.2 open by design; disposition ledger seeded all-Fixed.
