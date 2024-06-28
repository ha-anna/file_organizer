from src.file_organizer.project import create_directories
from unittest.mock import patch
from src.file_organizer.directories import DIRECTORIES
import os


def test_create_directories():
    base_path = "/fake/base"

    with patch("src.file_organizer.project.create_directory") as mock_create_directory:
        create_directories(base_path, DIRECTORIES)

        for directory in DIRECTORIES:
            mock_create_directory.assert_any_call(os.path.join(base_path, directory))
        assert mock_create_directory.call_count == len(DIRECTORIES)
