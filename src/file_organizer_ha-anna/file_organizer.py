import os
import sys
import re
import shutil
from pathlib import Path
from directories import DIRECTORIES


# TODO: testing
# TODO: record presentation
# TODO: submit project


def main():
    while True:
        try:
            BASE_PATH = Path(get_directory_path())
            create_directories(BASE_PATH, DIRECTORIES)
            organize_files(BASE_PATH, DIRECTORIES)
            print(f"Files in {str(BASE_PATH)} have been organized!")
            if get_delete_permission(BASE_PATH):
                delete_files(BASE_PATH)
            sys.exit(0)
        except ValueError:
            print("Invalid path, try something like: \nabc/def")
            pass


def get_directory_path():
    path = input("Input path to directory that you want to organize: ")
    absolute_path = str(Path().absolute()) + "/" + path
    validate_path(absolute_path)
    return absolute_path


def validate_path(str):
    res = re.search(r"^((/[a-zA-Z0-9-._ ]+)+|/)$", str)
    if res is None:
        raise ValueError


def create_directories(base_path, directories):
    for dir in directories:
        dir_path = os.path.join(base_path, dir)
        create_directory(dir_path)


def create_directory(dir_path):
    try:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            print(f"Successfuly created {dir_path} folder...")
    except PermissionError:
        sys.exit(f"Permission denied: Cannot create directory {dir_path}")
    except OSError as e:
        sys.exit(f"Error creating directory {dir_path}: {e}")


def organize_files(base_path, directories):
    for file_path in base_path.iterdir():
        if file_path.is_file():
            moved = False
            for directory, extensions in directories.items():
                if file_path.suffix.lower() in extensions:
                    try:
                        shutil.copyfile(
                            str(file_path), str(base_path / directory / file_path.name)
                        )
                        moved = True
                    except PermissionError:
                        print(
                            f"Permission denied: Cannot move file {file_path} to {base_path / directory}"
                        )
                    break
            if not moved:
                others_path = base_path / "Others"
                try:
                    create_directory(others_path)
                    shutil.copyfile(str(file_path), str(others_path / file_path.name))
                except PermissionError:
                    print(
                        f"Permission denied: Cannot move file {file_path} to {base_path / directory}"
                    )


def get_delete_permission(base_path):
    permission = input(f"Want to delete the moved files in {base_path}? ")
    if permission == "Y" or permission == "y":
        return True
    return False


def delete_files(base_path):
    for file_path in base_path.iterdir():
        if file_path.is_file():
            try:
                os.remove(str(base_path / file_path.name))
            except OSError:
                print(f"Failed to remove {file_path.name}")
                pass
    print(f"Files in {base_path} have been deleted")


if __name__ == "__main__":
    main()
