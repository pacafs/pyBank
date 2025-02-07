# main.py
from bank import Bank
from db.database import Database

def main():
    db = Database()
    bank = Bank(db)
    
    # Sample flow
    print("Welcome to the Banking Application!")
    customer = bank.create_customer("John Doe", "john@example.com", "securepassword123")
    print(f"Customer {customer.name} created.")
    
    acc = bank.create_account(customer.customer_id, "checking", 500)
    print(f"Account created with balance: {acc.get_balance()}")

    acc.deposit(100)
    print(f"Balance after deposit: {acc.get_balance()}")

    acc.withdraw(50)
    print(f"Balance after withdrawal: {acc.get_balance()}")

    db.close()

if __name__ == "__main__":
    main()
