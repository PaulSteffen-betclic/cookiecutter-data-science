import os
import shutil


def move_contents_to_parent_folder(folder_path):
    # Get a list of all files and directories in the folder
    contents = os.listdir(folder_path)

    # Iterate over each item
    for item in contents:
        # Form the full path to the item
        item_path = os.path.join(folder_path, item)

        # Move the item to the parent directory
        shutil.move(item_path, os.path.join(os.path.dirname(folder_path), item))

    # Remove the now empty folder
    os.rmdir(folder_path)

repository_name = '{{ cookiecutter.repo_name }}_'
move_contents_to_parent_folder(f"../{repository_name}")
