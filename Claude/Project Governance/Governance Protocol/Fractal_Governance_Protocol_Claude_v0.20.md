# Fractal Governance Protocol — Claude Series v0.20

**Topic:** The first Claude Code session — the queued handover batch decided and executed in one pass: the hygiene findings S2-6.2/S2-6.3 fixed from the new surface, the ChatGPT-era archive move decided (Max: **go**) and executed (`Archive/Foundation with ChatGPT/`, OQ-10 resolved → C-063), and the push ritual's executor promoted across the C-008 boundary under Max's standing authorization (C-064). The first protocol issued from the in-repo surface.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.19

---

## 1. Context

The C-059 auditable handover: *the previous package (Code-Migration-Handover) queued the first Claude Code session's batch — hygiene (S2-6.2/S2-6.3), the OQ-10 call of record (Max's stated inclination: go), and this protocol; this conversation executed all of it.* The bridge close had run both checkers as a pre-migration baseline (both PASS, no drift) and moved the operating surface from the Cowork device bridge to Claude Code working directly in the repo (C-018 exercised, not amended). The batch existed *because* of the old surface's limits: the bridge could not delete (hence `_to_delete/` and the stranded owner-files) and had no network (hence push always deferred to Max). The new surface dissolves both limits — this session is the proof by execution.

## 2. Questions investigated

1. The OQ-10 go/no-go: archive the ChatGPT-era layer, or leave it at root? *(→ Max: go — C-063; executed as `git mv`, history preserved.)*
2. What shape does the archive take? *(→ a root `Archive/` subfolder, the era-folder moved into it intact — no internal reorganisation, C-007.)*
3. Who executes `git push` now that the surface can? *(→ C-064: Claude, at every close, under Max's standing authorization — the first deliberate C-008 promotion.)*
4. Does the hygiene execution retire the `_to_delete/` convention? *(→ retired from need, kept latent: the `.gitignore` entry stays for any future Cowork session.)*

## 3. Decisions of record

- **C-063 — ChatGPT-era archive move (OQ-10 resolved: go — executed).** The entire ChatGPT-era layer moved **intact** via `git mv` (history preserved) into a root archive subfolder: `Foundation with ChatGPT/` → `Archive/Foundation with ChatGPT/`. C-007 preservation and C-029 pointer-only standing are untouched by the move; `Vision thought scramble.docx` stays at root per C-062's deliberate no-move. Living references swept in the same pass — Context Index (the one place paths are maintained, C-012) → v0.13, BOOTSTRAP → v0.7, Architecture State → v0.5, the Register's lineage pointers, `check_versions.py`'s skip/root lists — and the checker's path pass verifies the sweep. The first decision decided-and-executed from the Claude Code surface. *(Working Decision.)*
- **C-064 — Standing push authorization (the first C-008 promotion).** `git push` at close is executed by **whichever writer holds the surface**: from 2026-08-14, Claude pushes at every close under Max's standing authorization — granted in this conversation by explicit selection (over one-time confirmation and keep-manual, both offered), recorded here, in the Register, and in BOOTSTRAP §4. The C-037/C-056 ritual is unchanged — push still rides every coherent-change-set commit; only the executor changes. C-008 manual-first is satisfied: the ritual ran manually through the whole bridge era, and this is its first recorded promotion across the automation boundary (OQ-9 gains its first calibrated step). *(Working Decision.)*

## 4. Executed this close (one `[GOV]` commit, C-037; push = Claude, first exercise of C-064)

- **Hygiene batch (review-ledger dispositions → Fixed):** `_to_delete/` emptied and removed — `git fsck` run clean first, confirming the stray session-lock and `tmp_obj` hardlink files were not load-bearing (**S2-6.2**); the three root `~$*.docx` owner-files deleted (**S2-6.3**). Both were untracked/gitignored — no history rewriting involved.
- **Archive move:** `git mv "Foundation with ChatGPT" "Archive/Foundation with ChatGPT"` — pure renames, provenance intact (C-063).
- **Path sweep (living sources only; frozen sources keep their historical paths by design, C-058/C-060):** BOOTSTRAP → **v0.7** (§0 archive path; §4 push executor); Context Index → **v0.13** (GOV/AST/PROT rows; naming-convention section records the move as done); Architecture State → **v0.5** (ChatGPT-era pointer retargeted); Decision Register lineage pointers; `check_versions.py` `SKIP_DIRS`/rooted-path lists (`Foundation with ChatGPT` → `Archive`).
- **Decision Register → v0.18** — C-063/C-064 entered; OQ-10 → Resolved; S2-6.2/S2-6.3 → Fixed; Sources and revision history.
- **Rule Overview → v0.16** — sources-currency cure: the checker's first run at this close came back red (five stale citations across BOOTSTRAP, Index, and Rule Overview — left behind by this close's own version bumps) and every one was cured before commit; no rule added or retired. The mechanization worked exactly as C-060 intended.
- **Store** — this protocol DOC-minted (C-041: create + route alias + `topic:GOV` + `agent` placements); five `revise` events re-freeze the edited living canonicals (Register, BOOTSTRAP, Architecture State, Context Index, Rule Overview); **61 nodes / 262 events**; both checkers green before commit.
- **Local Context → v0.25** — batch recorded; checklist walked; queue empties (G offers + H roadmap stand).
- **Agenda Board** — republished file-first (stamp → Local Context v0.25).
- **Return Package** — `Return_Package_2026-08-14_First-Code-Session.md`.

## 5. Calls recorded (Max, 2026-08-14, this conversation)

1. **The batch:** "1. execute 2. OQ-10 move to archive" — hygiene executed as queued; the OQ-10 inclination confirmed as the call of record: **go**.
2. **Push:** standing authorization — Claude pushes at this close and every future close (chosen over one-time confirmation and keep-manual).
3. **Archive shape:** a root `Archive/` subfolder with the era-folder intact inside (proposed in-plan, approved with the plan).

## 6. Ratification record (2026-08-14, in-conversation per C-033)

Max opened the session on the queued handover batch, gave the two calls of record (OQ-10: go; push: standing authorization) by explicit selection, and approved the execution plan before any canonical file changed. Claude executed and committed as the attributed author per C-037 and pushed per C-064's first exercise. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None opened. **OQ-10 → Resolved** (C-063) · **S2-6.2 / S2-6.3 → Fixed** (executed from the new surface).
- Standing items carry: OQ-4, OQ-6, OQ-9, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. No open review findings remain — the S-ledger is fully green for the first time. **Scan #3 stays penciled** after the build track — earlier if the checker and the C-059 checklist disagree.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.20 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.20 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.19 |
| Related Documents | Return_Package_2026-08-14_Code-Migration-Handover.md (the queue); Decision Register v0.18; Local Context v0.25; Architecture State v0.5; Context Index v0.13; BOOTSTRAP.md v0.7; Return_Package_2026-08-14_First-Code-Session.md |
| Document ID | DOC-01M009EVKF91A4V68Y4E6YDVAW (minted 2026-08-14, C-041, per this protocol) |
