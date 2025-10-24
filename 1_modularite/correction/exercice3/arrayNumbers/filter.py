def eltsLessThan(tab, threshold):
    res = []
    i = 0
    while i < len(tab):
        if tab[i] < threshold:
            res.append(tab[i])
        i += 1
    return res

def eltsBetween(tab, a, b):
    res = []
    i = 0
    while i < len(tab):
        if a <= tab[i] and tab[i] <= b :
            res.append(tab[i])
        i += 1
    return res
    