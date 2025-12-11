# Exercice 3 : Filtrer les éléments négatifs d'une liste (Boucle et Condition)


                #-------Documentation du code-------#
# Ce code demande à l'utilisateur de saisir 10 nombres, qu'ils soient positifs ou négatifs, et les stocke dans une liste.
#D'abord, on initialise une liste vide pour stocker les nombres saisis par l'utilisateur.
# Ensuite, une boucle for est utilisée pour itérer 10 fois, demandant à l'utilisateur de saisir un nombre à chaque itération.
# Chaque nombre saisi est converti en entier et ajouté à la liste.
# Après avoir collecté les 10 nombres, une autre liste vide est initialisée pour stocker uniquement les nombres non négatifs (positifs et zéro).
# Une boucle for parcourt chaque nombre dans la liste initiale.
#L'utilisation d'une condition if permet de vérifier si le nombre est supérieur ou égal à zéro.
# Si c'est le cas, le nombre est ajouté à la liste des nombres non négatifs
# Après avoir filtré les nombres, la liste des nombres non négatifs est triée en ordre croissant à l'aide de la méthode sort().



liste_nombres = []

for i in range(10):
    nombre = int(input("Veuillez saisir un nombre (positif ou négatif) : "))
    liste_nombres.append(nombre)
    
liste_non_negatifs = []

for n in liste_nombres:
    if n >= 0:
        liste_non_negatifs.append(n)
        liste_non_negatifs.sort()

print("Avant filtrage, la liste des nombres est :", liste_nombres)
print("La liste des nombres non négatifs est :", liste_non_negatifs)