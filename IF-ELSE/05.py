# Simple Login System

def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        print("Login Successful!")
    else:
        print("Invalid Credentials")

login("admin", "1234")
login("user", "pass")
