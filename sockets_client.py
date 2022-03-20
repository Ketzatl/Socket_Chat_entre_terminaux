# -*-coding: utf8 -*-

import socket
import time
from pprint import pprint


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

print(f"\n \t {Colors.YELLOW}Connexion au Serveur{Colors.ENDC}{Colors.BLUE} {HOST_IP}{Colors.BLUE},"
      f"{Colors.YELLOW} Port {Colors.ENDC}: {HOST_PORT}....")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print(f"\n \t {Colors.RED}Erreur : Impossible de se connecter au Serveur....{Colors.ENDC}")
        print(f"\t {Colors.RED}Nouvelle tentative dans 4 secondes....{Colors.ENDC}\n")
        time.sleep(4)
    else:
        print(f"\n \t {Colors.YELLOW}Connecté au Serveur{Colors.ENDC}{Colors.BLUE} {HOST_IP}{Colors.BLUE},"
              f"{Colors.YELLOW} Port{Colors.ENDC} : {Colors.BLUE}{HOST_PORT}{Colors.ENDC}\n")
        break

while True:
    data_received = s.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print("Message : ", data_received.decode())
    text_message = input("Vous : ")
    s.sendall(text_message.encode())

s.close()
