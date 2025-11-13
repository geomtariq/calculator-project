# Tasks: Calculator Library

**Input**: Design documents from `specs/2-calculator-library/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 [P] Create project structure: `src/calculator`, `tests`
- [ ] T002 [P] Create initial files: `src/calculator/__init__.py`, `src/calculator/calculator.py`, `src/calculator/cli.py`, `src/calculator/exceptions.py`, `tests/__init__.py`, `tests/test_calculator.py`, `tests/test_cli.py`

---

## Phase 2: User Story 1 - Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement `add`, `subtract`, `multiply`, and `divide` functions with full test coverage.

### Tests for User Story 1 (TDD)

- [ ] T003 [P] [US1] Write failing test for `add` in `tests/test_calculator.py`
- [ ] T004 [P] [US1] Write failing test for `subtract` in `tests/test_calculator.py`
- [ ] T005 [P] [US1] Write failing test for `multiply` in `tests/test_calculator.py`
- [ ] T006 [P] [US1] Write failing test for `divide` in `tests/test_calculator.py`

### Implementation for User Story 1

- [ ] T007 [US1] Implement `add` method in `src/calculator/calculator.py` to pass test
- [ ] T008 [US1] Implement `subtract` method in `src/calculator/calculator.py` to pass test
- [ ] T009 [US1] Implement `multiply` method in `src/calculator/calculator.py` to pass test
- [ ] T010 [US1] Implement `divide` method in `src/calculator/calculator.py` to pass test

---

## Phase 3: User Story 2 - Advanced Operations (Priority: P2)

**Goal**: Implement `power` and `sqrt` functions with full test coverage.

### Tests for User Story 2 (TDD)

- [ ] T011 [P] [US2] Write failing test for `power` in `tests/test_calculator.py`
- [ ] T012 [P] [US2] Write failing test for `sqrt` in `tests/test_calculator.py`

### Implementation for User Story 2

- [ ] T013 [US2] Implement `power` method in `src/calculator/calculator.py` to pass test
- [ ] T014 [US2] Implement `sqrt` method in `src/calculator/calculator.py` to pass test

---

## Phase 4: User Story 3 - Robust Error Handling (Priority: P1)

**Goal**: Implement and test all specified error conditions.

### Tests for User Story 3 (TDD)

- [ ] T015 [P] [US3] Write failing test for division by zero in `tests/test_calculator.py`
- [ ] T016 [P] [US3] Write failing test for `0**0` in `tests/test_calculator.py`
- [ ] T017 [P] [US3] Write failing test for `sqrt` of a negative number in `tests/test_calculator.py`
- [ ] T018 [P] [US3] Write failing test for non-numeric input in `tests/test_calculator.py`

### Implementation for User Story 3

- [ ] T019 [US3] Add division by zero check in `divide` method in `src/calculator/calculator.py`
- [ ] T020 [US3] Add `0**0` check in `power` method in `src/calculator/calculator.py`
- [ ] T021 [US3] Add negative number check in `sqrt` method in `src/calculator/calculator.py`
- [ ] T022 [US3] Add type checking and `TypeError` for all methods in `src/calculator/calculator.py`

---

## Phase 5: CLI Implementation

**Goal**: Implement the command-line interface.

### Tests for CLI

- [ ] T023 [P] Write integration tests for the CLI in `tests/test_cli.py` for all operations.

### Implementation for CLI

- [ ] T024 Implement CLI logic in `src/calculator/cli.py` using `argparse`.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T025 [P] Add docstrings and type hints to all functions and methods.
- [ ] T026 [P] Run `mypy` to verify type checking.
- [ ] T027 [P] Run `pytest --cov=src/calculator` to ensure 100% test coverage.
- [ ] T028 [P] Update `quickstart.md` with final usage examples.
