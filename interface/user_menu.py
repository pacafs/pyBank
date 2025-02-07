from time import sleep
from .create_account import create_account_menu
from .view_accounts import view_accounts_menu
from .deposit import deposit_menu
from .withdraw import withdraw_menu
from .transfer import transfer_menu

def user_menu(bank, terminal_interface):
    while True:
        terminal_interface.clear_screen()
        print(f"👋 Welcome {terminal_interface.current_user.name}!")
        print("===================================")
        print("1. 🏦  Create an Account")
        print("2. 📄  View Your Accounts")
        print("3. 💵  Deposit Money")
        print("4. 💸  Withdraw Money")
        print("5. 🔀  Transfer Money")
        print("6. 🚪  Logout")
        choice = input("✨ Choose an option: ")
        if choice == '1':
            create_account_menu(bank, terminal_interface)
        elif choice == '2':
            view_accounts_menu(bank, terminal_interface)
        elif choice == '3':
            deposit_menu(bank, terminal_interface)
        elif choice == '4':
            withdraw_menu(bank, terminal_interface)
        elif choice == '5':
            transfer_menu(bank, terminal_interface)
        elif choice == '6':
            print("🚪 Logging out...")
            terminal_interface.current_user = None
            break
        else:
            print("❌ Invalid choice, please try again.")
            sleep(1)



