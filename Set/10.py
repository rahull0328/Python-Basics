# hecking if Two Strings are Anagrams Using Sets

def are_anagrams(str1, str2):
    return set(str1.lower()) == set(str2.lower())

print("Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))
print("Are 'hello' and 'world' anagrams?", are_anagrams("hello", "world"))
