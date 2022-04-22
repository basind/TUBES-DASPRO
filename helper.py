import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder")
args = parser.parse_args()

def panjang(item):
    # Helper panjang untuk mengecek panjang suatu item (list, string, dsb)

    # KAMUS LOKAL
    # counter: integer
    # j: iterator

    # ALGORITMA
    counter = 0
    for j in item:
        counter += 1
    return counter


def tambahArray(arr1, item):
    # Spesifikasi

    # KAMUS LOKAL

    # ALGORITMA
    return arr1 + item


def potongDataCSV(nama_file):
    # Spesifikasi

    # KAMUS LOKAL

    # ALGORITMA
    for filename in os.listdir(args.nama_folder):
        arr = []
        arrofarr = []
        delimiter = ';'
        with open(os.path.join(args.nama_folder, nama_file), 'r') as data:
            for item in data:
                arr = tambahArray(arr, [item])
        for item in arr:
            temp = []
            s = ""
            for i in range(panjang(item)):
                if item[i] == delimiter:
                    temp = tambahArray(temp, [s])
                    s = ""
                elif (i == panjang(item) - 1 and item[i] == '\n'):
                    break
                else:
                    s += item[i]
            temp = tambahArray(temp, [s])
            arrofarr = tambahArray(arrofarr, [temp])
        return arrofarr


def panjangMaksKolomTabel(data):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    panjang_maksimum_kolom = []
    for i in range(panjang(data[0])):
        maks_temp = 0
        for j in range(panjang(data)):
            if panjang(data[j][i]) > maks_temp:
                maks_temp = panjang(data[j][i])
        panjang_maksimum_kolom = tambahArray(
            panjang_maksimum_kolom, [maks_temp])
    return panjang_maksimum_kolom


def overwrite(nama_file, matriks):
    with open(nama_file, 'w+') as data:
        for i in range(panjang(matriks)):
            line = ""
            for j in range(panjang(matriks[i])):
                line += str(matriks[i][j])
                if j != panjang(matriks[i]) - 1:
                    line += ';'
            if (i != (panjang(matriks) - 1)):
                line += '\n'
            data.write(line)


def validasiSaldo(saldo):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    if panjang(saldo) == 0:
        return False
    else:
        temp = ''
        count = 0
        meet_titik = False
        for item in saldo:
            if item == '-':
                continue
            elif not meet_titik and item != '.':
                temp += item
                count += 1
            elif item != '.':
                count -= 1
                temp += item
            else:
                if not meet_titik and count > 3:
                    return False
                elif meet_titik and count != 0:
                    return False
                else:
                    count = 3
                    meet_titik = True
                    continue
        if count != 0 and meet_titik:
            return False
        try:
            temp = int(temp)
            return True
        except:
            return False


def formatSaldoInput(saldo):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    temp = ''
    for item in saldo:
        if item == '.':
            continue
        else:
            temp += item
    return temp


def formatSaldoOutput(saldo_init):
    # Spesifikasi
    # ...

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    saldo = ''
    for item in str(saldo_init):
        if item == '-':
            continue
        else:
            saldo += item
    panjang_saldo = panjang(saldo)
    count = 3 - (panjang_saldo % 3)
    temp = ''
    for i in range(panjang_saldo):
        if count == 3:
            if i == 0:
                temp += saldo[i]
            else:
                temp += '.' + saldo[i]
            count = 1
        else:
            temp += saldo[i]
            count += 1
    return temp


def findGame (gameId, gamDb):
    # Spesifikasi
    # Pengecek baris ke berapa dan ketersediaan stok game

    # KAMUS LOKAL
    # ...

    # ALGORITMA
    barisGame = 0
    isAvail = True
    for i in range(panjang(gamDb)):
        if (gamDb[i][0] == gameId): 
            barisGame = i
            if (int(gamDb[i][5]) == 0):
                isAvail = False
    return barisGame, isAvail


def sortKey (masukan):
    key = ""
    skema = ""

    for elm in masukan:
        if (elm == "+") or (elm == "-"):
            skema += elm
        else:
            key += elm
    
    return key, skema
    

def bubbleSortMatriks (matriks, kolomKey, skema):
    nMatriks = panjang(matriks)

    if (skema == "+"):
        for i in range(1,nMatriks - 1):
            for j in range(1, nMatriks-i-1):
                if (matriks[j][kolomKey] > matriks[j+1][kolomKey]):
                    matriks[j+1], matriks[j] = matriks[j], matriks[j+1]
    else:
        for i in range(1,nMatriks - 1):
            for j in range(1, nMatriks-i-1):
                if (matriks[j][kolomKey] < matriks[j+1][kolomKey]):
                    matriks[j+1], matriks[j] = matriks[j], matriks[j+1]
   
    return matriks

def pisah(data):
    # Implementasi manual fungsi split 

    # KAMUS LOKAL
    # result    : array of string
    # item      : char 

    # ALGORITMA
    result = []
    for item in data:
        result = tambahArray(result, [item])
    return result

def copyList2D(List):
    # Melakukan copy List-2D menjadi list baru

    # KAMUS LOKAL

    # ALGORITMA
    new_list = []
    for oitem in List:
        temp_list = []
        for item in oitem:
            temp_list = tambahArray(temp_list, [item])
        new_list = tambahArray(new_list, [temp_list])
    return new_list

def copyList1D(List):
    # Melakukan copy List-1D menjadi list baru

    # KAMUS LOKAL

    # ALGORITMA
    new_list = []
    for item in List:
        new_list = tambahArray(new_list, [item])
    return new_list


def maks (db, kolom):
    n = 0
    for i in range(panjang(db)):
        if (panjang(db[i][kolom]) > n):
            n = panjang(db[i][kolom])
    return n

def spasi (db, maks, baris, kolom):
    keluaran = " " * (maks - panjang(db[baris][kolom]))
    return keluaran

def perapih(db, baris, kolom):
    keluaran = str(db[baris][kolom]) + spasi(db, maks(db, kolom), baris,  kolom)
    return keluaran