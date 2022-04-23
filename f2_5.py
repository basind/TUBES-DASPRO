import helper as hp
from b01_chiper import *

def registrasi(user):
    nama = input('Masukkan nama: ')
    un = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    # === creating auto generated ID user ===
    # ---
    # ID user akan memiliki 2 tipe:
    # ADMXXXXX (sudah ada di database by default) dan USRXXXXX
    # dengan XXXXX adalah [00001..99999]
    # untuk sementara diasumsikan jumlah user tidak melebihi batas di atas :)

    # fetch user ID terkahir dari data user
    last_user_id = 'USR00000'
    for item in user:
        if item[0][0] != 'A':
            last_user_id = item[0]
    
    # creating new user ID
    splited_last_user_id = pisah(last_user_id)
    id_digits = ''
    mFirst = False
    for i in range(3, panjang(splited_last_user_id)):
        if not mFirst and splited_last_user_id[i] != '0':
            mFirst = True
        if mFirst:
            id_digits += splited_last_user_id[i]
    leading_char = ''
    if id_digits == '':
        id_digits = '0'
    for i in range(5-panjang(id_digits)):
        leading_char += '0'
    id_digits = int(id_digits)
    new_id = 'USR' + leading_char + str(id_digits + 1) 
    
    # cek apakah username valid
    if un == '':
        print('\n!!Username tidak valid!!\n')
        return user
    for i in un:
        if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or (ord(i) == 45) or (ord(i) == 95):
            pass
        else:
            print('\n!!Username tidak valid!!\n')
            return user

    # cek apakah password valid
    if pw == '':
        print('\n!!Password tidak valid!!\n')
        return user
    for item in pw:
        if panjang(pw) < 8 or ord(item) < 32 or ord(item) > 126:
            print('\n!!Password tidak valid!!\n')
            return user
    
    # cek apakah username telah ada
    isUSExist = False
    for item in user:
        if item[1] == un:
            isUSExist = True
            print(f'\n!!Username {un} sudah terpakai, silahkan menggunakan username lain!!\n')
            return user
    if not isUSExist:
        print(f'\nUser "{un}" telah berhasil dibuat!\n')
        return tambahArray(user, [[new_id, un, nama, chiperEncript(pw), 'User', 0]])


def login(user):
    # Spesifikasi
    
    # KAMUS LOKAL

    # ALGORITMA

    # Password encription
    key = 'tahusah!' # WARNING 

    # looping hingga input username dan password sesuai
    un = input('Masukkan username: ')
    pw = input('Masukkan password: ')
    check = False
    index = 0
    # validasi username dan password
    for i in range (1,hp.panjang(user)):
        if user[i][1] != un or chiperDecript(user[i][3], key) != pw:
            check = False
        else:
            check = True
            index = i
            break
    if check == True:
        print(f'\nHalo {user[index][2]}! Selamat datang di "Binomo"\n')
        if user[index][4] == 'Admin':
            return ["Admin", user[index][0], user[index][1]]
        else:
            return ["User", user[index][0], user[index][1]]
    else:
        print('\n!!Password atau username salah atau tidak ditemukan!!\n')

def tambahGame(data_game):
    # Spesifikasi

    # KAMUS LOKAL

    # ALGORITMA

    # copying data_game
    data_game = copyList2D(data_game)
    
    while True:
        ng = input('Masukkan nama game: ')
        ka = input('Masukkan kategori: ')
        tr = input('Masukkan tahun rilis: ')
        ha = input('Masukkan harga (Ex: Rp10.000 atau Rp10000): Rp')
        sa = input('Masukkan stok awal: ')

        if ng == '' or ka == '' or tr == '' or ha == '' or sa == '':
            print('\n!!Mohon masukkan semua informasi mengenai game agar dapat disimpan Binomo!!\n')
            continue

        # === validasi tahun rilis ===
        # kondisi valid: integer > 0

        # cek negativitas
        if tr[0] == '-':
            print('\n!!Input tahun rilis tidak valid!!\n')
            continue

        # cek illegal karakter
        try:
            tr = int(tr)
            tr = str(tr)
        except:
            print('\n!!Input tahun rilis tidak valid!!\n')
            continue

        # === validsi harga ===
        if validasiSaldo(ha):
            ha = formatSaldoInput(ha)
        else:
            print('\n!!Input harga tidak valid!!\n')
            continue

        # === validasi stok awal ===
        # cek negativitas
        if sa[0] == '-':
            print('\n!!Input stok awal tidak valid!!\n')
            continue

        # cek illegal karakter
        try:
            sa = int(sa)
            sa = str(sa)
        except:
            print('\n!!Input stok awal tidak valid!!\n')
            continue

        # === creating auto generated ID Game ===
        # ---
        # ID game akan memiliki 1 tipe: GMEXXXXX
        # dengan XXXXX adalah [00001..99999]
        # untuk sementara diasumsikan jumlah game tidak melebihi batas di atas :)

        # fetch game ID terkahir dari data game
        last_game_id = 'GME00000'
        for item in data_game:
            last_game_id = item[0]
    
        # creating new game ID
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

        print(f'Game "{ng}" berhasil ditambahkan.\n')
    
        return tambahArray(data_game, [[new_id, ng, ka, tr, ha, sa]])

def ubahGame(data_game):
    gid = input('Masukkan ID game: ')
    ng = input('Masukkan nama game: ')
    ka = input('Masukkan kategori: ')
    tr = input('Masukkan tahun rilis: ')
    ha = input('Masukkan harga (Ex: Rp10.000 atau Rp10000): Rp')

    # copy data_game
    data_game = copyList2D(data_game)

    # validasi ID Game:
    if gid == '':
        print('\n!!Silakan masukkan ID Game!!\n')
        return data_game

    # === validasi tahun rilis ===
    # kondisi valid: integer > 0
    if tr != '':
        # cek negativitas
        if tr[0] == '-':
            print('\n!!Input tahun rilis tidak valid!!\n')
            return data_game

        # cek illegal karakter
        try:
            tr = int(tr)
            tr = str(tr)
        except:
            print('\n!!Input tahun rilis tidak valid!!\n')
            return data_game

    # === validsi harga ===
    if ha != '':
        if validasiSaldo(ha):
            ha = formatSaldoInput(ha)
        else:
            print('\n!!Input harga tidak valid!!\n')
            return data_game

    # cek apakah game dengan id gid ada di data_game
    isExist = False
    game_index = 0
    for i in range(1, panjang(data_game)):
        if data_game[i][0] == gid:
            game_index = i
            isExist = True

            # handle empty input
            if ng == '':
                ng = data_game[i][1]
            if ka == '':
                ka = data_game[i][2]
            if tr == '':
                tr = data_game[i][3]
            if ha == '':
                ha = data_game[i][4]
            break
        
    # keluaran
    if isExist == True:
        data_game[game_index] = [gid, ng, ka, tr, ha, data_game[game_index][5]]
        print(f'\nGame dengan ID {gid} berhasil diupdate.\n')
    else:
        print('\n!!Input Game ID tidak valid!!\n')
    return data_game
