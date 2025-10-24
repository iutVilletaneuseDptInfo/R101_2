def readFromFile(filename):
    f = open(filename, "r")
    n = int(f.readline())
    tab = []
    i = 0
    while i < n:
        tab.append(float(f.readline()))
        i += 1
    f.close()
    return tab

def writeToFile(tab, filename):
    f = open(filename, "w")
    f.write(str(len(tab))+ "\n")
    i = 0
    while i < len(tab):
        f.write(str(tab[i]) + "\n")
        i += 1
    f.close()