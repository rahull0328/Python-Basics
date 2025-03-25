# Check if a Character is a Vowel or Consonant

def check_vowel_or_consonant(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        print(f"{char} is a Vowel")
    else:
        print(f"{char} is a Consonant")

check_vowel_or_consonant('A')
check_vowel_or_consonant('b')
