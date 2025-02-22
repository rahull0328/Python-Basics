grocery_list = []

def display_menu():
    print("\nGrocery List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View grocery list")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ")
    grocery_list.append(item)
    print(f"'{item}' has been added to the grocery list.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"'{item}' has been removed from the grocery list.")
    else:
        print(f"'{item}' not found in the grocery list.")

def view_list():
    if grocery_list:
        print("\nYour Grocery List:")
        for i, item in enumerate(grocery_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your grocery list is empty.")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
