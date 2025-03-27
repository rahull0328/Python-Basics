# Find the key with the maximum value

data = {'apple': 50, 'banana': 75, 'cherry': 60}

max_key = max(data, key=data.get)
print(f"Key with max value: {max_key} ({data[max_key]})")
