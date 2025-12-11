# Exercice 1 : Gestion de stock (Variables, Saisie et Condition) 

                 #-------Documentation du code-------#

#Ce code permet de gérer le stock de produits d'un magasin en demandant à l'utilisateur de saisir le stock initial et le nombre de produits vendus.
#D'abord, le code utilise un bloc try-except pour gérer les erreurs de saisie.
# A l'intérieur du bloc try, il demande à l'utilisateur de saisir le stock initial et le nombre de produits vendus, en convertissant ces valeurs en entiers.
 #Ensuite, il calcule le stock restant en soustrayant le nombre de produits vendus du stock initial.
 #Le code affiche ensuite le stock restant.
 #Si le stock restant est strictement inférieur à 10, il affiche un message d'avertissement pour inciter au réapprovisionnement.
 #Par ailleurs, si le stock restant est égal à 0, il affiche un message indiquant que le stock est épuisé et qu'un réapprovisionnement immédiat est nécessaire.
# Si une erreur de conversion se produit (par exemple, si l'utilisateur saisit une valeur non numérique), le bloc except capture l'exception ValueError et affiche un message demandant à l'utilisateur de saisir des valeurs numériques valides.
while True:
    try: 
         stock_initial = int(input("Veuillez saisir le stock initial de produits : "))
         produits_vendus = int(input("Veuillez saisir le nombre de produits vendus aujourdh'ui : "))
         resultat_stock = stock_initial - produits_vendus
         print(f"Le stock restant est de : {resultat_stock} produits.")
         if resultat_stock < 10:
            print("Attention ⚠️: stock faible, penser au réapprovisionnement.")
         elif resultat_stock ==  0:
            print("Le stock est épuisé. Veuillez réapprovisionner immédiatement.")
         elif resultat_stock < 0:
            print("Erreur : le nombre de produits vendus dépasse le stock initial.")
         break
    except ValueError as e:
      print("Veuillez entrer des valeurs numériques valides pour le stock et les produits vendus.")

   