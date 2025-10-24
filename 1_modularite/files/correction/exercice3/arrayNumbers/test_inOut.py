import math
from arrayNumbers.inOut import *
import math as m
import os

def test_readFromFile():
    f = open("test.txt", "w")
    f.write("4\n12.3\n32.4\n53.4\n-5\n")
    f.close()
    tab = readFromFile("test.txt")
    os.remove("test.txt")
    res = [12.3, 32.4, 53.4, -5]
    assert len(tab) == len(res)
    i = 0
    while i < len(tab):
        assert m.isclose(tab[i], res[i])
        i += 1
    print("test de la fonction readFromFile : ok")

def test_writeToFile():
    t = [15.6, 76, 75.789, -142.6]
    writeToFile(t, "test.txt")
    t2 = readFromFile("test.txt")
    os.remove("test.txt")
    assert t == t2
    print("test de la fonction writeToFile : ok")