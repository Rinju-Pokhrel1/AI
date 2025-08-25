import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
copy_file("file.txt", "file_backup.txt")
