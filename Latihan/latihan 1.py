# Dictionary daftar kontak
kontak = {
    'Ari': '081267888',
    'Dina': '087677776',
    'Budi': '081333221'
}

# Tampilkan kontak Ari
print("Kontak Ari: ", kontak['Ari'])

# Tambah kontak Riko
kontak['Riko'] = '087654544'

# Ubah kontak Dina
kontak['Dina'] = '088999776'

# Tampilkan semua Nama
print("Nama: ", kontak.keys())

# Tampilkan semua Nomor
print("Nomor: ", kontak.values())

# Tampilkan daftar Nama dan Nomor
print("Daftar Kontak:")
for item in kontak.items():
    print(item[0], ":", item[1])

# Hapus kontak Dina
del kontak['Dina']

print("Kontak setelah Dina dihapus: ", kontak)
