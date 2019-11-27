#Machelle Bakker - Python - 30/09/2019
from MenuCard import MenuCard
from socket import *
from config import config

class Person(object):

    static_personal_number = 1

    def __init__(self, name):
        self.__name = name
        self.__personal_number = self.generate_personal_number()

    def generate_personal_number(self):

        personal_number = self.static_personal_number
        self.static_personal_number = personal_number + 1
        return personal_number

    def get_name(self):
        return self.__name

    def get_personal_number(self):
        return self.__personal_number

    def display_menu_card(self):
        card = MenuCard()
        card.print_menu()

    def server_send_feedback(self):

        HOST = 'localhost'
        PORT = config["PORT"]
        BUFSIZE = config["BUFSIZE"]
        ADOR = (HOST, PORT)

        tcpCliSocket = socket(AF_INET, SOCK_STREAM)
        tcpCliSocket.connect(ADOR)

        while True:
            try:
                data = input('Your feedback: \n')
                tcpCliSocket.send(str.encode(data))
                if not data:
                    break
                tcpCliSocket.recv(BUFSIZE)
                if not data:
                    break
                print('The server has recieved your feedback, thank you!')
                break
            except Exception as error:
                print(f"Please fill in a valid input. Error: {error}")
