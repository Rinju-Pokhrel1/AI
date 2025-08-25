def compare_files_content(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            if content1 == content2:
                return True
            else:
                return False
    except FileNotFoundError:
        print("Error: One or both files were not found.")
        return False


# Example usage:
file1 = "file.txt"
file2 = "file_backup.txt"

if compare_files_content(file1, file2):
    print("Files have the same content.")
else:
    print("Files are different.")
