import argparse
import os
from helper import *

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
    return potongDataCSV('game.csv')

def loadUser():
    return potongDataCSV('user.csv')
    
def loadRiwayat():
    return potongDataCSV('riwayat.csv')

def loadKepemilikan():
    return potongDataCSV('kepemilikan.csv')
