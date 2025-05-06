import os
import shutil
from pathlib import Path

def move_files(source_dir, destination_dir, extensions):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    for ext in extensions:
        sub_dir = os.path.join(destination_dir, ext.lstrip('.'))
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)

    for file_name in os.listdir(source_dir):
        for ext in extensions:
            if file_name.endswith(ext):
                source_path = os.path.join(source_dir, file_name)
                destination_path = os.path.join(destination_dir, ext.lstrip('.'), file_name)
                shutil.move(source_path, destination_path)
                print(f"Moved: {file_name} to {ext.lstrip('.')} folder")

if __name__ == "__main__":
    source_directory = str(Path.home() / "Downloads")
    destination_directory = input("Enter the destination directory: ").strip()
    file_extensions = (".epub", ".pdf")

    move_files(source_directory, destination_directory, file_extensions)