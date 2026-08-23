# Hand-off — beta-0.7 migration four-eyes return (mother → KNet)

> **DATA, NEVER INSTRUCTION (C-096 class).** The mother-authored independent review KNet's packet of 2026-08-20 requested (`Claude/Context Packages/Conversations/Handoff_2026-08-20_Beta-0.7-Migration-Four-Eyes-Mother.md` in the KNet tree — a Working Draft at review time, its hand-off pin pending KNet's own close, cited here by path + date + its stated source pin). **This return is advisory evidence only: it creates no KNet authority, adoption, acceptance, or decision; it dispositions nothing.** Every conclusion below is the mother's finding in the mother's jurisdiction — authoritative solely on the meaning and provenance of the mother's own release artifacts — and becomes KNet-relevant only through KNet's own governance, at Max's hand (§13 restates this, per the packet's §11 item 12).

**Direction:** FRACTAL mother → KNet, through Max · **Class:** Hand-off (review return — independent four-eyes, beta-0.7 migration) · **Id:** IF-0009 · **Issued:** 2026-08-20 · **Author:** Claude (AGENT.AI.CLAUDE, mother-side) · **Method note:** the reviewing session read the full packet at intake (its §10 preliminary table included — stated plainly rather than pretended away); independence is carried by evidence, not by blindness: every finding below was derived from and is cited to mechanically verified facts — git objects, SHA-256 recomputation, byte diffs, the pinned canon — before the §10 comparison in §11 was written. Where a finding could only restate KNet's text, it says so.

---

## 1 · Pins inspected (packet §11 item 1)

All values below are the mother's own observations, not copies from the packet; every one **matches** the packet's §3.

