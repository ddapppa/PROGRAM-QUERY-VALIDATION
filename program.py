# import sqlite
import sqlite3
koneksi = sqlite3.connect('data_mahasiswa.db')
kursor = koneksi.cursor()

# Fungsi buatTabel()
def buatTabel():
    koneksi.execute('''CREATE TABLE IF NOT EXISTS data_mahasiswa(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama VARCHAR,
                    kampus VARCHAR,
                    tempat_lahir VARCHAR,
                    tahun_lahir INTEGER,
                    umur INTEGER 
                    )''')
    koneksi.commit()

# Fungsi tambahData()
def tambahData(nama, kampus, tempat_lahir, tahun_lahir, umur):
    koneksi.execute(''' INSERT INTO data_mahasiswa (nama, kampus, tempat_lahir, tahun_lahir, umur)
                      VALUES (?,?,?,?,?)''', (nama, kampus, tempat_lahir, tahun_lahir, umur))
    koneksi.commit()

# Fungsi tampilSemuaData()
def tampilSemuaData():
    kursor.execute("SELECT * FROM data_mahasiswa")
    baris_tabel = kursor.fetchall()

    # buat format tabel
    print("BIODATA MAHASISWA BARU 2024")
    print("="*110)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","NAMA","KAMPUS","TEMPAT LAHIR","TAHUN_LAHIR","UMUR"))
    print("-"*110)
    # tampilkan data dengan perulangan for
    for baris in baris_tabel:
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

# Fungsi mamaliadansumatera()
def mamaliadansumatera():
    kursor.execute("SELECT * FROM data_mahasiswa WHERE kampus = 'Mamalia' AND tempat_lahir = 'Sumatera'")
    baris_tabel_mamalia = kursor.fetchall()

    # buat format tabel
    print("\nData Mamalia di Sumatera:")
    print("="*110)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","NAMA","KAMPUS","TEMPAT LAHIR","TAHUN_LAHIR","UMUR"))
    print("-"*110)
    # tampilkan data dengan perulangan for
    for baris in baris_tabel_mamalia:
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

def umurkurangdari18():
    kursor.execute("SELECT * FROM data_mahasiswa WHERE umur <= 18 ")
    baris_table_umur = kursor.fetchall()

    print("\nData kurang atau sama dengan 18:")
    print("="*110)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","NAMA","KAMPUS","TEMPAT LAHIR","TAHUN_LAHIR","UMUR"))
    print("-"*110)
    # tampilkan data dengan perulangan for
    for baris in baris_table_umur:
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
def urutanumur():
    kursor.execute("SELECT * FROM data_mahasiswa ORDER BY tahun_lahir ASC") #ASC|DESC
    baris_table_urutanlahir = kursor.fetchall()


    print("\nData kurang atau sama dengan 18:")
    print("="*110)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","NAMA","KAMPUS","TEMPAT LAHIR","TAHUN_LAHIR","UMUR"))
    print("-"*110)
    # tampilkan data dengan perulangan for
    for baris in baris_table_urutanlahir:
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

def pencarian():
    nama = 'd%'  # Mencari nama yang dimulai dengan 'John'
    kursor.execute(f"SELECT * FROM data_mahasiswa WHERE nama LIKE ?", (nama,))
    baris_table_pencarian = kursor.fetchall()

    print("\nData pencarian D:")
    print("="*110)
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","NAMA","KAMPUS","TEMPAT LAHIR","TAHUN_LAHIR","UMUR"))
    print("-"*110)
    # tampilkan data dengan perulangan for
    for baris in baris_table_pencarian:
        print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))


# Fungsi untuk memperbarui data berdasarkan ID
def updateData(id, nama, kampus, tempat_lahir, tahun_lahir, umur):
    koneksi.execute('''UPDATE data_mahasiswa
                    SET nama = ?, kampus = ?, tempat_lahir = ?, tahun_lahir = ?, umur = ?
                    WHERE id = ?''', (nama, kampus, tempat_lahir, tahun_lahir, umur, id))
    koneksi.commit()

# Fungsi untuk menghapus data berdasarkan ID
def hapusData(id):
    koneksi.execute('''DELETE FROM data_mahasiswa WHERE id = ?''', (id,))
    koneksi.commit()

# Fungsi untuk validasi tipe data
def validasiData(nama, kampus, tempat_lahir, tahun_lahir, umur):
    if not all(map(str.isalpha, nama.split())):
        print("Nama harus terdiri dari huruf saja.")
        return False
    if not all(map(str.isalpha, kampus.split())):
        print("Nama kampus harus terdiri dari huruf saja.")
        return False
    if not all(map(str.isalpha, tempat_lahir.split())):
        print("Tempat lahir harus terdiri dari huruf saja.")
        return False
    if not tahun_lahir.isdigit() or len(tahun_lahir) != 4:
        print("Tahun lahir harus berupa angka 4 digit.")
        return False
    try:
        umur = int(umur)
        if umur < 0:
            print("Umur harus merupakan bilangan bulat positif.")
            return False
        return True
    except ValueError:
        print("Umur harus berupa bilangan bulat.")
        return False

# ================================
# ========= MAIN PROGRAM =========
# ================================
# Panggil fungsi buatTabel untuk membuat tabel jika belum ada
buatTabel()

# Menampilkan list menu program
while True:
    print("\nPROGRAM INPUT DATA MAHASISWA 2024:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    print("6. mamalia dan sumatera")
    print("7. kurang dari 18")
    print("8. urutan umur")
    print("9. pencarian nama depan D")

    pilihan = input("Pilih operasi yang diinginkan (1/2/3/4/5/6/7/8/9): ")

    if pilihan == '1':
        nama = input("Masukkan nama: ")
        kampus = input("Masukkan nama kampus: ")
        tempat_lahir = input("Masukkan tempat lahir: ")
        tahun_lahir = input("Masukkan tahun lahir (YYYY): ")
        umur = input("Masukkan umur: ")

        if validasiData(nama, kampus, tempat_lahir, tahun_lahir, umur):
            tambahData(nama, kampus, tempat_lahir, int(tahun_lahir), int(umur))
            print("Data berhasil ditambahkan.")

    elif pilihan == '2':
        print("\nData:")
        tampilSemuaData()

    elif pilihan == '3':
        id = input("Masukkan ID mahasiswa yang ingin diupdate: ")
        nama = input("Masukkan nama baru: ")
        kampus = input("Masukkan nama kampus baru: ")
        tempat_lahir = input("Masukkan tempat lahir baru: ")
        tahun_lahir = input("Masukkan tahun lahir baru (YYYY): ")
        umur = input("Masukkan umur baru: ")

        if validasiData(nama, kampus, tempat_lahir, tahun_lahir, umur):
            updateData(int(id), nama, kampus, tempat_lahir, int(tahun_lahir), int(umur))
            print("Data berhasil diupdate.")

    elif pilihan == '4':
        id = input("Masukkan ID mahasiswa yang ingin dihapus: ")
        hapusData(int(id))
        print("Data berhasil dihapus.")

    elif pilihan == '5':
        print("Program selesai.")
        break

    elif pilihan == '6':
        mamaliadansumatera()

    elif pilihan == '7':
        umurkurangdari18()

    elif pilihan == '8':
        urutanumur()

    elif pilihan == '9':
        pencarian()

    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
