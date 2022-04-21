from helper import *

def cariGameDimiliki(user_id, data_game, data_kepemilikan):
    # Spesifikasi
    # Mendapatkan informasi game sesuai dengan query yang diminta oleh pengguna pada
    # inventory.
    # Belum komplit (-) auth.

    # KAMUS LOKAL
    #

    # ALGORITMA
    print('Masukkan ID Game: ', end='')
    game_id = input()
    print('Masukkan Tahun Rilis Game: ', end='')
    tahun = input()

    game_data = copyList2D(data_game)

    current_user_game_id = []
    for i in range(1, panjang(data_kepemilikan)):
        if data_kepemilikan[i][1] == user_id:
            current_user_game_id = tambahArray(
                current_user_game_id, [data_kepemilikan[i][0]])

    # fetch game yang dimiliki current_user
    counter = 0
    renew_data_game = []
    for i in current_user_game_id and range(1, panjang(game_data)):
        if counter == panjang(current_user_game_id):
            break
        if current_user_game_id[counter] == game_data[i][0]:
            renew_data_game = tambahArray(renew_data_game, [game_data[i]])
            counter += 1

    # filter hasil pencarian
    daftar_game = [['ID', 'Nama', 'Kategori', 'Tahun Rilis', 'Harga']]
    for i in range(0, panjang(renew_data_game)):
        if game_id == '' and tahun == '':
            daftar_game = tambahArray(daftar_game, [renew_data_game[i]])
        elif game_id == '':
            if renew_data_game[i][3] == tahun:
                daftar_game = tambahArray(daftar_game, [renew_data_game[i]])
        elif tahun == '':
            if renew_data_game[i][0] == game_id:
                daftar_game = tambahArray(daftar_game, [renew_data_game[i]])
        else:
            if renew_data_game[i][0] == game_id and renew_data_game[i][3] == tahun:
                daftar_game = tambahArray(daftar_game, [renew_data_game[i]])
    
    for i in range(1, panjang(daftar_game)):
        daftar_game[i][4] = 'Rp' + formatSaldoOutput(daftar_game[i][4])

    # cetak game yang dimiliki
    print('Daftar game pada inventory yang memenuhi kriteria:')
    if panjang(daftar_game) == 1:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    else:
        panjang_maks_kolom = panjangMaksKolomTabel(daftar_game)
        for item in daftar_game:
            if(item[0] == 'ID'):
                print(f"{item[0] :^{panjang_maks_kolom[0]}}   {item[1] :^{panjang_maks_kolom[1]}}   {item[2] :^{panjang_maks_kolom[2]}}   {item[3] :^{panjang_maks_kolom[3]}}   {item[4] :^{panjang_maks_kolom[4]}}")
            else:
                print(
                    f"{item[0] :<{panjang_maks_kolom[0]}} | {item[1] :<{panjang_maks_kolom[1]}} | {item[2] :<{panjang_maks_kolom[2]}} | {item[3] :<{panjang_maks_kolom[3]}} | {item[4] :<{panjang_maks_kolom[4]}}")
    

