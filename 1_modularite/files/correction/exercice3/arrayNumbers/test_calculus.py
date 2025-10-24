from arrayNumbers.calculus import *
import math as m

def test_array_sum():
    assert array_sum([1,2,3]) == 6
    assert m.isclose(array_sum([2.3, 3.4, 4.5]), 10.2)
    print("Test de la fonction array_sum : ok")

def test_array_average():
    assert m.isclose(array_average([1, 2, 3]), 2)
    assert m.isclose(array_average([2.3, 3.4, 4.5]), 10.2 / 3)
    print("Test de la fonction array_average : ok")

def test_array_variance():
    assert m.isclose(array_variance([2, 2, 2, 2]), 0)
    assert m.isclose(array_variance([10, 0, 0, 0, 0]), 80/5)
    print("Test de la fonction array_variance : ok")
