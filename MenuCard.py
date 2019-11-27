import pickle
from Breakfast import Breakfast
from Lunch import Lunch
from Dinner import Dinner
from Drinks import Drink
from AllDayItem import AllDayItem


class MenuCard(object):

    item_number = 1
    pickle_file = "menuCardList.pickle"

    def __init__(self):
        self._item_list = self.__set_list() # = list of MenuItems
        self._drink_dict = self.__set_drinks_dict()
        self._breakfast_dict = self.__set_breakfast_dict()
        self._lunch_dict = self.__set_lunch_dict()
        self._dinner_dict = self.__set_dinner_dict()
        self._alldayitem_dict = self.__set_alldayitem_dict()

    def get_menu_item_list(self):
        return self._item_list

    def get_drink_dict(self):
        return self._drink_dict

    def get_breakfast_dict(self):
        return self._breakfast_dict

    def get_lunch_dict(self):
        return self._lunch_dict

    def get_dinner_dict(self):
        return self._dinner_dict

    def get_alldayitem_dict(self):
        return self._alldayitem_dict

    def __set_list(self):
        try:
            pickle_in = open(self.pickle_file, "rb")
            retrieved_list = pickle.load(pickle_in)
        except FileNotFoundError as FNFerror:
            print("Cant find the pickle file. Please make sure the file exist and is present in the right folder")

        return retrieved_list

    def __set_drinks_dict(self):
        drinks_dict = {}
        menu_list = self.get_menu_item_list()

        for item in range(len(menu_list)):
            # Add Drinks to drink_dict
            if type(menu_list[item]) is Drink:
                drinks_dict.update({self.item_number: [self.item_number, menu_list[item].get_name(), menu_list[item].get_price(), menu_list[item].get_amount_in_stock()]})
                self.item_number = self.item_number + 1

        return drinks_dict

    def __set_breakfast_dict(self):
        breakfast_dict = {}
        menu_list = self.get_menu_item_list()

        for item in range(len(menu_list)):
            # Add Breakfast items to breakfast_dict
            if type(menu_list[item]) is Breakfast:
                breakfast_dict.update({self.item_number: [self.item_number, menu_list[item].get_name(), menu_list[item].get_price(), menu_list[item].get_amount_in_stock()]})
                self.item_number = self.item_number + 1

        return breakfast_dict

    def __set_lunch_dict(self):
        lunch_dict = {}
        menu_list = self.get_menu_item_list()

        for item in range(len(menu_list)):
            # Add Lunch items to lunch_dict
            if type(menu_list[item]) is Lunch:
                lunch_dict.update({self.item_number: [self.item_number, menu_list[item].get_name(), menu_list[item].get_price(), menu_list[item].get_amount_in_stock()]})
                self.item_number = self.item_number + 1

        return lunch_dict

    def __set_dinner_dict(self):

        dinner_dict = {}
        menu_list = self.get_menu_item_list()

        for item in range(len(menu_list)):
            # Add Lunch items to lunch_dict
            if type(menu_list[item]) is Dinner:
                dinner_dict.update({self.item_number: [self.item_number, menu_list[item].get_name(), menu_list[item].get_price(), menu_list[item].get_amount_in_stock()]})
                self.item_number = self.item_number + 1

        return dinner_dict

    def __set_alldayitem_dict(self):

        alldayitem_dict = {}
        menu_list = self.get_menu_item_list()

        for item in range(len(menu_list)):
            # Add All day items to alldayitem_dict
            if type(menu_list[item]) is AllDayItem:
                alldayitem_dict.update({self.item_number: [self.item_number, menu_list[item].get_name(), menu_list[item].get_price(), menu_list[item].get_amount_in_stock()]})
                self.item_number = self.item_number + 1

        return alldayitem_dict


#----------------------------------------------------------------Displaying the menu, formatted------------------------------------------------------------------------------

    def print_menu(self):
        drinks_dict = self.get_drink_dict()
        breakfast_dict = self.get_breakfast_dict()
        lunch_dict = self.get_lunch_dict()
        dinner_dict = self.get_dinner_dict()
        alldayitem_dict = self.get_alldayitem_dict()

        print("\nMENU CARD")
        print(f"\n\nDrinks\n")

        # There is no key named 0 in the dict, so we need to use item_nr = 1 to start printing with the key named 1, then move from there
        item_nr = 1

        for item in range(len(drinks_dict)):
            print(f"{drinks_dict[item_nr][0]}.\t{drinks_dict[item_nr][1]}\tprice: €{drinks_dict[item_nr][2]} \tstock: {drinks_dict[item_nr][3]}")
            item_nr = item_nr + 1

        print(f"\n\nBreakfast\nAvailability: {Breakfast.availabilityTimeFrame}\n")
        for item in range(len(breakfast_dict)):
            print(f"{breakfast_dict[item_nr][0]}.\t{breakfast_dict[item_nr][1]}\tprice: €{breakfast_dict[item_nr][2]} \tstock: {breakfast_dict[item_nr][3]}")
            item_nr = item_nr + 1

        print(f"\n\nLunch\nAvailability: {Lunch.availabilityTimeFrame}\n")
        for item in range(len(lunch_dict)):
            print(f"{lunch_dict[item_nr][0]}.\t{lunch_dict[item_nr][1]}\tprice: €{lunch_dict[item_nr][2]} \tstock: {lunch_dict[item_nr][3]}")
            item_nr = item_nr + 1

        print(f"\n\nDinner\nAvailability: {Dinner.availabilityTimeFrame}\n")
        for item in range(len(dinner_dict)):
            print(f"{dinner_dict[item_nr][0]}.\t{dinner_dict[item_nr][1]}\tprice: €{dinner_dict[item_nr][2]} \tstock: {dinner_dict[item_nr][3]}")
            item_nr = item_nr + 1

        print(f"\n\nAll Day Items\nAvailability: {AllDayItem.availabilityTimeFrame}\n")
        for item in range(len(alldayitem_dict)):
            print(f"{alldayitem_dict[item_nr][0]}.\t{alldayitem_dict[item_nr][1]}\tprice: €{alldayitem_dict[item_nr][2]} \tstock: {alldayitem_dict[item_nr][3]}")
            item_nr = item_nr + 1


