from decimal import Decimal
from rich.console import Console
from rich.table import Table
from db.queries import get_customer_by_email, get_accounts_by_customer_id, update_account_balance

def transfer_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    console = Console()
    console.print("💱 Transfer Money:\n", style="bold cyan")

    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        # Create a table to display sender accounts
        table = Table(title="Select a Sender Account", header_style="bold magenta")
        table.add_column("No.", justify="center", style="yellow", no_wrap=True)
        table.add_column("Account ID", style="white")
        table.add_column("Account Type", style="cyan")
        table.add_column("Balance", justify="right", style="green")

        for index, acc in enumerate(accounts, start=1):
            table.add_row(
                str(index),
                str(acc.account_id),
                acc.__class__.__name__,
                str(acc.get_balance())
            )
        console.print(table)

        # User selection of sender account
        while True:
            try:
                selection = int(input("Select the account number to transfer from: "))
                if 1 <= selection <= len(accounts):
                    break
                else:
                    console.print("Invalid selection, please choose a valid number from the list.", style="bold red")
            except ValueError:
                console.print("Please enter a valid number.", style="bold red")

        sender_account = accounts[selection - 1]

        # Input transfer amount with error handling
        try:
            amount_input = input("Enter the amount to transfer: ")
            amount = Decimal(amount_input)
        except Exception:
            console.print(f"Invalid amount entered: '{amount_input}'. Please enter a numeric value.", style="bold red")
            return

        # Enter recipient email and lookup recipient data
        recipient_email = input("Enter recipient's email: ")
        recipient = get_customer_by_email(recipient_email)
        if not recipient:
            console.print("❌ Recipient not found!", style="bold red")
            return

        recipient_data = recipient[0]
        recipient_id = recipient_data[0]
        recipient_accounts = get_accounts_by_customer_id(recipient_id)
        if not recipient_accounts:
            console.print("❌ Recipient has no account", style="bold red")
            return

        recipient_account_data = recipient_accounts[0]
        recipient_account_id, _, _, recipient_balance = recipient_account_data

        # Check for sufficient funds and process the transfer
        if sender_account.get_balance() >= amount:
            sender_account.withdraw(amount)
            new_recipient_balance = recipient_balance + amount
            update_account_balance(recipient_account_id, new_recipient_balance)
            bank.process_transaction(sender_account.customer_id, recipient_id, float(amount))
            console.print(
                f"✅ Transferred {amount} to {recipient_email}. New balance: {sender_account.get_balance()}",
                style="bold green"
            )
        else:
            console.print("❌ Insufficient funds!", style="bold red")
    else:
        console.print("😕 No accounts found!", style="bold red")
