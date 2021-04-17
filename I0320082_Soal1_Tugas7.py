str = "Program Menghitung Jumlah Pesanan Makanan"
s = str.center(61,'*')
print(s)

nama_pemesan = input("Nama pemesan :")
print("Selamat datang", nama_pemesan)

print("\nMenu makanan : NASI GORENG , BAKSO, SATE")
str = input("Masukkan menu makanan yang dipesan dengan menuliskan menu sebanyak jumlah yang dipesan :")
pesanan =str.upper()
print("Pesanan: ", pesanan)

str = pesanan
a = str.count('NASI GORENG')
b = str.count('BAKSO')
c = str.count('SATE')
print("JUMLAH BAKSO: ", a)
print("JUMLAH MIE AYAM: ", b)
print("JUMLAH SOTO: ", c)
