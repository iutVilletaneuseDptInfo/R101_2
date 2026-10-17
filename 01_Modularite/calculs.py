def carre(x):
    """Retourne le carré de x.

    :param x: le nombre à mettre au carré.
    :type x: int
    :returns: le carré de x.
    :rtype: int"""
    return x * x


if __name__ == '__main__':
    print("Ce script est exécuté directement.")
    print("Le carré de 7 est", carre(7))
else:
    print("Le module calculs est importé.")
