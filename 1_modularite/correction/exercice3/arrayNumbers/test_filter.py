from arrayNumbers.filter import *

def test_eltsLessThan():
    assert eltsLessThan([1, 2, 3, 42, 5, 6], 4) == [1, 2, 3]
    assert eltsLessThan([1, 2, 3, 42, 5, 6], 0) == []
    assert eltsLessThan([1, 2, 3, 42, 5, 6], 100) == [1, 2, 3, 42, 5, 6]
    print("test de la fonction eltsLessThan : ok")

def test_eltsBetween():
    assert eltsBetween([1, 2, 3, 4, 5, 6], 0, 6) == [1, 2, 3, 4, 5, 6]
    assert eltsBetween([1, 2, 3, 4, 5, 6], 6, 0) == []
    assert eltsBetween([1, 2, 3, 4, 5, 6], 2, 4) == [2, 3, 4]
    print("Test de la fonction eltsBetween : ok")