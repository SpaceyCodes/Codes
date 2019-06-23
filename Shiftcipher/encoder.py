print ("Shift Cipher Encryptor")
plaintext = input("Key in your Plain text: ")
key = int(input("Key in your key: "))
ciphertext = []
for char in plaintext:
    if char.isupper():
        if ord(char)+key > 90:
            ciphertext.append(chr(64+ord(char)+key-90))
        else:
            ciphertext.append(chr(ord(char)+key))
    elif char.islower():
        if ord(char)+key > 122:
            ciphertext.append(chr(96+ord(char)+key-122))
        else:
            ciphertext.append(chr(ord(char)+key))
    else:
        ciphertext.append(char)
print ("It is: ")
print(''.join(ciphertext))

