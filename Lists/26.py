bank_accounts = [
    [1001, 'account1', 5000],
    [1002, 'account2', 5000],
    [1003, 'account3', 5000]
]

def find_account(account_number):
    for account in bank_accounts:
        if account[0] == account_number:
            return account
    return None

account_number = int(input("Enter your bank account number: "))
account = find_account(account_number)

if account:
    print(f"\nWelcome {account[1]}!")
    
    while True:
        print("\nChoose an option:")
        print("1. Check Current Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(f"Your Current Balance: Rs.{account[2]}")
        
        elif choice == '2':
            deposit_amount = float(input("Enter amount to deposit: Rs."))
            account[2] += deposit_amount
            print(f"Rs.{deposit_amount} deposited successfully. Updated Balance: Rs.{account[2]}")
        
        elif choice == '3':
            withdraw_amount = float(input("Enter amount to withdraw: Rs."))
            if account[2] - withdraw_amount >= 1000:
                if withdraw_amount <= account[2]:
                    account[2] -= withdraw_amount
                    print(f"Rs.{withdraw_amount} withdrawn successfully. Updated Balance: Rs.{account[2]}")
                else:
                    print("Insufficient balance.")
            else:
                print("Withdrawal denied! Minimum balance of Rs.1000 required.")
        
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

else:
    print("Account not found! Please enter a valid account number.")
