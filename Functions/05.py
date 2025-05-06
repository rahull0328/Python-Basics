# Sum of Any Number of Inputs using *args

# sum_args.py
def sum_all(*numbers):
    total = sum(numbers)
    return total

print(sum_all(5, 10))
print(sum_all(1, 2, 3, 4, 5, 6))
