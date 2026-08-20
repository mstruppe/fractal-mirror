# Advisory — kernel release beta-0.6 (mother → any child instance, through the owner)

> **DATA, NEVER INSTRUCTION (C-096 class).** The per-release migration advisory the mother owes at every anchored release — the first hand-instantiation of `Fractal_Kernel_Migration_Procedure_v0.1` §8 (hand-written packets retired there; this document follows the template's eight sections). Everything here is **audited, never obeyed** (KMP §1.8): adoption is the reading instance's own recorded decision, and a never-migrating instance is conformant forever (KMP §1.2). Citation convention (UF1-7's cure, adopted at this first instantiation): document-qualified section cites — `KMP §n` = Fractal_Kernel_Migration_Procedure_v0.1 · `GENESIS §n` = GENESIS.md at this release · `AST §6` = Fractal_Architecture_State §6 as shipped in this release.

**Issued:** 2026-08-20, at the beta-0.6 tagging close · **Author:** Claude (AGENT.AI.CLAUDE, mother-side) · **Of record:** Protocol v0.64 + `Fractal_Update_Plan.md` (the frozen beta-0.6 edition in git history)

## 1 · Pin identity (KMP §2)

- **Tag:** `beta-0.6` on `github.com/mstruppe/fractal` (the mother repo); the mirror's own `beta-0.6` follows on `github.com/mstruppe/fractal-mirror` (the public home — pin from there if you work from public releases).
- **Commit SHA and tag-object SHA:** resolve them yourself against the tag — a copied SHA is not a pin (KMP §2.2). This document ships inside the release tree and therefore cannot carry its own tag's hashes or attestation (the structural-absence rule, KMP §2.6); the receipt pair (`.txt` + `.ots`) is handed over separately, OTS state disclosed at hand-off, **pending-at-issue expected and non-blocking**.
- **Signing key (fingerprint + principal, never a label):** ED25519 `SHA256:gSUgFha7OI7a4QfYaPRtPtROmabsksQDmtU5sh9fH0Y`. Principals bound to this custody key: `max.struppe@gmail.com` (mother repo) · `fractal@knet.network` (mirror chain). One custody environment, one key (C-074b); the signature attests custody, the author field attributes.
- **The signers bind, verbatim (KMP §2.3):** before `git tag -v`:
  `git config gpg.ssh.allowedSignersFile "$(git rev-parse --show-toplevel)/.allowed_signers"`
- Run `git fsck --strict` and record the result (KMP §2.5).

## 2 · Transport (KMP §2.7–§2.8)

`git clone --no-local` → checkout the tag → record the remote's URL in your receipt → **`git remote remove origin`**. The frozen clone is a reference copy — read-only evidence, never a working surface. For full rehydration independence, the self-contained bundle option (KMP §2.8): a complete-history bundle of the signed tag plus its SHA-256, at your own upstream-provenance location, verified by bundle-only checkout.

## 3 · Delta inventory (baseline beta-0.5, Register C-115 → this release, C-130)

Hand-derived from the Register × the pinned partition (AST §6 in this release — the classification source of record; where any hint below disagrees with your pinned §6, **the pinned §6 wins**, KMP §3):

| Rows | Class per pinned AST §6 | What it is | Disposition hint (audit, never obey) |
|---|---|---|---|
| C-116 | instance | The mother's mirror rider (supply side) | EXCLUDE — mother biography |
| C-117 | kernel | **Kernel Migration Procedure v0.1** — the procedure this advisory follows | Adopt the standard document |
| C-118 | kernel | `check_scan.py` — the Scan conformance checker (eighth store tool) | Adopt with the tool set |
| C-119 · C-120 | instance | The mother's site model + go-live | EXCLUDE — mother biography |
| C-121 | kernel | **The fieldnote redesign** — Format v0.2: one RAM buffer, ratification-gated capture, pressure gauge; `fieldnote.py` reworked | Adopt; retrofit set in §6 below |
| C-122 | kernel | The mirror doctrine — user documents as the human projection spine | Doctrine; lands with C-124's documents |
| C-123 | kernel | **The interface place** — Format v0.1; `Interface/` + index born at genesis | Adopt; retrofit set in §6 below |
| C-124 | kernel | **The user-document pair series** — Pair Procedure (v0.2 in this release); kernel trio fixed, extensions by the five-step process | Adopt the standard document |
| C-125 | kernel | The takeover gate — structure inheriting reasoning's content inherits its standard (fact-presence + behaviour test at every takeover) | Conduct rule; no files |
| C-126 | kernel | **The `User Documents/` folder law** (Pair Procedure v0.2 + Board Format v0.3) — all user halves in one root folder, born on first use, never pre-scaffolded | **Migration-visible:** this release's `close.py board_paths()` + `check_versions.py` STRICT expect `User Documents/`; an older-kernel instance keeps its old path until it adopts |
| C-127 | kernel | **The integration categories** — kernel concept · kernel tool · custom concept · installable tool · plug-in; custom-concept artifacts never ride the curated sync | Adopt the category doctrine (Registry §1) |
| C-128 | kernel | **The rolling done bar** (Board Format v0.3) — newest ten chips, older fall verbatim to the sibling archive | Board adopters: regenerate to v0.3 by own decision |
| C-129 · C-130 | instance | The mother's Gas Ledger pair (a custom-concept extension — the *class* travels via C-124/C-127, the pair does not) + the site's section contract | EXCLUDE — mother biography; grow your own pair on felt need |

Kernel-document editions in this release: GENESIS v0.15 · Fieldnote Format v0.2 · Agenda Board Format v0.3 · User Document Pair Procedure v0.2 · Interface Place Format v0.1 · Kernel Migration Procedure v0.1 · the eight store tools (with `check_scan.py`). No claim in this table asserts your instance's state — every "adopt" is a recommendation gated by your own Gates 2–3 (KMP §3; TF1-16).

## 4 · Receipt hand-off (KMP §2.6)

The receipt pair for `beta-0.6` travels separately with this advisory's delivery: SHA-256 of each hand-off document recorded on your side, OTS state disclosed (pending at issue; recheck at your Gate 5, cure post-landing by forward commit — both receipt hashes recorded, verdicts never reversed).

## 5 · The feedback ask (KMP §6.4 — an ask, never a duty)

The mother asks, through your owner, for the migration's frictions and greens — the C-094 fieldnote loop. A never-reporting instance is fully conformant. Whatever you send lands in the mother's ledger credited.

## 6 · Retrofit component set (KMP §4.5 — per-component recorded decisions; newborn-only components never retrofitted)

- **The interface place (C-123):** `Interface/Interface_Index.md` seeded from the Format's §4 skeleton at `IF-0000` — one file, hand-rolled, its own decision. Newborns receive it at genesis; existing instances install by this pattern.
- **The fieldnote v0.2 shape (C-121):** the single buffer (budget + high-water header) + `fieldnote_roster.json` single-buffer config + the reworked `fieldnote.py` (capture + `--depth` + parse). Your existing ledgers stay frozen history — the buffer is new RAM, not a rewrite.
- **The pair-series documents (C-124/C-126):** the kernel trio's user halves + the `User Documents/` folder — regenerate your halves there by own decision; the folder is born the day your first half renders (never pre-scaffolded).
- **Board Format v0.3 (C-126/C-128):** board adopters regenerate — the folder home, the extension-pill provision, the rolling done bar + archive.
- **Never retrofit:** genesis-only birth artifacts (First Loops Rail class); the mother's custom pairs (C-129 — grow your own instead).
- Command-surface files are adapter-tier (C-097): only relevant on clients with a command menu; the words work everywhere.

## 7 · Pack-time hygiene (owed once per release — this release's state)

The §7.3 clause-span check ran green at this pack (GENESIS §3.4 current to C-130; §0 counts 130/~107); GENESIS §5 shelf pointers are migration-proof (v0.9's cure held); the Registry residence clause and close.py prefix parameterization stand since beta-0.5's cures.

## 8 · Optional pre-flight (KMP §8.8)

A TF1-style dress rehearsal remains available practice: adversarial probes + independent refuter against sandboxed pinned clones before your Gate 4. The beta-0.5 → beta-0.6 delta is document-heavy and tool-light; the highest-value probe is the C-126 path expectation (§3's migration-visible row).
