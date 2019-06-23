import hashlib
file = {"wen":"a5022ab8093f8d05fb848a067065bd9e0294eb54fff3f583878f5130142ae600075199ad6aea1d0bfef48c5f6bedeff6e83b9205f755110bae36212e95dab963"}
def start():
    print("1.Login     2.Sign Up")
    x = str(input(""))
    if x == "1":
        login()
    elif x == "2":
        signup()
    else:
        start()
def login():
    print ("Login Here")
    keyinuser = input("Key in your Username: ")
    keyinpass = input("Key in your Password: ")
    keyinpass_encrypted1 = hashlib.sha3_512(keyinpass.encode()).hexdigest()
    if file.get(keyinuser) == keyinpass_encrypted1:
        print ("sussessful")
    else:
        print ("incorrect")
        login()
def signup():
    print ("Sign up here")
    username = str(input("What is your username: "))
    password = str(input("What password: "))
    password_ecrypted1 = hashlib.sha3_512(password.encode()).hexdigest()
    if password_ecrypted1 == file.get(username):
        print ("Invalid try again")
        signup()
    else:
        file[username]=password_ecrypted1
        start()

start()
