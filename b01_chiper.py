"""
Bonus 01 - Chiper
implementasi dengan menggunakan 'vigenere chiper'
"""

import sys, time
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


def chiperEncript(password, key):  # Asumsi password at leats 8 karakter
    # SPESIFIKASI
    # (-) password character validation

    # KAMUS LOKAL

    # ALGORITMA

    # key enkripsi
    # perlu diperhatikan: len(key) <= len(password)]

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

def chiperUI():
    print('Pilih menu: ')
    print(f'{"enkripsi" :<8} -> Melakukan enkripsi')
    print(f'{"dekripsi" :<8} -> Melakukan dekripsi')
    choice = input('-> ')
    if choice == 'enkripsi':
        initial_data = input('Masukkan data yang ingin dienkripsi: ')
        key = input('Masukkan kunci enkripsi: ')
        if initial_data == '' or key == '':
            print('\n!!Input tidak valid!!\n')
        else:
            print('Melakukan enkripsi\nLoading', end='')
            sys.stdout.flush()
            for _ in range(3):
                time.sleep(2)
                print('.', end='')
                sys.stdout.flush()
            print('\nProses enkripsi berakhir.')
            time.sleep(1)
            print(f'Hasil enkripsi {initial_data}')
            print(f'-> {chiperEncript(initial_data, key)}\n')
    elif choice == 'dekripsi':
        initial_data = input('Masukkan data yang ingin didekripsi: ')
        key = input('Masukkan kunci dekripsi: ')
        print('Melakukan dekripsi\nLoading', end='')
        if initial_data == '' or key == '':
            print('\n!!Input tidak valid!!\n')
        else:
            sys.stdout.flush()
            for _ in range(3):
                time.sleep(2)
                print('.', end='')
                sys.stdout.flush()
            print('\nProses dekripsi berakhir.')
            time.sleep(1)
            print(f'Hasil dekripsi {initial_data}')
            print(f'-> {chiperDecript(initial_data, key)}\n')
    else:
        print("\n!!Tidak ada data yang dimasukkan!!\n")
