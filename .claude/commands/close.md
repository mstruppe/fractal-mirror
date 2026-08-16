---
description: Close a FRACTAL working cycle — walk the C-059 ritual, drive the mechanical ripple through close.py, commit and push
---
Close this FRACTAL working cycle per the standing close ritual (C-059; CLAUDE.md rule 5). This command orchestrates — the rows, rules, and marks live in their canonical homes, never here.

**0. Precondition — this command only works in a `/fractal`-opened session.** Verify this session is oriented: the Global Context, the active Local Context, and the latest Return Package have been read *in this session* and reflect current file state. If not oriented, **stop** — tell Max to open with `/fractal` first (or, on his explicit go, run that orientation now and then continue). Never close from an unoriented session: that is how records get mismarked (the S2-3.1 class).

1. **Determine the close's character.** What did this session decide (→ Governance Protocol due, C-033 ratification recorded) vs merely execute (→ recorded reason, no protocol)? Anything unratified: ask Max before proceeding — never ratify on his behalf.
2. **Judgment pass (prose — never delegated to tooling):** draft the protocol if due; update the Decision Register; then **walk the C-059 checklist exactly as written in the Local Context §Standing refresh items**, marking every row *changed (→ new version)* or *checked — unchanged* — including the Conversation Settings row's question (C-071: did any decision touch conduct? If yes, Settings reissues in this close and its projections restamp after — source first). Then: Local Context bump, Agenda Board restamp (file-first, C-048), Return Package or postscript with the auditable handover line.
3. **Mechanical pass:** run `python3 close.py` (in `Claude/Knowledge Graph Store/`) — review its plan output — then `--write` with a one-line `--note` per changed document; `--create` for any new canonical (C-061 handled by the tool). Hand-author only if the tool refuses for a reason its plan output makes legible; report any refusal. **Counts last (S4-1.2):** after `--write`, bring any store-count claim (the Local Context's and the Board's "N nodes / M events" line) to the tool's post-ripple totals — the mechanical pass appends events, so counts written in step 2 are stale by construction; `check_versions.py` errors on a mismatch.
4. **Gates (red blocks, no exceptions):** `python3 verify.py` and `python3 check_versions.py` both PASS before commit (C-050/C-060). Cure and re-run until green.
5. **Commit per C-037** (author = actual author; `[DOMAIN] imperative summary` + decision refs; one commit per coherent change-set), **push per C-064**.
6. **Report:** the change summary, the checklist marks, the store delta (nodes/events), anything newly pending on Max, and what stands open for the next session.

Refresh triggers for this file: a change to the close ritual itself (a C-059 amendment, a checker or close.py change, a commit/push convention change).

---
*Stamped-procedure projection (C-035 class, per Scan #3 S3-3.1 / Protocol v0.29): a thin orchestrator over the ratified close ritual — sources: the C-059 checklist in its normative home (the Local Context §Standing refresh items) + close.py (C-073) + the commit/push convention (C-037/C-064) + the counts-last step (Scan #4 S4-1.2). Stamped 2026-08-15. Sync-check = this stamp vs those sources; re-project on any trigger above.*
