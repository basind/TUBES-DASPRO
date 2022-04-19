list = [[]]

def tambahgame(list):
    ng = str(input('Masukkan nama game: '))
    ka = str(input('Masukkan kategori: '))
    tr = int(input('Masukkan tahun rilis: '))
    ha = int(input('Masukkan harga: '))
    sa = int(input('Masukkan stok awal: '))
    if ng == '' or ka == '' or tr == '' or ha == '' or sa == '':
        print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.')
        tambahgame()
    else:
        print(f'Selamat! Berhasil menambahkan game {ng}.')
        list+=[[ng,ka,tr,ha,sa]]
        print(list)
        return list

tambahgame(list)
