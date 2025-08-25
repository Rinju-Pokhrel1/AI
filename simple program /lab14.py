def contains_twinkle(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            if 'TWINKLE' in text:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False

filename = "sample.txt"
if contains_twinkle(filename):
    print("The word 'TWINKLE' is present in the file.")
else:
    print("The word 'TWINKLE' is NOT present in the file.")
