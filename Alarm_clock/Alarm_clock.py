import winsound
import time
def main():
    import time
    print ("How to use:")
    print ("Enter number of hours, minutes, and seconds.")
    print ("________________________________________________")
    t = int(input("Hours:"))
    if t < 0:
        print ("invalid")
        main()
    y = int(input("Minutes:"))
    if y < 0:
        print ("invalid")
        main()
    u = int(input("Seconds:"))
    if u < 0:
        print ("invalid")
        main()
    x = t*60*60 + y*60 + u
    while x != 0:
        print (str(x), "seconds left.")
        x -= 1
        time.sleep(1)
    if x == 0:
        print ("Time is up.")
        while True:
            time.sleep(0.1)
            winsound.Beep(5000,110)
            time.sleep(0.1)
            winsound.Beep(1000,110)

main()                                                                           #By WenKang
