from db.database import Database
from bank import Bank
from interface.terminal_interface import TerminalInterface

def main():
    db = Database()
    bank = Bank(db)

    print("\n🏦 Welcome to the Banking Application!\n")


    db = Database()  # Use your PostgreSQL database here
    bank = Bank(db)
    terminal = TerminalInterface(bank)
    # Start the menu
    terminal.main_menu()  

    # # Creating two customers
    # customer1 = bank.create_customer("Alice", "alice@example.com", "password123")
    # customer2 = bank.create_customer("Bob", "bob@example.com", "securepass456")
    
    # print(f"✅ Created Customer: {customer1.name} (ID: {customer1.customer_id})")
    # print(f"✅ Created Customer: {customer2.name} (ID: {customer2.customer_id})\n")

    # # Creating checking accounts for both customers
    # account1 = bank.create_account(customer1.customer_id, "checking", 500)
    # account2 = bank.create_account(customer2.customer_id, "checking", 300)

    # print(f"💰 {customer1.name} opened a Checking Account with balance: ${account1.get_balance()}")
    # print(f"💰 {customer2.name} opened a Checking Account with balance: ${account2.get_balance()}\n")

    # # Performing deposits
    # print("📥 Deposits:")
    # account1.deposit(200)
    # print(f"➡ {customer1.name} deposited $200. New balance: ${account1.get_balance()}")

    # account2.deposit(150)
    # print(f"➡ {customer2.name} deposited $150. New balance: ${account2.get_balance()}\n")

    # # Performing withdrawals
    # print("📤 Withdrawals:")
    # account1.withdraw(100)
    # print(f"⬅ {customer1.name} withdrew $100. New balance: ${account1.get_balance()}")

    # account2.withdraw(50)
    # print(f"⬅ {customer2.name} withdrew $50. New balance: ${account2.get_balance()}\n")

    # # Processing a transfer from Alice to Bob
    # print("🔄 Transfer:")
    # bank.process_transaction(customer1.customer_id, customer2.customer_id, 200)
    # print(f"💸 {customer1.name} transferred $200 to {customer2.name}")

    # db.close()
    # print("\n✅ Transactions completed successfully!")

if __name__ == "__main__":
    main()


