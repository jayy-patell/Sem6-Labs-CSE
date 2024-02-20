class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account Balance for {self.name}: ${self.balance}")


def open_account():
    account_number = input("Enter account number: ")
    name = input("Enter name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, name, initial_balance)
    print("Account opened successfully.")
    return account


def main():
    print("Welcome to the Simple Banking System")
    while True:
        print("\n1. Open Account\n2. Withdraw\n3. Deposit\n4. Check Balance\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            account = open_account()
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '4':
            account.check_balance()
        elif choice == '5':
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()