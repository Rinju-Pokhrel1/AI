
comment = input("Enter your comment: ")

spam_keywords = [
    "make a lot of money",
    "subscribe this",
    "click this"
]


is_spam = False
for keyword in spam_keywords:
  
    if keyword in comment.lower():
      
        is_spam = True
    
        break
print("Qn.3 Rinju Pokhrel")
if is_spam:
    print("This comment has been flagged as spam.")
else:
    print("This comment is not spam.")

