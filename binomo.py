"""
Program utama binomo
---
List Admin:
- Username: admin1 ;; Pass: pass_admin1
- Username: admin2 ;; Pass: pass_admin2
- Username: admin3 ;; Pass: pass_admin3
List User:
- Username: user1 ;; Pass: pass_user1
"""

from f2_5 import *
from f6_9 import *
from f10_13 import *
from f14_17 import *
from b01_chiper import *
from b02_kerangajaib import *
from b03_tictactoe import *
from helper import *
from load import *

# Data temp
data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp = [], [], [], []

# List command admin
list_cmd_admin = ['login', 'register', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'search_game_at_store', 'topup', 'help', 'save', 'exit', 'chiper', 'kerangajaib', 'tictactoe']

# List command user
list_cmd_user = ['login', 'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 'search_game_at_store', 'riwayat', 'help', 'save', 'exit', 'chiper', 'kerangajaib', 'tictactoe']

# list command admin dan user
list_cmd_admin_user = ['login', 'list_game_toko', 'search_game_at_store', 'help', 'save', 'exit', 'chiper', 'kerangajaib', 'tictactoe']

# Current user data
current_user_id = ''
current_user_role = ''

print('=== Selamat Datang  di Binomo ===\n')
user = []
current_user_id = ''
current_user_username = ''
current_user_role = ''

while(True):
    # Fetch data dari database
    data_game = loadGame()
    data_user = loadUser()
    data_kepemilikan = loadKepemilikan()
    data_riwayat = loadRiwayat()
    print('Ketik help untuk melihat list command.')
    if current_user_username != '':
        cmd = input(f'({current_user_username}) >>> ')
    else:
        cmd = input('>>> ')
    # pilih cmd
    if current_user_role == 'Admin':
        if cmd == 'login':
            user = login(data_user)
            if user != None:
                current_user_id = user[1]
                current_user_username = user[2]
                current_user_role = user[0]
        elif cmd == 'register':
            data_user_temp = registrasi(data_user)
        elif cmd == 'tambah_game':
            data_game_temp = tambahGame(data_game)
        elif cmd == 'ubah_game':
            data_game_temp = ubahGame(data_game)
        elif cmd == 'ubah_stok':
            data_game_temp = ubahStok(data_game)
        elif cmd == 'list_game_toko':
            listGameToko(data_game)
        elif cmd == 'search_game_at_store':
            cariGameToko(data_game)
        elif cmd == 'topup':
            data_user_temp = topUp(data_user)
        elif cmd == 'help':
            help(current_user_role)
        elif cmd == 'save':
            data = olahFinalData([data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp], [data_game, data_user, data_kepemilikan, data_riwayat])
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            data = olahFinalData([data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp], [data_game, data_user, data_kepemilikan, data_riwayat])
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            keluar(data, data_legend)
            break
        elif cmd == 'chiper':
            chiperUI()
        elif cmd == 'kerangajaib':
            kerangajaib()
        elif cmd == 'tictactoe':
            tictactoe()
        else:
            isFind = False
            for command in list_cmd_user:
                if command == cmd:
                    print(f'\n!!Perintah "{cmd}" hanya tersedia untuk role User!!\n')
                    isFind = True
                    break
            if not isFind: 
                print('\n!!Perintah tidak tersedia!!\n')
    elif current_user_role == 'User':
        if cmd == 'login':
            user = login(data_user)
            if user != None:
                current_user_id = user[1]
                current_user_username = user[2]
                current_user_role = user[0]
        elif cmd == 'list_game_toko':
            listGameToko(data_game)
        elif cmd == 'buy_game':
            beliGame(data_game, current_user_id, data_user, data_kepemilikan)
        elif cmd == 'list_game':
            listGame(current_user_id, data_game, data_kepemilikan)
        elif cmd == 'search_my_game':
            cariGameDimiliki(current_user_id, data_game, data_kepemilikan)
        elif cmd == 'search_game_at_store':
            cariGameToko(data_game)
        elif cmd == 'riwayat':
            lihatRiwayat(current_user_id, data_riwayat)
        elif cmd == 'help':
            help(current_user_role)
        elif cmd == 'save':
            data = olahFinalData([data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp], [data_game, data_user, data_kepemilikan, data_riwayat])
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            data = olahFinalData([data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp], [data_game, data_user, data_kepemilikan, data_riwayat])
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            keluar(data, data_legend)
            break
        elif cmd == 'chiper':
            chiperUI()
        elif cmd == 'kerangajaib':
            kerangajaib()
        elif cmd == 'tictactoe':
            tictactoe()
        else:
            isFind = False
            for command in list_cmd_admin:
                if command == cmd:
                    print(f'\n!!Perintah "{cmd}" hanya tersedia untuk role Admin!!\n')
                    isFind = True
                    break
            if not isFind:
                print('\n!!Perintah tidak tersedia!!\n')
    else:
        if cmd == 'login':
            user = login(data_user)
            if user != None:
                current_user_id = user[1]
                current_user_username = user[2]
                current_user_role = user[0]           
        elif cmd == 'help':
            help(current_user_role)
        elif cmd == 'exit':
            print('\n=== Terima kasih telah menggunakan Binomo ===')
            break
        else:
            isFind = False
            for command in list_cmd_admin_user:
                if command == cmd:
                    print(f'\n!!Perintah "{cmd}" hanya tersedia untuk role Admin dan User!!\n')
                    isFind = True
                    break
            if isFind:
                continue
            for command in list_cmd_user:
                if command == cmd:
                    print(f'\n!!Perintah "{cmd}" hanya tersedia untuk role User!!\n')
                    isFind = True
                    break
            if isFind: 
                continue
            for command in list_cmd_admin:
                if command == cmd:
                    print(f'\n!!Perintah "{cmd}" hanya tersedia untuk role Admin!!\n')
                    isFind = True
                    break
            if not isFind: 
                print('\n!!Perintah tidak tersedia!!\n')
