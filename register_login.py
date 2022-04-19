import helper as hp
user = hp.potongDataCSV('user.csv')
print (user)

def registrasi():
    nama = input('Masukkan nama: ')
    un = input('Masukkan username: ')
    pw = input('Masukkan password: ')
    for i in un:
        if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or (ord(i) == 45) or (ord(i) == 95):
            pass
        else:
            print('Username tidak valid')
    
    for i in range (hp.panjang(user)):
        if user[i][1] == un:
             print(f'Username {un} sudah terpakai, silahkan menggunakan username lain.')
        else:
            return

def login():
    un = input('Masukkan username: ')
    pw = input('Masukkan password: ')
    check = False
    for i in range (1,hp.panjang(user)):
        if user[i][1] != un and user[i][3] != pw:
            check = False
        else:
            check = True
            x = i
            break
    if check == True:
        print(f'Halo {user[x][2]}! Selamat datang di "Binomo"')
    else:
        print('Password atau username salah atau tidak ditemukan.')
            



             
