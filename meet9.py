# pemisahan string
# buat program untuk memisahkan string berikut
# masukkan nama domain anda: helmiati.net
# nama domain: helmiati
# domain yang anda gunakan: net

# input dari pengguna
alamat = input("Masukkan nama domain anda: ")

# memisahkan string menggunakan titik sebagai pemisah
nama, domain = alamat.split(".")

# menampilkan hasil
print("Nama domain:", nama)
print("Domain yang anda gunakan:", domain)