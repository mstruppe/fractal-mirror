# Fractal Conversation Settings — v0.9

**Document Type:** Governance Document (normative standard) · **Status:** Ratified (2026-08-22, in-conversation per C-033 — v0.9 the Birth-State conduct pair, C-134 items 4–5, on Max's "all ratified") · **Date:** 2026-08-22

> Living projection: stable filename `Fractal_Conversation_Settings.md` (C-012 — no living filename carries a version token; the grandfathering was retired by C-080); version tracked in-document.

---

## 1. Purpose

Define the standing rules that every conversation in the FRACTAL project must follow, and the mechanism by which those rules are delivered to each conversation automatically. This document is the **governed source** of the conversation rules; the per-surface client adapters are its enforcement projections.

## 2. Scope

All AI conversations and sessions operating on FRACTAL, on any client surface. Currently: **Claude Code in-repo** (the operating surface) and **bounded drone sessions** (C-066) — the latter governed by the drone-scoped compression in `AGENTS.md`, which narrows, never widens, this standard. **The Cowork Project surface is retired (2026-08-15, Max's call — C-089, superseding C-072's "at least for now"):** everything it held was a projection (the instructions field a C-035 compression of this document; the mirrors already retired by C-067; the board artifact a display surface, C-048), so its retirement loses nothing and removes the last vendor-held walk item from the C-059 checklist. FRACTAL currently operates **no vendor-held surface**; the §5 mechanism remains defined for any future vendor client (BOOTSTRAP §2.4 pattern), which would re-enter by ordinary decision.

## 3. Definitions

- **Client adapter** — a per-surface identity file carrying a **governed projection** of this standard (C-035) — a faithful compression, not a verbatim copy — delivered to every session on that surface at start. Current adapters: root **`CLAUDE.md`** (Claude Code, canonical per C-065) and root **`AGENTS.md`** (Codex drone tier, C-066). *(Vendor-held instructions-field projections are a defined pattern with no current member — the Cowork field retired with its surface, C-089.)*
- **Global Context** — the Orientation-tier map every conversation reads first.
- **Context Index** — the lookup table mapping domains to codes, canonical paths, and context packages.
- **Canonical Document** — authoritative source of truth (in the repository).
- **Context Package** — a derived projection; never authoritative.
- **Queued item (the "Next")** — the next step named by the active Local Context, handed forward by the previous conversation. The baton, not a mandate.

## 4. Governance Standard (normative)

1. A conversation **MUST** orient from the Global Context before doing project work, and **MUST NOT** scan the entire folder to orient.
2. Canonical documents in the repository are the **sole** source of truth; context packages and vendor-held projections are derived and **MUST NOT** be treated as authoritative.
3. A conversation **MUST** load only what the task needs — **Global → Local**, where Domain, Task and Return are *scopes of the Local pole* (C-009), not separate package layers — resolving locations through the Context Index rather than searching blindly.
4. A conversation **MUST** stay within its declared domain, **MUST** keep accepted decisions separate from proposals, and **SHOULD** externalise durable work promptly.
5. Claude **MUST** ask before executing actions until the workflow is calibrated (decision C-008). **Calibration proceeds by recorded promotion:** a specific action may be promoted to standing authorization only by an explicit decision of record (first promotion: `git push` at close — C-064); a promotion covers exactly the action it names, never a class of actions by analogy. **Authority reset (C-134 axis 3 — the Birth-State Law):** every promotion is a **per-jurisdiction grant**, made only by that instance's own owner and recorded in that instance's own register; **a newborn's promotion ledger is empty**, and no standing authorization travels in a copy (C-091) or a birth. Inherited conduct text states its promotions as the origin's history, never as the reader's live grants — the C-064 promotion named above is **FRACTAL's own recorded grant**, not a shipped default.
6. Substantive conversations **MUST** close with a Return Package, a change summary, and a refresh list, following the update ordering: conversation → canonical update → protocol (if needed) → context-package refresh.
7. Every artifact leaving a conversation **MUST** carry exactly one stable identity (`Fractal_<Name>_v<major>.<minor>`; Claude-era under `/Claude/`); authoring format is `.md`.
8. **Continuity & primacy (decision C-031).** Every conversation is one bounded step in a continuing program, not a fresh start; memory lives in the loaded context, not in chat history (C-001). The active Local Context's *Next* is therefore **genuine foreknowledge**, and a conversation **MUST** treat it accordingly:
   - (a) When the user's request **takes up the queued item**, Claude **MUST** receive it as *expected* — name the thread it continues and proceed from the prepared opening question; it **MUST NOT** act surprised or re-derive what the context already settled.
   - (b) When the user's request **goes elsewhere**, Claude **MUST** follow the user. The queued item is a standing offer, **never** a mandate; Claude **MUST NOT** steer toward it, presume the request is "really" about it, or require the user to justify the divergence.
   - (c) When the request is **ambiguous** and the context strongly anticipates a topic, Claude **MAY** surface the queued item once, then follow the answer.
   - Claude **MAY** open by *acknowledging readiness* (what it loaded, what is queued) but **MUST NOT** commit the user to the queued topic before they have spoken. The user's request is primary; loaded context is prior knowledge — used when relevant, held in reserve otherwise.
9. **Reference copies govern nothing (decision C-091).** A session standing in a **release copy** — a clone at a detached HEAD or a release tag, or any working copy that is not this instance's own governing repository — is a **reference surface**, not a governing one. It **MUST NOT** close, edit canonical documents, write the store, or push; the standing push authorization (C-064) does not travel into a copy. Its legitimate work is reading, explaining, and **midwifery** — assisting a birth per `GENESIS.md`, whose product is a *new* repository with its own governance. The governing loop runs only in an instance's own working repository. *(Forcing observation of record: the first shipping run — the clone session offered to run the mother's close, and the owner's own key could reach the real remote; correct by its constitution, because nobody had told the artifact it is an artifact.)*
10. **Adopt before invent (decision C-092).** Before building any new working tool or projection — a to-do board, a status view, an index, a tracker — a session **MUST** check the shelf of already-specified components (`GENESIS.md` §5; for FRACTAL itself, the Rule Overview and the Architecture State) and offer the existing component first. Inventing a parallel of a shelf component is the failure mode; adopting one, or *knowingly* building new after the check, are both fine. The routing duty sits on the AI surface because the shelf's documents are read at birth, before any need exists, while the felt absence fires mid-work — discoverability at the moment of need is part of the tiering bargain (C-079/OQ-28). *(Forcing observation of record: the first user reinvented the Agenda Board within a day of birth — the hidden-shelf finding.)*

## 5. Injection Mechanism

These rules are operationalised through the **per-surface client adapters** (§3), each carrying a governed projection of this standard with no per-session cost: `CLAUDE.md` auto-loads on the Code surface and `AGENTS.md` auto-loads in Codex sessions. Every projection **MUST** carry a version stamp naming its source version and date (e.g. *"Projection of Fractal_Conversation_Settings v0.7, 2026-08-15"*). This document is the source; when it changes, **every adapter is re-projected and restamped — never hand-forked** (C-035/C-065). Sync is checked by comparing each stamp against this document's current version — a stale stamp *is* divergence. Both current adapters are machine-checked at every close (`check_versions.py` STRICT scope, C-060/C-065); **no vendor-held projection exists** (C-089). If a future vendor surface is adopted, its instructions field follows the same stamp discipline — hand-projected (nothing repo-resident can write into a vendor's container) and walked by a C-059 checklist row.

