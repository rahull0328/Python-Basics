# Find the Index of an Element in a Tuple

def find_index(tup, element):
    if element in tup:
        return tup.index(element)
    return -1

values = (10, 20, 30, 40, 50)
print("Index of 30:", find_index(values, 30))
print("Index of 100:", find_index(values, 100))
