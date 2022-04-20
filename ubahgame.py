import helper as hp
game = hp.potongDataCSV('game.csv')
print(game)
list = [[]]

def ubahGame(list):
    gid = str(input('Masukkan ID game: '))
    ng = str(input('Masukkan nama game: '))
    ka = str(input('Masukkan kategori: '))
    tr = str(input('Masukkan tahun rilis: '))
    ha = str(input('Masukkan harga: '))
    check = False
    for i in range (1,hp.panjang(game)):
        if game[i][0] != gid:
            check = False
        else:
            check = True
            break
    if check == True:
        list+=[[gid,ng,ka,tr,ha]]
        return list
    else:
        print('Game ID tidak valid')

ubahGame(list)

    