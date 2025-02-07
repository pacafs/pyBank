from rich.console import Console
from rich.table import Table
from db.queries import get_transactions_by_customer

def view_transactions_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    console = Console()
    console.print("📜 Transaction History:\n", style="bold cyan")
    
    transactions = get_transactions_by_customer(terminal_interface.current_user.customer_id)
    
    if transactions:
        table = Table(title="Transaction History", header_style="bold magenta")
        table.add_column("ID", style="yellow")
        table.add_column("Type", style="cyan")
        table.add_column("Other Party", style="white")
        table.add_column("Amount", style="green", justify="right")
        table.add_column("Timestamp", style="magenta")
        
        for tx in transactions:
            transaction_id, sender_id, receiver_id, amount, timestamp = tx
            if sender_id == terminal_interface.current_user.customer_id:
                type = "Sent"
                other_party = str(receiver_id)
            else:
                type = "Received"
                other_party = str(sender_id)
            table.add_row(str(transaction_id), type, other_party, str(amount), str(timestamp))
        console.print(table)
    else:
        console.print("😕 No transactions found!", style="bold red")
    
    input("\nPress Enter to return to the menu.") 