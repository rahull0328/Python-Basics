# Finding the Missing Number in a Consecutive Series

def find_missing_number(lst):
    full_set = set(range(min(lst), max(lst) + 1))
    return full_set - set(lst)

numbers = [1, 2, 3, 5, 6, 8, 9]
print("Missing Numbers:", find_missing_number(numbers))