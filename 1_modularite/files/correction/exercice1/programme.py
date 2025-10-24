import cesar

message = input("Donnez un message \n")

i=1
while i<=26 :
    print(cesar.chiffre_cesar(message, i))
    i+=1
