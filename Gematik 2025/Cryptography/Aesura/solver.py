import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from itertools import permutations

data = bytes.fromhex(open("seal.txt", "r").read().strip())
L, R, P = "asdf", "jkl;", b'Gematik2025{'

for i in permutations(L):
    for j in permutations(R):
        for x in permutations(L):
            for y in permutations(R):
                k = ("".join(f"{a}{b}" for a,b in zip(i,j)) + 
                     "".join(f"{a}{b}" for a,b in zip(x,y))).encode()
                
                pt = AES.new(k, AES.MODE_ECB).decrypt(data)

                if pt.startswith(P):
                    try:
                        print(f"Key: {k.decode()}\nFlag: {unpad(pt, 16).decode()}")
                        sys.exit(0)
                    except ValueError:
                        pass
