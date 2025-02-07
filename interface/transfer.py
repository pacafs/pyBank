from decimal import Decimal
from db.queries import get_customer_by_email, get_accounts_by_customer_id, update_account_balance

def transfer_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("Transfer Money:")
    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        for index, acc in enumerate(accounts, start=1):
            print(f"{index}. Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
        while True:
            try:
                selection = int(input("Select the account number to transfer from: "))
                if 1 <= selection <= len(accounts):
                    break
                else:
                    print("Invalid seletion, please choose a valid nr from the list.")
            except ValueError:
                print("Please enter a valid number.")
        sender_account = accounts[selection - 1]
        amount = Decimal(input("Enter the amount to transfer: "))
        recipient_email = input("Enter recipient's email: ")
        recipient = get_customer_by_email(recipient_email)
        if recipient:
            recipient_data = recipient[0]
            recipient_id = recipient_data[0]
            recipient_accounts = get_accounts_by_customer_id(recipient_id)
            if recipient_accounts:
                recipient_account_data = recipient_accounts[0]
                recipient_account_id, _, _, recipient_balance = recipient_account_data
                if sender_account.get_balance() >= amount:
                    sender_account.withdraw(amount)
                    new_recipient_balance = recipient_balance + amount
                    update_account_balance(recipient_account_id, new_recipient_balance)
                    bank.process_transaction(sender_account.customer_id, recipient_id, float(amount))
                    print(f"Transferred {amount} to {recipient_email}. New balance: {sender_account.get_balance()}")
                else:
                    print("❌ No Funds!")
            else:
                print("❌ Recipient has no account")
        else:
            print("❌ Recipient not found!")
    else:
        print("❌ No accounts found!")
