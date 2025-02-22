numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Enter a number to check: "))

if num in numbers:
    index_position = numbers.index(num)
    print(f"{num} is available at index {index_position}.")
else:
    print(f"{num} is not in the list.")
