s = input("Enter a string: ").lower()

vowels = "aeiou"
count = 0
i = 0

while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1

print(f"Number of vowels in the given string: {count}")
