"""
Bonus 01 - Chiper
implementasi dengan menggunakan 'vigenere chiper'
"""

from helper import *

# const global
global list_of_chars
global table_of_chars

# list karakter yang dapat digunakan sebagai password
list_of_chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '\\', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

# pembuatan array of array dari list_of_chars
table_of_chars = []
for i in range(panjang(list_of_chars)):
    counter = 0
    index = i
    temp = []
    while counter < panjang(list_of_chars):
        if index == panjang(list_of_chars):
            index = 0
        temp = tambahArray(temp, [list_of_chars[index]])
        counter += 1
        index += 1
    table_of_chars = tambahArray(table_of_chars, [temp])


def chiperEncript(password):  # Asumsi password at leats 8 karakter
    # SPESIFIKASI
    # (-) password character validation

    # KAMUS LOKAL

    # ALGORITMA

    # key enkripsi
    # perlu diperhatikan: len(key) <= len(password)]
    key = 'tahusah!'

    # pembuatan keystream
    keystream = ''
    counter = 0
    for i in range(panjang(password)):
        if counter == panjang(key):
            counter = 0
        keystream += key[counter]
        counter += 1

    # menemukan index dari password dan keystream
    index_pass = []
    index_keystream = []
    counter = 0
    while counter < panjang(password):
        for i in range(panjang(list_of_chars)):
            if password[counter] == list_of_chars[i]:
                index_pass = tambahArray(index_pass, [i])
                break
        counter += 1
    counter = 0
    while counter < panjang(keystream):
        for i in range(panjang(list_of_chars)):
            if keystream[counter] == list_of_chars[i]:
                index_keystream = tambahArray(index_keystream, [i])
                break
        counter += 1

    # melakukan enkripsi
    # baris -> index_keystream
    # kolom -> index_pass
    encripted_pass = ''
    for i in range(panjang(password)):
        encripted_pass += table_of_chars[index_keystream[i]][index_pass[i]]
    return encripted_pass


def chiperDecript(encripted_pass, key):
    # Spesifikasi

    # KAMUS LOKAL

    # ALGORITMA

    # pembuatan keystream
    keystream = ''
    counter = 0
    for i in range(panjang(encripted_pass)):
        if counter == panjang(key):
            counter = 0
        keystream += key[counter]
        counter += 1

    # mencari indeks keystream
    index_keystream = []
    counter = 0
    while counter < panjang(keystream):
        for i in range(panjang(list_of_chars)):
            if keystream[counter] == list_of_chars[i]:
                index_keystream = tambahArray(index_keystream, [i])
                break
        counter += 1

    # melakukan dekripsi
    decripted_pass = ''
    for i in range(panjang(encripted_pass)):
        for j in range(panjang(table_of_chars[index_keystream[i]])):
            if encripted_pass[i] == table_of_chars[index_keystream[i]][j]:
                decripted_pass += list_of_chars[j]
    return decripted_pass
