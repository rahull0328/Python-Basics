# String Manipulation Using If-Else

text = input("Enter a string: ")

if text == text[::-1]:  # Checks for palindrome
    if len(text) > 5:
        print("Palindrome and has more than 5 characters")
    else:
        print("Palindrome but short")
else:
    print("Not a palindrome")
