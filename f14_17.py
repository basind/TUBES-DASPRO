import time, sys
from helper import *
import os

def save(data, data_legend):
    nama_folder = input('Masukkan nama folder penyimpanan: ')
    
    # get current working directory
    curr_path = os.getcwd()
    list_dirs = []
    isExist = False
    for (root_dir_path, sub_dirs, files) in os.walk(curr_path):
        list_dirs = tambahArray(list_dirs, sub_dirs)
        break

    # loop through the list_dirs
    for item in list_dirs:
        if item == nama_folder:
            isExist = True
            break

    # make a new dir if doesn't exist
    if not isExist:
        os.mkdir(nama_folder)
    defined_dir_path = curr_path + '\\' + nama_folder

    # write data to the folder defined
    for index in range(panjang(data)):
        temp_file_path = defined_dir_path + '\\' + data_legend[index]
        overwrite(temp_file_path, data[index])

    print('Loading', end='')
    sys.stdout.flush()
    for i in range(3):
        time.sleep(2)
        print('.', end='')
        sys.stdout.flush()
    print('\nFile berhasil disimpan.\n')


def keluar(data, data_legend):
    answer = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ')
    

    while not (answer == 'Y' or answer == 'N' or answer == 'y' or answer == 'n'):
        answer = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ')

    if answer == 'y' or answer == 'Y':
        save(data, data_legend)
    print('\n=== Terima kasih telah menggunakan Binomo ===')
