import math 
print("--- Program Lingkaran ---")
print("Pilih menu:")
print("1. Hitung keliling lingkaran")
print("2. Hitung luas lingkaran")
pilihan = int(input("Masukkan pilihan (1/2)"))
if pilihan == 1:
    r = float(input("Masukkan nilai jari-jari (r) lingkaran: "))
    keliling = 2 * math.pi * r
    print(f"Keliling lingkaran dengan jari-jari {r} adalah: {keliling:.2f}")
elif pilihan == 2: 
    r = float(input("Masukkan nilai jari-jari (r) lingkaran: "))
    luas = math.pi * (r ** 2)
    print(f"Keliling lingkaran dengan jari-jari {r} adalah: {luas:.2f}")
else: 
    print("Pilihan tidak valid. Silahkan jalankan ulang program dan masukkan angka 1 atau 2.")
    
