from bangun_datar import BangunDatar
from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang (19, 2)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(12, 2)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas bangun_datar')
b1 = BangunDatar()
print(b1.info())
print(b1.hitung_luas())

print('\nPolymorphism')
daftar_bangun_datar = []
daftar_bangun_datar.append(p1)
daftar_bangun_datar.append(s1)

for bangun_datar in daftar_bangun_datar :
    print(bangun_datar.info())