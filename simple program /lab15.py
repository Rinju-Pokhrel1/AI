filename = "file.txt"

with open(filename, "r") as file:
    data = file.read()

data = data.replace("DONKEY", "monkey")

with open(filename, "w") as file:
    file.write(data)

print("All occurrences of 'DONKEY' have been replaced with 'monkey'.")
