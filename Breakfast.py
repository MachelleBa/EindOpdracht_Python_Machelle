#Machelle Bakker - Python - 30/09/2019
from MenuItem import MenuItem


class Breakfast(MenuItem):

    availabilityTimeFrame = "until 11 AM"

    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)

