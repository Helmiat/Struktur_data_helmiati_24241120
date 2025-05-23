# Input teks dari pengguna
teks = input("Masukkan teks (misalnya: bima soromandi a): ")

# Menghilangkan spasi dan ubah ke huruf kecil
teks_bersih = teks.replace(" ", "").lower()

# Menghitung dan menampilkan setiap huruf
print("Jumlah kemunculan setiap huruf:")
for huruf in sorted(set(teks_bersih)):
    jumlah = teks_bersih.count(huruf)
    print(f"Huruf '{huruf}' muncul {jumlah} kali")



    # Input tempat tinggal
tempat_tinggal = input("Masukkan tempat tinggal anda: ")
jumlah_huruf_tempat = len(tempat_tinggal)
print("Jumlah huruf pada tempat tinggal:", jumlah_huruf_tempat)

# Input password
password = input("Masukkan password: ")
jumlah_huruf_password = len(password)
print("Jumlah huruf pada password:", jumlah_huruf_password)

# Validasi panjang password
if jumlah_huruf_password < 8:
    print("Password kurang panjang")
else:
    print("Password diterima")