def create_account_menu(bank, terminal_interface):
    terminal_interface.clear_screen()
    print("Create Account:")
    acc_type = input("Enter account type (checking/savings): ").lower()
    if acc_type in ["checking", "savings"]:
        initial_balance = float(input("Enter initial balance: "))
        account = bank.create_account(terminal_interface.current_user.customer_id, acc_type, initial_balance)
        print(f"{acc_type.capitalize()} account created with balance: {account.get_balance()}")
    else:
        print("Invalid account type!")
