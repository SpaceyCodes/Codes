
import math
def f1():
    x = str(input('are u finding hypotenuse? (y/n) '))
    if x == 'y':
        a = float(input('a: '))
        b = float(input('b: '))
        h = math.sqrt(a**2 + b**2)
        print('h =',h)
    elif x == 'n':
        a = float(input('a: '))
        b = float(input('b: '))
        if a > b:
            c = math.sqrt(a*a - b*b)
            print('c =', c)
        elif a < b:
            c = math.sqrt(b*b - a*a)
            print('c =',c)
        elif a == b:
            while a == b:
                a = float(input('a: '))
                b = float(input('b: '))
                if a > b:
                    c = math.sqrt(a*a - b*b)
                    print('c =', c)
                elif a < b:
                    c = math.sqrt(b*b - a*a)
                    print('c =',c)
    while x != 'y' or 'n':
        f1()
f1()                                                                              #By Xavier