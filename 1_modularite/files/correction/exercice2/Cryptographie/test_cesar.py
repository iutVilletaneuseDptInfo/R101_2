from cesar import *

def test_chiffre_cesar():
    assert chiffre_cesar("hello world!", 2) == "jgnnq yqtnf!"
    assert chiffre_cesar("HELLO WORLD!", 1) == "IFMMP XPSME!"
    assert chiffre_cesar("hello world!", 26) == "hello world!"
    assert chiffre_cesar("hello world!", 0) == "hello world!"
    assert chiffre_cesar("", 0) == ""
    assert chiffre_cesar("", 5) == ""
    print("test de la fonction chiffre_cesar : ok")


test_chiffre_cesar()

