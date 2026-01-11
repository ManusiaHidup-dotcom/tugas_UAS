import streamlit as st
import pandas as pd

# membuat list
angka = [10, 20, 30, 40, 50]

# menampilkan seluruh isi list
print("Isi list:", angka)

# mengambil satu data
print("Data pertama:", angka[0])
print("Data terakhir:", angka[-1])

# menambah data ke list
angka.append(60)
print("Setelah tambah data:", angka)

# mengubah data
angka[2] = 35
print("Setelah ubah data ke 3:", angka)

# menghapus data
angka.remove(20)
print("Setelah hapus 20:", angka)

# menghitung jumlah data
print("Jumlah data:", len(angka))

# menjumlahkan semua isi list
total = sum(angka)
print("Total isi list:", total)

# menampilkan list dengan perulangan
print("Isi list satu per satu:")
for x in angka:
    print(x)
