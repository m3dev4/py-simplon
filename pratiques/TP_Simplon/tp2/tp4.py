# Exercice 4 : Répartition de nombres (Tri selon la parité) 🌓

                #-------Documentation du code-------#
# Ce code demande à l'utilisateur de saisir 8 nombres et les répartit en deux listes : une pour les nombres pairs et une pour les nombres impairs.
# D'abord, deux listes vides, liste_A et liste_B, sont initialisées pour stocker respectivement les nombres pairs et impairs.
# Ensuite, une boucle for itère 8 fois, demandant à l'utilisateur de saisir un nombre à chaque itération.
# Chaque nombre saisi est converti en entier.
# Une condition if vérifie si le nombre est pair (c'est-à-dire si le reste de la division par 2 est égal à zéro).
# Si le nombre est pair, il est ajouté à la liste_A.
# Sinon, il est ajouté à la liste_B.
# Après la saisie de tous les nombres, le code affiche les deux listes : liste_A contenant les nombres pairs et liste_B contenant les nombres impairs.

liste_A = []
liste_B = []

for i in range(8):
    nombre = int(input("Veuillez saisir un nombre : "))
    if nombre % 2 == 0:
        liste_A.append(nombre)
    else:
        liste_B.append(nombre)

print("Liste des nombres pairs (A) :", liste_A)
print("Liste des nombres impairs (B) :", liste_B)