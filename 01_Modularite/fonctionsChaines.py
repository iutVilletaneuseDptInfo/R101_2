def occurence(s, c):
    """
        Retourne le nombre de fois où le caractère c apparaît dans la chaîne s.
    """
    compteur = 0
    i = 0
    while i < len(s):
        if s[i] == c:
            compteur += 1
        i += 1
    return compteur
