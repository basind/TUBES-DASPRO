import helper as hp


def ubahStok (gameToko):
    # ubahStok(gameToko). input berupa matriks
    # Fungsi mengubah stok game. Inputan ID GAME dan jumlah.
    # Lalu memberi pesan yang berisi informasi pengurangan atau penjumlahan
    # game, serta jumlah terkini game tersebut. 
    # Hanya dapat dilakukan oleh admmin.

    # KAMUS LOKAL

    # ALGORITMA
    gameToko = gameToko
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
                gameToko[i][5] = str(int(gameToko[i][5]) + ubahStok)
                print(f"Stok game {nama} berhasil dikurangi. Stok sekarang: {gameToko[i][5]}")
            else:
                print(f"Stok game {nama} gagal dikurangi karena stok kurang. Stok sekarang: {gameToko[i][5]} (< {ubahStok*(-1)})")
        elif (ubahStok > 0):
            gameToko[i][5] = str(int(gameToko[i][5]) + ubahStok)
            print(f"Stok game {nama} berhasil ditambahkan. Stok sekarang: {gameToko[i][5]}")
        else:
            print(f"Stok game {nama} tetap. Stok sekarang: {gameToko[i][5]}")

    return gameToko
        
 
def listGameToko (gameToko):
    # Prosedur menampilkan list game di toko berdasarkan keyword pengguna. 
    # Secara default diurutkan berdasar pada ID GAME dari terkecil ke terbesar. 
    # Menerima inputan sebuah string "<keyword><+/->". 
    # + menandakan diurutkan ascending, 
    # - menandakan diurutkan descending. 
    # dan akan menampilkan pesan error bila inputan tidak sesuai. 
    # Dapat dilakukan admin dan user. 

    # KAMUS LOKAL

    # ALGORITMA
    tmpGameToko = hp.copyList2D(gameToko)

    inputan = input("Skema sorting : ")

    key, skema = hp.sortKey(inputan)

    kolKey = 0
    for i in range(6):
        if gameToko[0][i] == key:
            kolKey = i
    

    for i in range(1, hp.panjang(tmpGameToko)):
        tmpGameToko[i][4] = hp.formatSaldoOutput(tmpGameToko[i][4])

    tmpGameToko = hp.bubbleSortMatriks(tmpGameToko, kolKey, skema)

    for i in range(1, hp.panjang(tmpGameToko)):
        kolom1 = hp.perapih(tmpGameToko, i, 0)
        kolom2 = hp.perapih(tmpGameToko, i, 1)
        kolom3 = hp.perapih(tmpGameToko, i, 2)
        kolom4 = hp.perapih(tmpGameToko, i, 3) 
        kolom5 = hp.perapih(tmpGameToko, i, 4)
        kolom6 = hp.perapih(tmpGameToko, i, 5)   
        print(f"{kolom1} | {kolom2} | {kolom3} | {kolom4} | Rp {kolom5} | {kolom6}")

   
  


def beliGame (gameToko,userId,user, kepemilikan, riwayat):
    # Prosedur beliGame akan mengurangi stok dari game yang ID nya diinput oleh user, serta
    # user memiliki saldo yang cukup dan belum memiliki game tersebut. 
    # Bila belum dimiliki, namun saldo belum cukup maka akan diberikan pesan saldo tidak cukup. 
    # Bila saldo cukup namun sudah dimiliki, akan ditampilkan pesan sudah dimiliki
    # Bila saldo cuku dan belum dimiliki namun stok habis, maka akan ditampilkan pesan stok habis.
    # Prosedur ini hanya dapat dilakukan oleh user.

    # KAMUS LOKAL
    # gameToko : matriks game yang akan berubah sepanjang program dijalankan.

    # ALGORTIMA
    # mencari posisi pengguna di data base user.csv
    barisUser = 0
    for i in range(hp.panjang(user)):
        if user[i][0] == userId:
            barisUser = i 
    
    # menerima input game id
    gameId = (input('Masukkan ID Game: ')).upper()

    # pengecekan game ada atau tidak
    barisGame, isAvail = hp.findGame(gameId, gameToko) 


    if isAvail == False:
        print("Stok Game tersebut sedang habis!")
    else:
        # pengecekan sudah dimiliki 
        isOwned = False
        for i in range(hp.panjang(kepemilikan)):
            if (kepemilikan[i][0] == gameId) and (kepemilikan[i][1] == user[barisUser][0]):
                isOwned = True
       
        # pembelian
        if (isOwned == True):
            print("Anda sudah memiliki Game tersebut!")
        else:
            # pengecekan saldo
            if (int(user[barisUser][5]) < int(gameToko[barisGame][4])):
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else:
                gameToko[barisGame][5] = f"{int(gameToko[barisGame][5]) - 1}"
                kepemilikan = hp.tambahArray(kepemilikan, [[gameId, userId]])
                user[barisUser][5] = str(int(user[barisUser][5]) - int(gameToko[barisGame][4]))
                riwayat = hp.tambahArray(riwayat, [[gameId, gameToko[barisGame][1], gameToko[barisGame][4], userId, "2022"]])
    return gameToko, kepemilikan, user, riwayat



def listGame (userId, gameToko, kepemilikan):
    # Prosedur menampilkan game yang dimiliki user ascending berdasar game ID.
    # Format : ID | Nama Game | Kategori | Tahun Rilis | Harga.
    # Menampilkan pesan error jika user tidak memiliki game.
    # Prosedur ini hanya dapat dilakukan oleh user. 

    # KAMUS LOKAL

    # ALGORITMA
    n = hp.panjang(kepemilikan)

    if (n == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        print("Daftar game :")
        for i in range (1,n):
            if (kepemilikan[i][1] == userId):
                barisGame, _ = hp.findGame(kepemilikan[i][0], gameToko)
                kolom1 = hp.perapih(kepemilikan, i, 0)
                kolom2 = hp.perapih(gameToko, barisGame, 1)
                kolom3 = hp.perapih(gameToko, barisGame, 2)
                kolom4 = hp.perapih(gameToko, barisGame, 3) 
                kolom5 = hp.formatSaldoOutput(hp.perapih(gameToko, barisGame, 4))   
                print(f"{i+1}. {kolom1}  |  {kolom2}  |  {kolom3}  |  {kolom4}   |   {kolom5}")
