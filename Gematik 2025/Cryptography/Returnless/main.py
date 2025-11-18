#!/usr/bin/env python3
from os import urandom

def encipher(a, b):
    c = ''
    for i, j in zip(a, b):
        c += chr(ord(i) ^ ord(j))
    return c

def rekey(key):
    k = ""
    for i, c in enumerate(key):
        if i == len(key) - 1:
            k += c
            k += chr(ord(c) ^ ord(key[0]))
        else:
            k += c
            k += chr(ord(c) ^ ord(key[i + 1]))
    key = k  

def main():
    key = urandom(8).decode('latin1')

    with open('flag.txt', 'r', encoding='latin1') as f:
        plaintext = f.read()

    i = 0
    ct = ''
    while i < len(plaintext):
        ct += encipher(plaintext[i:i+len(key)], key)
        i += len(key)
        rekey(key)  

    with open('output.txt', 'w', encoding='latin1') as f2:
        f2.write(ct)

if __name__ == "__main__":
    main()
