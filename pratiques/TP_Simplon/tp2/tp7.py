# Exercice 78 : Inverser une chaîne de caractères 

                #-------Documentation du code-------#
# Ce code demande à l'utilisateur de saisir une phrase ou un mot.
# Il définit une fonction reverse_string qui prend une chaîne de caractères en entrée et retourne la chaîne inversée.
# La fonction utilise le slicing avec un pas de -1 pour inverser la chaîne.
# Enfin, le code affiche la chaîne inversée.

words = input ("Entrer une phrase ou un mot: ")

def reverse_string(words):
    reversed_words = words[5:3:-1]
    return reversed_words

print(reverse_string(words))