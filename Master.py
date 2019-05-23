import socket
import threading

# Thread permettant de recevoir un client.
def thread_recevoir_client(client_socket):
        while True:
                request = client_socket.recv(1024)
                print("[*] Received: %s" %request)

# Thread permettant à plusieurs clients de se connecter.
def thread_connexion():
        while True:
                client,addr = server.accept()
                list_of_clients.append(client)
                print("[*] Accepted connection from: %s:%d" %(addr[0], addr[1]))
                thread_recevoir = threading.Thread(target=thread_recevoir_client,args={client,})
                thread_recevoir.start()

# Fonction permettant d'envoyer du texte au client. 
def envoyer(texte):
        if "mail" in texte:
                for client in list_of_clients:
                        for spamRec in list_of_spam:
                                nouTexte = texte + " " + spamRec
                                client.send(str.encode(nouTexte))
        else:
                for client in list_of_clients:
                        client.send(str.encode(texte))

# Début du main
bind_ip = "192.168.60.13"
bind_port = 9999
list_of_clients = []
fichier = open("contact.txt", "r")
list_of_spam = []

for ligne in fichier:
        list_of_spam.append(ligne)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(100)

print("Le serveur attend une connexion")

thread_connexion = threading.Thread(target=thread_connexion)
thread_connexion.start()

while True:
	texte = input()
	envoyer(texte)

