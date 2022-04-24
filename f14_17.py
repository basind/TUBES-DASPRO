import time, sys
from helper import *
import os

def save(data, data_legend):
    nama_folder = input('Masukkan nama folder penyimpanan: ')
    
    # get current working directory
    curr_path = os.getcwd()
    list_dirs = []
    isExist = False
    for (_, sub_dirs, _) in os.walk(curr_path):
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
    defined_dir_path = curr_path + '//' + nama_folder

    # write data to the folder defined
    for index in range(panjang(data)):
        temp_file_path = defined_dir_path + '//' + data_legend[index]
        overwrite(temp_file_path, data[index])

    print('Loading', end='')
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(2)
        print('.', end='')
        sys.stdout.flush()
    print('\nFile berhasil disimpan.\n')

def help (role): #bisa dipanggil di setiap momen dengan kode '-help'
    if role == 'Admin':
        print(f'======================= HELP =======================')
        print(f'1.  {"register" :<20} -> Melakukan registrasi user baru')    
        print(f'2.  {"login" :<20} -> Melakukan login ke dalam sistem')    
        print(f'3.  {"tambah_game" :<20} -> Menambah game yang dijual pada toko')    
        print(f'4.  {"list_game_toko" :<20} -> Melihat list game yang dijual pada toko')    
        print(f'5.  {"ubah_game" :<20} -> Mengubah data game pada toko')
        print(f'6.  {"ubah_stok" :<20} -> Mengubah data stok game pada toko')
        print(f'7.  {"search_game_at_store" :<20} -> Melakukan pencarian pada game toko')
        print(f'8.  {"topup" :<20} -> Melakukan topup dan topdown')
        print(f'9.  {"help" :<20} -> Melihat command list')
        print(f'10. {"save" :<20} -> Menyimpan semua file')
        print(f'11. {"chiper" :<20} -> Melakakukan simulasi chiper encrypt dan decrypt')
        print(f'12. {"kerangajaib" :<20} -> Melakukan simulasi kerangajaib')
        print(f'13. {"tictactoe" :<20} -> Melakukan simulasi game tictactoe')
        print(f'14. {"exit" :<20} -> Keluar dari sistem')
    elif role == 'User':
        print(f'======================= HELP =======================')
        print(f'1.  {"login" :<20} -> Melakukan login ke dalam sistem')    
        print(f'2.  {"list_game_toko" :<20} -> Melihat list game yang dijual pada toko')    
        print(f'3.  {"buy_game" :<20} -> Melakukan pembelian game')
        print(f'4.  {"list_game" :<20} -> Melihat list game yang dimiliki')
        print(f'5.  {"search_my_game": <20} -> Melakukan pencarian pada game yang dimiliki') 
        print(f'6.  {"search_game_at_store" :<20} -> Mencari pencarian pada game toko')
        print(f'7.  {"riwayat" :<20} -> Melihat riwayat pembelian game')
        print(f'8.  {"help" :<20} -> Melihat command list')
        print(f'9.  {"save" :<20} -> Menyimpan semua file')
        print(f'10. {"chiper" :<20} -> Melakakukan simulasi chiper encrypt dan decrypt')
        print(f'11. {"kerangajaib" :<20} -> Melakukan simulasi kerangajaib')
        print(f'12. {"tictactoe" :<20} -> Melakukan simulasi game tictactoe')
        print(f'13. {"exit" :<20} -> Keluar dari sistem')
    else:
        print(f'======================= HELP =======================')
        print(f'1. {"login" :<6} -> Melakukan login ke sistem')
        print(f'2. {"help" :<6} -> Menampilkan list command yang tersedia')
        print(f'3. {"exit" :<6} -> Keluar dari sistem')
    print()


def keluar(data, data_legend):
    answer = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ')
    

    while not (answer == 'Y' or answer == 'N' or answer == 'y' or answer == 'n'):
        answer = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ')

    if answer == 'y' or answer == 'Y':
        save(data, data_legend)
    print('\n=== Terima kasih telah menggunakan Binomo ===')
