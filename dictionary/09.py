# Group dictionary values by a common key

data = [
    {'name': 'Alice', 'subject': 'Math', 'score': 85},
    {'name': 'Bob', 'subject': 'Science', 'score': 90},
    {'name': 'Alice', 'subject': 'Science', 'score': 80},
    {'name': 'Bob', 'subject': 'Math', 'score': 88},
]

grouped_data = {}

for entry in data:
    name = entry['name']
    if name not in grouped_data:
        grouped_data[name] = []
    grouped_data[name].append({'subject': entry['subject'], 'score': entry['score']})

print(grouped_data)
