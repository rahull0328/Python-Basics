# Sorting List of Tuples using Lambda Function

# sort_lambda.py
students = [("Alice", 85), ("Bob", 78), ("Charlie", 92)]

# Sort by marks descending
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)

for name, score in students_sorted:
    print(f"{name}: {score}")
