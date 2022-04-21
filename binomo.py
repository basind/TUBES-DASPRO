"""
Program utama binomo
---
List Admin:
- Username: admin1 ;; Pass: pass_admin1
- Username: admin2 ;; Pass: pass_admin2
- Username: admin3 ;; Pass: pass_admin3
"""
from f2_5 import *
# from f6_9 import *
from f10_13 import *
from f14_f17 import *
from b01_chiper import *
from help import *
from helper import *
from load import *

# Fetch data dari database
data_game = loadGame()
data_user = loadUser()
data_kepemilikan = loadKepemilikan()
data_riwayat = loadRiwayat()

# Current user data
current_user_id = ''
current_user_role = ''

print('=== SELAMAT DATANG dI BINOMO ===')
user = login(data_user)
current_user_id = user[1]
current_user_role = user[0]

while(True):
    cmd = input('>> ')
    # pilih cmd
    if current_user_role == 'Admin':
        if cmd == 'register':
            data_user = registrasi(data_user)
        elif cmd == 'tambah_game':
            pass
        elif cmd == 'ubah_game':
            pass
        elif cmd == 'ubah_stok':
            pass
        elif cmd == 'list_game_toko':
            pass
        elif cmd == 'search_game_at_store':
            cariGameToko(data_game)
        elif cmd == 'topup':
            data_user = topUp(data_user)
        elif cmd == 'help':
            pass
        elif cmd == 'save':
            data = [data_game, data_user, data_kepemilikan, data_riwayat]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            break
        else:
            print('Perintah tidak tersedia.')
    else:
        if cmd == 'list_game_toko':
            pass
        elif cmd == 'buy_game':
            pass
        elif cmd == 'list_game':
            pass
        elif cmd == 'search_my_game':
            cariGameDimiliki(current_user_id, data_game, data_kepemilikan)
        elif cmd == 'search_game_at_store':
            cariGameToko(data_game)
        elif cmd == 'riwayat':
            lihatRiwayat(current_user_id, data_riwayat)
        elif cmd == 'help':
            pass
        elif cmd == 'save':
            data = [data_game, data_user, data_kepemilikan, data_riwayat]
            data_legend = ['game.csv', 'user.csv', 'kepemilikan.csv', 'riwayat.csv']
            save(data, data_legend)
        elif cmd == 'exit':
            break
        else:
            print('Perintah tidak tersedia.')
