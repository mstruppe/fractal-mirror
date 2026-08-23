# Fractal Rule Corpus — the classification baseline + the audit routine

> **WORKING ARTIFACT SET (Draft — pending ratification; every landing proposal-only, Ultracode Flight Protocol §6).** The rule-corpus flight (`Review_2026-08-21_Rule-Corpus-Flight.md`) classified the whole rule-set once; this folder makes that classification a **living baseline with an update mechanism** — Max's commission, thirty-seventh session: *"the consensus of habits needs an update mechanism … it iterates checks whether the rules landed in the right classification … a specific scan flight routine."* Per Flight Protocol §8, the routine's own standard is distilled **after** its first execution, from that execution (the C-094 friction-to-standard loop); until then this README is the working description.

**Status:** Draft v0.1 · **Commissioned:** 2026-08-22 (Max, the thirty-seventh session) · **Domain:** GOV · **Author:** Claude

## The three pieces

1. **`rule_corpus.json`** — the classification baseline. Salvaged from the first flight's journal (`wf_0002e9b0-8d7`, the session-local artifact rescued to durability 2026-08-22): 365 exact-id rows carrying per-lane tier votes, loci, enforcement text, the habit-by-accident enrichment (the 72), and evidence-file pins. **Honesty note:** the landing report's 289 count came from the crossmatch agent's *semantic* dedupe, whose merge map was never emitted as data — the 365→families reconciliation is the first audit's Phase 1, after which the count of record is mechanical. Recorded vs salvaged counts sit side-by-side in `_provenance`; the delta is reconciliation input, never silently normalized.
2. **`audit.py`** — the mechanical half (read-only; writes only `audit_manifest.json`). Scopes each run so agents never re-read all rules one-by-one: **DIRTY** (evidence drift — cited file gone, line pin dead) · **NEW** (Register C-refs the corpus has never seen) · **DISAGREEMENT** (lanes voted different classes, never adjudicated) · **UNRECONCILED** (no family yet) · **SAMPLE** (seeded random control rows — catches systematic misclassification that produces no drift signal).
3. **`.claude/workflows/classification-audit.js`** — the flight (repo root, named workflow). Phases: Reconcile (first run only) → Classify (manifest rows, fresh, against live code) → Adjudicate (two adversarial verifiers per dispute set, opposite mandates) → Assemble (delta report). A reclassification is proposed only when both adversarial verdicts agree against the standing class; sample rows that confirm land as CONFIRMED, as loudly as failures.

## The update loop

```
audit.py --seed <date>  →  manifest  →  flight (on the commissioner's go, two-turn)
        →  delta report (proposal-only)  →  Max's dispositions at an ordinary close
        →  rule_corpus.json updated, corpus_version bumped  →  next iteration is cheaper
```

Re-run triggers (offered, not mandated): after a §6 build lands (HABIT rows become MACHINE — the corpus must follow), at a tagging close, or on commission. Ratified deltas are applied to `rule_corpus.json` by hand at v0.1 (C-008 manual-first; an `apply.py` graduates when the routine proves robust).

---

**Sources:** `Review_2026-08-21_Rule-Corpus-Flight.md` (the taxonomy, the counts, the method of record) · Ultracode Flight Protocol v0.2 (the container: commissioning contract, verification tiers, proposal-only landing) · Scan Procedure v0.1 (the findings-ledger discipline the delta report follows).
**Revision history:** v0.1 (2026-08-22) first issue — corpus salvaged, detector built, flight routine written; first flight pending the commissioner's go.
