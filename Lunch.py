#Machelle Bakker - Python - 30/09/2019
from MenuItem import MenuItem


class Lunch(MenuItem):

    availabilityTimeFrame = "from 11 AM to 2 PM"

    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
