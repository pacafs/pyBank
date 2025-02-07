from decimal import Decimal
from time import sleep
from db.queries import update_account_balance

def deposit_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("Deposit Money:")
    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        for index, acc in enumerate(accounts, start=1):
            print(f"{index}. Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
        while True:
            try:
                selection = int(input("Select the account number to deposit into: "))
                if 1 <= selection <= len(accounts):
                    break
                else:
                    print("Invalid selection, please choose a valid number from the list.")
            except ValueError:
                print("Please enter a valid number.")
        selected_account = accounts[selection - 1]
        amount = Decimal(input("Enter the amount to deposit: "))
        selected_account.deposit(amount)
        update_account_balance(selected_account.account_id, selected_account.get_balance())
        print(f"Deposited {amount} into account {selected_account.account_id}. New balance: {selected_account.get_balance()}")
    else:
        print("No accounts found!")
    sleep(1)

