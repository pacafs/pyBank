from time import sleep

def main_menu(bank, terminal_interface):
    while True:
        terminal_interface.clear_screen()
        print("Main Menu:")
        print("1. Create a New User")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            from .create_user import create_user_menu
            create_user_menu(bank, terminal_interface)
        elif choice == '2':
            from .login import login_menu
            login_menu(bank, terminal_interface)
        elif choice == '3':
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice, please try again.")
