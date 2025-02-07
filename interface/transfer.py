from decimal import Decimal
from db.queries import fetchall, execute

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
                    print("Invalid selection, please choose a valid number from the list.")
            except ValueError:
                print("Please enter a valid number.")
        sender_account = accounts[selection - 1]
        amount = Decimal(input("Enter the amount to transfer: "))
        recipient_email = input("Enter recipient's email: ")
        recipient = fetchall("SELECT * FROM customers WHERE email=%s", (recipient_email,))
        if recipient:
            recipient_data = recipient[0]
            recipient_id = recipient_data[0]
            recipient_accounts = fetchall("SELECT * FROM accounts WHERE customer_id=%s", (recipient_id,))
            if recipient_accounts:
                recipient_account_data = recipient_accounts[0]
                recipient_account_id, _, _, recipient_balance = recipient_account_data
                if sender_account.get_balance() >= amount:
                    sender_account.withdraw(amount)
                    execute(
                        "UPDATE accounts SET balance=%s WHERE account_id=%s",
                        (sender_account.get_balance(), sender_account.account_id)
                    )
                    new_recipient_balance = recipient_balance + amount
                    execute(
                        "UPDATE accounts SET balance=%s WHERE account_id=%s",
                        (new_recipient_balance, recipient_account_id)
                    )
                    bank.process_transaction(sender_account.customer_id, recipient_id, float(amount))
                    print(f"Transferred {amount} to {recipient_email}. New balance: {sender_account.get_balance()}")
                else:
                    print("Insufficient balance!")
            else:
                print("Recipient has no account to receive transfers!")
        else:
            print("Recipient not found!")
    else:
        print("No accounts found!")
