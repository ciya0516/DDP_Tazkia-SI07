# buatlah sebuah list yang berisi bilangan bulat kurang dri 10
bilangan_bulat = [1,2,3,4,5,6,7,8,9]
print(bilangan_bulat)

# tambahkan dalam elemen 'hello' di akhir list
bilangan_bulat.append("Hello")
print(bilangan_bulat)

# hapus elemen ke 3 dari list dan simpan elemennya
menghapus_elemen = bilangan_bulat.pop(2)
print(menghapus_elemen)
print(bilangan_bulat)

# tugas 1. buat variabel dengan velue

kendaraan = ['beat karbu', 'motor', 200, 'pink', 3]
print(kendaraan)

kendaraan.append('10 jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

# Tugas 2.
angka_pilihan = int(input("""Masukkan Pilihan: 
                          1. Menghitung Luas Persegi
                          2. Menghitunng Luas Lingkaran
                          3. Menghitung Luas Segitiga
                          """))

match angka_pilihan:
    case 1:
        print("menghitung luas persegi")
        s = int(input("masukan nilai sisi: "))
        luas_persegi = s * s
        print(f"luas persegi dengan sisi (s) adalah (luas persegi)")
    case 2:
       print("menghitung luas lingkaran")
       pi = 3.14
       r = int(input("masukan nilai jari jari"))
       luaslingkaran = pi * r**2
       print(f"luas lingkaran dengan jari jari{r} adalah {luaslingkaran}")
    case 3:
        print("menghitung luas segitiga")
        alas = int(input("masukan nilai alas: "))
        tinggi = int(input("masukan nilai tinggi: "))
        luassegitiga = 1/2 *alas *tinggi
        print(f"luas segitiga dengan alas {alas} dan tinggi adalah {luassegitiga}")
    case _:
        print("input tidak valid")         