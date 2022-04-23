"""
Bonus 02 - Kerang Ajaib -- Implementasi LCG dengan time
"""

from helper import *
import time

# x = (a*x_0 + b) mod m
# nilai a = 8121
# nilai x_0 = dari time.time()
# nilai b = 28411
# nilai m = banyaknya pilihan jawaban = 8

# List jawaban:
# -> Ya
# -> Tidak
# -> Bisa jadi
# -> Lakukan
# -> Jangan lakukan
# -> Tidak mungkin
# -> Mungkin
# -> No komen

def pilihOutput(pilihan):
    if pilihan == 0.0:
        print('Ya')
    elif pilihan == 1.0:
        print('Tidak')
    elif pilihan == 2.0:
        print('Bisa jadi')
    elif pilihan == 3.0:
        print('Lakukan')
    elif pilihan == 4.0:
        print('Jangan lakukan')
    elif pilihan == 5.0:
        print('Tidak mungkin')
    elif pilihan == 6.0:
        print('Mungkin')
    else:
        print('No komen')

def kerangajaib():
    print('Pertanyaanmu: ', end='')
    input()
    pilihan = ((8121*(time.time()) + 28411)//1) % 8 
    print('Jawaban: ', end='')
    pilihOutput(pilihan)
    print()
