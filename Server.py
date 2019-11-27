#Machelle Bakker - Python - 30/09/2019
#To start the entire program, first run this file (Server.py), then run Program.py
from socket import *
from time import ctime
from config import config

HOST = ""
PORT = config["PORT"]
BUFSIZE = config["BUFSIZE"]
ADOR = (HOST, PORT)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADOR)
tcpSerSocket.listen(8)

while True:
    print("Waiting for connection...")
    tcpCliSocket, addr = tcpSerSocket.accept()
    print("successful connection with address: ", addr)

    while True:
        data = tcpCliSocket.recv(BUFSIZE)
        if not data:
            break
        print("recieved the following feedback: ", data.decode())

        tcpCliSocket.send(bytes('[%s] %s' % (ctime(), data), "utf-8"))