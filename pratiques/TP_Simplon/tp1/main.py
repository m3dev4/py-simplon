#Exo 1: Déclaration et Affichagede BAse

# nom = "Mouhamed Lo"
# age = 26

# print(f"Bonjour {nom}, votre age est de {age} ans.")

#____________________________________________________________________#

#Exo2: Typage Dynamique et Insepection
# prix_unitaire = 1500
# message = "Ceci est le message"

# print(type(message))
# print(type(prix_unitaire))


#____________________________________________________________________#

#Exo3: Opération et Entré Utilisateur
# nombre1 = int(input("Entrer le nombre une: "))
# nombre2 = int(input("Entrer le nombre une: "))

# #calcul

# resultatAdd = nombre1 + nombre2 #Addition
# resultatSous = nombre1 - nombre2 #Soustraction
# resultatMulti = nombre1 * nombre2 #Multiplication
# resultatDiv = nombre1 / nombre2 #Division


# print(f"Le resultat d'addition de ce nombre est: {resultatAdd}")
# print(f"Le resultat du soustraction de ce nombre est: {resultatSous}")
# print(f"Le resultat du mutliplication de ce nombre est: {resultatMulti}")
# print(f"Le resultat du division de ce nombre est: {resultatDiv}")

#____________________________________________________________________#

#Exo4: Condition simple (Pair ou impair)

# verifyNumber = int(input("Entrer un nombre pour verifier s'il est par ou impair: "))

# if verifyNumber % 2 == 0:
#     print(f"Cette nombre {verifyNumber} est pair")
# else:
#     print(f"Cette nombre {verifyNumber} est impair")

#____________________________________________________________________#

#Exo5: Boucle for et Somme cumulative

# askNumber = int(input("Entrer un nombre: "))
# count = 0

# for nbm in range(1, askNumber + 1):
#    count += nbm


# print(f"La somme est a: {count}")

#____________________________________________________________________#

#Exo6: Boucle & table de de multiplication
# askNumberToMultiply = int(input("Entrer un nombre: "))

# for nb in range(1, 11):
#     print(f"{askNumberToMultiply} x {nb} = {askNumberToMultiply * nb}")

#____________________________________________________________________#

#Exo7: Boucle while & authentification
# passwordCorrect = "python123"
# tentative = 3
# succes = False

# enterPassword = input("Entrer votre mot de passe: ")

# while enterPassword != passwordCorrect and tentative > 0:
#     tentative -= 1
#     enterPassword = input(f"Entrer votre mot de passe: il vous reste {tentative} tentative(s) ")
#     if tentative == 1:
#         print("Vous avez epuisez les tentatives")
#         succes = False
#         break
#     else:
#         print("Mot de passe incorrect")

# if enterPassword == passwordCorrect:
#         print("Bienvenue! admin")
#         succes = True

#____________________________________________________________________#

#Exo8: Introduction aux listes
# askUserToEnterNumber = input("Entrer 5 nombre précéder par un virgule: ")

# number = askUserToEnterNumber.split(",")
# listNumber = []

# for nb in number:
#     converNumber = int(nb)
#     listNumber.append(converNumber)
#     listNumber.sort()
# #affichage
# for nb in listNumber:
#     print(nb)

#____________________________________________________________________#


#Exo9: Stattiques de Base sur une liste
# N = 5
# tab = []
# for i in range(N): 
#    tab.append(int(input("Entrer un nombre: ")))

# somme = sum(tab)
# print(f"La somme est: {somme}")
# moyenne = somme / N
# print(f"La moyenne est: {moyenne}")
# maximum = max(tab)
# print(f"Le maximum est: {maximum}")
# minimum = min(tab)
# print(f"Le minimum est: {minimum}")

#____________________________________________________________________#


#Exo10: Fonctions et Portée des Variables 
# data_global = 10

# def function():
#     global data_global
#     data_global = 20
#     print(data_global)

# function()

#____________________________________________________________________#

#Exo11: Simulation de Diagnostic
# symptomes = {
#     "fièvre": 5,
#     "toux": 3,
#     "fatigue": 2,
#     "maux de tête": 4,
#     "essoufflement": 2
# }

# question = "Avez vous ces symptômes suivants ? (oui/non) :"

# for symptome in symptomes.items():
#     while True:
#         response = input(f"{question} {symptome[0]} ").lower()
#         if response in ["oui", "non"]:
#             break
#         else :
#             print("Veuillez répondre par 'oui' ou 'non'.")


# score = 0

# for symptome in symptomes.items():
#     if symptome in response:
#         score += symptome[1]

# if score >= 5:
#     print("Vous pourriez être malade. Veuillez consulter un médecin.")
# elif score >= 3:
#     print("Vous présentez quelques symptômes. Surveillez votre état de santé.")
# else:
#     print("Vous semblez en bonne santé.")