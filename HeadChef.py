#Machelle Bakker - Python - 30/09/2019
from Manager import Manager
from Cook import Cook

class HeadChef(Manager, Cook):
    def __init(self, name):
        super().__init__(name)

    #A HeadChef needs the same functions as both the Manager and the Cook, hence the need for mulitple enheritance