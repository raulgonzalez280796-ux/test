import os
import argparse
from pathlib import Path

def get_directory_size(path="."):
    """Calculates the total size of a directory in bytes."""
    total_size = 0
    try:
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # Skip if it is a symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
    except Exception as e:
        print(f"Error reading directory: {e}")
    return total_size

def format_size(size_in_bytes):
    """Formats the size in a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate total directory size.")
    parser.add_argument("-p", "--path", type=str, default=".", help="Path to the target directory")
    args = parser.parse_args()
    
    target_path = Path(args.path)
    if target_path.exists() and target_path.is_dir():
        size = get_directory_size(target_path)
        print(f"Total size of '{target_path.absolute()}': {format_size(size)}")
    else:
        print("Error: Invalid directory path.")