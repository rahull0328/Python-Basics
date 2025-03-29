# Get the Current Date & Time

from datetime import datetime  

# Get current date and time
now = datetime.now()

print("Current Date and Time:", now)
print("Formatted Date:", now.strftime("%Y-%m-%d"))
print("Formatted Time:", now.strftime("%H:%M:%S"))
