# Get the Day of the Week for a Given Date

from datetime import datetime  

date_input = "2025-03-29"  
date_object = datetime.strptime(date_input, "%Y-%m-%d")

# Get weekday name
day_name = date_object.strftime("%A")

print(f"The day on {date_input} is {day_name}")
