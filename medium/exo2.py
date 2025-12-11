# ============================================================================
# JEU DE DEVINETTE - CODE DOCUMENTÉ POUR DÉBUTANTS
# ============================================================================

# On importe les outils nécessaires pour générer des nombres aléatoires
import random
from random import choice  # Note: cette ligne n'est pas utilisée dans le code

# ============================================================================
# PARTIE 1 : CONFIGURATION DU JEU (Variables globales)
# ============================================================================

# Liste des niveaux de difficulté disponibles
level = ["Facile", "Moyen", "Difficile"]

# Dictionnaire qui associe chaque niveau au nombre d'essais autorisés
# Par exemple : niveau "facile" = 10 essais
try_number = {"facile": 10, "moyen": 7, "difficile": 5}

# Génération du nombre mystère que le joueur doit deviner
# random.randint(1, 100) choisit un nombre aléatoire entre 1 et 100 (inclus)
num_aleatoire = random.randint(1, 100)

# Variable pour stocker le score du joueur (non utilisée dans cette version)
score = 0

# ============================================================================
# PARTIE 2 : ACCUEIL DU JOUEUR
# ============================================================================

# Affichage du titre du jeu avec des bordures pour le rendre joli
print("=======================Bienvenue dans le jeu de devinette======================")

# Demande au joueur d'entrer son nom d'utilisateur
userProfile = input("Entrer votre username: ")

# Affiche un message personnalisé avec le nom du joueur
# Le f" " permet d'insérer des variables directement dans le texte
print(f"Hey 😊 {userProfile}, veuillez choisir un niveau ci-dessous: 👇")


# ============================================================================
# PARTIE 3 : FONCTION DE SÉLECTION DU NIVEAU
# ============================================================================

def choiceLevel():
    """
    Cette fonction permet au joueur de choisir son niveau de difficulté.
    Elle affiche les options et valide le choix de l'utilisateur.
    """
    
    # Affichage des niveaux disponibles avec numérotation automatique
    # enumerate(level, 1) donne un numéro à chaque élément en commençant par 1
    # Exemple : 1. Facile, 2. Moyen, 3. Difficile
    for i, lvl in enumerate(level, 1):
        print(f"{i}. {lvl}")
    
    # Boucle infinie qui continue jusqu'à ce qu'un choix valide soit fait
    while True:
        try:
            # Le mot-clé 'global' permet de modifier la variable 'choice' 
            # en dehors de cette fonction (accessible partout dans le programme)
            global choice
            
            # Demande au joueur de choisir un nombre entre 1 et 3
            # int() convertit le texte entré en nombre entier
            choice = int(input("Votre choix (1, 2 ou 3) : "))
            
            # ========== SI LE JOUEUR CHOISIT LE NIVEAU FACILE ==========
            if choice == 1:
                print("Vous avez choisi le niveau Facile")
                print("Vous devez deviner un nombre entre 1 et 100")
                print("Vous avez 10 essais")
                print("Bonne chance !")
                print("=====================================================================")
                break  # Sort de la boucle while car le choix est valide
            
            # ========== SI LE JOUEUR CHOISIT LE NIVEAU MOYEN ==========
            elif choice == 2:
                print("Vous avez choisi le niveau Moyen")
                print("Vous devez deviner un nombre entre 1 et 100")
                print("Vous avez 7 essais")
                print("Bonne chance !")
                print("=====================================================================")
                break  # Sort de la boucle while car le choix est valide
            
            # ========== SI LE JOUEUR CHOISIT LE NIVEAU DIFFICILE ==========
            elif choice == 3:
                print("Vous avez choisi le niveau Difficile")
                print("Vous devez deviner un nombre entre 1 et 100")
                print("Vous avez 5 essais")
                print("Bonne chance !")
                print("=====================================================================")
                break  # Sort de la boucle while car le choix est valide
            
            # ========== SI LE JOUEUR ENTRE UN AUTRE NOMBRE (4, 5, etc.) ==========
            else:
                print("Veuillez entrer un nombre valide pour le niveau de difficulté.")
            
        # Gestion des erreurs : si le joueur entre du texte au lieu d'un nombre
        # ValueError est l'erreur qui se produit quand on essaie de convertir
        # du texte (comme "abc") en nombre avec int()
        except ValueError as e:
            print("Veuillez entrer un nombre valide pour le niveau de difficulté.")


# ============================================================================
# PARTIE 4 : FONCTION PRINCIPALE DU JEU
# ============================================================================

def game():
    """
    Cette fonction contient toute la logique du jeu.
    Elle gère le choix du niveau et la boucle de devinettes.
    """
    
    # Boucle principale du jeu (niveau 1)
    while True:
        try:
            # Appel de la fonction pour choisir le niveau
            choiceLevel()
            
            # Boucle secondaire pour le jeu de devinette (niveau 2)
            while True:
                try:
                    # ========== ATTRIBUTION DU NOMBRE D'ESSAIS SELON LE NIVEAU ==========
                    # On utilise le choix du joueur pour récupérer le bon nombre d'essais
                    if choice == 1:
                        essai = try_number["facile"]  # 10 essais
                    elif choice == 2:
                        essai = try_number["moyen"]   # 7 essais
                    elif choice == 3:
                        essai = try_number["difficile"]  # 5 essais
                    else:
                        # Si le choix est invalide, on recommence
                        print("Veuillez entrer un nombre valide pour le niveau de difficulté.")
                        continue  # Retourne au début de la boucle while
                    
                    # ========== BOUCLE DE DEVINETTES (niveau 3) ==========
                    # Continue tant qu'il reste des essais
                    while essai > 0:
                        # Demande au joueur de deviner le nombre
                        devine = int(input("Devinez le nombre : "))
                        
                        # ===== CAS 1 : Le joueur a trouvé le bon nombre =====
                        if devine == num_aleatoire:
                            print("Félicitations ! Vous avez deviné le nombre.")
                            break  # Sort de la boucle, le jeu est terminé
                        
                        # ===== CAS 2 : Le nombre deviné est trop petit =====
                        elif devine < num_aleatoire:
                            print("Le nombre est plus grand.")
                            essai -= 1  # Retire un essai (équivalent à essai = essai - 1)
                            print(f"Il vous reste {essai} essai(s)")
                        
                        # ===== CAS 3 : Le nombre deviné est trop grand =====
                        else:
                            print("Le nombre est plus petit.")
                            essai -= 1  # Retire un essai
                            print(f"Il vous reste {essai} essai(s)")
                    
                    # ========== SI LA BOUCLE SE TERMINE SANS BREAK ==========
                    # Le "else" après un "while" s'exécute uniquement si la boucle
                    # se termine normalement (sans break), c'est-à-dire si essai atteint 0
                    else:
                        print("Désolé, vous avez épuisé vos essais. Le nombre était : ", num_aleatoire)
                        break  # Sort de la boucle secondaire
                
                # Gestion des erreurs lors de la saisie du nombre à deviner
                except ValueError as e:
                    print("Veuillez entrer un nombre valide.")
                
                break  # Sort de la boucle secondaire après une partie complète
            
            break  # Sort de la boucle principale
        
        # Gestion des erreurs au niveau de la boucle principale
        except ValueError as e:
            print("Veuillez entrer un nombre valide pour le niveau de difficulté.")


# ============================================================================
# PARTIE 5 : LANCEMENT DU JEU
# ============================================================================

# Appel de la fonction game() pour démarrer le jeu
# C'est ici que tout commence !
game()
