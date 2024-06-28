from src.file_organizer.project import create_directory
from unittest.mock import patch


def test_create_directory_success():
    with (
        patch("os.path.isdir", return_value=False),
        patch("os.makedirs") as mock_makedirs,
    ):
        create_directory("/fake/path")
        mock_makedirs.assert_called_once_with("/fake/path")


def test_create_directory_exists():
    with (
        patch("os.path.isdir", return_value=True),
        patch("os.makedirs") as mock_makedirs,
    ):
        create_directory("/fake/path")
        mock_makedirs.assert_not_called()


def test_create_directory_permission_error():
    with (
        patch("os.path.isdir", return_value=False),
        patch("os.makedirs", side_effect=PermissionError),
    ):
        with patch("sys.exit") as mock_exit:
            create_directory("/fake/path")
            mock_exit.assert_called_once_with(
                "Permission denied: Cannot create directory /fake/path"
            )


def test_create_directory_os_error():
    with (
        patch("os.path.isdir", return_value=False),
        patch("os.makedirs", side_effect=OSError("Error")),
    ):
        with patch("sys.exit") as mock_exit:
            create_directory("/fake/path")
            mock_exit.assert_called_once_with(
                "Error creating directory /fake/path: Error"
            )
