from time import sleep

def user_menu(bank, terminal_interface):
    while True:
        terminal_interface.clear_screen()
        print(f"Welcome {terminal_interface.current_user.name}!")
        print("1. Create an Account")
        print("2. View Your Accounts")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            from .create_account import create_account_menu
            create_account_menu(bank, terminal_interface)
        elif choice == '2':
            from .view_accounts import view_accounts_menu
            view_accounts_menu(bank, terminal_interface)
        elif choice == '3':
            from .deposit import deposit_menu
            deposit_menu(bank, terminal_interface)
        elif choice == '4':
            from .withdraw import withdraw_menu
            withdraw_menu(bank, terminal_interface)
        elif choice == '5':
            from .transfer import transfer_menu
            transfer_menu(bank, terminal_interface)
        elif choice == '6':
            print("Logging out...")
            terminal_interface.current_user = None
            break
        else:
            print("Invalid choice, please try again.")
