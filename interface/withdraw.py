from decimal import Decimal
from time import sleep
from rich.console import Console
from rich.table import Table
from db.queries import update_account_balance  # if needed

def withdraw_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    console = Console()
    console.print("💸 Withdraw Money:\n", style="bold cyan")

    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        table = Table(title="Select an Account to Withdraw From", header_style="bold magenta")
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
                selection = int(input("Select the account number to withdraw from: "))
                if 1 <= selection <= len(accounts):
                    break
                else:
                    console.print("Invalid selection, please choose a valid number from the list.", style="bold red")
            except ValueError:
                console.print("Please enter a valid number.", style="bold red")

        selected_account = accounts[selection - 1]

        try:
            amount_input = input("Enter the amount to withdraw: ")
            amount = Decimal(amount_input)
        except Exception:
            console.print(f"Invalid amount entered: '{amount_input}'. Please enter a numeric value.", style="bold red")
            sleep(2)
            return

        selected_account.withdraw(amount)
        # Optionally update the database with the new balance.
        # update_account_balance(selected_account.account_id, selected_account.get_balance())

        console.print(f"✅ Withdrew {amount} from account {selected_account.account_id}. "
                      f"New balance: {selected_account.get_balance()}", style="bold green")
    else:
        console.print("😕 No accounts found!", style="bold red")
    
    sleep(1)

# from decimal import Decimal
# from time import sleep
# from db.queries import update_account_balance

# def withdraw_menu(bank, terminal_interface):
#     terminal_interface.clear_screen()
#     print("Withdraw Money:")
#     accounts = terminal_interface.current_user.get_accounts()
#     if accounts:
#         # Display a selection menu for accounts
#         for index, acc in enumerate(accounts, start=1):
#             print(f"{index}. Account ID: {acc.account_id}, Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
#         while True:
#             try:
#                 selection = int(input("Select the account number to withdraw from: "))
#                 if 1 <= selection <= len(accounts):
#                     break
#                 else:
#                     print("Invalid selection, please choose a valid number from the list.")
#             except ValueError:
#                 print("Please enter a valid number.")
#         selected_account = accounts[selection - 1]
#         amount = Decimal(input("Enter the amount to withdraw: "))
#         selected_account.withdraw(amount)
#         print(f"Withdrew {amount} from account {selected_account.account_id}. New balance: {selected_account.get_balance()}")
#     else:
#         print("No accounts found!")
#     sleep(1)

    
    