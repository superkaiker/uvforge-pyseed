# UVForge PySeed

**A reusable, reproducible Python project template powered by uv, pytest, pytest-cov, Ruff and mypy.**

UVForge PySeed provides a clean and consistent foundation for starting Python projects, with dependency management, automated testing, code quality checks and static type analysis already configured.

## Features

- Python 3.13+
- Dependency and environment management with [uv](https://docs.astral.sh/uv/)
- `src` layout for clean package organization
- Automated testing with pytest
- Test coverage reporting with pytest-cov
- Code quality and linting with Ruff
- Static type checking with mypy
- Reproducible dependencies using `uv.lock`
- Ready-to-use project structure

## Requirements

- Python 3.13 or newer
- uv

## Getting started

Create a new repository using this GitHub template or clone the repository.

Open the project directory:

```powershell
cd your-project
```

Install dependencies and synchronize the environment:

```powershell
uv sync
```

## Run the application

```powershell
uv run plantilla-python-uv
```

Expected output:

```text
Mi proyecto Python está funcionando.
```

## Testing

Run the automated tests:

```powershell
uv run pytest
```

Run tests with coverage reporting:

```powershell
uv run pytest --cov --cov-report=term-missing
```

## Code quality

Check code style and potential errors with Ruff:

```powershell
uv run ruff check .
```

Check static types with mypy:

```powershell
uv run mypy
```

Verify that the lockfile and project environment are synchronized:

```powershell
uv sync --check
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

### Main components

- `src/`: application source code.
- `tests/`: automated tests.
- `pyproject.toml`: project metadata, dependencies and tool configuration.
- `uv.lock`: locked dependency versions for reproducible environments.
- `.python-version`: project Python version.
- `.gitignore`: files and directories excluded from Git.

## Development principles

- Keep dependencies to a minimum.
- Prefer reproducible environments.
- Test application behavior automatically.
- Maintain readable and consistent code.
- Use static analysis to catch issues early.
- Add tools only when they provide real value.

## License

No license has been specified yet.