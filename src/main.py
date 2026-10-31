"""
Program Kalkulator Geometri Bangun Datar.
File utama untuk menjalankan program.
"""

from geometri import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran,
)
from utilitas import tampilkan_menu, validasi_input, tampilkan_hasil


def minta_angka(pesan):
    """Meminta input angka positif dari pengguna."""
    while True:
        nilai = input(pesan)

        if validasi_input(nilai):
            return float(nilai)

        print("Input tidak valid. Masukkan angka yang lebih besar dari 0.")


def main():
    """Fungsi utama program."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun datar (0-4): ")

        if pilihan == "0":
            print("Terima kasih telah menggunakan Kalkulator Geometri!")
            break

        elif pilihan == "1":
            sisi = minta_angka("Masukkan panjang sisi: ")
            luas, keliling = hitung_persegi(sisi)

        elif pilihan == "2":
            panjang = minta_angka("Masukkan panjang: ")
            lebar = minta_angka("Masukkan lebar: ")
            luas, keliling = hitung_persegi_panjang(panjang, lebar)

        elif pilihan == "3":
            alas = minta_angka("Masukkan panjang alas: ")
            tinggi = minta_angka("Masukkan tinggi: ")
            sisi_a = minta_angka("Masukkan panjang sisi pertama: ")
            sisi_b = minta_angka("Masukkan panjang sisi kedua: ")
            luas, keliling = hitung_segitiga(alas, tinggi, sisi_a, sisi_b)

        elif pilihan == "4":
            jari_jari = minta_angka("Masukkan panjang jari-jari: ")
            luas, keliling = hitung_lingkaran(jari_jari)

        else:
            print("Pilihan tidak tersedia. Silakan pilih angka 0-4.")
            continue

        tampilkan_hasil(luas, keliling)


if __name__ == "__main__":
    main()