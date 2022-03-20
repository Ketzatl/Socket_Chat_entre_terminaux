# -*-coding: utf8 -*-

import socket


# Permet de colorer le texte affiché dans la console
class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"\n \t {Colors.YELLOW}Attente de connexion sur{Colors.ENDC} {Colors.BLUE}{HOST_IP}{Colors.BLUE},"
      f"{Colors.YELLOW} Port {Colors.ENDC}: {HOST_PORT}....")

connection_socket, client_adress = s.accept()
print(f" \n \t {Colors.GREEN}Connexion établie avec {Colors.ENDC} {client_adress}\n")

while True:
    text_message = input("Vous : ")
    connection_socket.sendall(text_message.encode())
    data_received = connection_socket.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print(f"Message : ", data_received.decode())

s.close()
connection_socket.close()
