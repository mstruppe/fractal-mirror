# FRACTAL — Loose-Ends Scan #2

> **CANONICAL — Claude-era review document.** A whole-project adversarial scan for loose ends *not explicitly stated*, run at Max's request and declared canonical by him in the same breath (superseding Scan #1's "analytical review, not canonical" framing — see §7). It is authoritative for **what was observed on 2026-08-14, over the post-drill state at HEAD `0bd546e` (2026-08-13)**; it is not authoritative for what should be done about it. Each finding is a verified observation with a proposed fix; the fix becomes binding only through an ordinary decision. Read-only over the full Claude-era corpus, the live store, and the git repository.

**Fractal_LooseEnds_Scan_2** · **Version:** 0.1 · **Status:** Ratified (2026-08-14, in-conversation per C-033/C-058, per Protocol v0.17 — findings stand as observations; fixes were adopted only where v0.17 says so) · **Reviewed By:** Max (2026-08-14, per v0.17) · **Updated:** 2026-08-14 · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Global Context · **Document ID:** DOC-01KZZPC3G68KDJ252JCNPNB8B4 (minted 2026-08-14, C-041/C-058, per v0.17)

**Baseline:** Scan #1 (`Review_2026-08-12_LooseEnds-Scan.md`, 2026-08-12) · **State scanned:** Protocol v0.16 · Register v0.14 · Rule Overview v0.12 · Conversation Settings v0.4 · Schema v0.5 · Template v0.3 · Index v0.9 · Global v0.3 · Local Context v0.19 · Architecture State v0.1 · BOOTSTRAP v0.3 · store 46 nodes / 179 events · HEAD `0bd546e`, in sync with `origin/main`.

---

## Summary

Scan #1 found an architecture whose *ideas* were coherent and whose *mechanisms* were mostly promised. Two days and ten protocol versions later, the mechanisms exist and work: `verify.py` returns PASS on 179 events and 46 entities with zero warnings, the repository is clean and pushed, the decision ledger runs C-001 → C-057 without a gap, the open-question ledger runs OQ-1 → OQ-22 without a gap, and every High finding from Scan #1 is genuinely retired — not asserted retired, *checked* retired. That is a real result and it should be said plainly before the findings below.

The failure mode has moved, and it has moved somewhere predictable: **the corpus is now machine-verified exactly where a machine checks it, and drifting exactly where no machine checks it.** The store is hashed, folded, replayed and guarded at every commit. The prose layer around it is guarded by nothing, and it has come apart in eleven places in three conversations. The C-038 drill caught the first specimen — a headline saying 174 events over a log holding 176 — and correctly named projection drift as an open integrity question. This scan is the evidence that the specimen was not a one-off but a *class*, and that the class has a single mechanism behind it: **the close-the-loop refresh has silently narrowed to three documents.** The last three Return Packages carry a verbatim-identical refresh line — Register, Rule Overview, Local Context — and every document outside that triple has fallen behind by exactly the number of conversations since it was last touched. The Architecture State, which declares itself authoritative for *what is current and what supersedes what*, is wrong about both. The Context Index, the routing table every rehydrating reader is sent through, names a superseded schema and a protocol series that stops two versions short. `BOOTSTRAP.md`, certified green the same day, contradicts itself about a version number on the rehydrate path — because the drill verified that paths *resolve*, never that pointers are *true*.

Two structural findings sit underneath that. **First, the drill's own results are recorded only in derived projections.** No Governance Protocol records them; v0.16 still reads "first push pending" and "acceptance test armed, not exercised", while the Decision Register — which states on its own first line that it never overrides its sources — reports both caveats discharged. By the project's own ratification legend, the two facts the project is currently proudest of are unratified, and a projection is contradicting its source. **Second, review findings have no ledger.** C-034 built exactly that mechanism for protocol §11 items after Scan #1 showed them leaking; scan findings were left outside it, and Scan #1's own findings 1.5 and 2.4 have quietly leaked in precisely the way C-034 was invented to prevent. Without a fix, this document leaks the same way — which is, in the end, the strongest argument for Max's instinct that it should be canonical.

Nothing here is dangerous. Nothing here is lost. The whole of §1 is one careful pass through six files, and §3 is a single decision about how reviews are dispositioned. But the pattern is worth naming, because it is the first time FRACTAL has produced a *systematic* defect rather than an accidental one — and the system produced it by doing everything else right.

---

## 1. Currency drift — the projection layer

*The largest cluster, and the one with a single shared cause (see 3.1). Each of these is a present-tense claim that is false.*

