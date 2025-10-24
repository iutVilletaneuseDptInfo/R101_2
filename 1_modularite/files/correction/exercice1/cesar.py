def chiffre_lettre(c, n):
    """
        Retourne le chiffrement de la lettre c : 
        - si c est une lettre, alors la lettre est décalée de n caractères
        - autrement, aucune modification n'est faite
    """
    if 'a' <= c and c <= 'z':  # si c est une lettre
        chiffree = chr((ord(c) + n - ord('a')) % 26 + ord('a'))  # décalée de n
    elif 'A' <= c and c <= 'Z':
        chiffree = chr((ord(c) + n - ord('A')) % 26 + ord('A'))  # décalée de n
    else:
        chiffree = c  # inchangée
    return chiffree


def chiffre_cesar(s, n):
    """
       Retourne la chaîne s où chaque lettre
       est décalée de n "vers la droite". 
       Exemple : chiffre_cesar("Hello World!", 2) 
                 retourne "Jgnnq Yqtnf!"
    """
    chiffree = ""  # chaîne chiffrée
    i=0
    while i< len(s):
        chiffree += chiffre_lettre(s[i], n)  
        i+=1
    return chiffree


def dechiffre_cesar(s, n):
    """
       Retourne la chaîne s où chaque lettre
       est décalée de 26-n "vers la droite" 
       pour retomber sur la lettre initiale
       Exemple : dechiffre_cesar("jgnnq yqtnf!", 24) 
                 retourne "hello world!"
    """
    return chiffre_cesar(s,26-n)

if __name__ == '__main__':
    print(dechiffre_cesar("Le script cesar.py est execute !",10))