#----------------------------------------------------------------Updating Items of the MenuCard-------------------------------------------------------------------

    def update_item_stock(self, selected_item_type, selected_item_nr, selected_item_amount):

        NUMBER = 0
        NAME = 1

        menu_card = MenuCard()
        menu_list = menu_card.get_menu_item_list()

        valid_beverage_type = False
        while not valid_beverage_type:
            try:
                valid_beverage_type = True
                if selected_item_type == "dinner" or selected_item_type == "di":
                    dinner_dict = menu_card.get_dinner_dict()
                    dinner = dinner_dict[selected_item_nr]

                    print(f"Selected dinner: \tnumber:{dinner[NUMBER]} \tname: {dinner[NAME]}")

                    for item in range(len(menu_list)):
                        if menu_list[item].get_name() == dinner[NAME]:
                            menu_list[item].update_amount_in_stock(selected_item_amount)

                            pickle_out = open(self.pickle_file, "wb")
                            pickle.dump(menu_list, pickle_out)
                            pickle_out.close()

                            print(f"\nSuccesfully updated amount in stock. new stock for item {menu_list[item].get_name()} is {menu_list[item].get_amount_in_stock()}")

                elif selected_item_type == "breakfast" or selected_item_type == "br":
                    breakfast_dict = menu_card.get_breakfast_dict()
                    breakfast = breakfast_dict[selected_item_nr]

                    print(f"Selected breakfast: \tnumber:{breakfast[NUMBER]} \tname: {breakfast[NAME]}")

                    for item in range(len(menu_list)):
                        if menu_list[item].get_name() == breakfast[NAME]:
                            #print(f"Found item in menu list: name: {menu_list[item].get_name()}")
                            menu_list[item].update_amount_in_stock(selected_item_amount)
                            print(f"\nSuccesfully updated amount in stock. New stock for item {menu_list[item].get_name()} is {menu_list[item].get_amount_in_stock()}")

                            pickle_out = open(self.pickle_file, "wb")
                            pickle.dump(menu_list, pickle_out)
                            pickle_out.close()

                elif selected_item_type == "lunch" or selected_item_type == "lu":
                    lunch_dict = menu_card.get_lunch_dict()
                    lunch = lunch_dict[selected_item_nr]

                    print(f"Selected lunch: \tnumber:{lunch[NUMBER]} \tname: {lunch[NAME]}")

                    for item in range(len(menu_list)):
                        if menu_list[item].get_name() == lunch[NAME]:
                            #print(f"Found item in menu list: name: {menu_list[item].get_name()}")
                            menu_list[item].update_amount_in_stock(selected_item_amount)
                            print(f"\nSuccesfully updated amount in stock. New stock for item {menu_list[item].get_name()} is {menu_list[item].get_amount_in_stock()}")

                            pickle_out = open(self.pickle_file, "wb")
                            pickle.dump(menu_list, pickle_out)
                            pickle_out.close()

                elif selected_item_type == "alldayitem" or selected_item_type == "ad" or selected_item_type == "all day item" or selected_item_type == "allday":
                    alldayitem_dict = menu_card.get_alldayitem_dict()
                    alldayitem = alldayitem_dict[selected_item_nr]

                    print(f"Selected all day item: \tnumber:{alldayitem[NUMBER]} \tname: {alldayitem[NAME]}")

                    for item in range(len(menu_list)):
                        if menu_list[item].get_name() == alldayitem[NAME]:
                            #print(f"Found item in menu list: name: {menu_list[item].get_name()}")
                            menu_list[item].update_amount_in_stock(selected_item_amount)
                            print(f"\nSuccesfully updated amount in stock. new stock for item {menu_list[item].get_name()} is {menu_list[item].get_amount_in_stock()}")

                            pickle_out = open(self.pickle_file, "wb")
                            pickle.dump(menu_list, pickle_out)
                            pickle_out.close()

                elif selected_item_type == "drink" or selected_item_type == "dr":
                    drink_dict = menu_card.get_drink_dict()
                    drink = drink_dict[selected_item_nr]

                    print(f"Selected breakfast: \tnumber:{drink[NUMBER]} \tname: {drink[NAME]}")

                    for item in range(len(menu_list)):
                        if menu_list[item].get_name() == drink[NAME]:
                            #print(f"Found item in menu list: name: {menu_list[item].get_name()}")
                            menu_list[item].update_amount_in_stock(selected_item_amount)
                            print(f"\nSuccesfully updated amount in stock. New stock for item {menu_list[item].get_name()} is {menu_list[item].get_amount_in_stock()}")

                            pickle_out = open(self.pickle_file, "wb")
                            pickle.dump(menu_list, pickle_out)
                            pickle_out.close()

                else:
                    raise Exception("that is not a valid beverage/item type. Please try again\n")
            except Exception as error:
                print(f"Error: {error}")
                valid_beverage_type = False


