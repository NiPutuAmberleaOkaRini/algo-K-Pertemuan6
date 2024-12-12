#Menghitung Luas dan Keliling Segitiga

#Input jari-jari lingkaran
import math
jari_jari=float(input("Masukkan jari-jari :"))

#Perhitungan luas dan keliling lingkaran
luas = (math.pi * jari_jari**2)
keliling = 2 * math.pi * jari_jari

#Menampilkan hasil yang telah dibulatkan
print("Luas lingkaran adalah :", math.ceil(luas))
print("Keliling lingkaran adalah :", math.ceil(keliling))
