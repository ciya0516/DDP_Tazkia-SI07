# 1. Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.
print('## 1. program bilangan ganjil genap ##')
print('======================')

#input bilangan
bilangan = int(input('masukkan bilangan anda: '))

if bilangan % 2 == 0:
    print(bilangan,'merupakan bilangan genap')
else:
    print(bilangan, 'merupakan bilangan ganjil')
print('======================')

# 2. Buatlah program yang meminta pengguna untuk memasukkan nilai ujian. Jika nilai lebih besar atau sama dengan 75, cetak "Lulus". Jika tidak, cetak "Tidak Lulus". Gunakan if dan if else.
print('## 2. program menentukan nilai ujian')
print('======================')

# input nilai
nilai_ujian = int(input('masukkan nila anda: '))

# proses dan output
if nilai_ujian >= 75:
    print('kamu dinyatakan LULUS')
else:
    print('kamu dinyatakan TDAK LULUS')
print('======================')
    
# 3. Buatlah program yang meminta pengguna untuk memasukkan usia. Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.
print('## 3. program menentukan usia dan status ##')
print('======================')

# input usia
usia =int(input('masukkan usia anda: '))

if usia >= 18:
    print('kamu dewasa')
elif usia >= 13 and usia <=17:
    print('kamu remaja')
else:
    print('kamu anak anak')
print('======================')

# 4. Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.
print ('## 4. program status menentukan keanggotaan ##')
print('======================')

# input status
status_anggota = input("""daftar keanggotaan dibawah ini
                       1. gold
                       2. silver
                       3. bronze
                       masukkan pilihan anda""").lower()

# proses dan output
if status_anggota == 'gold' or status_anggota == 'silver':
    print('selamat anda mendapatkan diskon')
elif status_anggota =='bronze':
    print('maaf anda tidak mendapatkan diskon')
else:
 print('masukkan kata dengan benar: ')

 # 5.Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
print('## 5.program yang meminta pengguna untuk memasukkan jumlah pembelian ##')
print ('======================')

#input status
jumlah_pembelian = int(input("masukkan jumlah pembelian"))
harga_item = 100
harga_diskon = harga_item * jumlah_pembelian * (10/100)
harga_total = harga_item * jumlah_pembelian 
total = harga_total - harga_diskon
print(f"Anda mendapatkan diskon 10%, harga per item {harga_item} jadi total yang harus dibayar {total}")


    