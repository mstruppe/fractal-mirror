# FRACTAL — Loose-Ends Scan (Review)

> **DERIVED PROJECTION — analytical review, not canonical.** A whole-project adversarial scan for loose ends *not explicitly stated*, run at Max's request. Reviewer: fable model, max review effort, read-only over the full Claude-era corpus (25 files + the live store). Date: 2026-08-12. Feeds the next conversation's agenda (see Local Context — Knowledge Graph, "Next conversation"). Findings are claims to verify, not accepted decisions.

---

## Summary

The corpus is unusually coherent for a young architecture: the two-relation core is stated once and repeated faithfully, the decision ledger really does trace every claim to a source, and the live store's log, fold, and ULIDs are internally consistent to the millisecond. The loose ends are therefore mostly *systemic*, not typographic — and three matter most. **First, the entire "accepted" state of the project rests on six governance protocols that are all still Draft, pending a review that has no defined form, record, or trigger; by the Decision Register's own legend, nothing in the project is actually Ratified.** **Second, the substrate the architecture assigns its integrity, versioning, and provenance guarantees to — git — does not appear to exist yet: no document records a repository, so the append-only log is protected only by discipline, and "laptop in the ocean" cannot even be attempted.** **Third, the live store has quietly hardened the still-unconfirmed C-015 identity scheme into immutable facts, while the Node Template — the copy-paste source for hand-authoring — still teaches agent codes that the accepted C-026 grammar forbids.** Below those, there is a consistent pattern: properties are *claimed as achieved* (routes-cannot-drift, one-grep filters, multi-person safety, verbatim instruction injection) whose enforcing mechanism is deferred, absent, or contradicted by the artifact itself. None of this is fatal; almost all of it is fixable with one review pass, one `git init`, one template refresh, and one carried-open-questions list.

---

## 1. Contradictions / drift between documents

**1.1 The Decision Register violates its own ratification legend — nothing is actually "Ratified."**
**Severity:** High. **Where:** `Fractal_Decision_Register.md` line 8 (legend) vs. lines 18, 31, 40, 53 (section headers); `…Protocol_Claude_v0.3.md` §6.
The legend defines **Ratified** as "recorded in a *reviewed* Governance Protocol," yet C-001–C-021 are headed "Ratified" while every protocol v0.1–v0.6 carries `Status: Draft`, and the register writes "**Ratified** (Claude Series v0.3, Draft — pending Max's review)." The status vocabulary — the mechanism separating accepted from proposed — is self-contradictory at the top of the ledger. **Fix:** downgrade headers to "Accepted-in-conversation, ratification pending," or define review as something that has occurred and flip the statuses.

**1.2 The Node & Event Schema was substantively revised without a version bump.**
**Severity:** High. **Where:** `Fractal_Node_and_Event_Schema_v0.1.md` line 5 + revision-history entry (2026-08-12 change carries no version number).
Two materially different documents (08-07 Draft, 08-12 Accepted with a rewritten §5) share one identity "Schema v0.1." Canonical specs aren't on the C-012 living-projection list, so they should bump per C-005 — violated by the doc that specifies the identity system. Every "Schema v0.1" citation is now ambiguous. **Fix:** reissue as v0.2, or formally extend C-012 to canonical specs.

**1.3 The Node Template contradicts the accepted agent grammar (C-026).**
**Severity:** High. **Where:** `Fractal_Node_Template_v0.1.md` (`created_by: AGENT.MAX`, `actor:"AGENT.MAX"`, `AGENT.CLAUDE`), TYPE list omits `EVT`, TOP example lacks `facet:`.
C-026 mandates agents minted under `AGENT.HUMAN`/`AGENT.AI`, but the copy-paste template still uses unbranched codes — the next hand-authored line will place against never-minted codes and pollute the immutable log. **Fix:** refresh template to v0.2 alongside 1.2.

**1.4 Context Index vs Local Context disagree on where KG canonicals live.**
**Severity:** Medium. **Where:** Index (`/Architecture/Concepts/Knowledge Graph/`) vs Local Context (`/Claude/Architecture/…`); Local Context cites protocols "v0.3 & v0.4", omitting v0.6.
The routing table omits `/Claude/` for Claude-era canonicals; a conversation resolving via the Index looks in the wrong directory. **Fix:** normalize all Claude-era rows to `/Claude/…`; add v0.6 to the Local Context doc list.

