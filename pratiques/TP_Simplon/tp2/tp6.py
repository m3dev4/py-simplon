# Exercice 6 : Compter les voyelles dans une liste de mots (Boucles Imbriquées) 


                #-------Documentation du code-------#
# Ce code demande à l'utilisateur de saisir 5 mots et compte le nombre de voyelles dans chaque mot.
# D'abord, une liste vide est initialisée pour stocker les mots saisis par l'utilisateur.
# Ensuite, une boucle while est utilisée pour s'assurer que l'utilisateur saisit exactement 5 mots.
# La méthode split() est utilisée pour diviser la chaîne de caractères saisie en une liste de mots.
# Si le nombre de mots saisis est correct, la liste est stockée dans liste_mots et la boucle se termine.
# Sinon, un message d'erreur est affiché et l'utilisateur est invité à ressaisir les mots.
# Après avoir obtenu la liste de mots, une boucle for parcourt chaque mot dans la liste.
# Pour chaque mot, une variable voyelle_count est initialisée à zéro pour compter les voyelles.
# Une boucle for imbriquée parcourt chaque lettre du mot.
# Une condition if vérifie si la lettre est une voyelle (a, e, i, o, u, y) en tenant compte des majuscules et des minuscules.
# Si la lettre est une voyelle, le compteur voyelle_count est incrémenté de un.
# Après avoir compté les voyelles dans le mot, le code affiche le mot et le nombre de voyelles qu'il contient.      

# vérifie si tous les éléments d'un itérable sont vrais

liste_mots = []


while True:
    mots = input("Veuillez saisir 5 mots séparés par un espace : ").split()
    if len(mots) == 5 and all(mot.isalpha() for mot in mots):
        liste_mots = mots
        break
    else:
        print("Erreur : vous devez saisir exactement 5 mots.")

print(f"Avant comptage, la liste des mots est : {liste_mots}")

for mot in liste_mots:
    voyelle_count = 0
    for lettre in mot:
        if lettre.lower() in 'aeiouy':
            voyelle_count += 1
        
 
        
    print(f"Le mot '{mot}' contient {voyelle_count} voyelles.")