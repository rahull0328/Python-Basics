# Find common keys in multiple dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'c': 7, 'd': 8, 'e': 9}

common_keys = set(dict1.keys()) & set(dict2.keys()) & set(dict3.keys())
print("Common keys:", common_keys)
