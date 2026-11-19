[project]
name = "plantilla-python-uv"
version = "0.1.0"
description = "Plantilla reutilizable para proyectos Python gestionados con uv"
readme = "README.md"
authors = [
    { name = "Enrique_Acero", email = "acero29@gmail.com" }
]
requires-python = ">=3.13"
dependencies = []

[project.scripts]
plantilla-python-uv = "plantilla_python_uv.main:main"

[build-system]
requires = ["uv_build>=0.13.9,<0.14.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "pytest>=9.2.0",
    "ruff>=0.17.5",
]
[tool.ruff]
line-length = 88
target-version = "py313"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

