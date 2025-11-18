#!/usr/bin/env python3

def xor(a, b):
    return "".join(chr(ord(i) ^ ord(j)) for i, j in zip(a, b))

try:
    ct = open('output.txt', 'r', encoding='latin1').read()
except FileNotFoundError:
    print("output.txt tidak ditemukan.")
    exit()

prefix = "Gematik2"
key = xor(prefix, ct[:len(prefix)])
pt = "".join(xor(ct[i:i+8], key) for i in range(0, len(ct), 8))

print(f"Key: {key!r}\nFlag: {pt!r}")
