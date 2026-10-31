
"""
Modul untuk perhitungan geometri bangun datar.
"""

import math


def hitung_persegi(sisi):
    """Menghitung luas dan keliling persegi."""
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling


def hitung_persegi_panjang(panjang, lebar):
    """Menghitung luas dan keliling persegi panjang."""
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling


def hitung_segitiga(alas, tinggi, sisi_a, sisi_b):
    """Menghitung luas dan keliling segitiga."""
    luas = 0.5 * alas * tinggi
    keliling = alas + sisi_a + sisi_b
    return luas, keliling


def hitung_lingkaran(jari_jari):
    """Menghitung luas dan keliling lingkaran."""
    luas = math.pi * jari_jari ** 2
    keliling = 2 * math.pi * jari_jari
    return luas, keliling
