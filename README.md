# Labotarium Praktikum 5 
# Dictionary pada Python
Dictionary adalah struktur data pada Python yang berisi pasangan key dan value.
Setiap item disimpan dalam bentuk key:value, dan ditulis menggunakan kurung kurawal { }.

## Latihan 1 (Daftar Kontak)
### Tujuan
Mempelajari cara membuat dan menggunakan Dictionary pada Python.
Menerapkan operasi dasar Dictionary: mengakses, menambah, mengubah, menampilkan, dan menghapus data.
### Permasalahan
1. Buat dictionary berisi daftar kontak dengan ketentuan:
2. Nama sebagai key
3. Nomor telepon sebagai value
4. Lakukan operasi berikut:
5. Tampilkan kontak Ari
6. Tambah kontak Riko: 087654544
7. Ubah kontak Dina menjadi 088999776
8. Tampilkan semua nama
9. Tampilkan semua nomor
10. Tampilkan daftar nama dan nomornya
11. Hapus kontak Dina
### Penjelasan penyelesaian 
1. Dictionary dibuat menggunakan pasangan key:value.
2. Kontak Ari diakses menggunakan kontak['Ari'].
3. Penambahan dan perubahan data menggunakan kontak['key'] = value.
4. Semua nama ditampilkan dengan kontak.keys(), dan semua nomor dengan kontak.values().
### Kesimpulan
Latihan ini membantu memahami penggunaan Dictionary dalam mengelola data kontak dengan berbagai operasi seperti membaca, menambah, mengubah, dan menghapus data.


## Tugas Pratikum 5 (Nilai Data Mahasiswa)
Program ini menggunakan dictionary sebagai tempat penyimpanan data mahasiswa.
Dictionary dipilih karena bisa menyimpan data dalam bentuk key : value, sehingga mudah untuk:
1. Menambah data
2. Mengubah data
3. Menghapus data
4. Menampilkan data
5. Mencari data
Setiap mahasiswa disimpan dengan nama sebagai key dan nilai-nilai sebagai value berupa dictionary lagi
### Tujuan
1. Memahami konsep Dictionary pada Python.
2. Menggunakan Dictionary untuk menyimpan dan mengelola data.
3. Menerapkan operasi dasar dictionary: menambah, mengubah, menghapus, dan menampilkan data.
4. Membuat program daftar nilai mahasiswa dengan menu berbasis dictionary.
### Operasi yang biasa dilakukan pada Dictionary:
1. Mengakses value → dict['key']
2. Mengubah value → dict['key'] = value_baru
3. Menambah item → dict['key_baru'] = value
4. Menghapus item → del dict['key']
### Nilai akhir dihitung dari:
1. Tugas 30%
2. UTS 35%
3. UAS 35%
### Program menyediakan menu:
1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
6. Keluar
### Setiap menu bekerja dengan operasi dasar dictionary seperti:
1. dict['key'] = value (menambah/mengubah)
2. del dict['key'] (menghapus)
3. dict.items() (melihat semua data)
### Kesimpulan
Program ini mempelajari tentang:
1. Konsep dasar dictionary
2. Operasi CRUD pada dictionary
3. Menggunakan dictionary untuk menyimpan data kompleks
4. Mengimplementasikan menu program sederhana
5. Menghitung nilai akhir menggunakan rumus

### Flowchart Program (Nilai Data Mahasiswa)

```python
        ┌──────────────┐
        │   MULAI       │
        └──────┬───────┘
               │
      ┌────────▼──────────┐
      │  Tampilkan Menu    │
      └────────┬──────────┘
               │
     ┌─────────▼─────────┐
     │   Pilih Menu?      │
     └─────────┬─────────┘
               │
 ┌─────────────┼─────────────────────┐
 │             │                     │
 ▼             ▼                     ▼
Tambah      Ubah                 Hapus
Data        Data                 Data
 │           │                     │
 ▼           ▼                     ▼
Simpan   Update data         Hapus data
data     pada dictionary     dari dictionary
 │           │                     │
 └───────────┴─────────────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Tampilkan   │
                    │    Data      │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Cari Data  │
                    └──────┬──────┘
                           │
                  ┌────────▼────────┐
                  │   Kembali ke     │
                  │       Menu       │
                  └────────┬────────┘
                           │
              ┌────────────▼────────────┐
              │   Keluar (menu = 0)     │
              └────────────┬────────────┘
                           │
                      ┌────▼────┐
                      │  SELESAI │
                      └─────────┘
```

