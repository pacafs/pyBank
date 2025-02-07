def view_accounts_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("Your Accounts:")
    accounts = terminal_interface.current_user.get_accounts()
    if accounts:
        for acc in accounts:
            print(f"Account Type: {acc.__class__.__name__}, Balance: {acc.get_balance()}")
    else:
        print("No accounts found!")
    input("\nPress Enter to return to the menu.")