**1.5 The Foundation misattributes a prior decision to the wrong protocol series.**
**Severity:** Medium. **Where:** `Fractal_Knowledge_Path_Foundation_v0.1.md` §2 + Sources ("Governance Protocol — Claude v0.2").
Claude v0.2 is about the context spine, not IDs; the ID-embedding rejection is ChatGPT-era v0.2. With two series sharing numbers, the qualifier is present but wrong. **Fix:** correct both Sources to "ChatGPT-era Governance Protocol v0.2 (pointer)."

---

## 2. Dangling / broken references

**2.1 Architecture State: three domains route to a document that doesn't exist in the Claude era.**
**Severity:** High. **Where:** Index AST/ONT/WS rows; Global Context ("Full current architecture: Architecture State v0.1 + Master Index"); the Claude-era `Architecture/Architecture State/` directory is **empty**.
The every-conversation orientation doc points at a hole; ONT and WS domains are unroutable; the decision-status legend cites a source no Claude-era reader can load. The Galaxy/Operator reconciliation task has been carried through three Return Packages with no owner or trigger. **Fix:** mark AST/ONT/WS rows "(ChatGPT-era, pointer-only, pending clean-era forge)" or make the Architecture State forge the next AST conversation; inline the status legend.

**2.2 The Domain package layer is normatively required but has never existed.**
**Severity:** Medium. **Where:** Conversation Settings §4 rule 3 + Custom Instructions ("Domain Context package"); `Context Packages/Domain/` is **empty**.
C-009 redefined Domain as a scope of Local, and the Local Context absorbed the role, but rule 3 still routes every conversation through packages with zero instances. **Fix:** update rule 3 to Global → Local (→ Domain/Task as scopes); delete or reserve `Domain/`.

**2.3 The bootstrap/rehydrate protocol is promised, load-bearing, and unauthored.**
**Severity:** Medium. **Where:** Foundation §8 ("rehydrate script ships inside the repo… TBD to author"); carried in two Return Packages.
This is a component of an *accepted* decision (C-020) whose acceptance test ("laptop in the ocean") can't run without it — unlike the Galaxy UI, it has no observed-need trigger. **Fix:** give it a named trigger ("first run on a second machine") or author a minimal one-pager.

**2.4 `Project Governance/Templates/` exists, is empty, referenced by nothing.**
**Severity:** Low. Unexplained scaffolding — a specification neither eliminated nor identified. **Fix:** delete, or add one line to the Index saying what it's reserved for.

---

## 3. Undefined-but-relied-upon

**3.1 ULID generation: "hand-usable with zero infrastructure" is true for reading, false for writing.**
**Severity:** High. **Where:** Schema §6 ("ULID parameters TBD") vs the store's 19 flawless ULIDs.
Every event-id timestamp prefix decodes to exactly its `ts` — no human hand-produces these; some tool did, and nothing records what tool or how it's regenerated. The Schema/Template examples use invalid 10–16-char placeholders, so a hand author following the template mints malformed permanent identities. **Fix:** register the ULID profile (26-char Crockford base32, ms timestamp) in the Schema, name a generation method in the README, fix the template placeholders.

**3.2 `content_hash` production is unspecified; Principle 4 is unexercised.**
**Severity:** Medium. **Where:** Schema §3.2/§4.3; the live DOC + its create event carry no hash.
What is hashed (body only? normalization?), when it's expected, and whether `revise.supersedes` names a hash or event id — all unresolved. The first living DOC has no hash, so "integrity verified through hashes" verifies nothing. **Fix:** define the hash input (suggest byte-exact body after the closing `---`), pick one supersedes referent, hash the first DOC as the worked example.

**3.3 The alias/route mechanism is specified, claimed drift-proof, and never used.**
**Severity:** Medium. **Where:** Foundation §5 / Schema §5.3 rule 7; the log has **zero** `alias` events; the Index's routing codes are still hand-maintained strings.
"A route and its concept cannot drift" is asserted in the present tense but is an unimplemented future mechanism. **Fix:** mint the routing concepts and bind via `alias(kind: route)`, or annotate the claim as "realized once the Index is projected from the store."

