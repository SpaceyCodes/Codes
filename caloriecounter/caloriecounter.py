table = {"chicken":284,"fish":339.5,"pork":251}
table2 = {"boiled":"a","fried":"b","steam":"c",}
table3 = {}
x3 = 0
def asking():
    msg = str(input("What did you eat?"))
    msg2 = str(input("how?"))
    print (table.get(msg))
    print (table2.get(msg2))
    print (table3)
    table3[msg]=table2.get(msg2)
    for x, y in table3.items():
        print (x, y)





while True:
    asking()