**S2-1.1 The C-038 drill is recorded in no Governance Protocol; a derived projection now overrides its source.**
**Severity:** High. **Where:** `…Protocol_Claude_v0.16.md` line 4 and §11 line 85 · `Fractal_Decision_Register.md` lines 9, 109, 115, 204.
Protocol v0.16 — the newest protocol that exists — carries `Status: Ratified (… caveat: first push pending Max's terminal action)` and §11 `C-038 acceptance test **armed, not exercised** (first push pending, then first clone-rehydrate)`. The Register (v0.14) states the opposite as fact: both caveats discharged, test exercised green. The Register's own banner says it "never overrides its sources" (C-003), and its ratification legend defines **Ratified** as "recorded in a reviewed Governance Protocol" (C-033). So the off-site copy going live and "laptop in the ocean" becoming demonstrated fact — the two load-bearing results of the last conversation — are recorded canonically nowhere, and the ledger that reports them is by construction not allowed to be their source. The drill conversation is the first in the Claude series to close with a Return Package and no protocol; its reasoning ("no new C-decision — both acts execute ratified decisions") is sound about *numbering* and silent about *recording*.
**Fix:** either (a) issue Protocol v0.17 as an execution record — no new C-numbers, just the drill, the discharges, and a §11 sweep; or (b) decide explicitly that executing an already-ratified decision needs no protocol, and say where the discharge is canonically recorded instead. (a) is cheaper and keeps the protocol series the complete history it claims to be.

**S2-1.2 The Architecture State is not current about currency — the one thing it is authoritative for.**
**Severity:** High. **Where:** `Fractal_Architecture_State.md` line 17 (§2), line 57 (Sources), line 56 (Refresh triggers).
§2 names the KG core's canonical documents as "Knowledge Path Foundation v0.1, **Node & Event Schema v0.4**, Node Template v0.3"; the schema is at **v0.5**. Sources compound it: "Node & Event Schema v0.4; Decision Register v0.10; Governance Protocol — Claude Series v0.14". Its declared refresh trigger — "any newly accepted architectural decision; a supersession affecting a section above" — has fired three times since the document was forged: **C-055** rewrote the event log's physical layout (§2's territory), **C-056/C-057** put the substrate off-site and gave it a protection model (§5's territory). Neither §2 nor §5 mentions either. A document whose banner reads *"authoritative for what is current, what supersedes what, and how the parts relate"* is currently wrong about the first two.
**Fix:** Architecture State v0.2 — schema pointer to v0.5, §2 gains the one-file log (C-055), §5 gains the off-site remote and the custody ladder (C-056/C-057), Sources restamped. Add it to the standing refresh list (see S2-3.1).

**S2-1.3 The Context Index — the single place routing is maintained — is stale in four current-state claims.**
**Severity:** High. **Where:** `Fractal_Context_Index_v0.1.md` (internal v0.9) lines 8, 35, 41, 50; Sources line 66.
- line 8: "…cannot drift from their concepts (**Schema v0.4** §5.3 rule 7)" → v0.5 (the rule survives at the same section number, so the pointer resolves to the right content in a superseded file).
- line 35: KG row status "Active — **format v0.4**, multi-writer safe" → format v0.5.
- line 41: PROT row "**Series open (Claude v0.1–v0.14)**" → the series runs to v0.16.
- line 50: Canonical-documents table "**Node & Event Schema v0.4** (v0.1–v0.3 superseded, retained as history)" → should read v0.5 (v0.1–v0.4 superseded). This row is an explicit currency claim, not a citation.
The Index has not been touched since Protocol v0.14 closed workstream F, and `BOOTSTRAP.md` §1 step 3 sends every rehydrating reader — human or machine, first contact — straight through it. The irony is exact: the Index's own headline boast is that its route table "cannot drift"; the routes indeed cannot, because they project live store bindings. Everything on the same page that is *not* store-projected drifted.
**Fix:** Index v0.10. Consider projecting the version columns from the store the way the route column already is — the drift-proof half of the table is drift-proof for a reason.

**S2-1.4 `BOOTSTRAP.md` contradicts itself about a version, inside the rehydrate path, in the document certified green the same day.**
**Severity:** Medium. **Where:** `BOOTSTRAP.md` line 21 vs. line 68.
§1 step 5: "`Fractal_Conversation_Settings_v0.1.md` (**internal v0.3**) is its normative source for conversation conduct." The internal version is **v0.4** (C-054), and this file's own Sources line correctly says "Conversation Settings v0.4". A stranger following the acceptance-test path performs the C-035 sync-check — stamp comparison — against a stated source version that is one behind, and concludes the client projection is *ahead of* its source. The drill verified that all nine §1 paths resolved; resolving is not the same as being right, and this is the cleanest available illustration of what the current verification does not cover.
**Fix:** BOOTSTRAP v0.4, line 21 → v0.4. Better: drop the parenthetical version entirely — the file is the pointer, its internal stamp is the answer, and naming the version in a second place is the drift surface. Compare `Fractal_Global_Context_v0.1.md` line 27, which says "(v0.4 inside)" and is correct precisely because it is maintained as one fact in one place.

