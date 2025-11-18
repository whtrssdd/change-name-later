enc = (
    b"\x0a\x2e\x52\x92\x28\x27\x4b\xb6\xe3\x44\xad\x4c\xc3\x7f\x96\xf4"
    b"\xa4\x5e\xfc\x9b\x74\x47\x68\xb1\x0b\x0c\xdb\x0c\x48\x60\xc1\x7a"
    b"\xcb\xf7\x4b\x9d\xb2\xa9\xe4\x3c\x99\x16\x2b\xb8"
)

seed = 0xDEADBEEFCAFEBABE
flag = bytearray()

for byte in enc:
    seed = ((seed << 0xD) ^ seed) & 0xFFFFFFFFFFFFFFFF
    seed = (seed ^ (seed >> 0x7)) & 0xFFFFFFFFFFFFFFFF
    seed = (seed ^ (seed << 0x11) ^ 0x9E3779B97F4A7C15) + 0x123456789ABCDEF
    seed &= 0xFFFFFFFFFFFFFFFF
    flag.append(byte ^ (seed & 0xFF))

print(flag.decode())
 
