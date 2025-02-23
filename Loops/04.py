initial_investment = float(input("Enter the initial investment amount: "))
current_valuation = float(input("Enter the current valuation of the investment: "))

percentage_change = ((current_valuation - initial_investment) / initial_investment) * 100

print("\n===== Investment Summary =====")
print(f"Initial Investment : ₹{initial_investment:,.2f}")
print(f"Current Valuation  : ₹{current_valuation:,.2f}")
print(f"Percentage Change  : {percentage_change:.2f}%")

if percentage_change > 0:
    print("Your investment has grown! 🎉")
elif percentage_change < 0:
    print("Your investment has shrunk. 📉")
else:
    print("No change in your investment value.")
