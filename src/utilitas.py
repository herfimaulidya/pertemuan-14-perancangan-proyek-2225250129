"""
Modul untuk fungsi pendukung program.
"""


def tampilkan_menu():
    """Menampilkan pilihan bangun datar."""
    print("\n=== KALKULATOR GEOMETRI ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("0. Keluar")


def validasi_input(nilai):
    """Memeriksa apakah input berupa angka positif."""
    try:
        angka = float(nilai)
        return angka > 0
    except ValueError:
        return False


def tampilkan_hasil(luas, keliling):
    """Menampilkan hasil perhitungan."""
    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Luas     : {luas:.2f}")
    print(f"Keliling : {keliling:.2f}")