correct_password = "password123"
attempts = 3 

while attempts > 0:
    password = input("Enter your password: ")
    
    if password == correct_password:
        print("Access granted ✅")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Access denied ❌. You have {attempts} attempt(s) left. Try again.")
        else:
            print("Access denied ❌. No more attempts left.")
