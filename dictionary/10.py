# Build an inverted index from a list of words

documents = [
    "Python is great",
    "Python is easy to learn",
    "Machine learning with Python"
]

inverted_index = {}

for i, doc in enumerate(documents):
    words = doc.lower().split()
    for word in words:
        if word not in inverted_index:
            inverted_index[word] = []
        inverted_index[word].append(i)

print(inverted_index)
