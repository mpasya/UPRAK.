produk = {
    'Caffe Americano' : 37000.00,
    'Caramel Macchiato' : 59000.00,
    'Asian Dolce Latte' : 55000.00,
    'Caramel latte' : 52000.00,
    'Vanilla latte' : 52000.00,
    'Caffe Latte' : 48000.00,
    'Cappuccino' : 48000.00,
    'Caffe Mocha' : 55000.00
    
}
def belanja():
    print('Selamat datang di toko daffahf, selamat berbelanja') 
    print('Berikut adalah daftar barang yang tersedia')
    for barang, harga in produk.items():
        print(f'{barang}: Rp{harga} per cup ')
    total_belanja = 0
    order_list = []
    while True:
        barang_dipilih = input("Masukkan nama pesanan anda (atau 'Order' untuk selesai): ")
        if barang_dipilih.lower() == 'order':
            break
        if barang_dipilih not in produk:
            print('Maaf, barang tersebut tidak tersedia, mohon untuk  memilih lagi')
            continue
        jumlah = int(input(f'berapa cup {barang_dipilih} yang anda inginkan? '))
        total_belanja += produk[barang_dipilih] * jumlah
        order_list.append(f'{jumlah} cup {barang_dipilih}')
    print(f'total Belanja anda adalah: Rp{total_belanja}')
    print('Daftar pesanan anda:')
    for item in order_list:
        print(item)
    
    if total_belanja >= 350000:
        diskon = total_belanja * 0.15
        print('Diskon anda kali ini adalah Rp',diskon)
        total_belanja -= diskon
    pajak = total_belanja * 0.1
    print('Pajak dari pesanan anda kali ini adalah Rp',pajak)
    print('Total yang harus dibayar adalah: Rp',total_belanja+pajak,' Terima Kasih telah berbelanja di toko Daffa')
            
belanja()