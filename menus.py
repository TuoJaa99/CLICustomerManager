import sqlite3
import dbconn
import os
import sys
import keyboard
from time import sleep

def clear():
    os.system('clear')

#main menu
def main_menu():
    print("--CLI Customer Manager--")
    print("1. Add a new customer")
    print("2. Add to an existing customer")
    print("3. Clear customer data")
    print("4. Customer list")
    print("5. Exit")

    menu_nav = input(": ").strip()
    while True:
        if menu_nav == "1":
            clear()
            dbconn.add_customer()
            sleep(3)
            clear()
            main_menu()
        
        elif menu_nav == "2":
            clear()
            dbconn.add_to_existing()
            sleep(3)
            clear()
            main_menu()

        elif menu_nav == "3":
            clear()
            dbconn.delete_customer()
            sleep(3)
            clear()
            main_menu()
        elif menu_nav == "4":
            clear()
            dbconn.print_table()
            print("")
            print("")
            print("1. Back to main menu")
            print_nav = input(": ")
            if print_nav == "1":
                clear()
                main_menu()

        elif menu_nav == "5":
            print("Bye Bye ヾ(＾∇＾)")
            sleep(3)
            clear()
            sys.exit(0)
        else:
            clear()
            main_menu()
