import math
print ("How to use:")
print ("If Length is unknown enter 0.")
print ("_________________________________")
a = float(input("What is the length of side A? "))
b = float(input("What is the length of side B? "))
h = float(input("What is the length of hypotenuse? "))

if h == 0:
    h = math.sqrt(a**2 + b**2)
    print ("Hypotenuse is", h)
elif a == 0:
    if (h**2 - b**2) <= 0 :
        print ("Side A and B cannot be more than or equal to the hypotenuse.")
    else :
        a = math.sqrt(h**2 - b**2)
    print ("Side A is", a)
elif b == 0:
    if (h**2 - a**2) <= 0 :
        print ("Side A and B cannot be more than or equal to the hypotenuse.")
    else :
        b = math.sqrt(h**2 - a**2)
        print ("Side B is", b)                                                                   #By WenKang and Xavier
