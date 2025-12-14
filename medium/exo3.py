from datetime import datetime
import json


DATA_FILE = "data.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        list_data = json.load(f)
except FileNotFoundError:
    list_data = []

def ajouter_depense(depenses):
    global list_data 
    dic_data = {}
    
    while True:
        montant = input("Entrez le montant de la dépense : ")
        if not montant.isdigit():
            print("Veuillez entrer un nombre valide")
            continue
        elif montant.isdigit() <= 0:
            print("Veuillez entrer un nombre positif")
            continue
        else:
            montant = int(montant)
            break
    
    while True:
        categories = input("Entrez la catégorie de la dépense : ")
        if not categories.isalpha():
            print("Veuillez entrer une catégorie valide")
            continue
        else:
            categories = categories.lower()
            categories = str(categories)
            break
    
    while True:
        date = input("Entrez la date de la dépense (jj/mm/aaaa) : ")
        formatDate = "%d/%m/%Y"
        try: 
            datetime.strptime(date, formatDate)
            break
        except ValueError:
            print("Veuillez entrer une date valide")  
      
    dic_data["montant"] = montant
    dic_data["categories"] = categories
    dic_data["date"] = date
    list_data.append(dic_data) 
    depenses.append(list_data)
    
    with open("data.json", "w") as f:
       json.dump(list_data, f)
       
    print("Dépense ajoutée avec succès")
    return list_data
       

def afficher_depenses():
    if not list_data:
        print("Aucune dépense enregistrée")
    for dep in list_data:
        print(f"Montant : {dep['montant']}, Catégorie : {dep['categories']}, Date : {dep['date']}")
        
    
    
def total_par_categorie():
    depense_par_categorie = {}

    for dep in list_data:
        categorie = dep["categories"]
        montant = dep["montant"]

        if categorie not in depense_par_categorie:
            depense_par_categorie[categorie] = montant
        else:
            depense_par_categorie[categorie] += montant

    for categorie, total in depense_par_categorie.items():
        print(f"Catégorie : {categorie}, Total : {total}")

            
    
    
def total_par_jour():
    for dep in list_data:
        print(f"Date : {dep['date']}, Total : {dep['montant']}")
    
def depense_max():
    for dep in list_data:
      #depense max
      max_depense = max(list_data, key=lambda x: x['montant'])
      print(f"La dépense maximale est de {max_depense['montant']}€, la catégorie est {max_depense['categories']} et la date est {max_depense['date']}")

    
def menu(): 
    
    
    print("""
  /$$$$$$$            /$$ /$$                      /$$                                                            
| $$__  $$          |__/| $$                      | $$                                                            
| $$  \ $$  /$$$$$$  /$$| $$ /$$   /$$        /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$ 
| $$  | $$ |____  $$| $$| $$| $$  | $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$_____/ /$$__  $$
| $$  | $$  /$$$$$$$| $$| $$| $$  | $$      | $$  | $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$$$$$$$
| $$  | $$ /$$__  $$| $$| $$| $$  | $$      | $$  | $$| $$_____/| $$  | $$| $$_____/| $$  | $$ \____  $$| $$_____/
| $$$$$$$/|  $$$$$$$| $$| $$|  $$$$$$$      |  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/|  $$$$$$$
|_______/  \_______/|__/|__/ \____  $$       \_______/ \_______/| $$____/  \_______/|__/  |__/|_______/  \_______/
                             /$$  | $$                          | $$                                              
                            |  $$$$$$/                          | $$                                              
                             \______/                           |__/                                                """)
    
    print("Que voulez vous faire ?")
    choix = input("1. Ajouter une dépense\n2. Afficher les dépenses\n3. Afficher le total des dépenses par catégorie\n4. Afficher le total des dépenses par jour\n5. Afficher la dépense maximale\n6. Quitter\n")
    while True:
        if choix == "1":
            ajouter_depense([])
            break
        elif choix == "2":
            afficher_depenses()
            break
        elif choix == "3":
            total_par_categorie()
            break
        elif choix == "4":
            total_par_jour()
            break
        elif choix == "5":
            depense_max()
            break
        elif choix == "6":
            print("Au revoir")
            break
        else:
            print("Veuillez entrer un choix valide")
            choix = input("Que voulez vous faire ?\n1. Ajouter une dépense\n2. Afficher les dépenses\n3. Afficher le total des dépenses par catégorie\n4. Afficher le total des dépenses par jour\n5. Afficher la dépense maximale\n6. Quitter\n")
            
    
    
if __name__ == "__main__":
    menu()