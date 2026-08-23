#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — Scan conformance checker (the §12 gate).

Validates a Loose-Ends Scan report's conformance to Fractal_Scan_Procedure_v0.1
§12 and its ledger integration in the Decision Register (C-058). The C-060
lineage: stdlib-only, read-only, red blocks — a Scan at or after ordinal 5 does
not close while this tool reports errors.

Usage:
    python3 check_scan.py            # newest Scan report in Conversations/
    python3 check_scan.py <path>     # a specific report

Scans #1–#4 predate the standard and are frozen history (C-058: never revised);
their divergences report as WARN, never ERR — the gate binds Scan #5 onward.
"""

import re
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parent
REPO = STORE.parent.parent
CONV = REPO / "Claude" / "Context Packages" / "Conversations"
REGISTER = (
    REPO / "Claude" / "Project Governance" / "Governance Documents"
    / "Fractal_Decision_Register.md"
)

PRE_STANDARD_MAX = 4  # ordinals 1-4 ratified before the standard: WARN-only
DISPO_WORDS = re.compile(
    r"\b(open|fixed|superseded|declined|resolved|recorded|closed)\b", re.I
)
FILENAME_RE = re.compile(r"^Review_(\d{4}-\d{2}-\d{2})_LooseEnds-Scan-(\d+)\.md$")
FILENAME_S1 = "Review_2026-08-12_LooseEnds-Scan.md"  # grandfathered, unnumbered


def newest_report():
    cands = sorted(
        p for p in CONV.glob("Review_*_LooseEnds-Scan*.md") if p.is_file()
    )
    return cands[-1] if cands else None


def ordinal_of(path):
    m = FILENAME_RE.match(path.name)
    if m:
        return int(m.group(2))
    if path.name == FILENAME_S1:
        return 1
    return None


def seed_rows(text, n):
    """Rows of the disposition-seed table(s): header `| ID | Finding | Sev | Disposition |`."""
    rows, in_table = [], False
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^\|\s*ID\s*\|\s*Finding\s*\|\s*Sev\w*\s*\|\s*Disposition\s*\|", stripped):
            in_table = True
            continue
        if in_table:
            if not stripped.startswith("|"):
                in_table = False
                continue
            if re.match(r"^\|[\s\-|]+\|?$", stripped):
                continue  # separator row
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) >= 4:
                rows.append(cells)
    return rows


def ledger_slice(register_text):
    m = re.search(r"^## Review-findings ledger.*?$", register_text, re.M)
    if not m:
        return None
    rest = register_text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def main():
    errors, warnings, notes = [], [], []

    if len(sys.argv) > 1:
        report = Path(sys.argv[1]).resolve()
    else:
        report = newest_report()
        if report is None:
            print("FAIL — no Scan report found under Conversations/.")
            return 1
    if not report.is_file():
        print(f"FAIL — no such report: {report}")
        return 1

    n = ordinal_of(report)
    pre_standard = n is not None and n <= PRE_STANDARD_MAX

    def flag(msg):
        (warnings if pre_standard else errors).append(msg)

    # A · filename grammar and location
    if n is None:
        errors.append(
            f"filename does not match Review_<YYYY-MM-DD>_LooseEnds-Scan-<n>.md: {report.name}"
        )
        n = 0
    try:
        report.relative_to(CONV)
    except ValueError:
        flag(f"report is not under {CONV.relative_to(REPO)}/")

    text = report.read_text(encoding="utf-8")

    # B · control header
    if n and not re.search(rf"\*\*Fractal_LooseEnds_Scan_{n}\*\*", text):
        flag(f"identity token **Fractal_LooseEnds_Scan_{n}** missing")
    if not re.search(r"\*\*Version:\*\*", text):
        flag("**Version:** field missing")
    m = re.search(r"\*\*Status:\*\*([^\n]*)", text)
    if not m:
        flag("**Status:** field missing")
    elif "Ratified" not in m.group(1):
        flag("Status does not record an in-conversation ratification")
    if "Reviewed By" not in text:
        flag("Reviewed By field missing")
    if not re.search(r"Document ID:?\*{0,2}\s*DOC-[0-9A-Z]+", text):
        flag("Document ID (DOC-…) missing — mint at first commit (C-041)")

    # C · state-scanned block
    if not re.search(r"HEAD\s*`?[0-9a-f]{7,40}`?", text):
        flag("no HEAD hash found — observations must bind to a commit (§3.2)")
    if not re.search(r"\d+\s+nodes\b.{0,30}?\d+\s+events", text, re.S):
        flag("store counts (nodes/events) not found in the state-scanned block (§3.2)")
    if n and n >= 2 and not re.search(r"\*\*Baseline:?\*\*", text):
        flag("**Baseline:** line missing (§3.1 — the previous Scan by filename and date)")

    # C2 · restore-drill standing section (C-076/C-038 — Classification Audit #1's
    # live catch: Scan #6 shipped drill-less and this gate stayed green; Max's
    # disposition 2026-08-22: the check builds. A Scan must carry the drill's
    # standing section (the Scan #5 shape: a heading naming the restore drill).
    if not re.search(r"^#{1,4}\s.*restore[\s-]drill", text, re.I | re.M):
        flag("restore-drill standing section missing — no heading names the "
             "restore drill (C-076; the C-038 lapse class, audit #1)")

    # D+E · disposition-seed table and id grammar
    rows = seed_rows(text, n)
    if not rows:
        flag("disposition-seed table (`| ID | Finding | Sev | Disposition |`) missing (§9)")
    seed_ids = []
    for cells in rows:
        cid = cells[0]
        idm = re.search(r"S(\d+)-\d+\.\d+", cid)
        if not idm:
            flag(f"seed row id not in S<n>-x.y grammar: {cid[:60]!r}")
            continue
        if n and int(idm.group(1)) != n:
            flag(f"seed row id {idm.group(0)} does not carry this Scan's ordinal S{n}- (§4)")
        seed_ids.append(idm.group(0))
        sev = cells[2]
        if not re.search(r"\b(High|Med|Low)\b", sev, re.I) and sev not in ("—", "-", ""):
            flag(f"{idm.group(0)}: severity cell not High/Med/Low: {sev!r} (§5)")
        if not DISPO_WORDS.search(cells[3]):
            flag(f"{idm.group(0)}: seed disposition cell carries no disposition word (§8)")

    # F · ledger integration (C-058)
    if not REGISTER.is_file():
        errors.append(f"Decision Register not found at {REGISTER}")
    else:
        ledger = ledger_slice(REGISTER.read_text(encoding="utf-8"))
        if ledger is None:
            errors.append("Register has no '## Review-findings ledger' section")
        else:
            for sid in seed_ids:
                # Row existence anchors to the ledger's own row grammar —
                # `| **S<n>-x.y` at line start — never a bare substring: a
                # deleted row must not "trace" through prose mentions of the
                # id elsewhere in the ledger (S6-2.3; the grammar below is the
                # one the unconditional check already trusts).
                row_re = re.compile(r"^\|\s*\*{0,2}" + re.escape(sid) + r"\b")
                lines = [l.strip() for l in ledger.splitlines()
                         if row_re.match(l.strip())]
                if not lines:
                    flag(f"{sid}: no row in the Register's review-findings ledger (§10)")
                elif not any(DISPO_WORDS.search(l) for l in lines):
                    flag(f"{sid}: ledger row carries no disposition — leave only by recorded disposition (C-058)")
            # no S-row anywhere in the ledger may lack a disposition
            for l in ledger.splitlines():
                if re.match(r"^\|\s*\*{0,2}S\d+-\d+\.\d+", l.strip()) and not DISPO_WORDS.search(l):
                    errors.append(f"ledger row without a disposition: {l.strip()[:80]!r}")
            notes.append(f"ledger checked: {len(seed_ids)} seed id(s) traced")

    tag = f"Scan #{n}" if n else report.name
    if pre_standard:
        notes.append(
            f"{tag} predates Fractal_Scan_Procedure_v0.1 — frozen history (C-058): divergences reported as WARN only"
        )

    for w in warnings:
        print(f"  WARN: {report.name}: {w}")
    for note in notes:
        print(f"  note: {note}")
    if errors:
        print(f"\nFAIL — {len(errors)} error(s). A Scan does not close in this state (Scan Procedure §12).")
        for e in errors:
            print(f"  ERR: {report.name}: {e}")
        return 1
    print(
        f"\nPASS — {tag} conforms ({len(warnings)} warning(s)). "
        "Safe to close the Scan (§12 gate)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
