from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

docs = [
    "Win money now", 
    "Limited time offer", 
    "Cheap loans available", 
    "Hello friend, how are you", 
    "Let's meet tomorrow", 
    "Dinner at my place"
]
labels = ["spam", "spam", "spam", "not_spam", "not_spam", "not_spam"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

clf = MultinomialNB()
clf.fit(X, labels)

test_docs = [
    "Win a free loan offer now",
    "Are you free for dinner tomorrow"
]
X_test = vectorizer.transform(test_docs)
pred = clf.predict(X_test)

for doc, p in zip(test_docs, pred):
    print(f"{doc} --> {p}")
