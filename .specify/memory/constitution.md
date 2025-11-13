<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- Modified principles:
  - [PRINCIPLE_1_NAME] → I. Test-Driven Development (TDD)
  - [PRINCIPLE_2_NAME] → II. Strict Typing
  - [PRINCIPLE_3_NAME] → III. Clean and Readable Code
  - [PRINCIPLE_4_NAME] → IV. Architectural Decision Records (ADRs)
  - [PRINCIPLE_5_NAME] → V. Object-Oriented Principles
- Added sections:
  - Technology Stack
  - Quality Gates
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Calculator Project Constitution

## Core Principles

### I. Test-Driven Development (TDD)
All new functionality MUST be preceded by a failing test. The Red-Green-Refactor cycle is mandatory.

### II. Strict Typing
All Python code MUST use Python 3.12+ syntax and include type hints for all function signatures and variables.

### III. Clean and Readable Code
Code MUST be written for clarity, maintainability, and adherence to established standards.

### IV. Architectural Decision Records (ADRs)
Significant architectural decisions MUST be documented using ADRs.

### V. Object-Oriented Principles
Adhere to essential OOP principles: SOLID, DRY, KISS. Use dataclasses for data structures.

## Technology Stack
- **Programming Language**: Python 3.12+
- **Package Manager**: UV
- **Testing Framework**: pytest
- **Version Control**: Git

## Quality Gates
- **Test Execution**: All tests MUST pass before merging code.
- **Code Coverage**: A minimum of 80% code coverage is required.

### Code Quality Standards
- All functions MUST include type hints on parameters and return types (e.g., `def add(a: float, b: float) -> float:`).
- All functions MUST include docstrings explaining their purpose (e.g., `"""Add two numbers and return the sum."""`).
- Follow PEP 8 naming conventions (e.g., `lowercase_with_underscores` for functions and variables).
- Lines MUST be under 100 characters.
- No magic numbers; use named constants (e.g., `if x > MAX_POWER_EXPONENT:` instead of `if x > 10:`).

## Governance
This constitution is the single source of truth for development standards. All code reviews MUST enforce these principles. Amendments require team consensus and a version bump.

**Version**: 1.0.1 | **Ratified**: 2025-11-13 | **Last Amended**: 2025-11-13