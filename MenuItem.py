#Machelle Bakker - Python - 30/09/2019

class MenuItem(object):
    def __init__(self, item_name, item_price, item_amount_in_stock):
        self.__name = item_name
        self.__price = item_price
        self.__amount_in_stock = item_amount_in_stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_amount_in_stock(self):
        return self.__amount_in_stock

    def update_amount_in_stock(self, new_amount):
        self.__amount_in_stock = self.__amount_in_stock + new_amount



