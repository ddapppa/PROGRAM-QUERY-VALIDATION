import sqlite3
conn = sqlite3.connect('data_mahasiswa.db')

# QUERY INSERT data ke dalam tabel data_mahasiswa
conn.execute("INSERT INTO data_mahasiswa (nama, kampus, tempat_lahir, tahun_lahir, umur) VALUES ('Orangutan', 'Mamalia', 'Sumatera', 2005, 2021)")
conn.execute("INSERT INTO data_mahasiswa (nama, kampus, tempat_lahir, tahun_lahir, umur) VALUES ('Komodo', 'reptil', 'Nusa Tenggara', 2004, 2019)")
conn.execute("INSERT INTO data_mahasiswa (nama, kampus, tempat_lahir, tahun_lahir, umur) VALUES ('Anoa', 'Mamalia', 'Sulawesi', 2000, 2022)")
conn.execute("INSERT INTO data_mahasiswa (nama, kampus, tempat_lahir, tahun_lahir, umur) VALUES ('Badak Jawa', 'Mamalia', 'Jawa', 2003, 2021)")


conn.commit()
conn.close()