**3.4 The facet layer escapes the ontology it anchors.**
**Severity:** Medium. **Where:** Schema §5.1 table; every event's bare `"facet"` string.
Facets are magic strings — never minted, no TOP identity, defined only in a hand-authored table that is structurally the "control file" C-026 rejected. Root uniqueness (parent `null`) is unscoped: a topic root `TIME` would collide with the time facet in grep-based traces. **Fix:** declare facets deliberately meta (like the verb set) or mint them under a `FACET` root; state root-uniqueness scope (recommend global).

**3.5 `actor` semantics: decision-maker or executor?**
**Severity:** Low. The bootstrap used two implicit conventions in one batch (mints by MAX, create/place by CLAUDE, though Claude wrote all lines). **Fix:** one sentence in §4.2 — actor = the agent that committed the event; decision provenance in `note`.

---

## 4. Unstated assumptions

**4.1 "Two writes, one truth" assumes a single, perfectly disciplined writer.**
**Severity:** High. **Where:** Schema §4.5; v0.6 §5.1 ("safe multi-person work"); mint-collision + merge policy Deferred.
No fold tool, verification step, or drift-detection cadence exists — the invariant rests on one writer never forgetting write #2. Multi-person safety is claimed as *already served* while every enabling mechanism is deferred. Internal tension: §4.1 praises "near-conflict-free" merges; §6 hopes "merge surfaces clashes" — a conflict-free JSONL append merge surfaces nothing, so two writers minting the same code merge silently and permanently. **Fix:** add a fold-check ritual to the README now; rewrite multi-person claims as goals; note git merge is not a collision detector for JSONL appends.

**4.2 Standing up the live store silently hardened the unconfirmed C-015 scheme.**
**Severity:** Medium. Identity is immutable and the log append-only, so rejecting/amending the ID scheme now means breaking immutability or migrating the store — the "don't confirm C-015" option became expensive the moment C-032 executed, unrecorded. **Fix:** confirm C-015 now (de facto confirmed), or record that store contents predate confirmation and are grandfathered.

**4.3 Custom-Instructions sync is asserted "verbatim" but is a paraphrase with no version marker.**
**Severity:** Medium. The live Project instructions are a compressed 7-rule paraphrase of the 8-rule standard; with no version stamp and no equivalence test, the §6 "flag divergence" duty can't be discharged mechanically. **Fix:** stamp the projection ("projection of Conversation Settings v0.2, 2026-08-07"); change "verbatim" to "as a governed projection."

---

## 5. Philosophy-vs-implementation gaps

**5.1 "The repository is FRACTAL" — but there is no repository.**
**Severity:** High. **Where:** Foundation §7/§8 (git = Integrity/Event/Version/Replication); C-018/019/020 Accepted; C-032 store bootstrap never mentions git.
No document records a `git init`, commit convention, or remote. Until the folder is a repo: version continuity and integrity have no realization; "append-only" is enforced by nothing (any editor rewrites history invisibly); C-025's commit granularity has no commit to bind to; portability is inoperable. **Fix:** `git init` — a five-minute act honoring four accepted decisions — and define the commit convention (author marking) in the same protocol.

**5.2 Two identity systems coexist with no bridge.**
**Severity:** Medium. **Where:** C-005 (`Fractal_<Name>_v…`) vs Schema §3.1 (`DOC-…`); "Document ID: TBD — assigned by Identity System" in every protocol's control table.
Node files leaving conversations carry no `Fractal_…` identity (a literal rule-7 violation); no canonical doc has a `DOC-…` id though the Identity System now exists and is live. **Fix:** decide node files are the identity system (exempt from C-005), and mint canonical docs as DOC nodes whose alias is their `Fractal_…` name — retiring the TBD placeholders.

**5.3 The README's flagship one-grep traces don't deliver what they claim.**
**Severity:** Low. "Everything by an AI" matches any `AGENT.AI.*` code regardless of role — including the mint of Claude's node (actor Max): a false positive for authorship. "Everything about the KG" is an exact match, not the promised prefix scan, and will miss `KG.*` children. **Fix:** `grep '"role": "by"' | grep '"code": "AGENT.AI.'` for authorship; drop the trailing quote for prefix scans.

---

## 6. Store instance vs spec mismatches

