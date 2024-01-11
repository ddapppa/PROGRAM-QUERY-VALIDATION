import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('data_mahasiswa.db')
qqqq

# Menjalankan query SELECT dengan ORDER BY
# AND harus dua-duanya terpenuhi
kursor.execute(f"SELECT * FROM data_mahasiswa WHERE kampus = 'Mamalia' AND tempat_lahir = 'Sumatera'")
baris_table = kursor.fetchall()

print("Data Hewan:")
print("=============================================================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan", " ""nama_hewan", "jenis", "asal", "jml_sekarang", "thn_ditemukan"))
print("-----------------------------------------------------------------------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()