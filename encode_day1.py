#!/usr/bin/python3

#Rotation Cipher

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
coding = input("Press 'e' to encode or 'd' to decode:  ")
plaintext = input("Enter text to be encoded or decoded?  ")

def encode():
    cipher = ""
    for x in plaintext:
        number = ((alphabet.index(x) + 3) % len(alphabet))
        a = alphabet[number]
        cipher +=a
    print (cipher)

def decode():
    cipher = ""
    for x in plaintext:
        number = ((alphabet.index(x) - 3) % len(alphabet))
        a = alphabet[number]
        cipher +=a
    print (cipher)

if (coding == "e"):
    encode()
elif (coding == "d"):
    decode()
else:
    print("Must choose 'e' or 'd'")

