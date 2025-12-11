user_input = input("Entrez une phrase ou un mot : ")

def word_analysis():
    wds = user_input.split()
    nombre_de_mots = len(wds)

    #voyelle dans la phrase
    voyelle = "aeiouyAEIOUY"
    count = 0

    for letter in user_input:
        if letter in voyelle:
            count += 1

    #frequence de chaque mot
    frequence = {}
    for word in user_input.split():
        if word in frequence:
            frequence[word] += 1
        else: 
            frequence[word] = 1
        
    return nombre_de_mots, count, frequence
        

print(f"Le nombre de mots dans la phrase est : {word_analysis()[0]}")
print(f"Le nombre de voyelles dans la phrase est : {word_analysis()[1]}")
print("La fréquence de chaque mot dans la phrase est : {}".format(word_analysis()[2]))
print("Le mot le plus long est : {}".format(max(user_input.split(), key=len)))