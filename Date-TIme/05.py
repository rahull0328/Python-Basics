# Add and Subtract Days from a Given Date

from datetime import datetime, timedelta  

# Get today's date
today = datetime.today()

# Add 10 days
future_date = today + timedelta(days=10)

# Subtract 7 days
past_date = today - timedelta(days=7)

print("Today's Date:", today.strftime("%Y-%m-%d"))
print("Future Date (10 days later):", future_date.strftime("%Y-%m-%d"))
print("Past Date (7 days ago):", past_date.strftime("%Y-%m-%d"))
