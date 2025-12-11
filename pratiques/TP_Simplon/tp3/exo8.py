# Écrire un algorithme qui demande 5 nombres à l'utilisateur, et les afficher dans l’ordre croissant.

#methode 1

numbers = []

for i in range(5):
    number = int(input(f"Veuillez saisir le nombre {i+1} : "))
    numbers.append(number)
    numbers.sort()
    
print("Les nombres dans l'ordre croissant sont :", numbers)

#methode 2
numbers_method2 = []

for i in range(5):
    number_two = int(input(f"Veuillez saisir le nombre {i+1} : "))
    numbers_method2.append(number_two)
    
for i in range(len(numbers_method2)):
    for j in range(i + 1, len(numbers_method2)):
        if numbers_method2[i] > numbers_method2[j]:
           numbers_method2[i], numbers_method2[j] = numbers_method2[j], numbers_method2[i]
            
print("Les nombres dans l'ordre croissant sont :", numbers_method2)



# La première boucle for i in range(len(numbers_method2)): parcourt chaque indice de la liste.
# La deuxième boucle for j in range(i + 1, len(numbers_method2)): parcourt tous les indices qui viennent après i.
# À chaque tour, on compare l’élément à la position i avec l’élément à la position j.
# Si l’élément à la position i est plus grand que celui à la position j, on échange leurs places.


# Cela veut dire :
# Pour chaque position i dans la liste, la boucle j commence à l’indice juste après (i + 1) et va jusqu’à la fin de la liste.

# Exemple :
# Si la liste a 5 éléments et que i = 1, alors j prendra les valeurs 2, 3, 4.
# On compare donc l’élément à la position i avec tous ceux qui sont après lui dans la liste.
# Cela permet de trouver, pour chaque position, s’il y a un nombre plus petit plus loin dans la liste, et de les échanger si besoin.