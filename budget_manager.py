# PERSONAL BUDGET MANAGER

# list to store all transactions

transactions = []

# Function to add transactions:
def add_transaction():
    type = input("Enter type (income/expense): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date: ")

    transaction = {
        "type": type,
        "category": category,
        "amount": amount,
        "date": date
    }
    transactions.append(transaction)
    print("transaction added successfully.\n")

# Function to show transactions:
def show_transactions():

    if len(transactions) == 0:
        print("No transactions yet.\n")
        return

    for transaction in transactions:
        print(transaction)

    print()

# Function to show balance
def show_balance():

    income = 0
    expense = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            income += transaction["amount"]

        elif transaction["type"] == "expense":
            expense += transaction["amount"]

    balance = income -expense

    print("Total Income: ", income)
    print("Total Expense: ", expense)
    print("Balance: ", balance)

while True:

    print("=== BUDGET MANAGER ===")
    print("1 - Add transaction")
    print("2 - Show transactions")
    print("3 - Show balance")
    print("4 - Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_transaction()

    elif choice == 2:
        show_transactions()

    elif choice == 3:
        show_balance()

    elif choice == 4:
        print("Thank you for using this program")
        break

    else:
        print("Invalid Choice\n")
