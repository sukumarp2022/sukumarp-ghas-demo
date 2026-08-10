---
name: Improve backend test coverage
about: Ask Copilot to add focused tests for uncovered backend branches
title: "Improve backend test coverage for user search"
labels: testing
assignees: ""
---

## Goal

Increase meaningful test coverage for the user-search endpoint in `app/main.py`.

## Requirements

- Run `python -m pytest --cov=app --cov-report=term-missing --cov-report=xml:coverage.xml`.
- Cover the missing-name response.
- Cover the name-too-long response.
- Cover the no-results response.
- Keep tests deterministic and isolated.
- Do not call external services.
- Do not use real credentials.
- Do not change production behaviour.
- Do not reduce a coverage threshold.

## Acceptance criteria

- The missing branches are covered.
- Existing tests continue to pass.
- The pull request reports before and after coverage.
