import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder")
args = parser.parse_args()

# pemisah di sini pakai fungsi pemisah kelompok mu. 
# ini ku ambil dari file lain.
def pemisah(str):
    split_list = []
    tmp = ''
    for s in str:
        if s == ';':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += s
    if tmp:
        split_list.append(tmp)
    return split_list

def panjang (obj):
    n = 0 
    for elm in obj:
        n += 1
    return n


# nilai "6" yang ada di inisiasi game itu berasal dari file percobaan yang kubuat.
# bisa diubah lagi.
def loadGame():
    for filename in os.listdir(args.nama_folder):
        game = [[]for i in range(6)]
        with open(os.path.join(args.nama_folder, 'game.csv'), 'r') as file_object:
            next(file_object)
            gameTmp = file_object.readlines()
            for i in range(panjang(gameTmp)):
                line = pemisah(gameTmp[i])
                game[i] = line
        return (game)

def loadUser():
    for filename in os.listdir(args.nama_folder):
        user = [[]for i in range(6)]
        with open(os.path.join(args.nama_folder, 'user.csv'), 'r') as file_object:
            next(file_object)
            userTmp = file_object.readlines()
            for i in range(panjang(userTmp)):
                line = pemisah(userTmp[i])
                user[i] = line
        return (user)
    
def loadRiwayat():
    for filename in os.listdir(args.nama_folder):
        riwayat = [[]for i in range(6)]
        with open(os.path.join(args.nama_folder, 'riwayat.csv'), 'r') as file_object:
            next(file_object)
            riwayatTmp = file_object.readlines()
            for i in range(panjang(riwayatTmp)):
                line = pemisah(riwayatTmp[i])
                riwayat[i] = line
        return (riwayat)


def loadKepemilikan():
    for filename in os.listdir(args.nama_folder):
        kepemilikan = [[]for i in range(6)]
        with open(os.path.join(args.nama_folder, 'kepemilikan.csv'), 'r') as file_object:
            next(file_object)
            kepemilikanTmp = file_object.readlines()
            for i in range(panjang(kepemilikanTmp)):
                line = pemisah(kepemilikanTmp[i])
                kepemilikan[i] = line
        return (kepemilikan)

print(loadGame())