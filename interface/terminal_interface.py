import sys
from time import sleep
from getpass import getpass
from models.customer import Customer
from decimal import Decimal  # Import Decimal to convert input strings to Decimal objects

class TerminalInterface:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def clear_screen(self):
        print("\033c", end="")

    def show_welcome_message(self):
        self.clear_screen()
        print("Welcome to the Banking Application!")
        sleep(1)

    def main_menu(self):
        while True:
            self.clear_screen()
            print("Main Menu:")
            print("1. Create a New User")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.create_user_menu()
            elif choice == '2':
                self.login_menu()
            elif choice == '3':
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice, please try again.")

    def create_user_menu(self):
        self.clear_screen()
        print("Create a New User:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")
        user = self.bank.create_customer(name, email, password)
        print(f"User {user.name} created successfully.")
        sleep(1)
        self.main_menu()

    def login_menu(self):
        self.clear_screen()
        print("Login:")
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")
        users = self.bank.db.fetchall("SELECT * FROM customers WHERE email=%s", (email,))
        if users:
            user_data = users[0]
            customer_id, name, email, stored_password = user_data
            if password == stored_password:
                self.current_user = Customer(customer_id, name, email, password)
                print(f"Welcome back, {self.current_user.name}!")
                self.user_menu()
            else:
                print("Incorrect password!")
        else:
            print("User not found!")
        sleep(1)
        self.main_menu()

    def user_menu(self):
        while True:
            self.clear_screen()
            print(f"Welcome {self.current_user.name}!")
            print("1. Create an Account")
            print("2. View Your Accounts")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                self.create_account_menu()
            elif choice == '2':
                self.view_accounts_menu()
            elif choice == '3':
                self.deposit_menu()
            elif choice == '4':
                self.withdraw_menu()
            elif choice == '5':
                self.transfer_menu()
            elif choice == '6':
                print("Logging out...")
                self.current_user = None
                break
            else:
                print("Invalid choice, please try again.")

    def create_account_menu(self):
        self.clear_screen()
        print("Create Account:")
        acc_type = input("Enter account type (checking/savings): ").lower()
        if acc_type in ["checking", "savings"]:
            initial_balance = float(input("Enter initial balance: "))
            account = self.bank.create_account(self.current_user.customer_id, acc_type, initial_balance)
            print(f"{acc_type.capitalize()} account created with balance: {account.get_balance()}")
        else:
            print("Invalid account type!")
        sleep(1)

    def view_accounts_menu(self):
        self.clear_screen()
        print("Your Accounts:")
        accounts = self.current_user.get_accounts(self.bank.db)
        if accounts:
            for acc in accounts:
                print(f"Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
        else:
            print("No accounts found!")
        input("\nPress Enter to return to the menu.")

    def deposit_menu(self):
        self.clear_screen()
        print("Deposit Money:")
        accounts = self.current_user.get_accounts(self.bank.db)
        if accounts:
            for acc in accounts:
                print(f"Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
            account_id = int(input("Enter the account ID to deposit into: "))
            amount = Decimal(input("Enter the amount to deposit: "))
            account = next(acc for acc in accounts if acc.account_id == account_id)
            account.deposit(amount)
            self.bank.db.execute(
                "UPDATE accounts SET balance=%s WHERE account_id=%s",
                (account.get_balance(), account.account_id)
            )
            print(f"Deposited {amount} into account {account_id}. New balance: {account.get_balance()}")
        else:
            print("No accounts found!")
        sleep(1)

    def withdraw_menu(self):
        self.clear_screen()
        print("Withdraw Money:")
        accounts = self.current_user.get_accounts(self.bank.db)
        if accounts:
            for acc in accounts:
                print(f"Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
            account_id = int(input("Enter the account ID to withdraw from: "))
            amount = float(input("Enter the amount to withdraw: "))
            account = next(acc for acc in accounts if acc.account_id == account_id)
            account.withdraw(amount)
            self.bank.db.execute(
                "UPDATE accounts SET balance=%s WHERE account_id=%s",
                (account.get_balance(), account.account_id)
            )
            print(f"Withdrew {amount} from account {account_id}. New balance: {account.get_balance()}")
        else:
            print("No accounts found!")
        sleep(1)

    def transfer_menu(self):
        self.clear_screen()
        print("Transfer Money:")
        accounts = self.current_user.get_accounts(self.bank.db)
        if accounts:
            for acc in accounts:
                print(f"Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
            account_id = int(input("Enter the account ID to transfer from: "))
            amount = float(input("Enter the amount to transfer: "))
            recipient_email = input("Enter recipient's email: ")
            recipient = self.bank.db.fetchall("SELECT * FROM customers WHERE email=%s", (recipient_email,))
            if recipient:
                recipient_data = recipient[0]
                recipient_id = recipient_data[0]
                recipient_accounts = [
                    acc for acc in self.bank.db.fetchall("SELECT * FROM accounts WHERE customer_id=%s", (recipient_id,))
                ]
                # Find recipient's corresponding account if applicable; adjust logic as needed.
                recipient_account = next((acc for acc in recipient_accounts if acc[0] == account_id), None)
                sender_account = next(acc for acc in accounts if acc.account_id == account_id)
                if sender_account.get_balance() >= amount:
                    sender_account.withdraw(amount)
                    self.bank.db.execute(
                        "UPDATE accounts SET balance=%s WHERE account_id=%s",
                        (sender_account.get_balance(), account_id)
                    )
                    print(f"Transferred {amount} to {recipient_email}. New balance: {sender_account.get_balance()}")
                else:
                    print("Insufficient balance!")
            else:
                print("Recipient not found!")
        else:
            print("No accounts found!")
        sleep(1)


