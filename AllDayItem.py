#Machelle Bakker - Python - 30/09/2019
from MenuItem import MenuItem


class AllDayItem(MenuItem):

    availabilityTimeFrame = "All day long"

    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