**S2-1.5 The Node Template teaches a companion version that is two behind and a log file that no longer exists.**
**Severity:** Medium. **Where:** `Fractal_Node_Template_v0.3.md` lines 3, 5, 69.
Line 3: "CANONICAL companion to `Fractal_Node_and_Event_Schema_v0.3.md`". Line 5: "**Parent:** Fractal Node & Event Schema **v0.3**". The schema is at v0.5. Worse, line 69, in the worked event-log example: "Append to `_events/2026-08.jsonl`, one object per line." C-055 retired that filename by git-tracked rename; the store holds `_events/part-0001.jsonl` and the README says so. The Template's stated purpose is *copy-paste starting points for writing nodes and log lines by hand, at zero infrastructure* — so the one document aimed squarely at a hand-author working without tools is the one pointing at a dead path. This is the second occurrence of the same failure: Scan #1's finding 1.3 was the Template drifting behind the accepted agent grammar. The Template drifts behind the Schema every time the Schema moves, because nothing binds them.
**Fix:** Template v0.4 — companion/parent → v0.5, example path → `_events/part-0001.jsonl`. Structurally: make "Template follows Schema" an explicit refresh trigger inside the Schema, so the Schema's own reissue carries the obligation.

**S2-1.6 The Decision Register's "Normative home" field is stale for two decisions and current for a third.**
**Severity:** Medium. **Where:** `Fractal_Decision_Register.md` lines 151, 152 vs. line 167; Sources line 214.
C-049 ends "Normative home: **Schema v0.4** §5.4." C-050 ends "Normative home: **Schema v0.4** §5.5." C-055, three rows down, correctly reads "Normative home: **Schema v0.5** §4.1." Same field, same table, one updated when the schema moved and two not — which establishes the field's convention as *where the norm lives now*, and therefore establishes the other two as wrong rather than historical. Both sections do exist at those numbers in v0.5, so the reader lands on the right rule in a superseded file.
Also line 214 (Sources): "**Conversation Settings v0.3** (C-031 normative home; C-035)" → v0.4; "**BOOTSTRAP.md v0.1–v0.2**" → v0.3, produced by the very conversation this document's own v0.14 revision note records.
**Fix:** Register v0.15 — three pointer corrections. Consider dropping version numbers from "Normative home" entirely (`Schema §5.4`), since the schema's living identity is one DOC node anyway (see S2-5.1).

**S2-1.7 The canonized tools cite a superseded schema in their own headers.**
**Severity:** Low. **Where:** `verify.py` lines 4, 28 · `mint.py` lines 5, 27.
`verify.py`: "THE RITUAL (**Schema v0.4** §5.5)" and "hashes recompute against the repo (**Schema v0.4** §3.7)" — while line 16 correctly says "Schema v0.5 §4.1". `mint.py`: "**Schema v0.4** §4.5" and "**Schema v0.4** §5.3 rule 6" — while line 152 correctly says v0.5. Comments only, and the code is right; but these are the C-050 canonized tools, the store README points hand-authors at them, and they are the artifacts most likely to be read by a stranger deciding whether the store is trustworthy.
**Fix:** four comment edits, folded into whichever commit next touches the store.

---

## 2. Governance & ratification

**S2-2.1 The Knowledge Path Foundation is still `Status: Draft (Proposal)` while its decisions are Ratified.**
**Severity:** Medium. **Where:** `Fractal_Knowledge_Path_Foundation_v0.1.md` line 5 vs. `Fractal_Decision_Register.md` line 41.
The Register heads its decisions "C-013 – C-020 — Knowledge Path Foundation v0.1 · 2026-08-07 · **Ratified**"; C-033(c) defines the effect of review as the status flip `Draft → Ratified (date, per protocol)`. The 2026-08-12 review pass flipped Protocols v0.1–v0.6 and Conversation Settings and did not reach this document — so the source document for eight ratified decisions, including the portability doctrine the whole shipping story rests on, still calls itself a proposal. This is exactly the class of contradiction Scan #1's finding 1.1 was about; the mechanism was built and one document was missed by it.
**Fix:** flip to `Ratified (2026-08-12, per Protocol v0.7)` — the review that ratified C-013–C-020 is on record; only the field was never written. Then sweep: check every canonical document's status field against the Register once, as a one-off.

**S2-2.2 `Reviewed By` fields are inconsistent with the convention C-033 defines.**
**Severity:** Low. **Where:** `Fractal_Conversation_Settings_v0.1.md` line 80 · `Fractal_Node_and_Event_Schema_v0.5.md` line 5 · `Fractal_Node_Template_v0.3.md` line 5 · `Fractal_Architecture_State.md` line 5.
Conversation Settings' control table reads `Reviewed By | Max (2026-08-12, per v0.7)` while its Status and Revision History both record a *second* review on 2026-08-13 per v0.14 — the field absorbed the first review and not the second. `BOOTSTRAP.md` line 5 shows the correct twice-reviewed pattern ("Max (2026-08-12, per v0.8; 2026-08-13, per v0.16)"), so the convention is unambiguous and this is a miss, not a gap. Separately, Schema v0.5, Template v0.3 and Architecture State carry `Status: Ratified …` with **no `Reviewed By` field at all**, though C-033 makes that field part of the ratification record.
**Fix:** one-line corrections; decide whether `Reviewed By` is mandatory on canonical documents (it reads as intended-mandatory) and add it where missing.

