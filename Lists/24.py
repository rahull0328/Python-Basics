data_list = []

n = int(input("Enter the number of elements you want to add: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    data_list.append(element)

print("Final List:", data_list)
