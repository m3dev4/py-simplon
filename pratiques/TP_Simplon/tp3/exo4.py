# Ecrire un algorithme qui permet de calculer le factoriel d’un nombre

nombre = int(input("Veuillez saisir un nombre entier positif : "))
resultat = 1

for i in range(1, nombre +1):
    resultat *= i
    
print(f"Le factoriel de {nombre} est : {resultat}")