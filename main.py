from prettytable import PrettyTable
Table_Heading = PrettyTable(["S.No.","Number", "Multiple", "Result"])
def Creating_Multiplication_Table(multiplicant,multiple,):
    for i in range(1,11):
        multiple+= 1
        Result = multiplicant * multiple
        Table_Heading.add_row([str(multiple),str(multiplicant) , str(multiple), str(Result)])
    print(Table_Heading)

Multiple = 0
Multiplicant = int(input("Multiplicand: "))
Creating_Multiplication_Table(Multiplicant,Multiple)
