print("===== RUMAH SAKIT HARAPAN =====")
print("DAFTAR PASIEN RAWAT INAP")

pasien = [
    "Andi", "Budi", "Citra", "Dina", "Eka",
    "Fajar", "Gita", "Hani", "Indra", "Joko"
]

for i, nama in enumerate(pasien, start=1):
    print(i, ".", nama)

pilihan = int(input("\nPilih nomor pasien: "))

if pilihan >= 1 and pilihan <= 10:
    nama = pasien[pilihan - 1]

    print("\nNama pasien:", nama)

    lama = int(input("Lama rawat inap (hari): "))
    kelas = int(input("Pilih kelas kamar (1-3): "))

    if kelas == 1:
        biaya = 500000
        nama_kelas = "VIP"
    elif kelas == 2:
        biaya = 300000
        nama_kelas = "Kelas 1"
    elif kelas == 3:
        biaya = 200000
        nama_kelas = "Kelas 2"
    else:
        biaya = 0
        nama_kelas = "Tidak tersedia"

    if lama <= 0:
        print("Lama rawat inap tidak valid.")
    elif biaya == 0:
        print("Pilihan kelas tidak tersedia.")
    else:
        total = lama * biaya

        print("\n===== DATA RAWAT INAP =====")
        print("Nama pasien:", nama)
        print("Kelas kamar:", nama_kelas)
        print("Lama rawat:", lama, "hari")
        print("Total biaya: Rp", total)

        if lama >= 7:
            print("Status: Rawat inap jangka panjang")
        elif lama >= 3:
            print("Status: Rawat inap sedang")
        else:
            print("Status: Rawat inap singkat")

        if total >= 3000000:
            print("Kategori biaya: Tinggi")
        else:
            print("Kategori biaya: Normal")
else:
    print("Nomor pasien tidak ditemukan.")