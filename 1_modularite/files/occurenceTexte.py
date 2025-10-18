import fonctionsChaines as fch

print("Saisir un texte")
texte = input()
texte = texte.lower()  # transforme le texte en minuscules

nbE = fch.occurence(texte, "e") # fonction occurence du module 
                                #fonctionsChaines renommé fch
print("Le texte contient", nbE, "fois la lettre e.")