#--------------------------------------------Adding new items to the menuList-----------------------------------------------

    def add_menu_item(self):

        try:
            pickle_in = open(self.pickle_file, "rb")
            retrieved_list = pickle.load(pickle_in)

            valid_input = False
            while not valid_input:
                try:
                    valid_input = True

                    #the beneath input text had to be put like this for formatting issues in the console... I dont think its ok either
                    type_of_beverage = input("""
What type of beverage would you like to add?
Pick from the following options:

\"drink\" or \"dr\"
\"breakfast\" or \"br\"
\"lunch\" or \"lu\"
\"dinner\" or \"di\"
\"alldayitem\" or \"ad\"

your choice: """)
                    lowercase_type = type_of_beverage.lower()

                    if lowercase_type == "lunch" or lowercase_type == "lu":
                        user_input_dict = self.read_new_item_info(lowercase_type)
                        retrieved_list.append(Lunch(user_input_dict["name"], user_input_dict["price"], user_input_dict["stock"]))
                        print("\nlunch item added succesfully!")

                    elif lowercase_type == "breakfast" or lowercase_type == "br" :
                        user_input_dict = self.read_new_item_info(lowercase_type)
                        retrieved_list.append(Breakfast(user_input_dict["name"], user_input_dict["price"], user_input_dict["stock"]))
                        print("\nbreakfast item added succesfully!")

                    elif lowercase_type == "dinner" or lowercase_type == "di":
                        user_input_dict = self.read_new_item_info(lowercase_type)
                        retrieved_list.append(Dinner(user_input_dict["name"], user_input_dict["price"], user_input_dict["stock"]))
                        print("\ndinner item added succesfully!")

                    elif lowercase_type == "drink" or lowercase_type == "dr":
                        user_input_dict = self.read_new_item_info(lowercase_type)
                        type_of_drink = self.read_new_drink_type()
                        retrieved_list.append(Drink(user_input_dict["name"], user_input_dict["price"], user_input_dict["stock"], type_of_drink))
                        print("\ndrink added succesfully!")

                    elif lowercase_type == "alldayitem" or lowercase_type == "adi" or lowercase_type == "all day item" or lowercase_type == "allday":
                        user_input_dict = self.read_new_item_info(lowercase_type)
                        retrieved_list.append(AllDayItem(user_input_dict["name"], user_input_dict["price"], user_input_dict["stock"]))
                        print("\nAll Day item added succesfully!")

                    else:
                        raise Exception("That beverage type does not exist.\n")
                except Exception as error:
                    print("\nError: Please enter a valid input: ", str(error))
                    valid_input = False
            #end of while loop

            pickle_out = open(self.pickle_file, "wb")
            pickle.dump(retrieved_list, pickle_out)
            pickle_out.close()
        except FileNotFoundError as FNFerror:
            print(f"Could not find the file to read. Please check if the file exist and is located in the right folder."
                  f" Error: {FNFerror}")

    def read_new_item_info(self, type_of_beverage):

        valid_user_input = False
        #if the user input is wrong, this boolean will be set to false. The user can then try again due to the while loop
        while not valid_user_input:
            try:

                name = str(input(f"Name of new {type_of_beverage}: "))
                price = float(input(f"Price of new {type_of_beverage}: "))
                stock = int(input(f"Current stock of new {type_of_beverage}: "))
                valid_user_input = True
            except Exception as error:
                print("""\n
Please enter a valid input. examples:
name: Beer
price: 3.50
stock: 130\n""")
                valid_user_input = False

        return {"name": name, "price": price, "stock" : stock}

    def read_new_drink_type(self):

        validated_type_of_drink = ""
        while validated_type_of_drink == "":
            try:
                type_of_drink = input("""
Type of drink, choose from:
 \"alcoholic\" or \"a\" 
 \"non-alcoholic\" or \"na\"

 your choice: """).lower()

                if type_of_drink == "alcoholic" or type_of_drink == "non-alcoholic" or type_of_drink == "na" or type_of_drink == "a" or type_of_drink == "non alcoholic":
                    validated_type_of_drink = type_of_drink
                else:
                    raise Exception("Please enter a valid drink type.")
            except Exception as exception:
                print("Error: ", str(exception))

        return validated_type_of_drink
