from src.file_organizer.project import delete_files
import pytest
from unittest.mock import patch


@pytest.fixture
def temp_dir2(tmp_path):
    file1 = tmp_path / "file1.jpg"
    file2 = tmp_path / "file2.pdf"
    file1.write_text("content1")
    file2.write_text("content1")

    return tmp_path


def test_delete_files(temp_dir2):
    with patch("os.remove") as mock_remove:
        delete_files(temp_dir2)
        mock_remove.assert_any_call(str(temp_dir2 / "file1.jpg"))
        mock_remove.assert_any_call(str(temp_dir2 / "file2.pdf"))
        assert mock_remove.call_count == 2
