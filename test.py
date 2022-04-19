from helper import *
# import time
# time_now = time.gmtime(time.time())
# print(f'{time_now.tm_mday}/{time_now.tm_mon}/{time_now.tm_year}')


# [' ', 'a', 'b', 'c']
# ['a', 'a', 'b', 'c']
# ['b', 'b', 'c', 'a']
# ['c', 'c', 'a', 'b']


password = 'jihucantik124'
key = 'tahu'
list_of_chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']


# password = input('Password: ')
# key = input('Key: ')

# cek apakah key dan password sudah valid:


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

""" ENCRYPTION STAGE """

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
print('Hasil enkripsi: ' + encripted_pass)

""" DECRYPTION STAGE """

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
print('Hasil dekripsi: ' + decripted_pass)
