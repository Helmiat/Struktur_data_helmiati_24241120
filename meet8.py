# Variabel sesuai soal
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Fungsi untuk setiap tugas
def tampilkan_data_terakhir(data):
    return data[-1]

def tampilkan_data_pertama(data):
    return data[0]

def tampilkan_data_ke3_sampai_ke6(data):
    return data[2:6]

# Pemanggilan fungsi dan output
print("=== HASIL APLIKASI DATA ===")
print("A. Data terakhir       :", tampilkan_data_terakhir(number))
print("B. Data pertama        :", tampilkan_data_pertama(number))
print("C. Data ke-3 sampai ke-6:", tampilkan_data_ke3_sampai_ke6(number))