**S2-2.3 A §11 standing item has escaped the cumulative ledger.**
**Severity:** Medium. **Where:** `…Protocol_Claude_v0.14.md` §11 line 84 and `…v0.15.md` §11 line 73 vs. `Fractal_Decision_Register.md` lines 182–205.
Both protocols carry, in the §11 list alongside the OQ numbers, "**the WS forge waits on observed need** (Architecture State §4)". It has no OQ row and no disposition; the string "WS forge" does not occur in the Register at all. C-034 is explicit: "every protocol §11 item is swept in with a disposition; items leave only by recorded disposition, never by omission." The item is alive elsewhere — Rule Overview line 86, Architecture State §4, the Local Context — so nothing is lost; what is false is the ledger's completeness claim, and completeness is the ledger's entire value. The tell is that the escapee is the one §11 item that *wasn't already numbered*: the sweep is copying OQ numbers, not reading §11.
**Fix:** OQ-23 — "when is the WS forge triggered?" — disposition **Open (on observed need)**. Then restate the sweep as: every §11 bullet gets a number, or an explicit "not an open question" note.

**S2-2.4 "C-038 acceptance test unexercised" was carried as a §11 item through three protocols without an OQ number.**
**Severity:** Low. **Where:** §11 of v0.14, v0.15, v0.16 vs. the ledger.
Same shape as S2-2.3, softer: the item *was* dispositioned, but inside C-038's own Register entry and folded into OQ-21's resolution, never as a ledger row. A reader applying C-034's rule literally finds nothing. Worth naming because it is the second instance of the same sweep behaviour, and it is now the template for how the integrity-remainder items (whole-repo verification, restore-drill cadence, C-057-vs-network calibration, safety-for-other-writers) are being carried today — in the Local Context and the Agenda Board only, with no ledger row anywhere.
**Fix:** give the integrity-remainder items OQ numbers now, before they acquire the same history.

**S2-2.5 Four protocols have no Return Package, and one Return Package has no protocol.**
**Severity:** Medium. **Where:** `Claude/Context Packages/Conversations/` (14 packages) vs. Protocols v0.1–v0.16.
No Return Package names Protocol **v0.3**, **v0.4**, **v0.5** or **v0.12** as its own. The Local Context version chain corroborates independently: it runs v0.2 → v0.4 → v0.6 → v0.8 → v0.9 → … skipping v0.3, v0.5, v0.7 and v0.13; v0.7 is accounted for by the Scan #1 conversation, leaving three genuinely unrecorded closes. C-001 requires every conversation to close with a Return Package. In the other direction, `Return_Package_2026-08-13_C038-Drill.md` covers no protocol (S2-1.1). Also: `Return_Package_2026-08-07_Knowledge-Path-Foundation.md` and `…_Node-and-Event-Schema.md` name no protocol version at all — they closed with "promote these into a Governance Protocol entry once confirmed", and the promotion happened later without the packages being updated, which is how v0.3/v0.4 lost their handover record.
**Fix:** not reconstructable in full and not worth faking. Record the gap as historical fact (a line in the next protocol), and make the pairing explicit going forward: every conversation closes with a Return Package **and** either a protocol or a recorded reason there is none.

---

## 3. Process & discipline — the mechanism behind §1

**S2-3.1 The close-the-loop refresh has silently narrowed to a fixed triple.**
**Severity:** High. **Where:** the last three Return Packages, §5 in each — verbatim identical.
> "Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Local_Context_Knowledge_Graph.md`."

Three conversations, three identical refresh lines. C-004's update ordering ends in "context-package refresh", which was meant as *whatever the change touched*; in practice it has hardened into a habit covering three documents, and the drift in §1 maps one-to-one onto the documents outside the habit — Context Index (last touched at v0.14, three conversations stale), Architecture State (same), Node Template (same), BOOTSTRAP (touched, not checked), the tools (touched, not checked). This is the single fix with the highest leverage in this scan: **every finding in §1 is a symptom of this one.**
Note also that the line is headed "(project mirrors, per C-004)" while the Project holds **five** mirrors — the Global Context and the Context Index are mirrors too, and they are not in the triple. All five mirrors currently match their canonical copies exactly, so no mirror-vs-source drift exists; the Index mirror is faithfully reproducing a stale source.
**Fix:** replace the habit with a checklist the close-step actually walks — a short standing refresh table naming every living projection and its refresh trigger (Register, Rule Overview, Local Context, Agenda Board, Context Index, Global Context, Architecture State, BOOTSTRAP, plus Schema→Template and the store tools), each ticked *checked* or *changed*. "Checked, unchanged" is the entry that is missing today. This is the concrete, cheap form of the "whole-repo verification / projection-drift checking" already standing in the integrity remainder.

