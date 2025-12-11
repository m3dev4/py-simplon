# Exercice 2 : Fusionner deux listes (Création de listes) 🤝


                 #-------Documentation du code-------#
# Dans cet exercice, nous allons demander à l'utilisateur de saisir deux listes de nombres.
#Declaration des listes vide A, B et C pour stocker les valeurs saisies et la liste fusionnée.
#les boucles for sont utilisées pour itérer 3 fois et demander à l'utilisateur de saisir des nombres pour les listes A et B.
# Les nombres saisis sont convertis en entiers et ajoutés aux listes respectives.
# Ensuite, la liste C est créée en fusionnant les listes A et B à l'aide de l'opérateur +.
# La liste C est ensuite triée en ordre croissant à l'aide de la méthode sort


liste_A = []
liste_B = []
liste_C = []

for i in range(3):
    nombre_A = int(input(f"Veuillez saisir le nombre {i+1} pour la Liste A : "))
    liste_A.append(nombre_A)

for i in range(3):
    nombre_B = int(input(f"Veuillez saisir le nombre {i+1} pour la Liste B : "))
    liste_B.append(nombre_A)

liste_C = liste_A + liste_B
liste_C.sort()
print("La Liste C fusionnée est :", liste_C)

