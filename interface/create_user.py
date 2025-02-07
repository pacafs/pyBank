from time import sleep
from getpass import getpass

def create_user_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("👤 Create a New User:")
    name = input("📝 Enter your name: ")
    email = input("📧 Enter your email: ")
    password = getpass("🔒 Enter your password: ")
    user = bank.create_customer(name, email, password)
    print(f"✅ User {user.name} created successfully!")
    sleep(2)
    terminal_interface.main_menu()
