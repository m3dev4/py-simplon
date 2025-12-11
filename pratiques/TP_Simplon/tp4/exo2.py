def reverse_number(a, b, temp):
    temp = a 
    a = b
    b = temp
    return a, b

numberA = int(input("Veuillez saisir le nombre de A: "))
numberB = int(input("Veuillez saisir le nombre de B: "))
temp = 0

print(reverse_number(numberA, numberB, temp))