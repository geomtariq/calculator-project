# Research: Calculator Library

## Decision: Use Python's `decimal` Module for All Calculations

**Rationale**:
- **Precision**: The `decimal` module provides user-configurable precision, avoiding the inherent inaccuracies of binary floating-point arithmetic (e.g., `0.1 + 0.2 != 0.3`). This is critical for a calculator where users expect exact decimal results.
- **Standard Library**: As a built-in module, it requires no external dependencies, simplifying the project setup.
- **Robustness**: It handles decimal arithmetic according to established standards, which is ideal for financial and scientific calculations.

**Alternatives considered**:
- **Standard floats**: Rejected due to their potential for precision errors, which would violate the core requirement of accuracy.

## Decision: CLI Implementation using `argparse`

**Rationale**:
- **Standard Library**: `argparse` is the standard, built-in Python library for parsing command-line arguments. It is powerful, flexible, and well-documented.
- **Simplicity**: For the basic CLI required by the spec (`python -m calculator <operation> <arg1> <arg2>`), `argparse` is straightforward to implement.

**Alternatives considered**:
- **`sys.argv`**: Rejected as it would require manual parsing of arguments, which is more error-prone and less maintainable than using `argparse`.
- **Third-party libraries (e.g., Click, Typer)**: Rejected as overkill for the simple CLI required. While powerful, they would add external dependencies for a non-core feature.
