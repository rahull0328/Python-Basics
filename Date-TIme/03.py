# Convert String to Datetime Object

from datetime import datetime  

date_string = "29-03-2025 14:30:00"  
date_object = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

print("Converted Datetime Object:", date_object)
