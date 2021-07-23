def Creating_Multiplication_Table(multiplicant,multiple,):
    for i in range(1,11):
        multiple+= 1
        Result = multiplicant * multiple
        Display = str(multiplicant) + " * " + str(multiple) + " = " + str(Result)
        print("______________________________________________________________________")
        print(Display)
Multiple = 0
Multiplicant = int(input("Multiplicand: "))
Creating_Multiplication_Table(Multiplicant,Multiple)