# CREATING A BankAccount CLASS

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def transfer(self, other_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.deposit(amount)
            return True
        else:
            return False

acc1 = BankAccount("SRA MARIA L DIAZ", 10000)
acc2 = BankAccount("SRA ANA MEDINA", 500)

accounts = {
    acc1.owner.strip().upper(): acc1,
    acc2.owner.strip().upper(): acc2
}

while True:
    print("\n____ WELCOME TO BANK ACCOUNT ____")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Transfer money")
    print("4. Balance")
    print("5. Exit")

    choice = int(input("\n___ ENTER THE OPTION TO THE MENU ____ : "))

    if choice == 1:
        amount = float(input("Enter amount you want to deposit: "))
        if acc1.deposit(amount):
            print("DEPOSIT SUCCESSFUL")
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = float(input("Enter amount you want to withdraw: "))
        if acc1.withdraw(amount):
            print("WITHDRAW SUCCESSFUL")
        else:
            print("Error")

    elif choice == 3:
        name = input("Enter account name: ").strip().upper()
        amount = float(input("Enter amount you want to transfer: "))
        if name in accounts:
            if accounts[name] == acc1:
                print("You cannot transfer to the same account")
            elif acc1.transfer(accounts[name], amount):
                print(f"TRANSFER SUCCESSFUL TO {accounts[name].owner}")
            else:
                print("ERROR: Not enough money")
        else:
            print("ACCOUNT NOT FOUND")

    elif choice == 4:
        print("Your balance is: ", acc1.get_balance())

    elif choice == 5:
        print("Thank you for your time")
        break

    else:
        print("Invalid option")
