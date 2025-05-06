# Display User Profile using **kwargs

# user_profile.py
def display_profile(**info):
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print()

display_profile(name="Alice", age=30, location="New York")
display_profile(username="coder123", level="Intermediate", language="Python")