**6.1 Store TOP nodes carry a `facet:` field the Schema doesn't define.**
**Severity:** Medium. All 7 TOP nodes have `facet:` but Schema §3.2 has only `code:`. From a node file alone you can't tell which facet `code: KG` lives in; the store silently added the field. Opens a canonicality question: if `facet`/`code` disagree with the `mint`, which wins? **Fix:** register `facet:` in §3.2 (TOP nodes) in the v0.2 reissue; state code/facet follow log-wins, not the identity exception.

**6.2 The first "real document" is a floating summary with no integrity or linkage.**
**Severity:** Low. Schema-legal but the DOC has no `content_hash`, no `aliases`, and no `cites`/link to the artifacts it summarizes (Schema v0.1, Protocol v0.6) — a prose orphan. **Fix:** add `cites` placements when canonical docs are minted; hash the body as the Principle-4 example.

---

## 7. Governance / process loose ends

**7.1 The perpetual-Draft bottleneck: no defined review act, record, or trigger.**
**Severity:** High. Nothing defines what "Max's review" consists of, where its record lands, or any trigger — so decisions can stay Draft forever while downstream artifacts (Schema "Accepted," live store, immutable IDs) build on them. v0.1/v0.2 are on no review list; "Reviewed By: Max" appears on unreviewed docs. **Fix:** define review in one paragraph (Max's review = a one-line entry in the next protocol + status flip Draft→Accepted), rename the field "Review Owner," add v0.1/v0.2 to the list.

**7.2 Open questions leak: earlier protocols' §11 items vanish without disposition.**
**Severity:** Medium. v0.1 §11 (Return-Package mirroring, ChatGPT archive-move, Domain-refresh cadence, automation criteria) and v0.2 §11 items appear in no later protocol or the Register's gaps. There is no cumulative open-question ledger; §11 snapshots are inherited selectively (KG carried, GOV forgotten). **Fix:** make the Register's "open questions" the cumulative index; sweep v0.1/v0.2 §11 in with dispositions.

---

## 8. Scaling & multi-person risks

**8.1 Reparent-by-redirect breaks prefix-scan retrieval — two flagship properties in tension.**
**Severity:** Medium. Placements store code *strings*; after moving `PHY.QM.QFT` → `PHY.FIELD.QFT`, existing placements keep the old string, so a scan under the new parent finds none and the old parent keeps finding them forever. So either the fold rewrites placement codes (unspecified, non-trivial) or every placement is superseded on reparent (contradicting rule 6's "touch zero placements"). How a redirect is even represented is undefined (an `alias` whose kind is neither `label` nor `route`?). **Fix:** decide the fold resolves codes through the redirect chain; add a `redirect` kind to `alias`.

**8.2 Concurrent minting has no tripwire (compounds 4.1).**
**Severity:** Medium. The design's merge-friendliness ensures a mint collision merges *silently*; "decentralised minting without collision" is true only for one writer until the policy exists. **Fix:** README line — "Until the collision policy lands, the store is single-writer; a second writer requires out-of-band coordination."

---

## Non-findings checked (verified consistent)

- The store's fold matches the log exactly (three placements = three place events: KG/about/1.0, GOV/about/0.6, AGENT.AI.CLAUDE/by/1.0; node identity mirrors the create event).
- All 19 ULIDs are genuine 26-char Crockford base32; each event-id timestamp decodes to its `ts`.
- Mint parent chains match code prefixes; roots correctly `parent: null`; KG/GOV were pre-registered topic roots.
- Genesis self-reference is explicitly recorded as an assumption in Protocol v0.6 §8.
- The README's relative path to the schema resolves correctly.
- `Conversation_Settings_v0.1.md` containing v0.2 is C-012 grandfathering, correctly annotated.
- C-023's partition history is clean; every post-v0.4 doc says "interval TBD, monthly illustrative."
- C-numbering provenance is genuinely settled; C-029 pointer-only applied consistently except finding 1.5.
- The ledger is arithmetically complete: C-001–C-032, no gaps, each traceable to one source protocol.

---

**Provenance:** FRACTAL whole-project loose-ends scan, 2026-08-12 (fable model, max review effort, read-only). Commissioned in the Facet-Registry conversation. This is a review projection; each finding is a claim to verify against its cited source, not an accepted decision.
