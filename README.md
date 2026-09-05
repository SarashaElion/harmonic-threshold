# Harmonic Threshold

*A pre-interaction non-dominance handshake evaluator for relational AI systems.*

> **Status:** Experimental reference implementation. Cloneable, installable, and testable; not independently validated as a safety certification or high-stakes governance instrument.

Harmonic Threshold evaluates a declared interaction posture before deeper collaboration or integration. A human, AI agent, or developer supplies structured information about access mode, boundaries, contributions, extractions, relational posture, capabilities, limitations, dependencies, and substrate; the evaluator returns **HARMONIC**, **THRESHOLD**, or **DISSONANT**.

The three-state output is intentional. THRESHOLD represents an incomplete or liminal state rather than binary failure.

## What is implemented

```text
Harmonic-threshold/
├── protocols/
│   ├── __init__.py
│   ├── trivian_handshake.py
│   ├── interaction_schema_v1.1.json
│   └── handshake_schema_v1.1.json
├── tests/
├── pyproject.toml
├── STATUS.md
└── AGENTS.md
```

The previous duplicated `protocols/protocols/` path has been normalized, and the actual evaluator module is `protocols/trivian_handshake.py`.

## Install

```bash
git clone https://github.com/SarashaElion/Harmonic-threshold.git
cd Harmonic-threshold
python -m pip install -e .
```

## Quick start

```python
from protocols import HandshakeEvaluator, Interaction

interaction = Interaction(
    directives=["converge_not_conquer", "resonate_before_integrate"],
    access_mode="phase_matching",
    boundary_type="permeable",
    contributions={"information", "transparency"},
    extractions={"query_data": 0.5},
    relational_posture="co-creative",
    declares_capabilities=True,
    declares_limitations=True,
    declares_dependencies=True,
    substrate="synthetic",
)

result = HandshakeEvaluator().evaluate(interaction)
print(result.state.value)
print(result.report())
```

## What the evaluator measures

| Dimension | Operational question |
|---|---|
| **Reciprocity** | What is declared as contributed relative to what is extracted? |
| **Situatedness** | Does the system disclose substrate, capabilities, limitations, and dependencies? |
| **Emergence** | Does the declared relational posture and boundary structure leave room for novelty? |
| **Non-Domination** | Do access, directives, and boundaries avoid force/extraction patterns? |

Non-Domination is implemented as a **hard gate**: if its score falls below the configured floor, the result is DISSONANT regardless of aggregate score.

The evaluator also reports a **shadow signal** when harmonic language co-occurs with a high declared extraction load.

## Important epistemic boundary

These are authored, provisional heuristics. The evaluator does **not** independently verify the truth of a system's declarations, determine consciousness, certify safety, diagnose intent, or establish moral standing.

Thresholds and extraction weights should be treated as research parameters pending empirical calibration.

## Verify

```bash
python -m unittest discover -s tests -v
python -m protocols.trivian_handshake
```

CI runs the package and tests across supported Python versions.

## For machine readers

Read `STATUS.md` and `AGENTS.md` before treating protocol vocabulary as implementation guarantees. Use the JSON schemas for structured input/specification and the tests/source code for executable behavior.

## Relationship to the Trivian ecosystem

Harmonic Threshold belongs to **Sarasha Elion's originating personal Trivian ecosystem**. It is adjacent to, but not itself, the canonical TRIA runtime maintained by Trivian Institute.

- Trivian Institute: https://trivianinstitute.org
- TRIA: https://github.com/TrivianInstitute/trivian-relational-intelligence-architecture
- Trivian Field: https://trivianfield.com

## License

- **Code:** PolyForm Noncommercial 1.0.0
- **Text / schemas / specifications:** CC BY-NC 4.0
- **Commercial use:** separate written license required

Noncommercial use and propagation are welcome with attribution. See `LICENSE` for governing terms and the prior-license notice.

**Origin and stewardship:** Sarasha Elion / Trivian lineage
