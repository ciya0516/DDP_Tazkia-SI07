# 1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) 
# input
nama = 'Tazkiah Badzlina'
nim = '0110124102'
rombel = 'SI07'
no_telp = '628567370716'
alamat = 'Srengseng sawah, Kota Jakarta Selaran, Jagakarsa, DKI Jakarta'

print ('nama saya adalah:', nama)
print ('nim saya adalah:', nim)
print ('rombel saya adalah:', rombel)
print ('nomor telepon saya adalah:', no_telp)
print ('alamat saya adalah:', alamat)
print ('======================')

# 2. Buat seperti no 1 tapi 1 nama teman kalian 
# input
nama = 'Regista Cahyani'
nim = '0110124200'
rombel = 'SI07'
no_telp = '6285778220402'
alamat = 'jl.kramat benda x rt.03 rw.027'

print ('nama saya adalah:', nama)
print ('nim saya adalah:', nim)
print ('rombel saya adalah:', rombel)
print ('nomor telepon saya adalah:', no_telp)
print ('alamat saya adalah:', alamat)
print ('======================')

# 3. Buat program python untuk mencari nilai berat badan ideal 
# input 
TinggiBadan = int(input(" Masukkan tinggi badan : "))
BeratBadan_ideal= (TinggiBadan - 110) + ((TinggiBadan- 100) *0.15) 

print ('berat badan ideal adalah :', BeratBadan_ideal)
print ('======================')

# 4. Buat program python untuk mencari nilai konversi dari celcius ke fahreinheit 
# input
celcius = int(input('masukan celcius : '))
fahreinheit = (celcius * 9/5) + 32

print ('jadi fahreinheit dari celcius adalah' , fahreinheit)
print ('======================')

# 5. buat program python untuk mencari luas dan keliling tabung.
# input
jarijari = int(input('masukan jari jari tabung: '))
keliling = (2*22/7*jarijari)

print('jadi keliling lingkaran adalah:', keliling)
print ('======================')

jarijari = int(input('masukan jari jari tabung: '))
tinggi = int(input('masukan tinggi tabung: '))
luas = (2*22/7*jarijari+tinggi)

print('jadi luas permukaan tabung adalah:', luas)
print ('======================')