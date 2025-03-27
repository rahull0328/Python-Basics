# Nested dictionary operations (CRUD)

students = {
    '101': {'name': 'Alice', 'age': 22, 'grade': 'A'},
    '102': {'name': 'Bob', 'age': 21, 'grade': 'B'}
}

# Add a new student
students['103'] = {'name': 'Charlie', 'age': 23, 'grade': 'A'}

# Update a student
students['101']['age'] = 23

# Delete a student
del students['102']

print(students)
