family_members_name = []
family_members_age = []

n = int(input("Enter the number of family members: "))

for i in range(n):
    name = input(f"Enter name of family member {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    
    family_members_name.append(name)
    family_members_age.append(age)

family_data = list(zip(family_members_name, family_members_age))

family_data.sort(key=lambda x: x[1], reverse=True)

print("\nFamily members sorted from older to younger:")
for name, age in family_data:
    print(f"{name} is {age} years old")