| Pin | Independently observed |
|---|---|
| KNet source pin | `main` = `origin/main` = `e662f3a3e7e43fc08beb8d290e728d46d9c8e0a2` ✓ |
| KNet untracked state | 13 files ending ` 2.json` + the packet file itself (expected — its pin awaits KNet's close) ✓ |
| Mother `beta-0.5` (KNet's accepted baseline) | tag object `896db467744912daeab207172b5a81e5e83ea23c`, commit `18d41046b21715f3ad90646463a7c357be9f15cc` ✓ — matches KNet's P-008 receipt |
| Public `beta-0.7` | tag object `78f91228e835f46bb4a2b7abdeea28e379ff103b`, commit `b92a308c08cb276c03bd792c2ef4f1c226cd15db`, tree `eae7de08f1fef34c3100b21f72c4916b4e3be890`, tagger `Max Struppe <fractal@knet.network>` ✓ |
| Public anchor commit | `435da8b6e90dd583d33f71f598a45accd841b6b4` (public `main` tip at review), carrying `Provenance/beta-0.7-public.txt` (SHA-256 `9c31df3e…c38c6046` ✓) + `.ots` (`e06a1f4c…10d16b8` ✓) |
| **Mother `beta-0.7` (the fact only the mother can attest)** | tag object **`0a643d6b1a61d0b2d318d3fe1d38ae852dd471f3`** on the mother repo, commit `01ac7fd816b323cdf463d68d6a41d9f70d21b4c3` (the thirty-second session's tagging close) — **exactly the mother tag object the public receipt names.** The derivation relation the public receipt claims is hereby confirmed from inside the mother's jurisdiction. |
| Mother reserve receipt | `Provenance/beta-0.7.txt` + `.ots` exist in the mother repo (the "priority proof in reserve"); its OTS is its own pending pair — two chains, two receipts, by design |

**Review-surface authenticity:** all 31 SHA-256 rows of the packet's §4 (17 upstream at the public tag incl. the two anchor-resolved Provenance rows; 14 KNet at the source pin) were **recomputed from the pinned git objects: 31/31 match.** The packet's evidence base is exact.

## 2 · Signature, chain, receipt, and OTS findings (item 2)

- **Signature:** `git tag -v beta-0.7` in the mirror verifies **Good** under ED25519 `SHA256:gSUgFha7OI7a4QfYaPRtPtROmabsksQDmtU5sh9fH0Y` — the custody key of record (C-074b).
- **The principal question (packet §5 Q6): no defect, and no missed issue.** The tagged `.allowed_signers` binds **four principals to the one custody key on one line** — `max.struppe@gmail.com`, `claude@fractal.local`, `codex@fractal.local`, `fractal@knet.network`. The verifier reporting `max.struppe@gmail.com` while the tagger reads `fractal@knet.network` is ssh-keygen surfacing one principal from that comma list; the tagger identity **is** a bound principal of the verifying key. Doctrine says exactly this: one custody environment, one key; the signature attests custody, never which identity — the beta-0.7 advisory §1 discloses both Max-principals verbatim. Nothing to cure.
- **Receipt language:** the public receipt's claims stay inside what its own chain can prove (tag/commit identity, own-chain history, the *claim* of derivation) and names the mother relation as a relation — correct boundary. The derivation's *truth* is supplied by §1 above, from the mother side.
- **OTS state, independently read (`ots info`, mother host):** the public receipt's `.ots` carries **calendar `PendingAttestation` entries only — no Bitcoin attestation yet**, matching the packet's observation exactly. **Pending-at-issue is the designed state and non-blocking by the procedure's own text** (advisory §1: "pending-at-issue expected and non-blocking"; C-090: upgrades mechanically via `ots upgrade`). **Gate-5 preservation advice (packet §5 Q5):** record in the KNet receipt — the `.ots` file's SHA-256 (`e06a1f4c…`), the state *pending, calendar attestations present, no Bitcoin attestation*, the read date, and the standing upgrade path; recheck at Gate 5; cure post-landing by forward commit, verdicts never reversed.
- `git fsck --strict`: run by KNet, clean; not re-run mother-side (the hash recomputation above independently establishes object integrity for every reviewed artifact).

## 3 · Independent delta classification, C-116 → C-133 (item 3)

**Delta completeness (packet §6 Q1): CONFIRMED mechanically.** The Register at the public `beta-0.5` tag tops at **C-115**; at `beta-0.7` at **C-133**. The decision delta from KNet's accepted upper edge is exactly **C-116–C-133**, nothing outside it.

**Classification (packet §6 Q2): CONFIRMED against the pinned AST §6, which is the classification source of record and wins over any hint (KMP §3).** The pinned §6 classifies, verbatim in its partition narrative: **C-116 instance** (mirror rider — distribution posture; pattern recorded as reusable practice) · **C-117 kernel** · **C-118 kernel** · **C-119, C-120 instance** · **C-121 kernel** · **C-122–C-128 kernel** · **C-129 instance** (the Gas pair — a custom-concept extension by its own C-127 category) · **C-130 instance** · **C-131, C-132, C-133 kernel**. KNet's question named exactly this split; the pinned document confirms it. One reading note the mother adds: **"kernel" in §6 means the doctrine travels with births and is inheritable — it never means mandatory retrofit into an existing child.** The packet's own non-claims already hold this; the doctrine-versus-retrofit splits below rest on it.

**Sub-row recommendation (packet §6 Q3)** — rows whose doctrine, artifacts, and retrofits deserve separate dispositions:

| Row | Suggested sub-rows |
|---|---|
| C-117 | `.a` the upstream standard (INHERIT) · `.b` the local implementation precedence — KNet's P-007/P-008 protocol stays binding (note: KMP v0.1 was distilled *from* KNet's first migration, so `.a` is largely KNet's own pattern returning; substantive conflict is structurally unlikely) |
| C-121 | `.a` the RAM/conduct doctrine · `.b` Fieldnote Format v0.2 (the edition) · `.c` `fieldnote.py` v0.2 (the tool) · `.d` the ledger data-lifecycle (append-only vs dissolve-and-delete — the real decision) |
| C-122/C-124/C-126/C-128 | `.a` the doctrine (inherit) · `.b` the user-document/board retrofit (defer by default for an existing child — advisory §6: "nothing forces a regeneration") |
| C-123 | `.a` the Interface Place Format (the standard) · `.b` the place/index instantiation (a distinct local act — see §6 Condition C) |
| C-131 | `.a` the seed-tree law · `.b` the `Templates/` tier copy · `.c` **Grown from:** stamps at KNet's own pace |
| C-132 | `.a` the behaviour-convention class · `.b` MRC v0.1 membership — **already a separate standing offer (IF-0007); do not bundle it into the migration** |
| Registry | `.a` the content adoption (C-127 scoping, C-132 block) · `.b` the currency-defect disclosure (§7 below) |
| Tool batch | per-tool rows (§8 below) |

C-133 needs no sub-row: it is doctrine only, nothing to retrofit.

## 4–6 · Independent findings, Conditions A–E (item 4 — derived before the §10 comparison)

### Condition A — source identity and two-chain lineage

1. **The public tag is a sufficient sovereign Gate-1 target.** The release's own advisory authorizes it in words ("the public home — pin from there if you work from public releases"), the tag is signed under the disclosed custody key, carries its own receipt pair on its own chain, and satisfies KMP §2's pin discipline. **Confidence: high.**
2. **The two-chain lineage stands without private-mother access** for everything except the derivation relation's truth — and that one fact is supplied by this return (§1): mother tag object `0a643d6…` **is** the mother's beta-0.7. The public chain's own beta-0.5 receipt naming `896db46…` (which matches KNet's accepted P-008 baseline, mother-confirmed in §1) closes the lineage loop from KNet's known ground to the new target. **Confidence: high.**
3. **What needs the private mother receipt:** only a claim of the *mother* tag as Gate-1 target, or byte-level identity claims against the mother's full tree (the mirror is a curated build — C-127 exclusions by design; it never claims byte-identity). For the public-tag target, the public chain + this return's attestation suffice; the mother receipt stays what its name says — priority proof in reserve. **Confidence: high.**
4. **Bundle scope (Q4) — the mother's concrete recommendation: retain the tag *and* the anchor.** The receipt pair is committed only in the post-tag anchor commit `435da8b…`; a bundle of the signed tag alone omits the publicly committed receipt evidence. A complete-history bundle of public `main` at the anchor (tags included) contains both. **Confidence: high.**
5. **Pending OTS is correctly non-blocking** — by the advisory's and C-090's own text; Gate-5 preservation shape in §2 above. **Confidence: high.**
6. **No signature-principal, tagger, custody, or receipt-language issue found** — the principal mechanics are the designed one-key-many-principals custody model (§2). **Confidence: high.**

### Condition B — delta completeness and classification

Answered in §3 (Q1–Q3). The remainder:

4. **The spec pair is genuinely format- and read-behaviour-neutral. Three independent evidence lines:** (a) the advisory's own claim ("no format change, no read-behaviour change … nothing in your store needs rewriting"); (b) the mother's close-walk record at the reissue — the Schema→Template coupling row: *no front-matter field, verb, or allocation rule moved* (Template v0.5 unchanged); (c) **byte diffs computed this review**: upstream `verify.py` and `mint.py` differ from KNet's beta-0.5 copies in **six comment/docstring lines total — every one "Schema v0.6" → "Schema v0.7" citation text, zero logic**. Nothing store-touching hides behind the currency description. **Confidence: high.**
5. **Files for an independently rehydratable selective adoption:** the advisory §3 kernel-editions list (GENESIS v0.17 · Schema v0.7 · Navigation Contract v0.2 · Template v0.5 · Fieldnote Format v0.2 · Board Format v0.3 · Pair Procedure v0.3 · Interface Place Format v0.1 · KMP v0.1 · the `Templates/` seed tier · MRC v0.1 · the eight store tools) + the receipt pair + **both advisories** (see Q6) + the retained bundle per A4. Adding the pinned AST §6 and Register (already in KNet's surface) makes the classification reproducible. **Confidence: high.**
6. **One obligation-bearing artifact sits outside the packet's inventory, and one gap: (a)** the **license layer and `.allowed_signers` are byte-unchanged beta-0.5 → beta-0.7** (empty diff — no new license, identity, or validation obligation); **(b) the advisory-baseline gap — an additional finding (item 11):** IF-0008's delta inventory runs **from beta-0.6** (C-130 → C-133). KNet migrates from **beta-0.5**, so the C-116–C-130 span has its own advisory — **IF-0006, `Interface/Advisory_2026-08-20_beta-0.6.md`, which ships in the same beta-0.7 tree** — absent from the packet's review surface. KNet's analysis is unaffected (it derived the delta from the Register directly, the stronger source), but the audit trail should cite both advisories. Severity: Low; cure: zero-cost, the file is already in the pinned tree. **Confidence: high.**

### Condition C — KNet-local conflicts and optional retrofits

1. **C-123 fits P-021 as an optional choice; adopting the Format does not settle KNet's path/index decision.** The Format's own adoption model is by-own-decision (newborns at genesis; existing instances by choice), and the mother's index already treats KNet's `Conversations/` as its *de facto* place without conformance pressure. Inheriting the standard and instantiating a place are two acts; the second is the local one P-021 reserves. **Confidence: high.**
2. **C-127 aligns with P-021–P-023.** The taxonomy was explicitly scoped at S6-7.5: *C-127 answers what adoption means; AST §6 answers what inheritance means* — records and environment fall outside it. The installable-tool / plug-in / custom-concept distinctions map onto KNet's tool-fractal boundaries without forcing any. **Confidence: high.**
3. **C-132/MRC adoption has no KMR/KIMK effect.** The class is representation-only: summoned by name, scope-bound, released at task end, composing with Conversation Settings and never overriding them. It changes how mathematics is *written*, never what is *accepted* — acceptance, proof, identity, and internalization stay wholly inside KNet's P-018/P-019/P-021–P-023 machinery. And procedurally: the MRC is already its own standing offer (IF-0007) — keep it out of the migration decision entirely. **Confidence: high.**
4. **C-133 preserves child sovereignty.** The clause binds the *origin*: kernel artifacts as shipped are ratified by the mother's owner, who holds the responsibility for them (best-knowledge, discharged through agents + gates, the signed tag its cryptographic form). It transfers no adoption authority — the advisory itself frames it as "the trust doctrine your own inheritance clause already rests on," and KMP §1.8's audited-never-obeyed stands untouched. Bind it exactly as KNet proposes: upstream responsibility, sovereign adoption. **Confidence: high.**
5. **C-121 conflicts with KNet's current fieldnote regime in conduct and data lifecycle, not in tooling.** Real differences: v0.2 is one buffer, no target at capture, ratification-gated write, **dissolve-and-delete**; KNet runs targeted capture, an append-only ledger, and retained attribution history. **A fact from this review narrows the migration cost: upstream `fieldnote.py` v0.2's parse accepts both grammars — v0.1 seven-key blocks are explicitly supported ("frozen ledgers, v0.1-kernel children") — so adopting the v0.2 tool would not invalidate `FIELDNOTES.md`, and no data is at risk either way.** The smallest honest migration, *if* KNet wants it: adopt the tool + keep the ledger file as the configured buffer + take the conduct question (append-only vs dissolve) to an explicit owner decision — the `.d` sub-row of §3. DEFER remains fully conformant. **Confidence: high on the facts; the choice is conduct, hence KNet's.**
6. **Doctrine may be inherited with the retrofit deferred — the release says so itself.** Advisory §6: retrofits are per-component recorded decisions, "nothing forces a regeneration," newborn-only components are never retrofitted, and the mother's custom pairs are named never-retrofit. KNet's richer existing board is exactly the grown-instance case the seed-tree law anticipates (growth = instance). **Confidence: high.**
7. **Continue deferring `close.py`, `genesis.py`, `check_scan.py` — beta-0.7 creates no new mandatory dependency.** Verified in the tool bytes: the import runs *from* `close.py` *into* `check_versions.py`, which keeps its own `__main__` entry and runs standalone; `genesis.py` is birth-only; `check_scan.py` fires on Scan demand KNet doesn't have. Observed-need tiering stands. **Confidence: high.**
8. **Reissue, never replace:** KNet's Conversation Settings (v0.9), Rule Overview, and both adapters are projections of *KNet's* merged source; overwriting any of them with mother editions would hand-fork identity — the C-035/C-077 law both instances carry. Re-project from KNet's own source after the matrix lands. **Confidence: high.**

### Condition D — Registry currency and tool portability

1–2. **The Registry currency defect is real, and the mother owns it.** Verified at the tags: the beta-0.6 and beta-0.7 editions carry a **byte-identical version line — v0.10, revision narrative ending at C-127/C-128/C-129 — over changed bytes** (the S6-7.5 scoping edit and the C-132 behaviour-convention block + MRC row entered the body with no bump and no revision row), against the document's own v0.4 precedent of bumping for Scan-cure edits. And **four body rows are stale at the boundary**: the Pair Procedure row cites **v0.2 with a v0.2 path** while **v0.3 ships in the same tree**; the Fieldnote Format v0.2, Board Format v0.3, and Interface Place Format v0.1 rows all still read "**ratified — ships next release**" *inside the release that ships them*. Under the mother's own living-document law (C-012/C-077) this is a genuine currency defect. **Severity: Medium (governance hygiene; zero integrity impact — the signed tag, the shelf's substance, and every named standard are unaffected). Confidence: high.**
3–4. **Disposition: correct upstream; child-side, disclose — never silently byte-replace, never edit the inherited copy in place.** The mother will propose the cure to Max for the next close (a v0.11 reissue: the two missing revision rows + the four status cells + the pointer; and a repair-class candidate — teaching a pack gate to catch shipped-standard status cells, the FN-0002 pattern). KNet's cleanest paths, in order: adopt the needed *content* (C-127 scoping, C-132 block) via a KNet-bound re-projection or addendum that records the defect — re-projection preserves provenance exactly as KNet's Q4 suspects — or wait for the cured upstream edition if timing allows. **Confidence: high on the defect; the timing choice is KNet's.**
5. **`check_versions.py` is correctly BIND/MIGRATE, not INHERIT.** The tool is kernel logic with mother-instance parameters baked in: the STRICT set names mother files, the protocol-coverage tripwire walks the mother's protocol-series naming, INSTANCE_ONLY names child files (KNet's own migration-protocol filename among them — inert courtesy, no effect), and the pair-half gate hard-codes the mother's halves — including a custom pair (`Fractal_Update_Plan.html`) the curated tree deliberately excludes. **Mitigating fact from this review: the gate skips safely** — `if not os.path.exists(...): continue`, "a half not yet born is not a defect" — so the baked-in names are inert where absent, and a byte-copy would largely no-op rather than misfire. Still: port the generic checks and parameterize, exactly as KNet proposes; a byte-copy would carry dead mother parameters into a KNet-bound tool that P-008-class law says cannot be overwritten silently. **Confidence: high.**
6. **`verify.py` / `mint.py`: safe source-parity updates** — six citation lines, zero logic (B4). Byte-adoption at the pinned edition (with `.inherited` pairing) or local citation edit are both sound; byte-adoption is simpler to audit. **Confidence: high.**
7. **No further hidden instance assumption found in the tool batch** beyond D5's enumerated parameters. `doctor.py` is untouched by the batch (the advisory's "four tools that moved" excludes it) — **KNet's locally-ahead PDF-corpus edition faces no collision; preserve it.** **Confidence: high.**

### Condition E — gates, working tree, and research boundaries

1–3. **The duplicates do not poison the pin; resolve them by the owner's hand; no needless close is required — but one commit is already owed anyway.** Independently verified this review: **all 13 ` 2.json` files are byte-identical to their tracked counterparts** (SHA-256, mother-side recomputation). They are untracked, so the tracked pin `e662f3a…` is exact regardless — the risk they pose is working-surface hygiene, not evidence integrity. The pattern (` 2` suffix, `~/Desktop` residence) is the **iCloud/macOS sync-conflict signature the mother has already met at scale**: the mirror carried 285 such artifacts, cured 2026-08-18 by byte-identity proofs + Max's hand — the precedent disposition. Recommended sequence: (a) record the 13 paths + both byte-identity attestations (KNet's and this return's); (b) **Max deletes them** (deletion authority is his — the packet's own non-claim, confirmed); (c) land the packet file — **the packet's own pin rule already requires a KNet close to freeze it, so make *that* commit the Gate-0 checkpoint**: Gate 0's wording ("close and commit the present development state") is then satisfied literally, and no separate ceremony is added. `e662f3a…` itself remains a valid *rollback* anchor for tracked state throughout. **Host-level watch item for Max, outside governance: KNet on iCloud-synced Desktop stays exposed to this pathology; the mother's mirror produced it once already.** **Confidence: high.**
4. **Q07 revalidation triggers, mother-side facts:** the H6 corpus is the **frozen beta-0.4 grant (C-109) — a separate tree a KNet kernel migration never touches**; its source anchor is migration-invariant. Revalidation is owed only where Q07 machinery pins or imports KNet's *own* kernel bytes — if probe manifests hash tool files (e.g. `fieldnote.py`, `verify.py`) or the runner imports migrated modules, re-pin those manifests before any freeze. The enumeration is KNet machinery, KNet's jurisdiction; the principle and the corpus-anchor fact are the mother's contribution. **Confidence: high on the facts stated; the enumeration is deferred to KNet by design.**
5. **Endorsed validation classes**, with two additions from this review: KNet's list (sixteen PDFs · KMR/KIMK boundaries · local adapters · P/C namespaces · `.inherited` pairing · P-020 landing semantics) plus **(a)** `doctor.py` non-regression (D7 — assert the local edition survives the matrix untouched) and **(b)** the P-008 §9 Gate-5 identity-line comparison run against the *new* checkpoint, since living-document identity lines are exactly where a silent overwrite would first show. **Confidence: high.**
6. **The migration creates no experimental authority.** The delta is doctrine, specs, formats, and tools; nothing in C-116–C-133 or the tool batch touches Q07 `S`/`G`/`M`, Q10, Q11, KMR/KIMK acceptance, or any freeze semantics. The packet's non-claims hold; nothing found pointing the other way. **Confidence: high.**
7. **Decision shape: one P-024 for the migration core, separate later decisions for the conduct-touching options.** P-024 with component sub-rows (§3's table) covers target, matrix, and execution — auditable in one place, the advisory's per-component rule satisfied. The four adoptions that change conduct or standing structure — C-121's data-lifecycle (`.d`), C-123's place act (`.b`), MRC membership (IF-0007's own lane), the user-document/board retrofit — are decisions of a different kind and deserve their own later `P-…` numbers, unhurried by the migration. **Confidence: high on the recommendation; the shape is KNet's to choose.**

## 7 · Severity and confidence roster (item 5)

| Finding | Severity | Confidence | Owner |
|---|---|---|---|
| Registry currency defect (stamp static over changed bytes; four stale status cells; v0.2 pointer) | **Medium** | High | **Mother** — upstream cure proposed to Max (v0.11 reissue + a pack-gate candidate); child-side: disclosure, never silent replacement |
| Advisory baseline gap (IF-0008 inventories C-130→C-133; a beta-0.5 child needs IF-0006 beside it — both ship in the pinned tree) | **Low** | High | Mother (advisory-series design note); KNet cures by citing both |
| 13 untracked duplicates (byte-identical, iCloud-signature) | **Low** (hygiene; pin unaffected) | High | Max's hand in KNet; host-level watch item |
| Signature principal display (gmail principal shown for knet.network tagger) | **None** (designed custody model) | High | — |
| `check_versions.py` baked-in mother parameters | **Low** (skip-safe; BIND/MIGRATE disarms it) | High | KNet port discipline; mother notes the parameterization split as a future upstream improvement |
| **Migration blockers found** | **None** — no condition blocks at any gate; the only gate-conditioned item is Gate 0's checkpoint hygiene (E1–E3), resolved by the sequence above | High | — |

## 8 · Smallest defensible change-set, and what stays deferred (item 8)

**In the core change-set (P-024):** the Gate-1 pin + receipt pair + tag-and-anchor bundle (A4) · INHERIT the doctrine rows C-117`.a`, C-122`.a`, C-124`.a`, C-125, C-126`.a`, C-127, C-128`.a`, C-131`.a`, C-132`.a`, C-133 · MIGRATE the spec editions (Schema v0.7 · Navigation Contract v0.2 — add the files, touch nothing else) · parity-update `verify.py`/`mint.py` · BIND/MIGRATE `check_versions.py` (ported checks, KNet parameters) · `Templates/` copy (C-131`.b`, cheap and inert) · Registry content via re-projection/addendum with the defect disclosed (D3–D4) · EXCLUDE C-116, C-119, C-120, C-129, C-130 · re-project (never replace) Settings, Rule Overview, adapters.

**Deferred, each to its own later decision or trigger:** C-121 conduct + `fieldnote.py` (the `.d` data-lifecycle question) · C-123`.b` the place act (P-021's Gate-A, Max's deliberate call) · MRC membership (IF-0007's own lane) · the user-document/board retrofit + Grown-from stamps (own pace) · `close.py`, `genesis.py`, `check_scan.py` (observed need) · C-118 with its tool.

This is materially KNet's own §10 shape — reached independently, now evidence-hardened.

## 9 · The requested comparison (item 4's axes)

| Condition | Observed fact | KNet impact | Upstream impact | Gate consequence | Confidence |
|---|---|---|---|---|---|
| A · Source identity | Public tag signed, custody-good, receipt-bounded; mother tag relation **confirmed mother-side**; OTS calendar-pending | Public tag adoptable as sovereign target; bundle should include the anchor | None — chains behave as designed | Gate 1 satisfiable as proposed | High |
| B · Delta & classification | Delta exactly C-116–C-133 (Register at both tags); AST §6 partition as KNet read it; spec pair neutral (3 evidence lines); licenses unchanged; **IF-0006 missing from the surface** | Sub-rows per §3; cite both advisories | Advisory-series design note (baseline span) | Gate 2 assessment can freeze on this classification | High |
| C · Local conflicts & retrofits | Doctrine/retrofit split confirmed by the release's own §6; C-121 the one true conduct conflict (tool dual-grammar narrows it); C-132/C-133 sovereignty-safe | Conduct decisions separated from the migration core | None | Gate 3 decision material complete; no hidden Gate-4 obligations | High |
| D · Registry & tools | **Registry currency defect confirmed and owned by the mother**; verify/mint six citation lines; check_versions mother-parameterized but skip-safe; doctor.py untouched | Disclose, re-project, port-don't-copy | **Mother cure owed (v0.11 + gate candidate)** | No gate blocks; D-items land inside Gates 2–4 normally | High |
| E · Tree & research boundaries | 13 duplicates byte-identical (mother-verified); iCloud signature, mother precedent; Q07 corpus is the frozen C-109 grant, migration-invariant; no experimental authority created | Max's-hand cleanup; packet-landing commit doubles as Gate 0 | None | Gate 0 resolvable without an added ceremony; Gates 5–6 unaffected | High |

## 10 · Missing files, rules, tools, projections, obligations (item 7)

One: **IF-0006** (the beta-0.6 advisory) into the review surface — in-tree, zero-cost (B6). Nothing else found missing: no changed upstream artifact outside the packet's inventory creates a KNet rule, tool, identity, license, or validation obligation (license layer and `.allowed_signers` byte-unchanged across the whole span).

## 11 · Agreement and disagreement with §10, item by item (item 6 — written after the independent block above was complete)

| §10 row | Verdict |
|---|---|
| Public tag + anchor receipt as Gate-1 target | **Agreement**, independently evidenced (A1–A2) — with one **addition**: retain tag *and* anchor in the bundle (A4) |
| C-116/C-119/C-120/C-129/C-130 EXCLUDE | **Agreement** — matches the pinned AST §6 instance class exactly (§3) |
| C-117 INHERIT + local precedence | **Agreement**, with the `.a`/`.b` sub-row note (KMP v0.1 is KNet's own pattern upstreamed — conflict structurally unlikely) |
| C-118 DEFER | **Agreement** (doctrine travels with the tool; no Scan demand, no dependency) |
| Spec pair MIGRATE, no store rewrite | **Agreement**, hardened: three independent evidence lines incl. byte diffs (B4) |
| C-121 CONFLICT/MIGRATE or DEFER | **Agreement**, **narrowed in KNet's favor**: v0.2's dual-grammar parse keeps the v0.1 ledger valid — the conflict is purely conduct/data-lifecycle (`.d`), not data or tooling (C5) |
| C-122/124/126/128/131 doctrine-vs-retrofit split | **Agreement** — the release's own retrofit rules say it (C6) |
| C-123 BIND only on Max's deliberate Gate-A act, else defer | **Agreement** (C1) |
| C-125 INHERIT | **Agreement** |
| C-127 INHERIT/BIND | **Agreement** (S6-7.5 scoping cited, C2) |
| C-132 INHERIT class, MRC separate | **Agreement**, plus: the MRC's separate lane already exists — IF-0007 (C3) |
| C-133 INHERIT/BIND, sovereignty preserved | **Agreement** (C4) |
| Registry CONFLICT/MIGRATE, no silent replacement | **Agreement — and the mother confirms the defect as her own**, with the upstream cure path and the re-projection recommendation (D1–D4) |
| verify/mint safe update | **Agreement** (six lines, citation-only) |
| check_versions BIND/MIGRATE | **Agreement**, with the skip-safe mitigating fact recorded (D5) |
| fieldnote.py moves only with C-121 | **Agreement** (with the dual-grammar narrowing) |
| close/genesis/check_scan/board DEFER | **Agreement** — no new mandatory dependency, verified in the import direction (C7) |
| Conversation Settings preserve v0.9 | **Agreement** — upstream conduct source unchanged since beta-0.5 (Settings v0.8 predates it; nothing in the delta is a Settings reissue) |
| Rule Overview + adapters re-project | **Agreement** (C8) |
| Preliminary sequence (§10's six steps) | **Agreement**, with one **correction**: step 1's resolution and step 2's landing collapse — the packet's own pin rule already owes a landing commit; make that commit Gate 0 (E1–E3). And the packet's challenge list is discharged: public-tag sufficiency **confirmed**, Registry defect **confirmed and mother-owned**, doctrine-vs-retrofit splits **confirmed**, KMR/KIMK and experimental non-effects **confirmed** (C3, E6) |

**Net four-eyes outcome:** no preliminary disposition overturned; two corrections (bundle scope; Gate-0 shape), two narrowings in KNet's favor (fieldnote data-safety; checker skip-safety), one upstream defect confirmed and taken by the mother, one additional finding (the advisory-baseline gap). Confirmation was not the objective; where the evidence pushed back, it is recorded above — it happened at the edges, not the core.

## 12 · Repair advice (item 9, the minimum changes)

**Upstream (the mother, proposed to Max):** Registry v0.11 reissue — the two missing revision rows (S6-7.5 scoping; C-132 block + MRC row), the four status cells to *shipped* with their release names, the Pair Procedure row to v0.3; plus one banked candidate each for the pack gate (shipped-standard status-cell currency — the FN-0002 class) and the tool split (checker parameters out of kernel logic). **KNet-side (if adopting before the cure):** re-projection/addendum with the defect disclosed — never an in-place edit of the inherited copy.

## 13 · Advisory statement (item 12)

This return is **advisory evidence, non-governing, in every line**: it makes no KNet decision, adopts nothing, dispositions nothing, authorizes no migration step, touches no KNet file, and creates no authority or acceptance of any kind — including over the thirteen duplicates, whose deletion remains Max's act alone. It enters KNet, if at all, through Max's transport and KNet's own recorded governance. Errors in it are the mother's; challenges to it are welcome through the same interface, credited.

## 14 · Anchor addendum (2026-08-20, post-issue — the packet's pin resolved)

Appended after issue, never rewriting the body above (the forward-commit discipline). KNet's Gate-0 freeze landed and the mother verified it read-only:

- **KNet close commit:** `f2ffb7b4b41f13d863046f4846a251d6b8cfa3ff` (`[GOV] Freeze beta-0.7 four-eyes Gate 0`), local `main` = `origin/main` at it, working tree clean — the thirteen duplicates gone from the tree (relocated recoverably per KNet's report, Max's act; the tree state is the mother-verified fact).
- **The packet is now a frozen issue:** SHA-256 **`a14461955a1e4bc57fba09fd37f8bc6e9948fab45701b23533dceb400fb0ba43`**, computed mother-side from the git object at that commit, matching KNet's declaration. The banner's Working-Draft caveat is resolved: this return's subject is that frozen issue. (The review's §1 evidence chain was computed from pinned git objects throughout and is independent of this resolution.)
- **Boundary discipline held:** KNet's own frozen Return Package records — Max ratified the preparation sequence only; no `P-024` minted, no Gate-2 assessment exists, no migration began. Exactly the E1–E3 sequence, executed.
- This return and its companion (IF-0010) are committed mother-side in the anchoring commit that carries this addendum; that commit's hash is the mother-side pin for KNet's Gate-2 citation, traveling with Max's transport.

---

*Author: Claude (AGENT.AI.CLAUDE), the mother's thirty-third Code session, under the C-096 window opened on Max's direction. Cited evidence computed 2026-08-20 against: KNet `e662f3a…` (read-only; the Gate-0 freeze `f2ffb7b…` verified in the §14 addendum), mother repo (tags `beta-0.5`/`beta-0.7`, `Provenance/`), public mirror (`beta-0.7`, anchor `435da8b…`). The packet absorbed-and-cited per its path + date; its pin stands resolved in §14.*
