# UVForge PySeed

Reusable Python project template powered by **uv**, **pytest** and **Ruff**.

A clean and reproducible starting point for building Python applications with a consistent development environment.

## Features

- Python 3.13+
- Dependency and environment management with uv
- Pytest for automated testing
- Ruff for linting and code quality
- src layout for package organization
- Reusable project structure

## Requirements

- Python 3.13 or newer
- uv

## Getting started

Clone or create a new repository using this template.

Open the project directory:

```powershell
cd your-project
```

Install dependencies:

```powershell
uv sync
```

## Run the application

```powershell
uv run plantilla-python-uv
```

## Run tests

```powershell
uv run pytest
```

## Check code quality

```powershell
uv run ruff check .
```

## Project structure

```text
project/
├── src/
│   └── plantilla_python_uv/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_ejemplo.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

## Development principles

- Keep dependencies to a minimum.
- Use reproducible environments.
- Write automated tests.
- Maintain readable and consistent code.
- Add tools only when they provide real value.

## License

No license has been specified yet.