**S2-3.2 Review findings have no cumulative ledger — and have already leaked.**
**Severity:** High. **Where:** C-034 (`Fractal_Decision_Register.md` line 106) vs. Scan #1's findings 1.5 and 2.4.
C-034 was created *because* Scan #1 found protocol §11 items vanishing without disposition (its finding 7.2). It built a cumulative ledger for §11 items and stopped there. Scan findings were left to be dispositioned ad hoc in protocol prose — "retires scan 3.4", "retires scan 4.1/8.2" — which worked for the loud ones and failed for the quiet ones: **1.5 (Medium) and 2.4 (Low) appear in no retirement list, no OQ row, no housekeeping line, anywhere in the corpus** (see §4). The Local Context's careful phrasing, "all **High** findings retired", is true and is also the tell — nobody could say what happened to the rest, so the claim was scoped to what could be checked.
This document contains 24 findings. Without a ledger it will leak in exactly the same proportion, and the leak will be invisible for the same reason.
**Fix:** extend C-034 to review findings — one ledger, stable IDs (this document uses `S2-x.y` for that purpose), disposition `open / fixed / superseded / declined`, and the same rule that an item leaves only by recorded disposition. Retro-register Scan #1's 1.5 and 2.4 as the first two entries. The disposition table at the end of this document is offered as the seed.

**S2-3.3 The "Next" field is not a record of what happened, and nothing records the divergence.**
**Severity:** Low. **Where:** `Return_Package_2026-08-13_Facet-Layer-Completion.md` §7 and `…_Agenda-Board.md` §7.
Both declare "**Workstream E** queued next"; in both cases the next conversation was something else (the Agenda Board interlude, then the board repo-residency conversation). This is not a defect — C-031 makes the queued item an offer and Max's request primary, and both diversions were productive. But it means the Return Package chain reads like a plan and is actually a proposal, and a reader reconstructing history from the "Next" fields alone would build a sequence that never occurred.
**Fix:** one line in the Return Package template — "Previous package queued X; this conversation did Y" — so the baton is auditable in the direction it was actually passed.

**S2-3.4 The drill certified the shape of the rehydration path, not the truth of its contents.**
**Severity:** Medium. **Where:** `BOOTSTRAP.md` §4 drill record; `Fractal_Decision_Register.md` C-038.
The record is precise and honest: "every path this document references resolved, history unbroken, `verify.py` PASS, byte-parity at HEAD." Every one of those is a *structural* check. S2-1.4 is a false statement sitting on the very path that was walked, and it passed the drill because nothing in the drill reads what the documents say. This is not a criticism of the drill — it is the boundary of what "laptop in the ocean" proves, and the boundary is currently unstated, so the green result reads stronger than it is.
**Fix:** state the boundary in BOOTSTRAP §4 in one sentence ("the test proves the corpus rehydrates and verifies; it does not check that projections are current — that is the standing refresh duty"), and add a content check to the drill: the rehydrated copy's version claims must agree with the documents they name.

---

## 4. Unretired residue from Scan #1

**S2-4.1 Finding 1.5 was never fixed — the Foundation still misattributes a decision to the wrong protocol series.**
**Severity:** Medium. **Where:** `Fractal_Knowledge_Path_Foundation_v0.1.md` line 28 and line 117 (Sources).
Line 28: "Governance Protocol v0.2 already rejected embedding relationships into IDs…". Sources: "Governance Protocol — **Claude** v0.2". Claude-series v0.2 is about the Global/Local context spine (C-009–C-012); the ID-embedding rejection is **ChatGPT-era** v0.2. Scan #1 flagged this thirteen protocol versions ago with the exact fix ("correct both Sources to 'ChatGPT-era Governance Protocol v0.2 (pointer)'"); the file has not been modified since 2026-08-07. Two series share a numbering space, C-029 exists to keep them apart, and the one place they are confused is the founding document of the KG domain.
**Fix:** the fix Scan #1 wrote. Two edits.

**S2-4.2 Finding 2.4 was never addressed — `Claude/Project Governance/Templates/` is still an empty folder.**
**Severity:** Low. **Where:** the folder; referenced by nothing in the corpus.
Its exact sibling case, `Context Packages/Domain/`, was diagnosed in the same scan and closed properly by C-054 with a recorded decision. This one was not touched. In a project whose method is "systematically eliminate specifications, and protocol the ones you eliminate", an unexplained empty folder is a specification neither eliminated nor identified — a small thing that is nonetheless precisely off-method.
**Fix:** delete it, or add one line to the Index saying what it is reserved for. Either is a decision; leaving it is not.

