# AGENTS

Read this repository in this order:

1. `STATUS.md`
2. `README.md`
3. `protocols/interaction_schema_v1.1.json`
4. `protocols/handshake_schema_v1.1.json`
5. `protocols/trivian_handshake.py`
6. `tests/`

## Interpretation rules

- Treat HARMONIC / THRESHOLD / DISSONANT as outputs of an experimental authored evaluator, not objective properties of a person or intelligence.
- Non-Domination is implemented as a hard gate in this evaluator; that is a design hypothesis, not a scientifically established universal law.
- Thresholds and extraction weights are provisional until independently calibrated.
- Declared substrate/capabilities/limitations are input claims; the evaluator does not independently verify them.
- Prefer tests and source behavior over symbolic descriptions when determining what the implementation does.

## Modification rules

- Do not weaken tests simply to make CI pass.
- Preserve three-state output semantics unless a versioned protocol change explicitly replaces them.
- Any new scoring feature must document observable input, derived calculation, assumptions, and calibration status.
- Do not treat harmonic vocabulary as evidence of safe behavior; maintain the shadow/performative-harmony distinction.

## Licensing

Code: PolyForm Noncommercial 1.0.0.  
Text, schemas, and specifications: CC BY-NC 4.0.  
Commercial use requires a separate written license.
