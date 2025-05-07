import os
import shutil
from pathlib import Path

def move_files(source_dir, destination_dir, extensions):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    moved_files_count = {ext: 0 for ext in extensions}

    for ext in extensions:
        sub_dir = os.path.join(destination_dir, ext.lstrip('.'))
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)

    for file_name in os.listdir(source_dir):
        file_lower = file_name.lower()
        for ext in extensions:
            if file_lower.endswith(ext.lower()):
                source_path = os.path.join(source_dir, file_name)
                sub_dir = os.path.join(destination_dir, ext.lstrip('.'))
                destination_path = os.path.join(sub_dir, file_name)

                # Handle duplicates by appending a counter
                base, extension = os.path.splitext(file_name)
                counter = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(sub_dir, f"{base}_{counter}{extension}")
                    counter += 1

                shutil.move(source_path, destination_path)
                print(f"Moved: {file_name} → {sub_dir}")
                moved_files_count[ext] += 1
                break  # Avoid double-moving if extensions overlap

    print("\nSummary:")
    for ext, count in moved_files_count.items():
        print(f"  {ext}: {count} file(s) moved")

if __name__ == "__main__":
    source_directory = str(Path.home() / "Downloads")
    destination_directory = input("Enter the destination directory: ").strip()

    user_input = input("Enter file extensions to move (comma-separated, e.g. .pdf,.epub), or press Enter for default [.pdf, .epub]: ").strip()
    if user_input:
        file_extensions = tuple(ext.strip() for ext in user_input.split(','))
    else:
        file_extensions = (".epub", ".pdf")

    move_files(source_directory, destination_directory, file_extensions)
