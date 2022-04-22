from helper import *
from load import loadGame

data_game = loadGame()

def tambahGame(data_game):
    # Spesifikasi

    # KAMUS LOKAL

    # ALGORITMA

    # copying data_game
    data_game = copyList2D(data_game)

    ng = input('Masukkan nama game: ')
    ka = input('Masukkan kategori: ')
    tr = input('Masukkan tahun rilis: ')
    ha = input('Masukkan harga (Ex: Rp10.000 atau Rp10000): Rp')
    sa = input('Masukkan stok awal: ')

    if ng == '' or ka == '' or tr == '' or ha == '' or sa == '':
        print('\n!!Mohon masukkan semua informasi mengenai game agar dapat disimpan Binomo!!\n')
        tambahGame(data_game)

    # === validasi tahun rilis ===
    # kondisi valid: integer > 0

    # cek negativitas
    if tr[0] == '-':
        print('\n!!Input tahun rilis tidak valid!!\n')
        tambahGame(data_game)

    # cek illegal karakter
    try:
        tr = int(tr)
        tr = str(tr)
    except:
        print('\n!!Input tahun rilis tidak valid!!\n')
        tambahGame(data_game)

    # === validsi harga ===
    if validasiSaldo(ha):
        ha = formatSaldoInput(ha)
    else:
        print('\n!!Input harga tidak valid!!\n')
        tambahGame(data_game)

    # === validasi stok awal ===
    # cek negativitas
    if sa[0] == '-':
        print('\n!!Input stok awal tidak valid!!\n')
        tambahGame(data_game)

    # cek illegal karakter
    try:
        sa = int(sa)
        sa = str(sa)
    except:
        print('\n!!Input stok awal tidak valid!!\n')
        tambahGame(data_game) 

    # === creating auto generated ID Game ===
    # ---
    # ID game akan memiliki 1 tipe: GMEXXXXX
    # dengan XXXXX adalah [00001..99999]
    # untuk sementara diasumsikan jumlah game tidak melebihi batas di atas :)

    # fetch user ID terkahir dari data user
    last_game_id = 'GME00000'
    for item in data_game:
        last_game_id = item[0]
    
    # creating new user ID
    splited_last_game_id = pisah(last_game_id)
    id_digits = ''
    mFirst = False
    for i in range(3, panjang(splited_last_game_id)):
        if not mFirst and splited_last_game_id[i] != '0':
            mFirst = True
        if mFirst:
            id_digits += splited_last_game_id[i]
    leading_char = ''
    if id_digits == '':
        id_digits = '0'
    for i in range(5-panjang(id_digits)):
        leading_char += '0'
    id_digits = int(id_digits)
    new_id = 'GME' + leading_char + str(id_digits + 1)
    
    return tambahArray(data_game, [[new_id, ng, ka, tr, ha, sa]])
tambahGame(data_game)
