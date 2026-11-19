
import subprocess
import sys

from plantilla_python_uv.main import main


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out == "Mi proyecto Python está funcionando.\n"
    assert captured.err == ""


def test_main_module_execution():
    result = subprocess.run(
        [sys.executable, "-m", "plantilla_python_uv.main"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout == "Mi proyecto Python está funcionando.\n"
    assert result.stderr == ""
