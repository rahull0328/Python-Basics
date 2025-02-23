a = input("Enter first string: ")
x = input("Enter second string: ")

max_length = max(len(a), len(x))

result = ""
for i in range(max_length):
    if i < len(a):
        result += a[i]
    if i < len(x):
        result += x[i]

print("Combined String:", result)
