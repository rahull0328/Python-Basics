# Swapping Values Using Tuples

def swap_values(a, b):
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After Swap: a = {a}, b = {b}")

swap_values(5, 10)