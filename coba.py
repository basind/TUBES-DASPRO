def panjang (a):
    n = 0
    for elm in a:
        n += 1
    return n


def pemisah (kalimat,jumlahKolom,delimiter):
    kalimatBaru = ["a" for i in range(jumlahKolom)]
    ke = 0
    n = 0
    while (n<jumlahKolom):
        kata = ""
        flag = True
        while flag and (ke < panjang(kalimat)):
            if (kalimat[ke] != delimiter):
                kata += kalimat[ke]
                ke += 1
            else:
                flag = False
                ke += 1
        kalimatBaru[n] = kata
        n += 1
            
    kataBaruTmp = ""
    for i in range (panjang(kalimatBaru[jumlahKolom-1])-1):
        kataBaruTmp += kalimatBaru[jumlahKolom-1][i]
    kalimatBaru[jumlahKolom-1] = kataBaruTmp
    return kalimatBaru


f = open("db.csv", "r")
user = f.readlines()

for i in range(panjang(user)):
    user[i] = pemisah(user[i], 6, ";")

for baris in user:
    print(baris)

f.close()