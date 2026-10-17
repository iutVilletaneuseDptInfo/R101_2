def compteMots(s):
    """
        Retourne le nombre de mots dans une phrase.(un mot est une 
        séquence non vide de caractères comprise entre deux espaces)
    """
    # split découpe la chaîne selon les espaces et retourne un tableau
    # contenant les différentes parties
    return len(s.split())
