age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ").strip().lower()

if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote.")
