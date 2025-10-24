import Cryptographie.cesar as cesar

def chiffre_ROT13(message):
    return cesar.chiffre_cesar(message,13)

def dechiffre_ROT13(message):
    return chiffre_ROT13(message)

