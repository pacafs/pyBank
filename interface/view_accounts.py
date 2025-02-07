from rich.console import Console
from rich.table import Table

def view_accounts_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    console = Console()

    accounts = terminal_interface.current_user.get_accounts()

    if accounts:
        table = Table(title="Your Accounts 😊")

        table.add_column("🏦 Account Type", justify="left", style="cyan", no_wrap=True)
        table.add_column("💰 Balance", justify="right", style="green")

        for acc in accounts:
            table.add_row(acc.__class__.__name__, str(acc.get_balance()))
        
        console.print(table)
    else:
        console.print("😕 No accounts found!", style="bold red")

    input("\nPress Enter to return to the menu.")

# def view_accounts_menu(bank, terminal_interface):
#     terminal_interface.clear_screen()
#     print("Your Accounts:")
#     accounts = terminal_interface.current_user.get_accounts()
#     if accounts:
#         for acc in accounts:
#             print(f"Account Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
#     else:
#         print("No accounts found!")
#     input("\nPress Enter to return to the menu.")