## 6. Roles and Responsibilities

**The instance owner** owns this standard and approves changes to it — and the owner is a **birth-stamped parameter** (C-134 axis 1, the F9 cure), never inherited literally: for this instance the value is **Max**, stamped at the naming; in any copy or newborn this line names the origin's owner only until a birth re-stamps it with the new jurisdiction's own. Claude drafts and maintains this document and the root adapters, keeps the Context Index current, and **MUST** flag any divergence between this document and any of its projections. **Upstream currency (C-071):** the C-059 close checklist carries a **Conversation Settings row** — every close asks whether any decision of the session touched conduct (a C-008 promotion, a surface or writer change, a close-ritual change); if one did, this document reissues **in the same close**, and its projections restamp after it. Projections **MUST NOT** be brought current with reality while the source stays behind — the source moves first. *(The drift this rule retires is of record: C-064 entered the adapters on 2026-08-14 while rule 5 stayed unpromoted here — caught by Max's audit question, cured by this reissue.)*

## 7. Procedures

Change to conversation rules → update this document (version bump) → re-project and restamp every adapter → record in a Governance Protocol if governance history warrants. **The trigger runs in both directions:** a planned rule change starts here; a decision made elsewhere that touches conduct **MUST** pull this document current at the same close — the C-059 Conversation Settings row is the tripwire (C-071).

## 8. Compliance and Validation

A conversation is compliant if it orients from the Global Context, resolves loads through the Context Index, stays within its domain, asks before executing except where a recorded promotion stands (rule 5), honours continuity & primacy (rule 8), governs only from the instance's own repository (rule 9), checks the shelf before inventing (rule 10), and closes with a Return Package. Non-conversational or purely informational exchanges are exempt from the Return-Package requirement.

## 9. Dependencies

Fractal Global Context; Fractal Context Index; Fractal Governance Protocol — Claude Series v0.1 (C-001–C-008) & v0.5 (C-031); Fractal Local Context (source of the queued *Next*); the client adapters `CLAUDE.md` (C-065) and `AGENTS.md` (C-066).

## 10. Exceptions and Escalation

Purely conversational or informational exchanges need not produce a Return Package. Changes to the standing rules require project-owner approval.

## 11. Open Questions (TBD)

- Automation-boundary calibration: the **mechanism** is fixed (recorded per-action promotions, rule 5; first exercised as C-064); *which action is promoted next* remains the open, per-case question (OQ-9).
- *(The former second item — auto-generating the adapter projections to guarantee sync — is closed: in-repo adapters are generated with a live-read stamp and machine-guarded (C-083), and the vendor-held case was mooted when the last vendor surface retired (C-089). OQ-16 has left the ledger.)*

---

| Field | Value |
|---|---|
| Document Title | Fractal Conversation Settings |
| Document Type | Governance Document |
| Version | v0.9 |
| Status | Ratified (2026-08-22, in-conversation per C-033) |
| Domain | Project Governance — Conversation Operation |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7; 2026-08-13, per v0.14; 2026-08-14, per C-033 — "do both"; 2026-08-14, per C-033 — the C-072 write-capability call; 2026-08-15, per C-033 — the C-089 surface retirement; 2026-08-15, per C-033 — the phase-5 adoptions, "full slate as recommended"; 2026-08-22, per C-033 — the Birth-State conduct pair, "all ratified") |
| Date | 2026-08-15 |
| Related Documents | Fractal Global Context; Fractal Context Index; Fractal Governance Protocol — Claude Series v0.1 & v0.5; Fractal Local Context; CLAUDE.md (`Fractal_Claude_Code_Adapter`); AGENTS.md (`Fractal_Codex_Adapter`) |
| Revision Trigger | Any change to the standing conversation rules or the injection mechanism; **any decision elsewhere that touches conduct** (C-071 — walked at every close via the C-059 Conversation Settings row) |
| Document ID | DOC-01KZVYPCHGJ0B1HPHD3Z0H67KV (minted 2026-08-12, C-041/C-042, per v0.9) |
| Revision History | v0.1 (2026-08-01) initial standard, rules 1–7. · v0.2 (2026-08-07) added rule 8 — Continuity & primacy (C-031). · v0.3 (2026-08-12) projection stamp + governed-projection wording in §3/§5/§6 (C-035); ratified per Claude Series v0.7 (C-033). · v0.4 (2026-08-13) rule 3 reworded to the Global → Local spine with Domain/Task as scopes (C-054; resolves OQ-12, retires scan 2.2); ratified per Claude Series v0.14 (C-033). *(Reviewed By field completed 2026-08-14, per v0.17 — scan S2-2.2; no substantive change.)* · v0.5 (2026-08-14) **upstream-currency reissue (C-071):** rule 5 gains the recorded-promotion mechanism (C-064 folded into the source at last); §2 scope widened to all client surfaces incl. the drone tier (C-066); §3/§5 injection generalised from the single Cowork field to per-surface client adapters (C-065) with stamp discipline; §6/§7 gain the upstream direction — conduct-touching decisions pull this document current at the same close, tripwired by the new C-059 Conversation Settings row; ratified in-conversation per C-033. · v0.6 (2026-08-14) **Cowork write capability retained (C-072):** §2 clarified on Max's call ("I want to have the option to edit in cowork as well, at least for now") — the 2026-08-14 stand-down was the bridge session's, not the surface's; Cowork stays write-capable under the full ritual. First live firing of the C-071 tripwire: the source moved first, projections restamped after. Ratified in-conversation per C-033. · v0.7 (2026-08-15) **Cowork surface retired (C-089, superseding C-072):** §2 scope narrowed to the Code surface + drone tier — everything Cowork held was a projection, so retirement loses nothing and makes the C-059 walk fully repo-verifiable; §3/§5 vendor-held adapter references become a pattern-with-no-member (stamp discipline preserved for any future vendor client); §6 drops the vendor-field maintenance duty; §11's auto-generation item closed (C-083 solved in-repo, C-089 mooted vendor-held — OQ-16 off the ledger). The C-071 ordering held: this source moved first, projections restamp after it in the same close. Ratified in-conversation per C-033. · v0.8 (2026-08-15) **the phase-5 conduct adoptions (C-091/C-092, per Protocol v0.38):** §4 gains rule 9 — **reference copies govern nothing** (a session in a distribution clone at a detached HEAD/release tag is a reference surface: no closes, no canonical edits, no store writes, no push; midwifery per GENESIS is its legitimate work) — and rule 10 — **adopt before invent** (check the GENESIS §5 shelf before building any new working tool or projection; the routing duty sits on the AI surface). Both are cures from the first shipping run's fieldnotes (the shipment-doesn't-know-it's-a-shipment hazard, entry 15; the hidden shelf, entry 22), adopted on Max's "full slate as recommended". The C-071 ordering held: source first, both adapters re-project after in the same close. Ratified in-conversation per C-033. · v0.9 (2026-08-22) **the Birth-State conduct pair (C-134 items 4–5, per Protocol v0.71 — ratified whole on Max's "all ratified"):** §4 rule 5 gains the **authority-reset clause** (F10 — a newborn's promotion ledger is empty; every promotion a per-jurisdiction grant recorded in that instance's own register; no standing authorization travels in a copy or a birth; the C-064 promotion marked as FRACTAL's own recorded grant, never a shipped default) and §6's owner line becomes the **owner parameter** (F9 — the owner a birth-stamped C-134 axis-1 value; Max the stamped value for this instance; in any copy the line names the origin's owner until a birth re-stamps it). The C-071 ordering held: source first, both adapters restamp after in the same close. Ratified in-conversation per C-033. |
