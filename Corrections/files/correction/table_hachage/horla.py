# -*- coding: utf-8 -*-
import json
import hachage
from time import time

f = open("../data/le_horla.json")
str = f.read()
f.close()

mots = json.loads(str)

#Vérification
s = ""
i = 0
while i < 32:
    s += mots[i] + " "
    i += 1
print(s)

# Nombre de mots différents
table = hachage.initialiser_table(1000)

i = 0
while i < len(mots):
    hachage.ajouter(table,mots[i])
    i += 1

print("Le livre le Horla contient", len(mots), "mais seulement", hachage.nb_valeurs(table), "sont différents.")

# Etudes de performances
tic = time()       # top départ
table1 = hachage.initialiser_table(1000)
i = 0
while i < len(mots):
    hachage.ajouter(table1,mots[i])
    i += 1
tac = time()           # arrêt du chronomètre
#print(tac-tic)                    # en secondes
print(round(1000*(tac-tic),2)," ms pour un table de 1000 cases") # convertit en ms et on arrondit au centième

tic = time()       # top départ
table2 = hachage.initialiser_table(100)
i = 0
while i < len(mots):
    hachage.ajouter(table2,mots[i])
    i += 1
tac = time()           # arrêt du chronomètre
#print(tac-tic)                    # en secondes
print(round(1000*(tac-tic),2)," ms pour un table de 100 cases") # convertit en ms et on arrondit au centième

tic = time()       # top départ
table3 = hachage.initialiser_table(10)
i = 0
while i < len(mots):
    hachage.ajouter(table3,mots[i])
    i += 1
tac = time()           # arrêt du chronomètre
#print(tac-tic)                    # en secondes
print(round(1000*(tac-tic),2)," ms pour un table de 10 cases") # convertit en ms et on arrondit au centième

tailles = [10, 100, 1000, 10000]
t = 0
while t < len(tailles):
    table = hachage.initialiser_table(tailles[t])

    i = 0
    while i < len(mots):
        hachage.ajouter(table,mots[i])
        i += 1
    print("c = ", hachage.c(table), "idéalement =", hachage.ideale(table))
    t += 1
