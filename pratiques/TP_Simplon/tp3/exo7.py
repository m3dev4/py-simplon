# mdp

password_correct = "python123"
tentative = 3
succes = False

enter_password = input("Entrer votre mot de passe: ")

while enter_password != password_correct and tentative > 0:
    tentative -= 1
    enter_password = input(f"Entrer votre mot de passe: il vous reste {tentative} tentative(s) ")
    if tentative == 1:
        print("Vous avez epuisez les tentatives")
        succes = False
        break    