from time import sleep
from .create_user import create_user_menu
from .login import login_menu

def main_menu(bank, terminal_interface):
    while True:
        terminal_interface.clear_screen()
        print("🌟 Welcome to the Banking App! 🌟")
        print("===================================")
        print("1. 👤  Create a New User")
        print("2. 🔑  Login")
        print("3. 🚪  Exit")
        choice = input("✨ Choose an option: ")
        if choice == '1':
            create_user_menu(bank, terminal_interface)
        elif choice == '2':
            login_menu(bank, terminal_interface)
        elif choice == '3':
            print("🚪 Exiting... Goodbye!")
            sleep(1)
            exit(0)
        else:
            print("❌ Invalid choice, please try again.")
            sleep(1)
