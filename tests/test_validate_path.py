from src.file_organizer.project import validate_path
from pathlib import Path
import pytest


def test_validate_path():
    path = str(Path().absolute())
    assert validate_path(f"{path}/mess") is None
    with pytest.raises(ValueError):
        validate_path("abc")
