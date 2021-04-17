print("=====Program menentukan nilai max dan min dari nilai akar kuadrat bilangan yang dibulatkan ke atas=====")

import math
r = float(input("Masukkan bilangan pertama : "))
s = float(input("Masukkan bilangan kedua : "))
t = float(input("Masukkan bilangan ketiga : "))
bilangan_pertama = math.sqrt(r)
bilangan_kedua = math.sqrt(s)
bilangan_ketiga = math.sqrt(t)
print("\nnilai akar kuadrat dari bilangan pertama= ", bilangan_pertama)
print("nilai akar kuadrat dari bilangan kedua= ", bilangan_kedua)
print("nilai akar kuadrat dari bilangan ketiga= ", bilangan_ketiga)

import math
pembulatan_pertama = math.ceil(bilangan_pertama)
pembulatan_kedua = math.ceil(bilangan_kedua)
pembulatan_ketiga = math.ceil(bilangan_ketiga)
print("\npembulatan dari nilai akar kuadrat pertama: ", pembulatan_pertama)
print("pembulatan dari nilai akar kuadrat kedua: ", pembulatan_kedua)
print("pembulatan dari nilai akar kuadrat ketiga: ", pembulatan_ketiga)

import math
print("\nhasil pembulatan nilai akar kuadrat pertama= ", pembulatan_pertama)
print("hasil pembulatan nilai akar kuadrat kedua= ", pembulatan_kedua)
print("hasil pembulatan nilai akar kuadrat ketiga= ", pembulatan_ketiga)
print("nilai max hasil pembulatan= ", max(pembulatan_pertama,pembulatan_kedua,pembulatan_ketiga))
print("nilai min hasil pembulatan= ", min(pembulatan_pertama,pembulatan_kedua,pembulatan_ketiga))
