# Écrire un algorithme qui demande 10 nombres à l'utilisateur.
# # Calculer et afficher la somme et la moyenne de tous les élémentsa.

numbers = []

for i in range(10):
    number = int(input(f"Veuillez saisir le nombre {i+1} : "))
    numbers.append(number)
    
somme = sum(numbers)
moyenne = somme / len(numbers)

print(f"La somme des nombres est : {somme}")
print(f"La moyenne des nombres est : {moyenne}")