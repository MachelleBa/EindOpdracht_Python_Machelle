#Machelle Bakker - Python - 30/09/2019
from Person import Person
from MenuCard import MenuCard


class Cook(Person):

    def __init__(self, name):
        super().__init__(name)

    def cook_item(self):
        self.display_menu_card()

        menu_card = MenuCard()

        valid_input = False
        while not valid_input:
            valid_input = True
            try:
                print("\nWhich menu item would you like to cook? Fill in its type and item number:\n")
                selected_item_type = input("Item type: ").lower()
                selected_item_nr = int(input("Item number: "))
                selected_item_amount = int(input("\nHow much portions of the item would you like to cook? "))

                #this turns selected item amount into a negative number, which will be used to substract from the current stock
                to_subtract_from_current_stock = selected_item_amount - 2 * selected_item_amount

                menu_card.update_item_stock(selected_item_type, selected_item_nr, to_subtract_from_current_stock)

            except Exception as error:
                print(f"Error: that is not a valid input: {error}")
                valid_input = False
