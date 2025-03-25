# Count Occurrences of an Element in a Tuple

def count_occurrences(tup, element):
    return tup.count(element)

data = (1, 2, 3, 4, 2, 2, 5, 6)
element = 2
print(f"Element {element} appears {count_occurrences(data, element)} times.")
