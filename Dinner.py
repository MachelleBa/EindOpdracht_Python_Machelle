#Machelle Bakker - Python - 30/09/2019
from MenuItem import MenuItem

class Dinner(MenuItem):

    availabilityTimeFrame = "from 4 to 8.30 PM"

    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