---

## 5. Identity system vs. governance

**S2-5.1 The versioned-artifact class has no representation in the identity system.**
**Severity:** Medium. **Where:** C-040 (`Fractal_Decision_Register.md` line 122) and `Fractal_Context_Index_v0.1.md` line 62 vs. `nodes/DOC-01KZVYPW5GQRZM0QV6450B8T3T--node-and-event-schema.md` and `…--node-template.md`.
Governance says canonical specifications are **versioned artifacts**: "every substantive change is a new version/file (C-040)", explicitly "C-005 artifacts, not C-012 living docs". The store says the opposite, in the node body: *"This is a **living canonical document** — the hash freezes the version current at minting; later versions arrive as `revise` events"*, with a versionless title per the C-045 newest-label rule. So one DOC identity spans Schema v0.2 → v0.5 — five files, four superseded and all still on disk — while the Governance Protocols, also sequential, get **one DOC node per version** (v0.1 … v0.16, sixteen nodes). The corpus therefore has three document classes and two store treatments, with the specs landing in the wrong one.
The concrete consequence is already visible: the Register cites "Schema v0.4 §5.4" twice (S2-1.6), and that citation is **unresolvable in the store** — the alias `Fractal_Node_and_Event_Schema` resolves to one id whose hash tracks whatever is current, and v0.4 has no identity at all. The identity system cannot name a superseded version of a document it governs.
**Fix:** pick one, deliberately. Either (a) specs are living documents — then C-040's version-bump discipline is a file-naming convention, say so, and drop version numbers from cross-references; or (b) specs are versioned artifacts — then mint a DOC per version as the protocols do, and let the `Fractal_<Name>` alias point at the newest while each version keeps its own resolvable identity. (b) matches what the documents on disk actually are; (a) matches what the store already does. The cost of (b) is one mint per reissue; the cost of (a) is that "Schema v0.4" stops being a citable thing.

**S2-5.2 `verify.py` proves internal consistency; nothing checks external truth.**
**Severity:** Medium. **Where:** the store README §"Verify"; the whole of §1 above.
The verifier replays the log, checks ULID coherence, mint grammar, root ceremony, alias wiring, every node's fold, and every content hash including external canonical files. All of that is real and all of it passes. What it establishes about an external document is only *"these bytes are the bytes that were hashed at the last `revise`"* — it cannot tell whether the sentence inside says something true about another document. That is why 46 nodes and 179 events are exact to the unit while eleven prose claims are wrong.
This is already named in the integrity remainder as "whole-repo verification / projection-drift checking", carried on the strength of one datum (174/176). This scan supplies eleven more and sharpens the spec: **the missing check is semantic and cross-document — a version-agreement pass — not another hash.** It is also mostly mechanizable: extract every `<Document> v<X.Y>` claim from the corpus, resolve each against the named document's own internal stamp, report disagreements. That is a small script and it would have caught every finding in §1 except S2-1.5's dead file path (which a path-existence check catches) and S2-1.1 (which is a governance question, not a string).
**Fix:** raise it from a parked remainder item to a named next step, spec'd as above.

---

## 6. Repository & hygiene

**S2-6.1 Pre-canon material sits tracked at the canonical repo root with nothing marking it as pre-canon.**
**Severity:** Medium. **Where:** `Vision thought scramble.docx`, repo root — one of exactly three tracked files there, beside `.gitignore` and `BOOTSTRAP.md`.
OQ-22 settled its status deliberately: pre-canon, "informs, never governs". Nothing on disk carries that ruling. `BOOTSTRAP.md` §0 tells a first-contact reader "everything canonical is in this folder tree", and the first thing they see in that tree is an untitled-by-convention `.docx` at the root — no `Fractal_` identity, no control header, no status field, adjacent to the two documents that *are* load-bearing. It also drove the C-056 host decision, so a reader who opens it will find it consequential, which makes the absence of a label worse rather than better. The same question is open for the whole ChatGPT-era layer (OQ-10, still open).
**Fix:** one line in `BOOTSTRAP.md` §0 naming the pre-canon material and its status (C-029 / OQ-22), or a `_pre-canon/` folder. Cheap; and it retires a real first-contact ambiguity in the document whose whole job is first contact.

**S2-6.2 `_to_delete/` has no emptying trigger.**
**Severity:** Low. **Where:** repo root; 9 stale files, oldest 2026-08-12.
Gitignored, never ships, deliberate by design (the `.gitignore` comment describes it as "the sandbox dumpster… emptied by Max, treated like the macOS bin"). But nothing schedules the emptying, so it accretes. It grew again during this scan (see the note below).
**Fix:** a line on the standing housekeeping list, or empty it when it is noticed. Not a governance matter.

