# ADR-1: Use Decimal Module for Precision

- **Status:** Accepted
- **Date:** 2025-11-13
- **Feature:** 2-calculator-library
- **Context:** The calculator library requires a high degree of precision to avoid common floating-point inaccuracies (e.g., `0.1 + 0.2 != 0.3`). The chosen calculation engine must guarantee accurate decimal arithmetic as a core functional requirement.

## Decision

All internal arithmetic operations within the calculator library MUST be performed using Python's built-in `decimal` module. All inputs (integers, floats) will be converted to `Decimal` objects before any calculation.

## Consequences

### Positive

- **Accuracy**: Guarantees that calculations are free from binary floating-point rounding errors, providing the exactness expected from a calculator.
- **No External Dependencies**: The `decimal` module is part of the Python standard library, so it doesn't add any external dependencies to the project.
- **Configurable Precision**: The precision of calculations can be easily configured.

### Negative

- **Performance**: `Decimal` objects are slower than native floats. For a simple calculator, this is not a significant concern, but it would be a consideration for high-performance computing applications.
- **Type Complexity**: Requires careful handling of type conversions at the library's public API boundary.

## Alternatives Considered

- **Standard Floats**: This was rejected because standard binary floating-point arithmetic does not guarantee decimal precision, which is a core requirement of the specification. Using floats would lead to unexpected and incorrect results for certain calculations.

## References

- Feature Spec: `specs/2-calculator-library/spec.md`
- Implementation Plan: `specs/2-calculator-library/plan.md`
- Related ADRs: None
- Evaluator Evidence: None
