a = input("Enter first string: ")
x = input("Enter second string: ")

min_length = min(len(a), len(x))

for i in range(min_length):
    print(a[i], x[i])
