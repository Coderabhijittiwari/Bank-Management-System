import os

class AccountDetail:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account No: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

class Banks:
    def __init__(self):
        self.accounts = []
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(r"C:\Users\Dell\Desktop\101,John Doe,1000.0.txt"):
            with open(r"C:\Users\Dell\Desktop\101,John Doe,1000.0.txt", "r") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",")
                    self.accounts.append(AccountDetail(account_number, name, float(balance)))

    def save_accounts(self):
        with open("accounts.txt", "w") as file:
            for account in self.accounts:
                file.write(f"{account.account_number},{account.name},{account.balance}\n")

    def register_account(self, account_number, name):
        """Register a new account."""
        for account in self.accounts:
            if account.account_number == account_number:
                print("Error: Account number already exists!")
                return
        new_account = AccountDetail(account_number, name)
        self.accounts.append(new_account)
        self.save_accounts()
        print(f"Account created successfully for {name} with Account No: {account_number}.")

    def login(self, account_number):
        """Log in to an existing account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Error: Account not found!")
        return None

    def withdraw(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            print(f"Successfully withdrew {amount}. Remaining balance: {account.balance}")
            self.save_accounts()
        else:
            print("Error: Insufficient balance.")

    def deposit(self, account, amount):
        account.balance += amount
        print(f"Successfully deposited {amount}. New balance: {account.balance}")
        self.save_accounts()

    def check_balance(self, account):
        print(f"Account balance: {account.balance}")

    def close_account(self, account):
        self.accounts.remove(account)
        self.save_accounts()
        print(f"Account {account.account_number} closed successfully.")

    def menu(self):
        while True:
            print("\n=== Bank Management System ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                account_number = input("Enter account number: ")
                name = input("Enter your name: ")
                self.register_account(account_number, name)
            elif choice == "2":
                account_number = input("Enter account number to log in: ")
                account = self.login(account_number)
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def account_menu(self, account):
        while True:
            print("\n=== Account Services ===")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Close Account")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(account, amount)
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(account, amount)
            elif choice == "3":
                self.check_balance(account)
            elif choice == "4":
                self.close_account(account)
                break
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

# Main Prog
if __name__ == "__main__":
    bank_system = Banks()
    bank_system.menu()