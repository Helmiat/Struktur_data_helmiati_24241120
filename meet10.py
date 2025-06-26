# Data harga
harga_normal = 15.5935
harga_diskon = 16.45987
harga_retail = 14.96884

# Ambil 1 digit di belakang koma
satu_digit_normal = int((harga_normal * 10) % 10)
satu_digit_diskon = int((harga_diskon * 10) % 10)
satu_digit_retail = int((harga_retail * 10) % 10)

# Ambil 2 digit di belakang koma
dua_digit_normal = int((harga_normal * 100) % 100)
dua_digit_diskon = int((harga_diskon * 100) % 100)
dua_digit_retail = int((harga_retail * 100) % 100)

# Tampilkan hasil
print("Satu digit di belakang koma:")
print("harga_normal:", satu_digit_normal)
print("harga_diskon:", satu_digit_diskon)
print("harga_retail:", satu_digit_retail)

print("\nDua digit di belakang koma:")
print("harga_normal:", dua_digit_normal)
print("harga_diskon:", dua_digit_diskon)
print("harga_retail:", dua_digit_retail)