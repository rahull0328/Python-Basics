# Find the Difference Between Two Dates

from datetime import datetime  

date1 = datetime(2025, 5, 1)  # May 1, 2025
date2 = datetime(2025, 3, 29) # March 29, 2025

# Calculate difference
difference = date1 - date2

print(f"Difference: {difference.days} days")