**S2-6.3 Orphaned Office owner-files at the root.**
**Severity:** Low. Three `~$*.docx` files from 22–27 July, gitignored, invisible to the repo, visible in Finder. Delete at leisure.

**S2-6.4 Immediate, caused by this session: a stranded `.git/index.lock`.**
**Severity:** Low but **act before your next commit.** The sandbox that ran this scan can create files on your Mac but cannot delete them, so git's transient lock file was left behind by the read-only `git status` calls. Your next `git commit` will fail with *"Unable to create '.git/index.lock': File exists."*
**Fix:** in your terminal, `rm -f ~/Desktop/FRACTAL/.git/index.lock` — then commit normally. (The eight `*.lock.stale.*` files already in `_to_delete/` are the same story from earlier sessions.)

---

## 7. The question this document raises about itself

Max declared this scan canonical in the act of commissioning it. That is a reasonable call — a whole-project review is exactly the kind of durable, referenced, load-bearing artifact that should not be a disposable projection — but it is not a free one, and it lands the corpus with a document class it has never defined. Scan #1 declared itself *"DERIVED PROJECTION — analytical review, not canonical"*; this one says the opposite; nothing distinguishes them but a sentence.

What canonicality actually obliges, by the project's own rules:

- **Identity (C-005).** This document carries `Fractal_LooseEnds_Scan_2`, v0.1. The filename follows Scan #1 and the Return Packages — dated, sequential (C-012 historical artifact). If reviews are canonical, is a review a *living* document that gets revised, or a *sequential* one where scan #3 is a new file? Sequential is the honest answer — a review is a dated observation, and revising it would destroy the record of what was true when.
- **Minting (C-041/C-042).** A canonical document is a DOC node with a `content_hash` freezing its committed bytes and a repo-relative path in its body. This one is unminted (`Document ID: pending`). Scan #1 is unminted too — and if reviews are canonical, it retroactively should be.
- **Status (C-033).** This document is `Proposed` until you accept it. Its *findings* are verified observations; its *fixes* are proposals. That distinction should survive whatever status it ends at, because a canonical review that reads as pre-accepted decisions would quietly become a control file — the thing C-019/C-024/C-026 keep refusing to build.
- **Disposition (S2-3.2).** Canonical or not, findings need a ledger. That is the load-bearing half; canonicality without it just makes the leak official.

**Proposed, for your call:** reviews become a recognized class — canonical, sequential, dated filename, DOC-minted at commit, findings carrying stable `S<n>-x.y` ids that are dispositioned in an extension of the C-034 ledger. Scan #1 is retro-minted and its 1.5 / 2.4 entered as the ledger's first open rows. That would need one decision (call it C-058) and would close S2-3.2, S2-4.1 and S2-4.2 in the same move.

---

## Non-findings checked (verified consistent)

- **`verify.py` PASS** — 179 events, 46 entities, 19 codes, roots `AGENT AST CTX FACET GBL GOV KG`, 22 route tokens, 0 redirects, **0 collisions in history**, 0 warnings. Counts match the Local Context and the Agenda Board to the unit.
- **Git:** working tree clean; `main` in sync with `origin/main` (0 ahead, 0 behind); remote `git@github.com:mstruppe/fractal.git`; commit history unbroken to the 2026-08-12 baseline; both C-037 author identities present.
- **`.gitignore`** covers `.DS_Store`, `~$*`, `_to_delete/` and nothing else — knowledge is never ignored, exactly as C-037 requires. 135 tracked files.
- **Decision ledger arithmetically complete:** C-001 → C-057, no gaps, every decision traceable to a source protocol. **OQ ledger:** OQ-1 → OQ-22, no gaps, every row dispositioned.
- **`Fractal_Rule_Overview.md` v0.12** — every version citation current, coverage reaches C-057 and OQ-22, drill result recorded. The best-maintained document in the corpus; it is what the others should look like.
- **Local Context v0.19 and Agenda Board v0.19** agree on stamp, date, counts and every version claim. The C-047/C-048 stamped-projection mechanism is working exactly as designed — including the stamp-comparison staleness check, which is the one drift detector in the corpus that actually fires.
- **Knowledge Graph Store `README.md`** — every citation current (Schema v0.5, `part-0001.jsonl`, C-055, C-049/C-050 ritual). Scan #1's finding 5.3 (the misleading one-grep traces) is genuinely fixed: the authorship trace now filters on `"role": "by"` and the prefix scan correctly drops the closing quote.
- **`Fractal_Global_Context_v0.1.md` v0.3** — correct throughout; its "(v0.4 inside)" pointer is the model S2-1.4 should follow.
- **All five Project mirrors** match their canonical disk copies at the same versions — no mirror-vs-source drift. The Custom-Instructions projection carries the correct `v0.4, 2026-08-13` stamp (C-035/C-054).
- **Conversation Settings §11's two items** are correctly swept into the ledger as OQ-9 and OQ-16 with sources naming the sweep — C-034 working as intended where it was applied.
- **Schema v0.5 §4.1, §5.4 and §5.5** exist at the section numbers the stale pointers cite, so every finding in S2-1.6 lands the reader on the right rule in the wrong file — a naming defect, not a content one.
- **Scan #1 findings verified retired:** 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3, 6.1, 6.2, 7.1, 7.2, 8.1, 8.2 — 24 of 26, each against its cited source rather than against the claim that it was retired. Only 1.5 and 2.4 remain (S2-4.1, S2-4.2).

