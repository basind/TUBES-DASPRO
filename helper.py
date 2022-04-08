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