def cariGameToko(game_data):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    # input data
    print('Masukkan ID Game: ', end='')
    game_id = input()
    print('Masukkan Nama Game: ', end='')
    game_nama = input()
    print('Masukkan Harga Game (Ex: Rp100.000 atau Rp100000): Rp', end='')
    game_harga = input()
    print('Masukkan Kategori Game: ', end='')
    game_kategori = input()
    print('Masukkan Tahun Rilis Game: ', end='')
    game_tahun = input()

    # copy game_data
    data_game = copyList2D(game_data)

    # filter data
    daftar_game = []
    daftar_game_temp = []
    for i in range(panjang(data_game)):
        if i == 0:
            continue
        else:
            daftar_game = tambahArray(daftar_game, [data_game[i]])
    if game_id != '':
        for i in range(panjang(daftar_game)):
            if daftar_game[i][0] == game_id:
                daftar_game_temp = tambahArray(
                    daftar_game_temp, [daftar_game[i]])
        daftar_game = daftar_game_temp
        daftar_game_temp = []
    if game_nama != '':
        for i in range(panjang(daftar_game)):
            if daftar_game[i][1] == game_nama:
                daftar_game_temp = tambahArray(
                    daftar_game_temp, [daftar_game[i]])
        daftar_game = daftar_game_temp
        daftar_game_temp = []
    if game_harga != '':
        for i in range(panjang(daftar_game)):
            if daftar_game[i][4] == formatSaldoInput(game_harga):
                daftar_game_temp = tambahArray(
                    daftar_game_temp, [daftar_game[i]])
        daftar_game = daftar_game_temp
        daftar_game_temp = []
    if game_kategori != '':
        for i in range(panjang(daftar_game)):
            if daftar_game[i][2] == game_kategori:
                daftar_game_temp = tambahArray(
                    daftar_game_temp, [daftar_game[i]])
        daftar_game = daftar_game_temp
        daftar_game_temp = []
    if game_tahun != '':
        for i in range(panjang(daftar_game)):
            if daftar_game[i][3] == game_tahun:
                daftar_game_temp = tambahArray(
                    daftar_game_temp, [daftar_game[i]])
        daftar_game = daftar_game_temp
    daftar_game = tambahArray(
        [['ID', 'Nama', 'Kategori', 'Tahun Rilis', 'Harga', 'Stok']], daftar_game)

    for i in range(1, panjang(daftar_game)):
        daftar_game[i][4] = 'Rp' + formatSaldoOutput(daftar_game[i][4])

    # Cetak game yang dimiliki
    print('Daftar game pada toko yang memenuhi kriteria:')
    if panjang(daftar_game) == 1:
        print('Tidak ada game pada toko yang memenuhi kriteria')
    else:
        panjang_maks_kolom = panjangMaksKolomTabel(daftar_game)
        for item in daftar_game:
            if(item[0] == 'ID'):
                print(f"{item[0] :^{panjang_maks_kolom[0]}}   {item[1] :^{panjang_maks_kolom[1]}}   {item[2] :^{panjang_maks_kolom[2]}}   {item[3] :^{panjang_maks_kolom[3]}}   {item[4] :^{panjang_maks_kolom[4]}}   {item[5] :^{panjang_maks_kolom[5]}}")
            else:
                print(
                    f"{item[0] :<{panjang_maks_kolom[0]}} | {item[1] :<{panjang_maks_kolom[1]}} | {item[2] :<{panjang_maks_kolom[2]}} | {item[3] :<{panjang_maks_kolom[3]}} | {item[4] :<{panjang_maks_kolom[4]}} | {item[5] :<{panjang_maks_kolom[5]}}")


def topUp(data_user):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # input
    print('Masukkan username: ', end='')
    username = input()
    print('Contoh format saldo yang valid:')
    print('Rp10.000, Rp10.500, Rp1.000.000, Rp1000, Rp10500')
    print('Masukkan saldo: Rp', end='')
    saldo = input()

    # validasi user
    is_valid = False
    current_user_index = 0
    for i in range(1, panjang(data_user)):
        if data_user[i][1] == username:
            current_user_index = i
            is_valid = True
            break

    if not is_valid:
        print(f'Username "{username}" tidak ditemukan.')
    else:
        # validasi saldo
        if validasiSaldo(saldo):
            saldo = int(formatSaldoInput(saldo))
            data_user[current_user_index][5] = int(
                data_user[current_user_index][5])
            if saldo >= 0:
                data_user[current_user_index][5] += saldo
                print(
                    f'Top up berhasil. Saldo {username} bertambah menjadi Rp{formatSaldoOutput(data_user[current_user_index][5])}')
            else:
                if data_user[current_user_index][5] + saldo < 0:
                    print(
                        f'Masukan tidak valid. Anda tidak dapat mengurangi saldo sebesar Rp{formatSaldoOutput(saldo)}')
                else:
                    data_user[current_user_index][5] += saldo
                    print(
                        f'Top down berhasil. Saldo {username} berkurang menjadi Rp{formatSaldoOutput(data_user[current_user_index][5])}')
        else:
            print('Maaf, saldo yang anda masukkan tidak valid.')

    return data_user


def lihatRiwayat(user_id, riwayat_data):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA

    # copy riwayat_data
    data_riwayat = copyList2D(riwayat_data)

    # Fetching riwayat user yang bersesuaian
    user_riwayat = [['ID', 'Nama', 'Harga', 'User ID', 'Tahun Beli']]
    for i in range(1, panjang(data_riwayat)):
        if data_riwayat[i][3] == user_id:
            user_riwayat = tambahArray(user_riwayat, [data_riwayat[i]])

    for i in range(1, panjang(user_riwayat)):
        user_riwayat[i][2] = 'Rp' + formatSaldoOutput(user_riwayat[i][2])

    # cetak hasil fetching
    if panjang(user_riwayat) == 1:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah "beli_game" untuk membeli.')
    else:
        print('Daftar Game: ')
        panjang_maks_kolom = panjangMaksKolomTabel(user_riwayat)
        for item in user_riwayat:
            if(item[0] == 'ID'):
                print(f"{item[0] :^{panjang_maks_kolom[0]}}   {item[1] :^{panjang_maks_kolom[1]}}   {item[2] :^{panjang_maks_kolom[2]}}   {item[4] :^{panjang_maks_kolom[4]}}")
            else:
                print(
                    f"{item[0] :<{panjang_maks_kolom[0]}} | {item[1] :<{panjang_maks_kolom[1]}} | {item[2] :<{panjang_maks_kolom[2]}} | {item[4] :<{panjang_maks_kolom[4]}}")
