# Tic-Tac-Toe Test Automation Project

This repository contains a complete Playwright + Python + Pytest + POM automation project for the provided Tic-Tac-Toe application.

## Included Deliverables

- Test plan
- Test cases
- Gherkin scenarios
- Page Object Model structure
- Priority-based test folders: P0, P1, P2
- Allure reporting support
- GitHub Actions workflow

## Important Test Flow

The suite is intentionally written to create the account first, then use that account in the application, and validate logout at the end of the critical flow.

Default user used in the main flow:
- `nima`

## Project Structure

```text
.
├── app/
│   └── index.html
├── gherkin/
│   ├── auth.feature
│   ├── game.feature
│   ├── history.feature
│   ├── profile.feature
│   └── settings.feature
├── pages/
│   ├── __init__.py
│   ├── auth_page.py
│   ├── game_page.py
│   ├── history_page.py
│   ├── profile_page.py
│   └── settings_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── p0/
│   ├── p1/
│   └── p2/
├── test-plan.md
├── test-cases.md
├── requirements.txt
├── pytest.ini
└── .github/workflows/tests.yml
```

## Installation

```bash
pip install -r requirements.txt
python -m playwright install
```

## Run the application

```bash
cd app
python -m http.server 8000
```

## Run all tests

```bash
python -m pytest -v
```

## Run by priority

```bash
python -m pytest tests/p0 -v
python -m pytest tests/p1 -v
python -m pytest tests/p2 -v
```

## Run with Allure

```bash
python -m pytest -v --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```
