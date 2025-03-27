# Merge two dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}  # Latest values are taken if keys overlap
print(merged_dict)
