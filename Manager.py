#Machelle Bakker - Python - 30/09/2019
from Person import Person
from MenuCard import MenuCard


class Manager(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_item_to_menu(self):
        card = MenuCard()
        card.add_menu_item()

    def update_item_stock(self):
        self.display_menu_card()

        menu_card = MenuCard()

        valid_input = False
        while not valid_input:
            valid_input = True
            try:
                print("\nWhich menu item would you like to update the stock of? Fill in its type and item number:\n")
                selected_item_type = input("Item type: ").lower()
                selected_item_nr = int(input("Item number: "))
                selected_item_amount = int(input("\nwith what number would you like to increase or decrease the current stock of the item? Example: 5 or -5"))

            except Exception as error:
                print(f"Error: that is not a valid input: {error}")
                valid_input = False

        menu_card.update_item_stock(selected_item_type, selected_item_nr, selected_item_amount)
