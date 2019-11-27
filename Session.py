#Machelle Bakker - Python - 30/09/2019
#To start the entire program, first run Server.py, then run Program.py
from Manager import Manager
from Cook import Cook
from HeadChef import HeadChef


class Session(object):
    def __init__(self):
        self.login = self.new_login()

    def logout(self):
        self.login = ["", ""]
        self.new_login()

    def new_login(self):
        login = ["", ""]
        NAME = 0
        ROLE = 1

        login_val = False
        while not login_val:

            login_val = True
            try:

                login[NAME] = input("What is your name?: ")
                login_type = input("""
As who would you like to login?
Options:
\"manager\" or \"m\"
\"cook\" or \"c\"
\"headchef\" or \"hc\"

 Your choice: """).lower()

                if login_type == "manager" or login_type == "m":
                    login[ROLE] = "Manager"
                elif login_type == "cook" or login_type == "c":
                    login[ROLE] = "Cook"
                elif login_type == "headchef" or login_type == "hc":
                    login[ROLE] = "HeadChef"
                else:
                    raise Exception("That role does not exist, please choose an existing role to login as.\n")

            except Exception as error:
                login_val = False
                print(f"\nError: {error}")

        self.login_specific_role(login)

        return login

    def login_specific_role(self, login):
        NAME = 0
        ROLE = 1

        if login[ROLE] == "Manager":
            self.managerOptionsMenu(login)
        elif login[ROLE] == "Cook":
            self.cookOptionsMenu(login)
        elif login[ROLE] == "HeadChef":
            self.headChefOptionsMenu(login)

    def headChefOptionsMenu(self, login):
        NAME = 0
        ROLE = 1

        LOG_OUT = 6

        menu_choice = 0
        headChef = HeadChef(login[NAME])

        while not menu_choice == LOG_OUT:

            try:

                menu_choice = int(input(f"""
Logged in as Head Chef
Welcome, {login[NAME]}. How can I help you today?
Options:
1 = Check menu card and stock
2 = Cook an item; subtract it from the stock
3 = Add a new item to the menu Card
4 = Update stock of item
5 = Give feedback about system
6 = Log out

Your choice: """))
                if menu_choice == 1:
                    headChef.display_menu_card()
                elif menu_choice == 2:
                    headChef.cook_item()
                elif menu_choice == 3:
                    headChef.add_item_to_menu()
                elif menu_choice == 4:
                    headChef.update_item_stock()
                elif menu_choice == 5:
                    headChef.server_send_feedback()
                elif menu_choice == LOG_OUT:
                    self.logout()
                else:
                    raise Exception("Please choose a valid item from the menu. Example: 1 ")

                back_to_menu = input("\n\nPress Enter to return to your menu of options")

            except Exception as error:
                print(f"\n\nError: {error}")

    def cookOptionsMenu(self, login):
        NAME = 0
        ROLE = 1

        LOG_OUT = 4

        menu_choice = 0
        cook = Cook(login[NAME])

        while not menu_choice == LOG_OUT:

            try:

                menu_choice = int(input(f"""
Logged in as Cook
Welcome, {login[NAME]}. How can I help you today?
Options:
1 = Check menu card and stock
2 = Cook an item; subtract it from the stock
3 = Give feedback about the system
4 = Log out

Your choice: """))
                if menu_choice == 1:
                    cook.display_menu_card()
                elif menu_choice == 2:
                    cook.cook_item()
                elif menu_choice == 3:
                    cook.server_send_feedback()
                elif menu_choice == LOG_OUT:
                    self.logout()
                else:
                    raise Exception("Please choose a valid item from the menu. Example: 1 ")

                back_to_menu = input("\n\nPress Enter to return to your menu of options")

            except Exception as error:
                print(f"Error: {error}")

    def managerOptionsMenu(self, login):
        NAME = 0
        ROLE = 1

        LOG_OUT = 5

        menu_choice = 0
        manager = Manager(login[NAME])

        while not menu_choice == LOG_OUT:

            try:

                menu_choice = int(input(f"""
Logged in as Manager
Welcome, {login[NAME]}. How can I help you today?
Options:
1 = Check menu card and stock
2 = Add a new menu item
3 = Update stock of item
4 = Give feedback about the system
5 = Log out

Your choice: """))
                if menu_choice == 1:
                    manager.display_menu_card()
                elif menu_choice == 2:
                    manager.add_item_to_menu()
                elif menu_choice == 3:
                    manager.update_item_stock()
                elif menu_choice == 4:
                    manager.server_send_feedback()
                elif menu_choice == LOG_OUT:
                    self.logout()
                else:
                    raise Exception("Please choose a valid item from the menu. Example: 1 ")

                back_to_menu = input("\n\nPress Enter to return to your menu of options")

            except Exception as error:
                print(f"Error: {error}")

