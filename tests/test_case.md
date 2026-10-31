# TEST CASE KALKULATOR GEOMETRI

## 1. Pengujian Normal

| ID | Input | Expected Result |
|---|---|---|
| TC01 | Persegi, sisi = 5 | Luas = 25, keliling = 20 |
| TC02 | Persegi panjang, panjang = 8, lebar = 4 | Luas = 32, keliling = 24 |
| TC03 | Segitiga, alas = 6, tinggi = 4, sisi = 5 dan 5 | Luas = 12, keliling = 16 |
| TC04 | Lingkaran, jari-jari = 5 | Luas sekitar 78,54, keliling sekitar 31,42 |

## 2. Pengujian Batas

| ID | Input | Expected Result |
|---|---|---|
| TC05 | Persegi, sisi = 0 | Input ditolak karena ukuran harus positif |

## 3. Pengujian Invalid

| ID | Input | Expected Result |
|---|---|---|
| TC06 | Memilih bangun datar yang tidak tersedia | Program menampilkan pesan kesalahan |
| TC07 | Memasukkan huruf sebagai ukuran bangun | Program menampilkan pesan kesalahan |

## Kesimpulan

Pengujian dilakukan untuk memastikan perhitungan luas dan keliling berjalan sesuai rumus matematika serta program dapat menangani input yang tidak valid.