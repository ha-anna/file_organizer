from src.file_organizer.project import get_delete_permission
from pathlib import Path

path = str(Path().absolute())


def test_get_delete_permission_true(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert get_delete_permission(f"{path}/mess") is True
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert get_delete_permission(f"{path}/mess") is True


def test_get_delete_permission_false(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert get_delete_permission(f"{path}/mess") is False
    monkeypatch.setattr("builtins.input", lambda _: "qwertyuio")
    assert get_delete_permission(f"{path}/mess") is False
