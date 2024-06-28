from src.file_organizer.project import get_directory_path
from pathlib import Path


def test_get_directory_path(monkeypatch):
    path = str(Path().absolute())
    monkeypatch.setattr("builtins.input", lambda _: "resources/mess")
    assert get_directory_path() == f"{path}/resources/mess"
    monkeypatch.setattr("builtins.input", lambda _: "folder copy")
    assert get_directory_path() == f"{path}/folder copy"
    monkeypatch.setattr("builtins.input", lambda _: "Folder_.Name-")
    assert get_directory_path() == f"{path}/Folder_.Name-"
