#Exo 1
# numero1 = input("Enter un nombre: ")
# numero2 = input("Enter un nombre: ")

# resultatSomme = int(numero1) + int(numero2)
# resultatProduit = int(numero1) * int(numero2)
# resultatMoyenne = int(numero1) / int(numero2)

# print(f"La somme est: {resultatSomme}")
# print(f"La produit est: {resultatProduit}")
# print(f"La moyenne est: {resultatMoyenne}")

#-------------------------_---------------------------

#Exo 2
# nombre = int(input("Entrer un nombre: "))
# formule = float( nombre * 1.8 / 32)

# print(f"La conversion de celcius en fahrenheit: °{formule}")

#-------------------------_---------------------------

#Exo3
# chaine = input("Entrer une chaine de caractere: ")

# print(len(chaine))

#-------------------------_---------------------------

#Exo4
# course = ["riz", "lait", "poulet"]
# course.append("poulet")
# course.remove("poulet")
# course[1] = "poivron"
# course.sort()
# print(course)


#-------------------------_---------------------------

#Exo5
# nombres = [14, 7, 22, 3, 9]
# plusGrand = max(nombres)
# plusPetit = min(nombres)
# print(nombres)
# print(plusGrand)
# print(plusPetit)

#-------------------------_---------------------------

# nombre1 = input("Entrer le nombre une: ")
# operator = input("chosir une de ces signes: \n +, \n -, \n *, \n / \n")
# nombre2 = input("Entrer le nombre deux: ")

# while operator != "+" and operator != "-" and operator != "*" and operator != "/":
#     operator = input("chosir une de ces signes: \n +, \n -, \n *, \n / \n")

# if nombre1.isnumeric and nombre2.isnumeric:
#    nombre1 = int(nombre1)
#    nombre2 = int(nombre2)

# else :
#     raise SystemExit("Fin du programme !")

# if operator == "+":
#     resultat = nombre1 + nombre2
#     print(resultat)
# elif operator == "-":
#     resultat = nombre1 - nombre2
#     print(resultat)
# elif operator == "*":
#     resultat = nombre1 * nombre2
#     print(resultat)
# elif operator == "/":
#     if nombre1 == 0 or nombre2 == 0:
#         raise SystemExit("Fin du programme !")
#     else :
#         resultat = nombre1 / nombre2
#         print(resultat)
# else :
#     raise SystemExit("Fin du programme !")


#-------------------------_---------------------------

# askNumber = input("Veuillez entrer des nombres précéder par des , : ")
# nombres = askNumber.split(",")

# liste_entiers = []

# for nombre in nombres:
#     nombres_entiers = int(nombre)
#     nombres_entiers = liste_entiers.append(nombres_entiers)
  
# #calcul le somme
# for nombre in liste_entiers:
#     somme = sum(liste_entiers)
#     print(somme)
    
# #caluul la moyenne
# for nombre in liste_entiers:
#     moyenne = somme / len(liste_entiers)
#     print(moyenne)

# #calculez le nombre de nombre superieur à la somme
# for nombre in liste_entiers:
#     if nombre > moyenne:
#         print(nombre)

#-------------------------_---------------------------
# def salaire_mensuel(salaire_annuel):
#     return salaire_annuel / 12

# def salaire_hebdomadaire(salaire_mensuel):
#     return salaire_mensuel / 4

# def salaire_horaire(salaire_hebdomadaire, heure_de_travail):
#     return salaire_hebdomadaire / heure_de_travail

# salaire = int(input("Entrer votre salaire annuel: "))
# heure = int(input("Entrer votre heure de travail: "))


# print(f"Votre salaire horaire est de: {salaire_horaire(salaire, heure)} €")

