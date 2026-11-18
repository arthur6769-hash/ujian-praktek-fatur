print ('====SELAMAT DATANG DI KANTIN====')
total = 0

while True:
    print('menu :')
    print('1. nasi goreng = 17000')
    print('2. ayam penyet = 15000')
    print('3. kopi sanger = 17000')
    print('4. es teh = 5000')
    print('0. selesai')

    pilihan = int(input('masukkan pilihan : '))

    if pilihan == 0:
        break

    elif pilihan == 1:
        harga = 17000
        nama = "nasi goreng"
    elif pilihan == 2:
        harga = 5000
        nama = "ayam penyet"
    elif pilihan == 3:
        harga = 15000
        nama = 'kopi sanger'
    elif pilihan == 4:
        harga = 5000
        nama = 'es teh'

    else:
        print('menu tidak tersedia')
        continue

    jumlah = int(input("masukkan jumlah:"))
    subtotal = harga * jumlah
    total += subtotal

print('STRUK PEMBAYARAN')
print('total belanja: rp', total)

if total >= 50000:
    diskon = total*10/100
else:
    diskon = 0

total_bayar = total - diskon

print('diskon:rp', diskon)
print('total bayar: rp', total_bayar)
print('terima kasih telah berbelanja di coffe shop kami')