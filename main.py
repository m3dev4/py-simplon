def palindrome(chaine) :
    chaine = chaine.lower()
    chaine = chaine.replace(" ", " ")
    return chaine == chaine[::-1]


user_input = input("Entrez un mot ou une phrase : ")

if palindrome(user_input) :
    print("C'est un palindrome !")
else :
    print("Ce n'est pas un palindrome.")

palindrome(user_input)