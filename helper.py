from tkinter import E


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
    arr = []
    arrofarr = []
    delimiter = ';'
    with open(nama_file, 'r') as data:
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
            for j in range(panjang(matriks[i]) - 1):
                line += str(matriks[i][j]) + ";"
            if (i == (panjang(matriks) - 1)):
                line += str(matriks[i][5])
            else:
                line += str(matriks[i][5]) + "\n"
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
        if count != 0:
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
