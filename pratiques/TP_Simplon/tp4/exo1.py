def multi(table) :
    for i in range(1, 11):
        print(i, "x", table, "=", i * table)
        
        
number = int(input("Enter the number: "))
multi(number)