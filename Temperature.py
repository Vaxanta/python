print("========KALKULATOR SUHU========\nDibuat oleh: Axel")
print("\nOpsi dari mana dikonversi:\n1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin")

# Kumpulan function yang berisi formula
def cConvert(c):
    print("Reamur =", 4/5 * c)
    print("Fahrenheit =", 9/5 * c + 32)
    print("Kelvin =", c + 273.15)
def rConvert(r):
    print("Celcius =", 5/4 * r)
    print("Fahrenheit =", 9/4 * r + 32)
    print("Kelvin =",5/4 * r + 273.15)
def fConvert(f):
    print("Reamur =", 4/9 * (f - 32))
    print("Celcius =", 5/9 * (f - 32))
    print("Kelvin =", 5/9 * (f - 32) + 273.15)
def kConvert(k):
    print("Reamur =", 4/5 * (k - 273.15))
    print("Fahrenheit =", 9/5 * (k - 273.15) + 32)
    print("Celcius =", k - 273.15)

# Input memilih konversi
userInput = input("Ketik pilihan anda contoh(1): ")

# Proses untuk mencegah error dan proses input suhu
try :
    angka = int(userInput)
    print(angka)
    if (angka == 1):
        cConvert(float(input("Masukan suhu celcius jika menggunakan koma ganti dengan titik: ")))
    elif (angka == 2):
        rConvert(float(input("Masukan suhu reamur jika menggunakan koma ganti dengan titik: ")))
    elif (angka == 3):
        fConvert(float(input("Masukan suhu fahrenheit jika menggunakan koma ganti dengan titik: ")))
    elif (angka == 4):
        kConvert(float(input("Masukan suhu kelvin jika menggunakan koma ganti dengan titik: ")))
    else :
        print("Opsi harus 1-4")
except ValueError :
    print("Input haruslah angka saja")