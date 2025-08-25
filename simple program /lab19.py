filename = "file.txt"

# Open the file in write mode, which clears its contents
with open(filename, "w") as file:
    pass  # Do nothing, just open and close

print(f"The contents of '{filename}' have been wiped out.")
