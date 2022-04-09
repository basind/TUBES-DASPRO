import helper as hp

global gameToko
gameToko = hp.potongDataCSV("game.csv")

def ubahStok ():
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

    # while (gameId != gameToko[i][0]) and ((ketemu != True) or (i < hp.panjang(gameToko) - 1)):
    #     i += 1
    # else:       # ketemu
    #     i = i
    #     ketemu = True
    
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
    
    hp.overwrite("game.csv", gameToko)
        


 
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


def beliGame ():
    # Prosedur beliGame akan mengurangi stok dari game yang ID nya diinput oleh user, serta
    # user memiliki saldo yang cukup dan belum memiliki game tersebut. 
    # Bila belum dimiliki, namun saldo belum cukup maka akan diberikan pesan saldo tidak cukup. 
    # Bila saldo cukup namun sudah dimiliki, akan ditampilkan pesan sudah dimiliki
    # Bila saldo cuku dan belum dimiliki namun stok habis, maka akan ditampilkan pesan stok habis.
    # Prosedur ini hanya dapat dilakukan oleh user.

    # KAMUS LOKAL

    # ALGORTIMA
    ...


def listGame ():
    # Prosedur menampilkan game yang dimiliki user ascending berdasar game ID.
    # Format : ID | Nama Game | Kategori | Tahun Rilis | Harga.
    # Menampilkan pesan error jika user tidak memiliki game.
    # Prosedur ini hanya dapat dilakukan oleh user. 

    # KAMUS LOKAL

    # ALGORITMA
    ...

ubahStok()