print ("Shift Cipher Decryptor")
ciphertext = input("Key in your Cipher text: ")
key = int(input("Key in your key: "))
plaintext = []
for char in ciphertext:
    if char.isupper():
        if ord(char)-key < 65:
            plaintext.append(chr(91-(65-(ord(char)-key))))
        else:
            plaintext.append(chr(ord(char)-key))
    elif char.islower():
        if ord(char)-key < 97:
            plaintext.append(chr(123-(97-(ord(char)-key))))
        else:
            plaintext.append(chr(ord(char)-key))
    else:
        plaintext.append(char)
print ("It is: ")
print(''.join(plaintext))
