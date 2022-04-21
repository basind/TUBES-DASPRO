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
    for i in un:
        if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or (ord(i) == 45) or (ord(i) == 95):
            pass
        else:
            print('Username tidak valid')
            break

    # cek apakah password valid
    for item in pw:
        if panjang(pw) < 8 and ord(item) < 32 and ord(item) > 126:
            print('Password tidak valid')
            break
    
    # cek apakah username telah ada
    isUSExist = False
    for item in user:
        if item[1] == un:
            isUSExist = True
            print(f'Username {un} sudah terpakai, silahkan menggunakan username lain.')
    if not isUSExist:
        print(f'User {un} telah berhasil dibuat!')
        return tambahArray(user, [[new_id, un, nama, chiperEncript(pw), 'User', 0]])

def login(user):
    # Spesifikasi
    
    # KAMUS LOKAL

    # ALGORITMA

    # Password encription
    key = 'tahusah!' # WARNING 

    # looping hingga input username dan password sesuai
    while(True):
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
            print(f'Halo {user[index][2]}! Selamat datang di "Binomo"')
            if user[index][4] == 'Admin':
                return ["Admin", user[index][0]]
            else:
                return ["User", user[index][0]]
        else:
            print('\n!!Password atau username salah atau tidak ditemukan!!\n')
