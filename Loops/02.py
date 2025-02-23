bill_amount = float(input("Enter the total purchase amount: "))

if bill_amount < 5000:
    discount_rate = 5
elif 5000 <= bill_amount < 10000:
    discount_rate = 10
else:
    discount_rate = 15

discount_amount = (discount_rate / 100) * bill_amount
final_amount = bill_amount - discount_amount

print("\n===== Bill Summary =====")
print(f"Total Purchase Amount: ₹{bill_amount:,.2f}")
print(f"Discount Applied ({discount_rate}%): ₹{discount_amount:,.2f}")
print(f"Final Amount to Pay: ₹{final_amount:,.2f}")
