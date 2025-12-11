# -----------------------------------------------------------------------------
# Script : Détection et comptage des doublons dans une liste de nombres
# -----------------------------------------------------------------------------
# Objectif :
#   - Permettre à l'utilisateur de saisir 7 nombres entiers.
#   - Afficher la liste complète des nombres saisis.
#   - Détecter les doublons (nombres apparaissant plus d'une fois).
#   - Afficher pour chaque doublon combien de fois il apparaît.
#   - Afficher la liste des doublons ou un message s'il n'y en a pas.
#
# Fonctionnement détaillé :
#
# 1. Saisie des nombres :
#    - Une boucle for s'exécute 7 fois.
#    - À chaque itération, l'utilisateur saisit un nombre via input().
#    - Le nombre est converti en entier et ajouté à la liste nb_liste.
#
# 2. Affichage de la liste :
#    - Après la saisie, la liste complète des nombres est affichée.
#
# 3. Comptage des occurrences :
#    - Un dictionnaire compteur est créé pour compter le nombre d'occurrences de chaque nombre.
#    - Pour chaque nombre de la liste, on incrémente son compteur dans le dictionnaire.
#
# 4. Détection des doublons :
#    - On parcourt le dictionnaire compteur.
#    - Si un nombre apparaît plus d'une fois (valeur > 1), il est ajouté à la liste doublons.
#
# 5. Affichage des résultats :
#    - Pour chaque doublon, on affiche combien de fois il apparaît.
#    - Si la liste doublons n'est pas vide, on affiche tous les doublons trouvés.
#    - Sinon, on affiche "Aucun doublon".
#
# Exemple d'exécution :
#    Entrer un nombre: 2
#    Entrer un nombre: 3
#    Entrer un nombre: 2
#    Entrer un nombre: 5
#    Entrer un nombre: 3
#    Entrer un nombre: 7
#    Entrer un nombre: 2
#    Liste des nombres saisis : [2, 3, 2, 5, 3, 7, 2]
#    Le nombre 2 apparaît 3 fois.
#    Le nombre 3 apparaît 2 fois.
#    Doublons trouvés: [2, 3]
# -----------------------------------------------------------------------------
nb_liste = []

for i in range(7):
    nb = int(input("Entrer un nombre: "))
    nb_liste.append(nb)

print("Liste des nombres saisis :", nb_liste)
    
compteur = {}
doublons = []

for nb in nb_liste:
    if nb in compteur:
        compteur[nb] += 1
    else:
        compteur[nb] = 1
print(compteur)
 
for nb, c in compteur.items():
    if c > 1:
        doublons.append(nb)

for nb in doublons:
    print(f"Le nombre {nb} apparaît {compteur[nb]} fois.")

if doublons:
    print(f"Doublons trouvés: {doublons}")
else:
    print("Aucun doublon")