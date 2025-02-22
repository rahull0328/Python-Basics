emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
experience = int(input("Enter Number of Years of Experience: "))
current_salary = float(input("Enter Current Salary: "))

increment_amount = current_salary * 0.10
updated_salary = current_salary + increment_amount

print("\n===== Employee Salary Details =====")
print(f"Employee ID        : {emp_id}")
print(f"Employee Name      : {name}")
print(f"Years of Experience: {experience}")
print(f"Current Salary     : ₹{current_salary:,.2f}")
print(f"Increment Amount   : ₹{increment_amount:,.2f}")
print(f"Updated Salary     : ₹{updated_salary:,.2f}")
