#!/usr/bin/env python3
import socket
import sys

HOST = '217.216.111.220'
PORT = 2738
PTEXT = b'A' * 50

def xor(b1, b2):
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])

def ru(s, prompt):
    buf = b""
    while prompt not in buf:
        chunk = s.recv(1024)
        if not chunk: raise EOFError("Connection closed")
        buf += chunk

def r_all(s):
    buf = b""
    while True:
        chunk = s.recv(1024)
        if not chunk: break
        buf += chunk
    return buf

try:
    # --- Get Key ---
    with socket.create_connection((HOST, PORT), timeout=3) as s:
        ru(s, b'Masukkan pilihan: ') # Server prompt (must be Indonesian)
        s.sendall(b'1\n')
        ru(s, b'Masukkan pesan yang ingin kamu enkripsi: ') # Server prompt
        s.sendall(PTEXT + b'\n')
        resp = r_all(s).split(b'Pesan terenkripsi kamu: ')[-1].strip() # Server prompt
        key = xor(bytes.fromhex(resp.decode()), PTEXT)

    # --- Get Secret ---
    with socket.create_connection((HOST, PORT), timeout=3) as s:
        ru(s, b'Masukkan pilihan: ') # Server prompt
        s.sendall(b'2\n')
        resp = r_all(s).split(b'Secret-nya adalah: ')[-1].strip() # Server prompt
        enc_secret = bytes.fromhex(resp.decode())

    # --- Decrypt ---
    flag = xor(enc_secret, key).decode()
    print(f"\nFLAG: {flag}\n")
    
    if not flag.startswith("Gematik2025{"):
        print("[!] Wrong flag format. Try running again.", file=sys.stderr)

except Exception as e:
    print(f"\n[!] Failed: {e}", file=sys.stderr)
