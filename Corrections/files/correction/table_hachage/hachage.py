# -*- coding: utf-8 -*-
def hachage(str):
    nombre =  0
    i = 0
    while i < len(str):
        nombre += ord(str[i])
        i += 1
    return nombre

def rechercher(table,valeur):
    indice = hachage(valeur)%len(table)
    j = 0
    while j < len(table[indice]):
        if table[indice][j] == valeur:
            return True
        j += 1
    return False

def ajouter(table,valeur):
    if not rechercher(table,valeur):
        indice = hachage(valeur)%len(table)
        table[indice].append(valeur)

def supprimer(table,valeur):
    if rechercher(table,valeur):
        indice = hachage(valeur)%len(table)
        # On cherche la position de l'entier dans table[indice]
        j = 0 
        while j < len(table[indice]) and table[indice][j] != valeur:
            j+= 1
        #On met le dernier élément de table[indice] à la place de entier
        table[indice][j] = table[indice][len(table[indice])-1] 
        table[indice].pop() # On supprime le dernier élément de table[indice]

def initialiser_table(n):
    table = []
    i = 0
    while i < n:
        table.append([])
        i += 1
    return table

def nb_valeurs(table):
    nb = 0
    i = 0
    while i < len(table):
        nb += len(table[i])
        i += 1
    return nb


def c(table):
    if len(table) == 0:
        return 0
    lmax = len(table[0])
    i = 1
    while i < len(table):
        if len(table[i]) > lmax:
            lmax = len(table[i])
        i += 1
    return lmax


def ideale(table):
    return nb_valeurs(table) / len(table)
