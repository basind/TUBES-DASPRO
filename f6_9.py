import helper as hp

global gameToko
gameToko = hp.potongDataCSV("game.csv")

def ubahStok (gameToko):
    # ubahStok(gameToko). input berupa matriks
    # Fungsi mengubah stok game. Inputan ID GAME dan jumlah.
    # Lalu memberi pesan yang berisi informasi pengurangan atau penjumlahan
    # game, serta jumlah terkini game tersebut. 
    # Hanya dapat dilakukan oleh admmin.

    # KAMUS LOKAL

    # ALGORITMA
    gameId = input("Masukkan ID game: ")

    i = 0
    ketemu = False
    while (ketemu == False) and (i < hp.panjang(gameToko)):
        if (gameId != gameToko[i][0]):
            i += 1
        elif (gameId == gameToko[i][0]):
            ketemu = True

    if (ketemu == False):
        print("Tidak ada game dengan ID tersebut!")
    elif (ketemu == True):
        nama = gameToko[i][1]
        ubahStok = int(input("Masukkan jumlah: "))
        if (ubahStok < 0):
            if (int(gameToko[i][5]) >= (ubahStok * (-1))):
                gameToko[i][5] = int(gameToko[i][5]) + ubahStok
                print(f"Stok game {nama} berhasil dikurangi. Stok sekarang: {gameToko[i][5]}")
            else:
                print(f"Stok game {nama} gagal dikurangi karena stok kurang. Stok sekarang: {gameToko[i][5]} (< {ubahStok*(-1)})")
        elif (ubahStok > 0):
            gameToko[i][5] = int(gameToko[i][5]) + ubahStok
            print(f"Stok game {nama} berhasil ditambahkan. Stok sekarang: {gameToko[i][5]}")
        else:
            print(f"Stok game {nama} tetap. Stok sekarang: {gameToko[i][5]}")

    return gameToko
        


 
def listGameToko ():
    # Fungsi menampilkan list game di toko berdasarkan keyword pengguna. 
    # Secara default diurutkan berdasar pada ID GAME dari terkecil ke terbesar. 
    # Menerima inputan sebuah string "<keyword><+/->". 
    # + menandakan diurutkan ascending, 
    # - menandakan diurutkan descending. 
    # dan akan menampilkan pesan error bila inputan tidak sesuai. 
    # Dapat dilakukan admin dan user. 

    # KAMUS LOKAL

    # ALGORITMA
    ...


def beliGame (gameToko,username,user,game, kepemilikan):
    # Prosedur beliGame akan mengurangi stok dari game yang ID nya diinput oleh user, serta
    # user memiliki saldo yang cukup dan belum memiliki game tersebut. 
    # Bila belum dimiliki, namun saldo belum cukup maka akan diberikan pesan saldo tidak cukup. 
    # Bila saldo cukup namun sudah dimiliki, akan ditampilkan pesan sudah dimiliki
    # Bila saldo cuku dan belum dimiliki namun stok habis, maka akan ditampilkan pesan stok habis.
    # Prosedur ini hanya dapat dilakukan oleh user.

    # KAMUS LOKAL

    # ALGORTIMA
    # mencari posisi pengguna di data base user.csv
    barisUser = 0
    for i in range(hp.panjang(user)):
        if user[i][1] == username:
            baris = i 
    
    # menerima input game id
    gameId = (input()).upper()

    # pengecekan game ada atau tidak
    barisGame = 0
    isAvail = True
    for i in range(hp.panjang(game)):
        if (game[i][0] == gameId): 
            barisGame = i
            if (int(game[i][5]) == 0):
                isAvail = False

    if isAvail == False:
        print("Stok Game tersebut sedang habis!")
    else:
        # pengecekan sudah dimiliki 
        isOwned = False
        for i in range(hp.panjang(kepemilikan)):
            if (kepemilikan[i][0] == gameId) and (kepemilikan[i][1] == user[baris][0]):
                isOwned = True
        
        # pembelian
        if (isOwned == True):
            print("Anda sudah memiliki Game tersebut!")
        else:
            # pengecekan saldo
            if (user[baris][5] < game[i][4]):
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else:
                gameToko[barisGame][5] = int(gameToko[barisGame][5]) - 1
    return gameToko



def listGame ():
    # Prosedur menampilkan game yang dimiliki user ascending berdasar game ID.
    # Format : ID | Nama Game | Kategori | Tahun Rilis | Harga.
    # Menampilkan pesan error jika user tidak memiliki game.
    # Prosedur ini hanya dapat dilakukan oleh user. 

    # KAMUS LOKAL

    # ALGORITMA
    ...
