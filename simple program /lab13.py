def remove_word_from_list(word_list, word_to_remove):
    
    word_to_remove = word_to_remove.strip()
    
   
    new_list = [word for word in word_list if word.strip() != word_to_remove]
    
    return new_list


my_list = ["apple", " banana ", "orange", " banana", "grape"]
word = "banana"
result = remove_word_from_list(my_list, word)
print(result)
