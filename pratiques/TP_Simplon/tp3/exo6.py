# Écrire un algorithme qui demande 100 nombres à l'utilisateur, puis trouver le plus grand élément ensuite le plus petit

numbers = []

for i in range(1, 101):
    number = int(input(f"Veuillez saisir le nombre {i+1} : "))
    numbers.append(number)

plus_grand = max(numbers)
plus_petit = min(numbers)

print(f"Le plus grand nombre est : {plus_grand}")
print(f"Le plus petit nombre est : {plus_petit}")