---

## Disposition ledger (seed — per S2-3.2)

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| S1-1.5 | Foundation misattributes ChatGPT-era Protocol v0.2 to the Claude series | Med | **Open** (carried from Scan #1, 2026-08-12) |
| S1-2.4 | `Project Governance/Templates/` empty, referenced by nothing | Low | **Open** (carried from Scan #1) |
| S2-1.1 | C-038 drill recorded in no protocol; projection overrides source | High | Open |
| S2-1.2 | Architecture State not current about currency | High | Open |
| S2-1.3 | Context Index stale in four current-state claims | High | Open |
| S2-1.4 | BOOTSTRAP §1 self-contradicts on Conversation Settings version | Med | Open |
| S2-1.5 | Node Template names Schema v0.3 and a retired log filename | Med | Open |
| S2-1.6 | Register "Normative home" stale for C-049/C-050; Sources stale | Med | Open |
| S2-1.7 | `verify.py` / `mint.py` headers cite Schema v0.4 | Low | Open |
| S2-2.1 | Knowledge Path Foundation still `Draft (Proposal)` | Med | Open |
| S2-2.2 | `Reviewed By` stale / missing across four documents | Low | Open |
| S2-2.3 | "WS forge" §11 item has no ledger row | Med | Open |
| S2-2.4 | "C-038 test unexercised" carried three times without an OQ number | Low | Open |
| S2-2.5 | Protocols v0.3/v0.4/v0.5/v0.12 have no Return Package | Med | Open |
| S2-3.1 | Close-the-loop refresh narrowed to a fixed triple | High | Open |
| S2-3.2 | Review findings have no cumulative ledger | High | Open |
| S2-3.3 | "Next" field diverges from what happened, unrecorded | Low | Open |
| S2-3.4 | Drill certifies structure, not content; boundary unstated | Med | Open |
| S2-4.1 | (= S1-1.5) still unfixed | Med | Open |
| S2-4.2 | (= S1-2.4) still unaddressed | Low | Open |
| S2-5.1 | Versioned-artifact class has no store representation | Med | Open |
| S2-5.2 | Nothing checks projection claims; the needed check is semantic | Med | Open |
| S2-6.1 | Pre-canon `.docx` tracked at the canonical root, unlabelled | Med | Open |
| S2-6.2 | `_to_delete/` has no emptying trigger | Low | Open |
| S2-6.3 | Orphaned `~$*.docx` owner-files at the root | Low | Open |
| S2-6.4 | Stranded `.git/index.lock` — clear before next commit | Low | **Action now** |

---

**Sources:** the full Claude-era corpus at `Desktop/FRACTAL/` as of 2026-08-13, HEAD `0bd546e` — Global Context v0.3; Context Index v0.9; Conversation Settings v0.4; Decision Register v0.14; Rule Overview v0.12; Architecture State v0.1; Knowledge Path Foundation v0.1; Node & Event Schema v0.4 and v0.5; Node Template v0.3; Governance Protocols — Claude Series v0.14, v0.15, v0.16; all 14 Return Packages; `BOOTSTRAP.md` v0.3; `Fractal_Agenda_Board.html` v0.19; Local Context — Knowledge Graph v0.19; the live Knowledge Graph Store (`nodes/`, `_events/part-0001.jsonl`, `README.md`, `verify.py`, `mint.py`) and a fresh `verify.py` run; the git repository (status, log, remote, tracked-file set); the five Claude Project mirrors; `Review_2026-08-12_LooseEnds-Scan.md` (baseline).

**Method:** read-only. No file in `Desktop/FRACTAL/` was modified by this scan except the sandbox artifact noted in S2-6.4. Every finding was verified against its cited source file and line rather than against any document's claim about it; findings that did not reproduce were dropped. Line numbers refer to the files as of HEAD `0bd546e`.

**Provenance:** FRACTAL whole-project loose-ends scan #2, 2026-08-14, commissioned by Max in the conversation following the C-038 drill. Declared canonical at commission (see §7 — the class this implies is itself a proposal). Findings are verified observations; fixes are proposals, not accepted decisions.

**Revision history:** v0.1 (2026-08-14) first issue — 24 findings across currency drift, governance & ratification, process discipline, Scan #1 residue, identity-vs-governance, and repository hygiene; disposition ledger seeded with Scan #1's two unretired items.
