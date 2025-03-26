# Nested If-Else with Exception Handling

try:
    num = float(input("Enter a number: "))
    if num > 0:
        if num % 2 == 0:
            print("Positive Even Number")
        else:
            print("Positive Odd Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
