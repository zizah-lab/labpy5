# Program Daftar Nilai Mahasiswa (Dictionary)

data = {}

while True:
    print("\n=== Menu ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    # Tambah Data
    if menu == "1":
        nama = input("Nama   : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))

        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        data[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': akhir
        }

        print("Data berhasil ditambah.")

    # Ubah Data
    elif menu == "2":
        nama = input("Nama yang akan diubah: ")
        if nama in data:
            tugas = float(input("Nilai Tugas baru : "))
            uts = float(input("Nilai UTS baru   : "))
            uas = float(input("Nilai UAS baru   : "))
            akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

            data[nama] = {
                'tugas': tugas,
                'uts': uts,
                'uas': uas,
                'akhir': akhir
            }

            print("Data berhasil diubah.")
        else:
            print("Data tidak ditemukan.")

    # Hapus Data
    elif menu == "3":
        nama = input("Nama yang akan dihapus: ")
        if nama in data:
            del data[nama]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    # Tampilkan Data
    elif menu == "4":
        print("\n=== Daftar Nilai Mahasiswa ===")
        print("Nama | Tugas | UTS | UAS | Akhir")
        for item in data.items():
            nama = item[0]
            nilai = item[1]
            print(nama, "|", nilai['tugas'], "|", nilai['uts'], "|", nilai['uas'], "|", nilai['akhir'])

    # Cari Data
    elif menu == "5":
        nama = input("Masukkan nama yang dicari: ")
        if nama in data:
            nilai = data[nama]
            print("Data ditemukan:")
            print("Tugas:", nilai['tugas'])
            print("UTS  :", nilai['uts'])
            print("UAS  :", nilai['uas'])
            print("Akhir:", nilai['akhir'])
        else:
            print("Data tidak ditemukan.")

    elif menu == "0":
        break

    else:
        print("Menu tidak tersedia.")
