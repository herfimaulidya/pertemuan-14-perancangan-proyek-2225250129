# PROPOSAL PROYEK

## 1. Judul Proyek

Kalkulator Geometri Bangun Datar Berbasis Python

## 2. Latar Belakang

Geometri merupakan salah satu materi dalam matematika yang mempelajari bentuk, ukuran, luas, dan keliling bangun datar. Dalam pembelajaran matematika, peserta didik sering melakukan perhitungan luas dan keliling berbagai bangun datar.

Untuk membantu proses pembelajaran dan mempermudah perhitungan, diperlukan sebuah program sederhana yang dapat menghitung luas dan keliling bangun datar secara otomatis. Oleh karena itu, proyek ini dirancang untuk membuat Kalkulator Geometri berbasis Python yang dapat dijalankan melalui terminal.

## 3. Pengguna dan Tujuan

**Pengguna:**
- Siswa yang sedang mempelajari materi geometri.
- Guru matematika sebagai media pendukung pembelajaran.

**Tujuan:**
- Membantu pengguna menghitung luas dan keliling bangun datar.
- Mempermudah proses perhitungan geometri.
- Menerapkan konsep algoritma dan pemrograman Python dalam permasalahan matematika.

## 4. Ruang Lingkup

**Fitur wajib:**
1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Memvalidasi input agar sesuai dengan ketentuan perhitungan.

**Batasan proyek:**
- Program menggunakan bahasa Python.
- Program dijalankan melalui terminal atau console.
- Perhitungan dibatasi pada empat jenis bangun datar.
- Input ukuran bangun harus berupa bilangan positif.

## 5. Kebutuhan

### A. Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Menampilkan pilihan jenis bangun datar. | Wajib |
| F02 | Menerima input ukuran bangun datar. | Wajib |
| F03 | Menghitung luas bangun datar. | Wajib |
| F04 | Menghitung keliling bangun datar. | Wajib |
| F05 | Memvalidasi input pengguna. | Wajib |
| F06 | Menampilkan hasil perhitungan. | Wajib |

### B. Kebutuhan Nonfungsional

- Program mudah dijalankan melalui terminal VS Code.
- Tampilan hasil perhitungan mudah dipahami.
- Nama fungsi dan variabel menggunakan istilah yang jelas.
- Program memberikan pesan kesalahan jika input tidak valid.

## 6. Input, Proses, dan Output (IPO)

| Input | Proses | Output |
|---|---|---|
| Pilihan bangun datar | Memeriksa pilihan pengguna | Jenis bangun datar |
| Panjang sisi | Menghitung luas dan keliling persegi | Luas dan keliling persegi |
| Panjang dan lebar | Menghitung luas dan keliling persegi panjang | Luas dan keliling persegi panjang |
| Alas, tinggi, dan sisi segitiga | Menghitung luas dan keliling segitiga | Luas dan keliling segitiga |
| Jari-jari lingkaran | Menghitung luas dan keliling lingkaran | Luas dan keliling lingkaran |

## 7. Algoritma

Pseudocode program:

MULAI

1. Tampilkan menu pilihan bangun datar.
2. Pengguna memilih jenis bangun datar.
3. Jika pilihan adalah 0, tampilkan pesan terima kasih dan akhiri program.
4. Jika pilihan tidak tersedia, tampilkan pesan kesalahan dan kembali ke menu utama.
5. Jika pilihan tersedia:
   - Minta input ukuran bangun datar.
   - Validasi input yang diberikan.
   - Jika input tidak valid, tampilkan pesan kesalahan dan minta input kembali.
   - Jika input valid, hitung luas dan keliling sesuai rumus.
6. Tampilkan hasil perhitungan.
7. Kembali ke menu utama.

SELESAI

## 8. Struktur Program

Program dibagi menjadi beberapa fungsi dan modul:

| Fungsi/Modul | Tanggung Jawab |
|---|---|
| tampilkan_menu() | Menampilkan menu pilihan bangun datar. |
| hitung_persegi() | Menghitung luas dan keliling persegi. |
| hitung_persegi_panjang() | Menghitung luas dan keliling persegi panjang. |
| hitung_segitiga() | Menghitung luas dan keliling segitiga. |
| hitung_lingkaran() | Menghitung luas dan keliling lingkaran. |
| validasi_input() | Memeriksa apakah input berupa angka positif. |
| tampilkan_hasil() | Menampilkan hasil perhitungan luas dan keliling. |
| minta_angka() | Meminta dan memvalidasi input ukuran dari pengguna. |
| main() | Mengatur alur utama program. |

**Struktur folder:**

```text
pertemuan-14-perancangan-proyek-2225250129/
├── data/
│   └── data_contoh.txt
├── output/
│   └── .gitkeep
├── src/
│   ├── geometri.py
│   ├── main.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── bug_log.md
├── .gitignore
├── proposal.md
└── README.md

## 9. Struktur Data

Struktur data dan tipe data yang digunakan:

- **Float:** Menyimpan ukuran bangun datar dan hasil perhitungan.
- **String:** Menyimpan pilihan menu dan input dari pengguna.
- **Tuple:** Mengembalikan dua nilai berupa luas dan keliling dari fungsi perhitungan.

Struktur data tersebut digunakan untuk mendukung proses input, perhitungan, dan penampilan hasil program.

## 10. Test Case

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Persegi, sisi 5 | Luas 25 dan keliling 20 |
| TC02 | Normal | Persegi panjang, panjang 8 dan lebar 4 | Luas 32 dan keliling 24 |
| TC03 | Normal | Segitiga, alas 6, tinggi 4, sisi lainnya 5 dan 5 | Luas 12 dan keliling 16 |
| TC04 | Normal | Lingkaran, jari-jari 5 | Luas sekitar 78,54 dan keliling sekitar 31,42 |
| TC05 | Batas | Persegi, sisi 0 | Ditolak karena ukuran harus positif |
| TC06 | Invalid | Pilihan bangun datar tidak tersedia | Menampilkan pesan kesalahan |
| TC07 | Invalid | Input ukuran berupa huruf | Menampilkan pesan kesalahan |

## 11. Pembagian Tugas

Proyek ini dikerjakan secara individu. Seluruh tahapan pengerjaan dilakukan oleh satu orang, mulai dari perencanaan, implementasi program, pengujian, hingga dokumentasi.

| No. | Tahapan | Tanggung Jawab |
|---|---|---|
| 1 | Perencanaan | Menyusun proposal dan rancangan proyek. |
| 2 | Pemrograman | Mengembangkan fitur perhitungan geometri dan validasi input. |
| 3 | Pengujian | Menyusun dan menjalankan test case serta mencatat hasil pengujian. |
| 4 | Dokumentasi | Menyusun README, proposal, dan bug log. |
| 5 | Pengelolaan Proyek | Mengelola repository dan riwayat perubahan menggunakan Git dan GitHub. |

## 12. Jadwal

| Waktu | Target |
|---|---|
| Pertemuan 14 | Penyusunan proposal, algoritma, struktur program, dan test case. |
| Antara P14–P15 | Implementasi awal fitur wajib. |
| Pertemuan 15 | Integrasi program, testing, debugging, dan dokumentasi. |
| Pertemuan 16 | Presentasi, demonstrasi, dan evaluasi proyek. |

## 13. Repository

Repository GitHub:

URL: (https://github.com/herfimaulidya/pertemuan-14-perancangan-proyek-2225250129)
