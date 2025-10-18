import fonctionsChaines as fch
import Outils.words as uw


print("saisir un texte ")
texte = input()
nbE = fch.occurence(texte, "e")
nbMots = uw.compteMots(texte)
print("Le texte contient", nbE, "lettres e et", nbMots, "mots.") 
