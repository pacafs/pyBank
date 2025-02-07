from decimal import Decimal
from time import sleep
from rich.console import Console
from rich.table import Table
from db.queries import update_account_balance

def deposit_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    console = Console()
    console.print("💰 Deposit Money:\n", style="bold cyan")

    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        table = Table(title="Select an Account to Deposit Into", header_style="bold magenta")
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

        while True:
            try:
                selection = int(input("Select the account number to deposit into: "))
                if 1 <= selection <= len(accounts):
                    break
                else:
                    console.print("Invalid selection, please choose a valid number from the list.", style="bold red")
            except ValueError:
                console.print("Please enter a valid number.", style="bold red")

        selected_account = accounts[selection - 1]

        try:
            amount_input = input("Enter the amount to deposit: ")
            amount = Decimal(amount_input)
        except Exception:
            console.print(f"Invalid amount entered: '{amount_input}'. Please enter a numeric value.", style="bold red")
            sleep(2)
            return

        selected_account.deposit(amount)
        update_account_balance(selected_account.account_id, selected_account.get_balance())
        console.print(f"✅ Deposited {amount} into account {selected_account.account_id}. New balance: {selected_account.get_balance()}", style="bold green")
    else:
        console.print("😕 No accounts found!", style="bold red")
    
    sleep(1)

