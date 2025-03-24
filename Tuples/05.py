# Checking for an Element in a Tuple

fruits = ("apple", "banana", "cherry", "mango")

# Checking if an element exists
fruit_to_check = "banana"
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is present in the tuple.")
else:
    print(f"{fruit_to_check} is not present in the tuple.")
