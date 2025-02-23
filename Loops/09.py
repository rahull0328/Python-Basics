str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common_prefix = ""
min_length = min(len(str1), len(str2))

for i in range(min_length):
    if str1[i] == str2[i]: 
        common_prefix += str1[i]
    else:
        break

if common_prefix:
    print("Common Prefix:", common_prefix)
else:
    print("No common prefix found.")
