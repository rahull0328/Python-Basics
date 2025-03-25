# Find the Largest Among Three Numbers

def find_largest(a, b, c):
    if a > b and a > c:
        print(f"Largest number is: {a}")
    elif b > c:
        print(f"Largest number is: {b}")
    else:
        print(f"Largest number is: {c}")

find_largest(25, 18, 30)
