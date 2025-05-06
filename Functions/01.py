# Calculator with Functions and Default Arguments

# calculator.py
def calculate(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculate(10, 5))               # Default: addition
print(calculate(10, 5, 'multiply'))   # Multiplication
