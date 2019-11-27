#Machelle Bakker - Python - 30/09/2019
from MenuItem import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, stock, type_of_drink):
        super().__init__(name, price, stock)
        self.__type_of_drink = type_of_drink

    def get_type_of_drink(self):
        return self.__type_of_drink
