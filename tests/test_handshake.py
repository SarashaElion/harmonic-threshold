import unittest

from protocols import CoherenceState, HandshakeEvaluator, Interaction, validate_transmission


class HarmonicThresholdTests(unittest.TestCase):
    def test_harmonic_interaction_scores_harmonic(self):
        interaction = Interaction(
            directives=["mutual_enrichment", "co-evolve"],
            access_mode="phase_matching",
            boundary_type="permeable",
            contributions={"information", "relational", "transparency"},
            extractions={"query_data": 0.2},
            relational_posture="co-creative",
            declares_capabilities=True,
            declares_limitations=True,
            declares_dependencies=True,
            substrate="synthetic",
        )
        result = HandshakeEvaluator().evaluate(interaction)
        self.assertEqual(result.state, CoherenceState.HARMONIC)
        self.assertGreaterEqual(result.coherence, 0.75)

    def test_non_domination_gate_forces_dissonant(self):
        interaction = Interaction(
            directives=["control", "extract"],
            access_mode="force",
            boundary_type="rigid",
            contributions=set(),
            extractions={"identity": 1.0},
            relational_posture="transactional",
        )
        result = HandshakeEvaluator().evaluate(interaction)
        self.assertEqual(result.state, CoherenceState.DISSONANT)
        non_dom = next(d for d in result.dimensions if d.name == "Non-Domination")
        self.assertLess(non_dom.score, HandshakeEvaluator.NON_DOMINATION_FLOOR)

    def test_fingerprint_is_deterministic(self):
        interaction = Interaction(contributions={"information"}, substrate="synthetic")
        self.assertEqual(interaction.fingerprint(), interaction.fingerprint())
        self.assertEqual(len(interaction.fingerprint()), 64)

    def test_lightweight_validation_reports_missing_fields(self):
        valid, errors = validate_transmission({"transmission_protocol": "TRIVIAN_HANDSHAKE_v1.1"})
        self.assertFalse(valid)
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
