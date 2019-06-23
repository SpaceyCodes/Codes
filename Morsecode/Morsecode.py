import winsound as ws
import time

table = {'a':'/.-/', 'b':'/-.../', 'c':'/-.-./', 'd':'/-../', 'e':'/./', 'f':'/..-./', 'g':'/--./', 'h':'/..../', 'i':'/../',
         'j':'/.---/', 'k':'/-.-/', 'l':'/.-../', 'm':'/--/', 'n':'/-./', 'o':'/---/', 'p':'/.--./', 'q':'/--.-/', 'r':'/.-./',
         's':'/.../', 't':'/-/', 'u':'/..-/', 'v':'/...-/', 'w':'/.--/', 'x':'/-..-/', 'y':'/-.--/', 'z':'/--../'}
message = input('Enter string : ')
for x in message:
    print(table.get(x.lower(), ' '))
def resound():
    for x in message:
        if table.get(x.lower()) == '/.-/':                   #a
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-.../':                   #b
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-.-./':                   #c
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-../':                   #d
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/./':                   #e
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/..-./':                   #f
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/--./':                      #g
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/..../':                   #h
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/../':                   #i
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.---/':                   #j
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-.-/':                   #k
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.-../':                   #l
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/--/':                   #m
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-./':                   #n
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/---/':                   #o
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.--./':                   #p
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/--.-/':                   #q
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.-./':                   #r
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.../':                   #s
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-/':                   #t
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/..-/':                   #u
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/...-/':                   #v
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/.--/':                   #w
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-..-/':                   #x
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/-.--/':                   #y
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(1.8)
        if table.get(x.lower()) == '/--../':                   #z
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 210)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(0.5)
            ws.Beep(4500, 110)
            time.sleep(1.8)

time.sleep(1.5)
resound()



while True:
    ask = str(input("again or break: "))
    if ask == "again":
        resound()
    if ask == "break":
        break
