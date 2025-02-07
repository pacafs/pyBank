from db.database import Database
import db.queries as queries
from bank import Bank
from interface.terminal_interface import TerminalInterface

def main():
    # Instantiate your Database connection.
    db_conn = Database()
    # Initialize the global DB connection in queries module.
    queries.set_db(db_conn)

    bank = Bank()
    terminal = TerminalInterface(bank)
    
    # Start the menu
    terminal.main_menu()  

    # Close the database connection when finished.
    db_conn.close()

if __name__ == "__main__":
    main()


