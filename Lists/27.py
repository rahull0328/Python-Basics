users = [
    ['user1', 8000, (12000, 4000, 'W'), (17000, 5000, 'W'), (15000, 2000, 'D')],
    ['user2', 25000, (23000, 3000, 'D'), (18000, 5000, 'D'), (16000, 2000, 'D')],
]

def count_users():
    return len(users)

def print_balances():
    print("\nCurrent balance of each user:")
    for user in users:
        print(f"{user[0]}: Rs.{user[1]}")

def print_transaction_details():
    print("\nFirst and Last Transaction Details:")
    for user in users:
        first_transaction = user[2] 
        last_transaction = user[-1] 
        print(f"{user[0]}:")
        print(f"  First Transaction -> Initial Balance: {first_transaction[0]}, Amount: {first_transaction[1]}, Type: {first_transaction[2]}")
        print(f"  Last Transaction  -> Initial Balance: {last_transaction[0]}, Amount: {last_transaction[1]}, Type: {last_transaction[2]}")

def add_transaction(user_name, initial_balance, amount, transaction_type):
    for user in users:
        if user[0] == user_name:
            if transaction_type == 'W': 
                if user[1] - amount >= 0: 
                    user[1] -= amount
                    user.append((initial_balance, amount, 'W'))
                    print(f"Withdrawal of Rs.{amount} added for {user_name}. Updated balance: Rs.{user[1]}")
                else:
                    print("Insufficient balance!")
            elif transaction_type == 'D': 
                user[1] += amount
                user.append((initial_balance, amount, 'D'))
                print(f"Deposit of Rs.{amount} added for {user_name}. Updated balance: Rs.{user[1]}")
            return
    print("User not found!")

def add_user(user_name, initial_balance):
    new_user = [user_name, initial_balance]
    users.append(new_user)
    print(f"User {user_name} added successfully with balance Rs.{initial_balance}.")

def print_bank_statement():
    print("\nBank Statement Report:")
    for user in users:
        print(f"\nAccount Holder: {user[0]}")
        print(f"Current Balance: Rs.{user[1]}")
        print("Transactions:")
        for transaction in user[2:]:
            print(f"  Initial Balance: {transaction[0]}, Amount: {transaction[1]}, Type: {transaction[2]}")
        print("-" * 40)

print(f"Total Users: {count_users()}") 
print_balances() 
print_transaction_details() 

add_transaction('user1', 15000, 3000, 'D')

add_user('user3', 5000)

print_bank_statement()
