weekly_expenses = [
    ("Monday", 120, "Groceries"),
    ("Monday", 50, "Transport"),
    ("Tuesday", 200, "Shopping"),
    ("Tuesday", 80, "Lunch"),
    ("Wednesday", 300, "Electronics"),
    ("Wednesday", 40, "Snacks"),
    ("Thursday", 150, "Dinner"),
    ("Thursday", 100, "Utilities"),
    ("Friday", 250, "Party"),
    ("Friday", 60, "Transport"),
    ("Saturday", 400, "Furniture"),
    ("Saturday", 90, "Coffee"),
    ("Sunday", 180, "Movies"),
    ("Sunday", 70, "Books"),
]

def count_expenses():
    expense_count = {}
    for day, _, _ in weekly_expenses:
        expense_count[day] = expense_count.get(day, 0) + 1
    return expense_count

def average_expenses():
    total_expenses = sum(amount for _, amount, _ in weekly_expenses)
    days = len(set(day for day, _, _ in weekly_expenses)) 
    return total_expenses / days

def highest_lowest_expense():
    highest_expense = max(weekly_expenses, key=lambda x: x[1])
    lowest_expense = min(weekly_expenses, key=lambda x: x[1])
    return highest_expense, lowest_expense

def highest_lowest_day():
    daily_totals = {}
    for day, amount, _ in weekly_expenses:
        daily_totals[day] = daily_totals.get(day, 0) + amount

    highest_day = max(daily_totals, key=daily_totals.get)
    lowest_day = min(daily_totals, key=daily_totals.get)

    return highest_day, daily_totals[highest_day], lowest_day, daily_totals[lowest_day]

def total_weekly_expense():
    return sum(amount for _, amount, _ in weekly_expenses)

def print_expense_report():
    print("\nWeekly Expense Report:")
    day_wise_expenses = {}
    for day, amount, description in weekly_expenses:
        if day not in day_wise_expenses:
            day_wise_expenses[day] = []
        day_wise_expenses[day].append((amount, description))

    for day, expenses in day_wise_expenses.items():
        print(f"\n{day}:")
        for amount, description in expenses:
            print(f"  Rs.{amount} - {description}")
    print("-" * 40)


print("Number of expenses per day:", count_expenses())

print("\nAverage expense per day: Rs.", round(average_expenses(), 2))

highest, lowest = highest_lowest_expense()
print(f"\nHighest expense: Rs.{highest[1]} on {highest[2]}")
print(f"       Lowest expense: Rs.{lowest[1]} on {lowest[2]}")

highest_day, highest_amt, lowest_day, lowest_amt = highest_lowest_day()
print(f"\nHighest total expense on {highest_day}: Rs.{highest_amt}")
print(f"       Lowest total expense on {lowest_day}: Rs.{lowest_amt}")

print("\nTotal weekly expense: Rs.", total_weekly_expense())

print_expense_report() 
