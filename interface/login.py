from time import sleep
from getpass import getpass
from models.customer import Customer
from db.queries import fetchall
from .user_menu import user_menu

def login_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("🔑 Login:")
    email = input("📧 Enter your email: ")
    password = getpass("🔒 Enter your password: ")
    users = fetchall("SELECT * FROM customers WHERE email=%s", (email,))
    if users:
        user_data = users[0]
        customer_id, name, email, stored_password = user_data
        if password == stored_password:
            terminal_interface.current_user = Customer(customer_id, name, email, password)
            print(f"✅ Welcome back, {terminal_interface.current_user.name}!")
            sleep(1)
            user_menu(bank, terminal_interface)
        else:
            print("❌ Incorrect password!")
    else:
        print("❌ User not found!")
    sleep(2)
    terminal_interface.main_menu()
