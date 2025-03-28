# Finding Duplicate Elements in a List Using Sets

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 3]
print("Duplicate Elements:", find_duplicates(numbers))