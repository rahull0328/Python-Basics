# Remove keys with duplicate values

data = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
unique_values = {}
filtered_dict = {}

for key, value in data.items():
    if value not in unique_values.values():
        unique_values[key] = value

print(unique_values)
