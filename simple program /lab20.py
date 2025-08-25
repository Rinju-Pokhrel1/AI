import os

old_filename = "file.txt" 
new_filename = "RENAMED_BY_PYTHON.TXT"

try:
    os.rename(old_filename, new_filename)
    print(f"File has been renamed to '{new_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{old_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
