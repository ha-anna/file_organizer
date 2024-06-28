import pytest
from unittest.mock import patch
from src.file_organizer.project import organize_files
from src.file_organizer.directories import DIRECTORIES


@pytest.fixture
def temp_dir(tmp_path):
    base_path = tmp_path / "base"
    base_path.mkdir()
    (base_path / "file1.mp3").write_text("content1")
    (base_path / "file2.jpg").write_text("content2")
    (base_path / "file3.pdf").write_text("content3")

    return base_path


def test_organize_files(temp_dir):
    with (
        patch("src.file_organizer.project.create_directory"),
        patch("shutil.copy2") as mock_copy2,
        patch("os.path.isdir", return_value=True),
        patch("os.makedirs"),
    ):

        organize_files(temp_dir, DIRECTORIES)

        mock_copy2.assert_any_call(
            str(temp_dir / "file1.mp3"), str(temp_dir / "Music" / "file1.mp3")
        )
        mock_copy2.assert_any_call(
            str(temp_dir / "file2.jpg"), str(temp_dir / "Images" / "file2.jpg")
        )
        mock_copy2.assert_any_call(
            str(temp_dir / "file3.pdf"), str(temp_dir / "Documents" / "file3.pdf")
        )
        assert mock_copy2.call_count == 3


def test_organize_files_with_others(temp_dir):
    (temp_dir / "file4.txt").write_text("content4")

    with (
        patch("src.file_organizer.project.create_directory") as mock_create_directory,
        patch("shutil.copy2") as mock_copy2,
        patch("os.path.isdir", return_value=True),
        patch("os.makedirs"),
    ):

        organize_files(temp_dir, DIRECTORIES)

        mock_copy2.assert_any_call(
            str(temp_dir / "file1.mp3"), str(temp_dir / "Music" / "file1.mp3")
        )
        mock_copy2.assert_any_call(
            str(temp_dir / "file2.jpg"), str(temp_dir / "Images" / "file2.jpg")
        )
        mock_copy2.assert_any_call(
            str(temp_dir / "file3.pdf"), str(temp_dir / "Documents" / "file3.pdf")
        )
        mock_copy2.assert_any_call(
            str(temp_dir / "file4.txt"), str(temp_dir / "Others" / "file4.txt")
        )
        assert mock_copy2.call_count == 4

        others_path = temp_dir / "Others"
        mock_create_directory.assert_called_with(others_path)
