"""
Program utama binomo
---
List Admin:
- Username: admin1 ;; Pass: pass_admin1
- Username: admin2 ;; Pass: pass_admin2
- Username: admin3 ;; Pass: pass_admin3
"""
from f2_5 import *
from f6_9 import *
from f10_13 import *
from f14_17 import *
from b01_chiper import *
from help import *
from helper import *
from load import *

# Data temp
data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp = [], [], [], []

# Current user data
current_user_id = ''
current_user_role = ''

print('=== SELAMAT DATANG dI BINOMO ===\n')
user = login(loadUser())
current_user_id = user[1]
current_user_role = user[0]

while(True):
    # Fetch data dari database
    data_game = loadGame()
    data_user = loadUser()
    data_kepemilikan = loadKepemilikan()
    data_riwayat = loadRiwayat()
    cmd = input('>>> ')
    # pilih cmd
    if current_user_role == 'Admin':
        if cmd == 'register':
            data_user_temp = registrasi(data_user)
        elif cmd == 'tambah_game':
            data_game_temp = tambahGame(data_game)
        elif cmd == 'ubah_game':
            data_game_temp = ubahGame(data_game)
        elif cmd == 'ubah_stok':
            ubahStok(data_game)
        elif cmd == 'list_game_toko':
            listGameToko(data_game)
        elif cmd == 'search_game_at_store':
            cariGameToko(data_game)
        elif cmd == 'topup':
            data_user_temp = topUp(data_user)
        elif cmd == 'help':
            pass
        elif cmd == 'save':
            data = [data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            data = [data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            keluar(data, data_legend)
            break
        else:
            print('Perintah tidak tersedia.')
    else:
        if cmd == 'list_game_toko':
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
            pass
        elif cmd == 'save':
            data = [data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            data = [data_game_temp, data_user_temp, data_kepemilikan_temp, data_riwayat_temp]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            keluar(data, data_legend)
            break
        else:
            print('Perintah tidak tersedia.')
