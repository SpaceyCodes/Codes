print ("How to use:")
print ("Addition: +           Subtraction: -")
print ("Multiplication: *     Power: **")
print ("_________________________________________")
z = float(input("What is your number? "))
u = str(input("What is your sign? "))
c = float(input("What is your number? "))

if u == "-" :
    i = z - c
    print (i)
elif u == "+" :
    i = z + c
    print (i)
elif u == "*" :
    i = z * c
    print (i)
elif u == "**" :
    i = z ** c
    print (i)
else :
    print ("It is not a sign.")                                             #By WenKang
