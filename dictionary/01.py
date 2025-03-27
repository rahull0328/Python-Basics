# Count the frequency of each word in a sentence

sentence = "apple orange banana apple orange apple"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
