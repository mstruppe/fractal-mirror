#!/usr/bin/env python3
"""audit.py — the Classification Audit's mechanical half (v0.1, Draft — pending ratification).

The update mechanism's scoping instrument (Max's commission, thirty-seventh session):
instead of re-reading all rules one by one, each audit run consumes a MANIFEST of rows
that actually deserve agent attention:

  DIRTY        evidence drift — a cited file is gone/moved, or a file:line pin no longer resolves
  NEW          C-refs present in the Decision Register but absent from the corpus (rules born
               after the last corpus update)
  DISAGREEMENT rows where the inventory lanes voted different classes and no audit has
               adjudicated them yet
  UNRECONCILED rows not yet assigned to a semantic family (the first flight's 530->289 merge
               judgment was never emitted as data; reconciliation rebuilds it as data)
  SAMPLE       a seeded random control sample of clean rows — catches systematic
               misclassification that produces no drift signal

Usage:  python3 audit.py [--corpus rule_corpus.json] [--repo <root>] [--sample N] [--seed N]
                         [--manifest audit_manifest.json]
Read-only over the repo; writes only the manifest beside the corpus. Exit 0 always —
this is a scoping instrument, not a gate (the flight's landing is proposal-only).
"""
import argparse, collections, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REGISTER = "Claude/Project Governance/Governance Documents/Fractal_Decision_Register.md"
SKIP_DIRS = {".git", "Archive", "node_modules", "__pycache__"}
PIN_RE = re.compile(r"([A-Za-z0-9_./-]+\.py):(\d+)\b")
CREF_RE = re.compile(r"\bC-(\d{3})[a-z]?\b")


def repo_file_index(root):
    """basename -> set of repo-relative paths (skipping non-governing trees)."""
    idx = collections.defaultdict(set)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            idx[fn].add(os.path.relpath(os.path.join(dirpath, fn), root))
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default=os.path.join(HERE, "rule_corpus.json"))
    ap.add_argument("--repo", default=DEFAULT_REPO)
    ap.add_argument("--sample", type=int, default=12)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--manifest", default=os.path.join(HERE, "audit_manifest.json"))
    args = ap.parse_args()

    corpus = json.load(open(args.corpus))
    rows = [r for r in corpus["rules"] if r.get("class") != "RETIRED"]
    idx = repo_file_index(args.repo)

    manifest = {"dirty": [], "new": [], "disagreement": [], "unreconciled": [], "sample": []}

    # --- A/B: evidence drift ---
    for r in rows:
        reasons = []
        for f in r.get("evidence_files", []):
            base = os.path.basename(f)
            if base not in idx:
                reasons.append(f"evidence file missing from tree: {f}")
        for text in r.get("loci", []) + r.get("enforcement", []):
            for fname, line in PIN_RE.findall(text):
                base = os.path.basename(fname)
                paths = idx.get(base, set())
                if not paths:
                    continue  # already reported above
                ln = int(line)
                if not any(
                    sum(1 for _ in open(os.path.join(args.repo, p), errors="replace")) >= ln
                    for p in paths
                ):
                    reasons.append(f"line pin no longer resolves: {fname}:{line}")
        if reasons:
            manifest["dirty"].append({"id": r["id"], "class": r["class"], "reasons": reasons})

    # --- C: register delta (rules the corpus has never seen) ---
    covered = set()
    for r in corpus["rules"]:
        covered.update(CREF_RE.findall(json.dumps(r)))
    reg_path = os.path.join(args.repo, REGISTER)
    reg_refs = set(CREF_RE.findall(open(reg_path, errors="replace").read())) if os.path.exists(reg_path) else set()
    manifest["new"] = sorted(f"C-{n}" for n in reg_refs - covered)

    # --- D: lane disagreement not yet adjudicated ---
    for r in rows:
        votes = set(r.get("lane_votes", {}).values())
        if len(votes) > 1 and not r.get("adjudicated"):
            manifest["disagreement"].append({"id": r["id"], "class": r["class"], "lane_votes": r["lane_votes"]})

    # --- reconciliation debt ---
    manifest["unreconciled"] = [r["id"] for r in rows if not r.get("family")]

    # --- E: control sample from clean rows ---
    flagged = {d["id"] for d in manifest["dirty"]} | {d["id"] for d in manifest["disagreement"]}
    clean = [r for r in rows if r["id"] not in flagged]
    rng = random.Random(args.seed)
    for r in sorted(rng.sample(clean, min(args.sample, len(clean))), key=lambda x: x["id"]):
        manifest["sample"].append({"id": r["id"], "class": r["class"]})

    manifest["_meta"] = {
        "corpus_version": corpus["_provenance"]["corpus_version"],
        "seed": args.seed,
        "counts": {k: len(v) for k, v in manifest.items() if isinstance(v, list)},
    }
    with open(args.manifest, "w") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)

    c = manifest["_meta"]["counts"]
    print(f"corpus rows: {len(rows)} · dirty: {c['dirty']} · new C-refs: {c['new']} · "
          f"lane-disagreement: {c['disagreement']} · unreconciled: {c['unreconciled']} · sample: {c['sample']}")
    print("manifest:", args.manifest)


if __name__ == "__main__":
    main()
