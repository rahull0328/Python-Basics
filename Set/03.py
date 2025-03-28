# Removing Elements from a Set

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Raises error if not found
my_set.discard(4)  # Does not raise error if not found
print("Set after removal:", my_set)
