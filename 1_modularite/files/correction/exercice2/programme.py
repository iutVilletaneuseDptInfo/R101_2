##################
#   Question 1   #
##################

import Cryptographie.cesar as cesar

message = input("Donnez un message \n")

i=1
while i<=26 :
    print(cesar.chiffre_cesar(message, i))
    i+=1


##################
#   Question 3   #
##################


import Cryptographie.rot13  as rot13

print("Chiffrement ROT13 :", rot13.chiffre_ROT13("hello world"))
