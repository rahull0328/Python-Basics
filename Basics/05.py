import datetime

age = int(input("Enter your age: "))

current_year = datetime.datetime.now().year

birth_year = current_year - age

print("Your birth year is:", birth_year)
