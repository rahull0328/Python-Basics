# Removing Stop Words from a Sentence

def remove_stop_words(sentence, stop_words):
    words = set(sentence.lower().split())
    filtered_words = words - stop_words
    return " ".join(filtered_words)

sentence = "Python is an amazing programming language for development"
stop_words = {"is", "an", "for"}
print("Filtered Sentence:", remove_stop_words(sentence, stop_words))
