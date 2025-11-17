from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
import math

# Baca kedua kunci publik
pubkey1_pem = """-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBJ4n6F2RUMI0FEIOFVTm38
VL+ekVIgz9s0ReVru1Mniqqdtge8LMUeo/2tSB/ObMybtcseND+5vnUH8piB6kxs
cNaezOqMurruVDLhk14W+VJzrrQ6QMpiG00vy325kFP9jwk/M5FOPtqGWz8M7dA4
ewc0cOhCdsEtMOGlXkGAafKudjzmFs+Tlwc0MSH3NwuNkOav98Pk3hE0gU6OWqEr
BwQKEDhMTed1GwQfxQpRFVS0QpDGvfjBzMLJEzRzvy+nzHfooK7NfKHwgNDyol1s
X+gy2ntLTtdBoB6zPiq1aL17WubngnKfr8zVRa6nJyY9E7D41upLG1K65sWXQLan
AgMBAAE=
-----END PUBLIC KEY-----"""

pubkey2_pem = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAjOzpokEiibG/IaDy6y3C
iuukJ9J7gTv/C7Kf7D99y6OYn3CDDBdzNF//+7xNwf4yMgWFNUbCJARkJ0tvvVvo
q4y/kI2eswJOKBqOyAdi6PbwZ5HiS5KFRrgT3SYMSLZ7arCOexb1Pu0q8GOtM3/+
BW1hLVfi++YNxRv5c6oRhUw7KdHWxq7v2A/kgeBqYClZFIhKutPJ2as6Mn82t1A2
hRfkfQ6EQkdwFYXfEMVqSNh2aLjuNwzgMvNudjO1jc32y7BWJ/cdDTtgzr/6qSNH
n7gd2r5K4jfcyxx+t5inghgCr0wHtTbIWkUzL3AzxOms+9u9R0B+UNGwSk2ohYnN
KwIDAQAB
-----END PUBLIC KEY-----"""

# Parse kunci publik
key1 = RSA.import_key(pubkey1_pem)
key2 = RSA.import_key(pubkey2_pem)

n1 = key1.n
e1 = key1.e
n2 = key2.n
e2 = key2.e

print("Kunci Publik 1:")
print(f"n1 = {n1}")
print(f"e1 = {e1}")
print()
print("Kunci Publik 2:")
print(f"n2 = {n2}")
print(f"e2 = {e2}")
print()

# Cari GCD dari n1 dan n2 - ini akan memberikan faktor prima bersama
print("Mencari faktor prima bersama...")
p = math.gcd(n1, n2)

if p > 1 and p != n1 and p != n2:
    print(f"✓ Faktor prima bersama ditemukan!")
    print(f"p = {p}")
    print()
    
    # Hitung faktor prima lainnya untuk setiap kunci
    q1 = n1 // p
    q2 = n2 // p
    
    print(f"Faktor untuk kunci 1: p = {p}, q1 = {q1}")
    print(f"Faktor untuk kunci 2: p = {p}, q2 = {q2}")
    print()
    
    # Verifikasi faktoring
    assert p * q1 == n1, "Faktoring kunci 1 salah!"
    assert p * q2 == n2, "Faktoring kunci 2 salah!"
    print("✓ Faktoring terverifikasi!")
    print()
    
    # Hitung private key untuk kunci 1
    phi1 = (p - 1) * (q1 - 1)
    d1 = pow(e1, -1, phi1)
    
    print(f"Private exponent d1 = {d1}")
    print()
    
    # Baca ciphertext
    with open('ciphertext.hex', 'r') as f:
        ciphertext_hex = f.read().strip()
    
    ciphertext_int = int(ciphertext_hex, 16)
    print(f"Ciphertext (int) = {ciphertext_int}")
    print()
    
    # Dekripsi menggunakan kunci privat yang dihitung
    print("Mendekripsi ciphertext...")
    plaintext_int = pow(ciphertext_int, d1, n1)
    plaintext_bytes = long_to_bytes(plaintext_int)
    
    print(f"Plaintext (bytes): {plaintext_bytes}")
    print(f"Plaintext (string): {plaintext_bytes.decode('utf-8', errors='ignore')}")
    
else:
    print("✗ Tidak ada faktor prima bersama yang ditemukan!")
    print("Kemungkinan serangan lain diperlukan.")
