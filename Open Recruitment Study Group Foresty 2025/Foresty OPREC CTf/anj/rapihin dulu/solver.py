# 1. Ini adalah data target dari output Anda
the_flag = [1423, 1432, 1403, 1422, 1404, 1405, 1410, 1444, 1436, 1437, 1450, 1437, 1458, 1452, 1416, 1450, 1463, 1450, 1461, 1442, 1436, 1458, 1436, 1416, 1458, 1437, 1416, 1458, 1436, 1416, 1450, 1455, 1372, 1369, 1452, 1453, 1446]

# 2. Kita akan membangun flag yang sudah dipecahkan di sini
solved_flag = ""

# 3. Loop melalui setiap angka (y) di 'the_flag'
for y in the_flag:
    # 4. Terapkan rumus pembalik yang kita temukan
    # x = chr((y - 1337) ^ 16)
    
    original_ord_value = (y - 1337) ^ 16
    
    # 5. Tambahkan karakter yang ditemukan ke string kita
    solved_flag += chr(original_ord_value)

# 6. Cetak hasilnya
print("Password/Flag yang ditemukan:")
print(solved_flag)
