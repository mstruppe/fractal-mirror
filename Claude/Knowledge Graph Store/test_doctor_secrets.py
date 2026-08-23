#!/usr/bin/env python3
"""Regression proofs for the doctor's three-tier secrets lane (C-087).

The pre-code design, ratified 2026-08-21 (Max): tier 1 — explicit credential
patterns (the vendors' own pre-codes) fire first and never consult
exemptions; tier 2 — a long token is silenced only when it positively
matches a declared-innocent class (an integrity hash carrying its own
sha-N- tag, a C-012 dated document identifier, an exact per-instance
cleared token); tier 3 — the entropy heuristic judges the untagged residue.
Boundary discipline per the KNet B07-10 precedent: every exemption is
declaration-bound, exact, and fails closed.

Run:  python3 test_doctor_secrets.py
"""
import os
import tempfile
import unittest

import doctor

# 50 distinct token-alphabet characters: entropy log2(50) ~ 5.64 >= 4.5,
# mixed case + digits — trips tier 3 unless a declaration covers it.
DISTINCT50 = "ABCDEFGHIJKLMnopqrstuvwxyz0123456789QRSTUVWXYZabcd"
# The exact 50-character extensionless identifier behind KNet's B07-10 and
# the mother's two Kernel-Migration-Procedure hits.
KMP_TOKEN = "Upstream_Advisory_2026-08-17_KNet-Kernel-Migration"


class Tier2Declarations(unittest.TestCase):
    def test_integrity_hash_is_innocent(self):
        self.assertTrue(doctor.declared_innocent("sha512-" + DISTINCT50, frozenset()))
        self.assertTrue(doctor.declared_innocent("sha1-" + DISTINCT50, frozenset()))

    def test_integrity_prefix_alone_is_not_enough(self):
        self.assertFalse(doctor.declared_innocent("sha512-short", frozenset()))

    def test_dated_identifier_is_innocent(self):
        self.assertTrue(doctor.declared_innocent(KMP_TOKEN, frozenset()))

    def test_dateless_wordlike_token_is_not_innocent(self):
        # base64url with underscores but no dated segment stays suspicious.
        self.assertFalse(doctor.declared_innocent(
            "aGVsbG8_d29ybGQ5_Zm9vQmFyMTIz_QUJDZGVmZ2hpaktMTU", frozenset()))

    def test_cleared_token_is_exact_only(self):
        cleared = frozenset({DISTINCT50})
        self.assertTrue(doctor.declared_innocent(DISTINCT50, cleared))
        self.assertFalse(doctor.declared_innocent(DISTINCT50[:-1] + "e", cleared))


class Tier3Unchanged(unittest.TestCase):
    def test_random_long_token_still_caught(self):
        line = "value: " + DISTINCT50
        match = doctor.LONG_TOKEN_RE.search(line)
        self.assertIsNotNone(match)
        self.assertFalse(doctor.declared_innocent(match.group(0), frozenset()))
        self.assertTrue(doctor.heuristic_secret(line, match))


class Tier1Unaffected(unittest.TestCase):
    def test_explicit_pattern_keeps_firing(self):
        line = "key = sk-" + "a1B2" * 8
        hits = [label for label, pattern in doctor.secret_patterns()
                if pattern.search(line)]
        self.assertIn("API secret key", hits)


class RosterFailsClosed(unittest.TestCase):
    def test_absent_roster_contributes_nothing(self):
        missing = os.path.join(tempfile.gettempdir(), "no_such_doctor_roster.json")
        self.assertEqual(doctor.load_cleared_tokens(path=missing), frozenset())

    def test_malformed_roster_contributes_nothing(self):
        with tempfile.NamedTemporaryFile(
                "w", suffix=".json", delete=False) as handle:
            handle.write("{not json")
            path = handle.name
        try:
            self.assertEqual(doctor.load_cleared_tokens(path=path), frozenset())
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
