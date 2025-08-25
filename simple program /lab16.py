def censor_multiple_words_in_file(filename, words_to_censor, replacement_string):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        for word in words_to_censor:
            content = content.replace(word, replacement_string)
        
        with open(filename, 'w') as file:
            file.write(content)
            
        print(f"All specified words have been censored in '{filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# Example usage:
filename = "file.txt"
words_to_censor = ["DONKEY", "MONKEY"]
replacement_string = "###"

censor_multiple_words_in_file(filename, words_to_censor, replacement_string)
