print("--- Mencari Angka Terbesar dari 2 Angka ---")
angka1 = float(input("Masukkan angka pertama:"))
angka2 = float(input("Masukkan angka kedua:"))
if angka1 > angka2:
    maksimal = angka1
    print(f"Angka maksimal adalah: {maksimal}")
elif angka2  > angka1:
    maksimal = angka2
    print(f"Angka maksimal adalah: {maksimal}")
else:
    print("Kedua angka bernilai sama.")
