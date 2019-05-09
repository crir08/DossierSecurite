#2019-04-17
#Créé par Nathan Lessard et Christophe Roux

import sys
import time

alphabet = 'abcdefghijklmnopkrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = sys.argv[2]
debut = time.time()


# Force brute faible qui teste toutes les possibilités de a à z.
def BruteForceFaible():
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for i in range(0, 26):
        for j in range(0,26):
            for k in range(0,26):
                for l in range(0,26):
                    for m in range(0,26):
                        resultat = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[l] + alphabet[m]
                        if resultat == password:
                            print("Mot de passe " + resultat + " décrypté en : ")
                            return
    print("Échec du programme...")

# Force brute moyen qui teste toutes les possibilités de a à Z.
def BruteForceMoyen():
    debut = time.time()
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for i in range(0, 52):
        for j in range(0, 52):
            for k in range(0, 52):
                for l in range(0, 52):
                    for m in range(0, 52):
                        resultat = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[l] + alphabet[m]
                        if resultat == password:
                            print("Mot de passe " + resultat + " décrypté en : ")
                            return
    print("Échec du programme...")

# Force brute fort qui teste toutes les possibilités de a à 9.
def BruteForceFort():
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for i in range(0, 62):
        for j in range(0, 62):
            for k in range(0, 62):
                for l in range(0, 62):
                    for m in range(0, 62):
                        resultat = alphabet[i] + alphabet[j] + alphabet[k] + alphabet[l] + alphabet[m]
                        if resultat == password:
                            print("Mot de passe " + resultat + " décrypté en : ")
                            return
    print("Échec du programme...")

if sys.argv[1] == "faible":
    BruteForceFaible()
if sys.argv[1] == "moyen":
    BruteForceMoyen()
if sys.argv[1] == "fort":
    BruteForceFort()

fin = time.time()
duree = (fin - debut)
print(str(duree) + " secondes")
