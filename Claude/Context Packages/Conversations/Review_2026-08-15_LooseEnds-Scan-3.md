# FRACTAL — Loose-Ends Scan #3

> **CANONICAL — Claude-era review document (C-058 class).** A whole-project adversarial scan for loose ends *not explicitly stated*, run at Max's request ("let's do the 3rd scan"), executed on the governing surface by his call ("should we send codex or fable?" — Fable: a Scan is the review layer itself, and this one carries the custody drill). It is authoritative for **what was observed on 2026-08-15, over the post-custody state at HEAD `98e2952` (2026-08-14)**; it is not authoritative for what should be done about it. Each finding is a verified observation with a proposed fix; the fix becomes binding only through an ordinary decision. Read-only over the full Claude-era corpus, the live store, the git repository, and — new this scan — a fresh clone of the off-site copy (§4, the first Scan-riding restore drill per C-076).
>
> **First scan under full machine guard:** both checkers (C-050/C-060) were green at scan start and stayed green throughout. Everything below was found where the machines do not look.

**Fractal_LooseEnds_Scan_3** · **Version:** 0.1 · **Status:** Ratified (2026-08-15, in-conversation per C-033/C-058, per Protocol v0.29 — findings stand as observations; fixes were adopted where v0.29 says so: the full slate, S3-2.2 open on its named trigger) · **Reviewed By:** Max (2026-08-15, per v0.29 — surface call "go", OQ-13 call "OQ-13 A", slate call "Full slate") · **Updated:** 2026-08-15 · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Global Context · **Document ID:** DOC-01M01883670AE5M59QKNDGKX81 (minted 2026-08-15 via `close.py --create`, C-041/C-058 — the hardened `MINTED:` flow's first live use)

**Baseline:** Scan #2 (`Review_2026-08-14_LooseEnds-Scan-2.md`, 2026-08-14) · **State scanned:** Protocol series v0.28 · Register v0.26 · Rule Overview v0.24 · Conversation Settings v0.6 · Schema v0.6 · Template v0.4 · Navigation Contract v0.1 · Index v0.20 · Global v0.3 · Local Context v0.39 · Architecture State v0.7 · BOOTSTRAP v0.13 · `CLAUDE.md` v0.3 · `AGENTS.md` v0.3 · board stamp v0.39 · store 75 nodes / 362 events · 54 commits, HEAD `98e2952`, clean, in sync with `origin/main`.

---

## Summary

Scan #1 found promised mechanisms; Scan #2 found the prose layer drifting wherever no machine checked it, and the project answered with `check_versions.py`, the C-059 checklist, and the C-058 ledger. This scan is the first run over a corpus that is machine-guarded end to end — and the result is the smallest findings list of the series: **eight findings, none High** (Scan #1: 26; Scan #2: 24). The ledgers are arithmetically complete (C-001 → C-076, OQ-1 → OQ-27, no gaps), every conversation since C-059 closes with a Return Package and a protocol or a recorded reason, the drone branches are gone as C-075 prescribes, both checkers pass in the source *and* in a fresh clone of the off-site copy, and the restore drill rode a Scan for the first time and came back green (§4). That is the headline, and it is a good one.

The failure mode has moved again, and again predictably: **drift now lives exactly in the checker's declared blind spots.** Five of the eight findings sit where `check_versions.py` by design does not look — tolerant-class body text (S3-1.2), filename tokens (S3-1.3a), absence-of-claim rather than stale-claim (S3-1.3b/c, S3-2.2), a tree outside the walk entirely (S3-3.1), and adapter *content* behind a stamp the checklist walks only as a stamp (S3-3.2). The sharpest specimen is S3-1.1: the custody session's flagship claim — *"the whole history verifies `G`"* — is **false as stated**, and the mechanism is visible in the protocol's own text: a correctly *scoped* evidence line ("every commit … since the C-066 arming") was generalized into an unscoped conclusion four sentences later. 38 of 54 commits predate signing and can never be signed without rewriting history — which the project rightly forbids. The truth is strictly better than the claim: every commit that *can* verify does, with zero bad or unknown signatures — but a custody layer is exactly where the words must match the evidence, and the fix makes the claim machine-checkable so the drill carries it forward (§4).

Nothing here is dangerous; nothing is lost; no finding survives one ordinary close. The pattern worth naming is the third-generation lesson: **each guard, once built, defines the next drift surface at its own boundary.** Scan #2's cure was to mechanize verification; this scan's proposals are mostly about *scope* — widen the walk to `.claude/`, sharpen one claim into a checkable expectation, and put a tripwire on the two remaining unguarded currencies (adapter content, disposition forward-commitments).

---

## 1 · Currency drift — in the machine's blind spots

**S3-1.1 The custody layer's flagship claim is false as stated: "the whole history verifies `G`."**
**Severity:** Medium. **Where (living):** `Fractal_Decision_Register.md` line 255 (C-074c: "the whole history verifies `G`") · `Fractal_Rule_Overview.md` line 52 (protection-model row: "the whole history checks `G`") · Local Context lines 7, 23, 30 ("the whole history now verifies `G`", "whole history `G`", "history-wide `G` confirmed"). **Where (frozen, for the record):** Protocol v0.28 lines 3, 20, 26, 38; Custody Return Package §2/§3.
**Evidence:** `git log --format='%G?'` over all 54 commits, with the repo's own `.allowed_signers` binding: **16 `G`, 38 `N`, zero `B`/`E`/`U`.** The boundary is exact and clean — every commit from `b043982` (the first drone write, where the C-057 trigger fired) onward verifies `G`; every commit before it carries no signature, *necessarily*: they predate `commit.gpgsign`, and signing them retroactively would rewrite history (forbidden, C-037). Reproduced identically in the fresh clone (§4).
**Mechanism:** Protocol v0.28 §2 states the evidence correctly scoped — "every commit … carries an SSH signature (`commit.gpgsign=true` **since the C-066 arming**)" — and §3/§4/§6 restate it unscoped ("the whole history verifies `G`"; "historical verification confirmed `G` across the log"). The likely instrument: `git log --show-signature` prints Good-signature blocks for signed commits and *nothing* for unsigned ones — absence of errors reads as `G`-everywhere. `%G?` prints the truth per commit.
**What is actually true (and is strictly the better custody statement):** *every signed commit verifies `G` against the in-repo signers file; zero bad, unknown, or unverifiable signatures exist anywhere; the 38 pre-signing commits are unsigned by design — evident, preserved, unsignable without rewriting; the signing boundary (`b043982`, 2026-08-14) is itself part of the custody record.*
**Fix:** (a) reword the three living loci to the scoped statement (Register row annotation; Rule Overview row; Local Context at its next bump); frozen records stay frozen — this ledger entry is their correction, per the C-058 pattern. (b) Make the claim machine-checkable where the custody checklist lives: one line in BOOTSTRAP §4 — `git log --format='%G?' | sort | uniq -c` with the expected shape (all commits since `b043982` = `G`; zero `B`/`E`/`U` anywhere; earlier = `N` by design) — so every future drill (§4 cadence, C-076) verifies the *claim*, not just the mechanism. The next signing-era commit shifts the counts, never the shape.

**S3-1.2 The Rule Overview's §5 ledger pointer is one close behind — in the tolerant zone the checker deliberately doesn't guard.**
**Severity:** Low. **Where:** `Fractal_Rule_Overview.md` line 92: "Full open-question ledger: **Decision Register v0.25**, OQ-1–OQ-27 …" — the Register stamps **v0.26** (the custody postscript bumped it; the Rule Overview's own v0.24 postscript entry updated the revision history but not the §5 pointer).
**Why the machine missed it:** the Rule Overview is a **tolerant**-class source (C-060) — currency is enforced on Sources / Normative-home lines only; §5 is body text. The claim is attributable and wrong, and by design it neither errors nor warns. First observed specimen of drift *inside* the machine-guarded era's tolerance zone.
**Fix:** the pointer is already version-agnostic everywhere else in the document ("Decision Register (stamp inside, C-012)" in Sources) — apply the same C-012 stamp-inside cure to the §5 line and the churn class ends here, as it did for BOOTSTRAP (S2-1.4) and the adapters.

**S3-1.3 The store README — the hand-author's front page — is three closes stale in three ways.**
**Severity:** Medium. **Where:** `Claude/Knowledge Graph Store/README.md` lines 4, 12–13, and the trace section (~line 63).
- **(a)** Line 4: "Format spec: `…/Fractal_Node_and_Event_Schema_v0.5.md`" — the Schema is at **v0.6**. The pointer hides in a *filename token*, and the superseded file legitimately exists on disk (C-061 keeps every version), so the path pass is green and no version claim is attributed — the exact blind-spot class the Navigation close already met (`CLAUDE.md`'s "(v0.4 inside)", cured version-agnostic there). A rehydrating hand-author lands on a spec that predates the Navigation Contract registration and the in-spec C-061 documentation.
- **(b)** Lines 12–13: "`verify.py` / `mint.py` / `check_versions.py` — the canonized tools (C-050, C-060)" — **`close.py` is missing** (canonized C-073, the fourth tool; it sits in the same directory the README fronts).
- **(c)** The "Trace by hand" section teaches the grep ritual with **no pointer to the Navigation Contract** — since C-070 the grep tier is a *derived realisation checked against that contract*, and the store's own front page doesn't name it. Zero occurrences of "Contract" or "close.py" in the file.
**Why the machine missed it:** (a) filename token; (b)/(c) are absences — the checker verifies claims that exist, not claims that should.
**Fix:** one README pass — spec pointer version-agnostic or → v0.6; the fourth tool on the tools line; one sentence heading the trace section ("the read ritual below implements the Navigation Contract — the contract is canonical, this is the zero-infra tier"). Rides any store-touching commit.

## 2 · Supersession & spec hygiene

**S3-2.1 The Architecture State still recommends the interface direction that C-068 dissolved.**
**Severity:** Medium. **Where:** `Fractal_Architecture_State.md` line 40 (§4, second bullet): "The near-term interface direction is client-side and thin: **entry-point DOC nodes** opened via custom instructions / the client adapter (roadmap item H in the Local Context) …"
C-068's decision of record: *"No entry nodes, no home screen; the default lobby (`FACET`) is client configuration. The WS 'entry-point nodes' idea dissolves into UI defaults over this rule."* The v0.6 reissue (per v0.24) carried the supersession into §2 — the navigation line is there and correct — but §4, the WS section the supersession most directly touches, kept the pre-C-068 language. Its cross-pointer compounds it: "roadmap item H" no longer contains an entry-point item (H reads "entry settled per C-068; what remains is rendering"). This is S2-1.2's little sibling: the document *authoritative for supersession* carrying a superseded idea as current direction, in the one section a future WS-forge reader will open first.
**Fix:** AST v0.8, §4 bullet rewritten to the C-068 posture (entry is settled as a query shape; near-term = rendering `enter` spatially and `trace` as navigation, client-side; the lobby is client configuration). Two sentences.

**S3-2.2 The `Reviewed By` commitment from Scan #2 regressed at its own trigger: Schema v0.6 and the Navigation Contract carry no such field.**
**Severity:** Low. **Where:** `Fractal_Node_and_Event_Schema_v0.6.md` line 5 · `Fractal_Navigation_Contract_v0.1.md` line 5 — full control headers, no `Reviewed By`; Template v0.4 has one.
The S2-2.2 disposition (Register, review-findings ledger): "versioned artifacts add it at next reissue (Template v0.4 does; **Schema at its next reissue**)." The Schema's next reissue *was* v0.6 (C-070, 2026-08-14) — the field was not added; the Contract was born in the same close without it. Nothing false is asserted (both Status fields record ratification correctly); what failed is the *forward half of a Fixed disposition*, silently, at exactly its named trigger.
**Class note (the structural point):** a disposition marked **Fixed** can contain a commitment that only executes later; nothing watches those. This is the disposition-ledger sibling of S2-3.1 — "Fixed" reads as done while a fragment is still pending. Candidate cure: forward-dated halves of dispositions get their own OQ row or a named-trigger annotation instead of riding inside a Fixed mark.
**Fix:** add the field at the next reissue of each (no out-of-cycle churn — the omission is cosmetic); adopt the class note as ledger practice.

## 3 · The ungoverned edge — artifact classes the guards don't reach

**S3-3.1 The command tier is recorded as "stamped-procedure projections" — but neither file carries a stamp, and `.claude/` is outside every machine guard.**
**Severity:** Medium. **Where:** `.claude/commands/fractal.md` · `.claude/commands/close.md` (tracked, ship with every clone) · `check_versions.py` scope rule (three root files + `Claude/**` — `.claude/` is not walked; case-sensitive prefix excludes it) · First-Code-Session RP Postscript 5 and Navigation-Close RP Postscript 4 (the class naming: "a **stamped**-procedure projection", twice).
Both files are behavioral instruction surfaces the governing session executes verbatim — the same auto-loaded class C-065 canonized `CLAUDE.md` for — yet: no version stamp naming source + date (the C-035 discipline their own recorded class invokes); no identity; no checker coverage of their referenced paths or (absent) claims; and `fractal.md` line 7 hard-codes the active Local Context filename — a duplicate of the Index's routing datum, the "one place routing is maintained" (C-012), mitigated only by its "named in the Index — currently" phrasing. `close.md` half-conforms already (it carries its own refresh triggers and points to normative homes rather than copying them).
**Fix (a deliberate call either way):** *either* stamp both files (source + date, exactly the adapter pattern) and extend the checker walk by one line (`rel.startswith(".claude/commands/")` — path pass and stamp discipline come free), *or* re-class them by record as deliberately unstamped thin orchestrators and still extend the walk (the path references deserve existence checks regardless). The first option matches what the RPs already call them.

**S3-3.2 The drone adapter's content is frozen at v0.1 while the doctrine moved twice — its forbidden-paths list predates the custody layer it now operates under.**
**Severity:** Medium. **Where:** `AGENTS.md` line 9 (rule 1, the never-edit list) and revision history (v0.2/v0.3 explicitly "stamp-only").
The never-edit list — `Claude/Project Governance/**`, `Claude/Context Packages/**`, store `_events/**`+`nodes/**`, `BOOTSTRAP.md`, `CLAUDE.md`, itself, `Archive/**` — was authored at C-066, before the repo grew **`.allowed_signers`** (C-074: the custody layer's verification trust anchor), **`.claude/commands/`** (the governing surface's own behavioral files), and before **C-075** pinned the branch lifecycle (a drone reading its adapter doesn't learn its branch dies after merge — mildly relevant to "resume" behavior). A drone editing the signers file or a command file would violate no line of its adapter; the protections that remain are the brief-scope rule and the governing surface's diff review — real, but the list is the defense-in-depth layer, and it went stale.
**Structural cause (the finding under the finding):** `AGENTS.md`'s own refresh triggers name "a change to the drone doctrine (C-066)" — C-075 *extends C-066* and fired that trigger with no re-projection; nothing caught it because **the C-059 adapter row walks stamps, not content**, and stamps only move when *Settings* moves. Adapter content that compresses non-Settings doctrine (the drone rules) has no currency tripwire at all.
**Fix:** at the next re-projection: add `.allowed_signers`, `.claude/**`, `.gitignore` (and arguably the store tools `*.py`, absent a brief that names them) to rule 1; one lifecycle clause in rule 3 or 6 ("the governing surface deletes your branch after merge — every brief starts fresh"). Structurally: widen the C-059 adapter row's question from "stamps current?" to "stamps current *and* content conformant with doctrine decided this close?" — one clause in the checklist row.

**S3-3.3 BOOTSTRAP's adapter section doesn't know the command tier exists.**
**Severity:** Low. **Where:** `BOOTSTRAP.md` §2.2 ("Claude — skill / plugin tier (**queued, not yet built**) … Until built, §2.1 is the adapter") and §2.1's Claude Code paragraph ("the file is the whole adapter").
The project's own records count **three landed slices of the OQ-16 skill tier** — `/fractal` ("first concrete slice", First-Code RP P5), `close.py` (mechanics), `/close` ("third slice — open · mechanics · close", Navigation RP P4) — and BOOTSTRAP's §2.2 status line still reads fully queued. No rehydration gap results (the commands are tracked files: a clone carries them, Claude Code auto-discovers them — nothing to install), which is why this is Low: it is prose currency, not a broken path. But §2's job is exactly this story, and its refresh trigger ("the skill/plugin tier landing") has half-fired three times.
**Fix:** one clause in §2.1 ("…the file is the whole adapter, plus the tracked `.claude/commands/` pair — `/fractal` opens, `/close` closes — which ship with every clone") and §2.2 reworded to "partially landed: three slices; the full SKILL.md unit remains queued (OQ-16 untouched)."

## 4 · The restore drill (standing section, C-076 — first Scan-riding execution)

Executed 2026-08-15 from a clean scratch directory, per BOOTSTRAP §1/§4 and the S2-3.4 content-check rider. **Result: green, every step.**

| Step | Result |
|---|---|
| Clone `git@github.com:mstruppe/fractal.git` (SSH, custody credential) | **OK** — full history |
| HEAD parity vs source | **exact** — `98e2952` both sides (byte-parity by git content addressing) |
| History unbroken to baseline | **OK** — `a9daa6f` (2026-08-12 `[GBL]` snapshot) reachable, 54 commits |
| BOOTSTRAP §1 chain (Global → Index → Local Context → Rule Overview / Settings / Register → store log), plus root adapters + `.allowed_signers` | **all 11 paths resolve** |
| §4 layer-3 rebind on the fresh clone (`git config gpg.ssh.allowedSignersFile <clone>/.allowed_signers`) | **works exactly as documented** — one command |
| Signature verification in the clone | **16 `G` / 38 `N` / zero `B`·`E`·`U`** — identical to source; every signed commit verifies against the in-repo signers file |
| `verify.py` in the clone | **PASS** — 362 events / 75 entities / 0 collisions / 0 warnings |
| `check_versions.py` in the clone (the content check riding the drill, S2-3.4 → first exercised) | **PASS** — every attributable claim agrees |

Two datums for the record: **(1)** the §4 rebind step, written for a stranger, was exercised by one for the first time — it is sufficient as written. **(2)** The drill's signature step is what surfaced S3-1.1's evidence: the drill now *measures* the custody claim, which is precisely what C-076 wanted the cadence for. If S3-1.1's fix (b) lands, every future drill checks the claim's shape mechanically.

Scope boundary (S2-3.4, restated): the drill proves the corpus rehydrates, verifies, and matches — structure and, since this run, version-claim agreement. It does not read prose for truth; that remains the Scans' half, exercised in §§1–3 above.

## 5 · OQ-13, worked (rides this scan by disposition)

**The question (Register, v0.2 §11 sweep):** "Normalise remaining grandfathered `_v0.1` filenames to versionless names?" — Open, deferred; grandfathering (C-012) holds.

**The population is exactly three** (living documents whose filename carries a frozen `_v0.1` while the version lives inside): `Fractal_Global_Context_v0.1.md` (internal v0.3) · `Fractal_Context_Index_v0.1.md` (internal v0.20) · `Fractal_Conversation_Settings_v0.1.md` (internal v0.6). *(Foundation v0.1 and Navigation Contract v0.1 are genuinely at v0.1 — versioned-artifact class, correctly named; every other living doc is already versionless.)*

**What binds the names (measured):** ~36 in-scope files reference them — Global 10 (3 frozen, 1 store node) · Index 14 (**8 frozen**, 1 store node) · Settings 12 (4 frozen, 1 store node). Plus: `check_versions.py`'s LIVING registry hard-codes all three paths; the three DOC node bodies record them (C-041); `CLAUDE.md`, `AGENTS.md`, `.claude/commands/fractal.md`, and BOOTSTRAP §1 walk them by name.

**Option A — keep, and resolve the OQ with a named trigger (recommended).** Grandfathering is already a ratified, labelled mechanism (C-012); the stamp-inside rule is how every living doc works; the suffix costs one recurring parenthetical. Renaming's one real gain — first-contact readers not misreading `_v0.1` as "version 0.1" — has no audience yet: every current reader (Max, Claude, Codex) resolves through the Index. Resolution: **keep; the rename question re-fires at the first public-facing boundary** (public flip or curated mirror, C-056's sharing branch; or the OQ-16 shipping/packaging pass — whichever first), as an ordinary decision then. This moves OQ-13 from open-deferred limbo into the fire-on-trigger class, per the robust-ordering method and the OQ-26 precedent (resolve now, future rungs fire from named triggers).
**Option B — rename now** (`git mv` ×3 → versionless). Full cost, measured: ~18 living-file edits (checker-verified), 3 node-body path updates + 3 `revise` events (`verify.py` red until done — it hashes external canonicals at their recorded paths), `check_versions.py` registry edits, adapter/command/BOOTSTRAP sweeps — one heavy but mechanical close. The unfixable part: **15 frozen files** (protocols, RPs, Scan #2 among them) would permanently cite filenames that no longer exist — the frozen layer's pointers become false forever, and the checker's existence pass needs either 3 standing SUPPRESS entries (Max-ratified, "stays short") or a basename-tolerance carve-out. Gain: naming consistency; the parenthetical dies.
**Option C — leave the OQ open as-is** (status quo; costs nothing, decides nothing, carries forever).

**Decision pending Max** — recorded here as analysis only (C-058: fixes are proposals). Severity of the underlying issue: none — nothing is false today; C-012's label does exactly what it says.

## 6 · Residue from Scans #1 and #2

Verified against sources, not against the ledger's claims: **S1 both holding** (1.5: Foundation §2 + Sources cite the ChatGPT-era lineage correctly · 2.4: `Templates/` gone). **S2: 25 of 26 holding** — spot-verified across classes: Foundation status field (2.1) ✓ · BOOTSTRAP §0 pre-canon label (6.1) ✓ · version-agnostic normative homes (1.6) ✓ · the C-058 ledger live and complete (3.2) ✓ · checklist walked with per-row marks every close since (3.1) ✓ · RP↔protocol pairing unbroken v0.17–v0.28 (2.5) ✓ · `_to_delete/` and owner-files gone (6.2/6.3) ✓. The 26th — **S2-2.2 — regressed in its forward half** at its named trigger and re-enters as S3-2.2.

## Non-findings checked (verified consistent)

- **Both checkers PASS** at source and in the fresh clone: 362 events / 75 entities / 20 codes / 7 roots / 50 route tokens / 0 redirects / 0 collisions / 0 warnings; every attributable version claim agrees (155 files, 1530 claims).
- **Git:** clean tree, `main` = `origin/main` (0/0); **no `drone/*` branches anywhere** — C-075 executed and holding; remote SSH as recorded.
- **Committer patterns all conformant** per C-074a (Claude→Max, Codex→Max, Codex→Codex, Claude→Claude all present in history; the field is mechanical, exactly as pinned).
- **`.allowed_signers` well-formed:** three principals over the one custody key, self-documenting header, repo-local binding present; matches C-074c as executed.
- **Ledgers arithmetically complete:** C-001 → C-076 no gaps; OQ-1 → OQ-27 no gaps, every row dispositioned; review-findings ledger: all 28 rows dispositioned (fully green at scan start).
- **Every conversation since C-059 pairs RP + protocol or recorded reason** — First-Code-Session (v0.20–v0.23 + two execution-only postscripts), Navigation-Close (v0.24–v0.27 across four postscripts), Custody-Close (v0.28 + postscript). The S2-2.5 class is structurally cured in practice.
- **Store counts exact everywhere:** the RP chain's running totals (330 → 340 → 349 → 359 → 362) reconcile with the log to the unit; Local Context, board, and `stats.py` agree (75/362).
- **Board current:** stamp v0.39, agenda content matches the Local Context (custody session + Scan #3 pencil present).
- **Settings v0.6 coherent** across §2/§3/§5/§6; both root adapter stamps current at v0.6 (machine-checked); the Cowork field stamp is **unverifiable from this surface** (vendor-held — recorded as pasted-verbatim and confirmed, Navigation RP P3; the C-059 adapter row remains its only walk).
- **Architecture State §5's custody sentence** — "custody is layered and evident-and-reversible (C-057)" — verified still true under the C-074 pins, exactly as the custody close marked it (the close's judgment held; §4's entry-point bullet is S3-2.1, a different section).
- **`close.py` hardening present** as recorded (dry-run ids labelled illustrative; `MINTED:` printed last on `--write --create`) — the postscript's cure verified in code.
- **No stale `/open` references** (the rename's only trace is the frozen RP that records it). **Hygiene clean:** no strays at root, no `~$*`, no `_to_delete/`; `.gitignore` = OS/app noise + `.claude/settings.local.json` (correctly local — session settings are not knowledge).
- **The midnight-crossing commits** (52–54, 00:07–00:22 +0200) remain 2026-08-14 in UTC — every document's "2026-08-14" date and every store ULID stay coherent; no finding.
- **OQ-16's absence from the Local Context's G list is deliberate** (it rides the H roadmap's shipping-tier line, where its dissolution actually lives); the Register carries the open row — no drift.

## Disposition ledger (seed — enters the Register per C-058)

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| S3-1.1 | "Whole history verifies `G`" false as stated (16 G / 38 N); scoped truth generalized; fix = reword living loci + machine-checkable drill expectation | Med | Open |
| S3-1.2 | Rule Overview §5 cites Register v0.25 (at v0.26) — tolerant-zone body text | Low | Open |
| S3-1.3 | Store README: Schema v0.5 pointer (filename token) · `close.py` missing from tools line · no Navigation Contract pointer in trace section | Med | Open |
| S3-2.1 | Architecture State §4 still carries "entry-point DOC nodes" — dissolved by C-068; supersession not carried into the affected section | Med | Open |
| S3-2.2 | Schema v0.6 + Navigation Contract v0.1 lack `Reviewed By` — S2-2.2's forward half regressed at its trigger; class: Fixed dispositions with pending forward-commitments have no tripwire | Low | Open |
| S3-3.1 | Command tier unstamped despite recorded "stamped-projection" class; `.claude/` outside the checker walk; `fractal.md` duplicates the active-Local routing datum | Med | Open |
| S3-3.2 | `AGENTS.md` content frozen at v0.1 through C-074/C-075: forbidden-paths list omits `.allowed_signers`, `.claude/**`, `.gitignore`; no lifecycle clause; adapter-content currency has no checklist tripwire | Med | Open |
| S3-3.3 | BOOTSTRAP §2.1/§2.2 don't record the landed command tier (three OQ-16 slices) | Low | Open |

*(OQ-13's worked options in §5 are analysis, not a finding — its disposition is Max's call at this close.)*

---

**Sources:** the full Claude-era corpus at `Desktop/FRACTAL/` as of 2026-08-15, HEAD `98e2952` — every document named in the State-scanned line above, read at that state; the live Knowledge Graph Store and fresh runs of `verify.py`, `check_versions.py`, and `stats.py`; the git repository (status, branches, remote, full log with `%G?` signature verification under the repo's `.allowed_signers` binding); `.claude/commands/fractal.md` + `close.md`; `.gitignore`; `.allowed_signers`; Return Packages First-Code-Session, Navigation-Close, Custody-Close (postscripts included); Protocols v0.27–v0.28 in full, earlier versions as cited; Scan #1 and Scan #2 (baselines); the §4 drill's fresh clone of `mstruppe/fractal`.

**Method:** read-only over the repository; the drill ran in an isolated scratch directory against a fresh clone; no file in `Desktop/FRACTAL/` was created or modified by this scan except this document. Every finding was verified against its cited source file and line at HEAD `98e2952`, and against live command output where the claim is about repo state; findings that did not reproduce were dropped (one: a suspected silent G-list drop of OQ-16, disproved by history — recorded as a non-finding instead). Line numbers refer to the files at that HEAD.

**Provenance:** FRACTAL whole-project loose-ends scan #3, 2026-08-15, commissioned by Max in the fourth Claude Code session ("let's do the 3rd scan"); executed by the governing surface (Fable) on Max's surface call, carrying the first Scan-riding restore drill (C-076). Canonical per the C-058 class: sequential, dated, DOC-minted at commit, never revised. Findings are verified observations; fixes are proposals, not accepted decisions.

**Revision history:** v0.1 (2026-08-15) first issue — 8 findings (5 Medium, 3 Low, 0 High) across machine-blind-spot currency, supersession/spec hygiene, and the ungoverned artifact edge; first Scan-riding restore drill executed green with the S2-3.4 content check; OQ-13 worked to a decision-ready option set; Scan #1/#2 residue verified 27 of 28 holding (S2-2.2's forward half re-entered as S3-2.2); disposition ledger seeded.
