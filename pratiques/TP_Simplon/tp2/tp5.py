# Exercice 5 : Recherche de doublons dans une liste (Boucle et Vérification) 



                  #-------Documentation du code-------#
#Ce code demande à l'utilisateur de saisir 7 nombres et vérifie s'il y a des doublons parmi les nombres saisis.
#D'abord, une liste vide est initialisée pour stocker les nombres saisis par l'utilisateur.
#Ensuite, une boucle for itère 7 fois, demandant à l'utilisateur de
#saisir un nombre à chaque itération. Chaque nombre saisi est converti en entier et ajouté à la liste.
#Apres le saisie des nombres, une variable set est utilisée pour suivre les nombres déjà vus.
#Set est une methode efficace pour vérifier les doublons car elle ne permet pas les valeurs dupliquées.
#Une autre liste est initialisée pour stocker les doublons trouvés.
#Une boucle for parcourt chaque nombre dans la liste des nombres saisis.
#Si un nombre est déjà dans le set des nombres vus, cela signifie qu'il s'agit d'un doublon.
#Le code vérifie ensuite si ce doublon n'a pas déjà été ajouté à la liste des doublons trouvés avant de l'ajouter.
#Si le nombre n'est pas dans le set, il est ajouté au set des nombres vus
#Enfin, le code vérifie si des doublons ont été trouvés.
#Si des doublons existent, ils sont affichés. 
    
liste_nombres = []

for i in range(7):
    nombre = int(input("Veuillez saisir un nombre : "))
    liste_nombres.append(nombre)

doublons_trouves = set()
doublon_liste = []

for d in liste_nombres:
    if d in doublons_trouves:
        if d not in doublon_liste:
            doublon_liste.append(d)
    else:
        doublons_trouves.add(d)

if doublon_liste:
    print(f"Doublons trouvés: {doublon_liste}")
else:
    print("Aucun doublon")