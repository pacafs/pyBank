import sys
from time import sleep
from getpass import getpass
from models.customer import Customer
from decimal import Decimal  # Import Decimal to convert input strings to Decimal objects
from .main_menu import main_menu

class TerminalInterface:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def clear_screen(self):
        print("\033c", end="")

    def show_welcome_message(self):
        self.clear_screen()
        print("Welcome to the Banking Application!")
        sleep(1)

    def main_menu(self):
        main_menu(self.bank, self)
        

