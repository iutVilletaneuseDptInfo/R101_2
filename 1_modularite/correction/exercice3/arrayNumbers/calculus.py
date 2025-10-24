def array_sum(tab):
    somme = 0
    i = 0
    while i < len(tab):
        somme += tab[i]
        i += 1
    return somme

def array_average(tab):
    return array_sum(tab) / len(tab)

def array_variance(tab):
    m = array_average(tab)
    somme = 0
    i = 0
    while i < len(tab):
        somme += (tab[i] - m)**2
        i += 1
    return somme / len(tab)