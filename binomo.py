"""
Program utama binomo
"""
from f2_5 import *
# from f6_9 import *
# from f10_13 import *
# from b01_chiper import *
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

# Testing purpose -> cariGameDimiliki()
# print(data_game)
# print('--------------')
# print(data_user)
# print('--------------')
# print(data_kepemilikan)
# print('--------------')
# print(data_riwayat)

# cariGameDimiliki(current_user_id, data_game, data_kepemilikan)

# cariGameToko(data_game)

# data_user = topUp(data_user)

# lihatRiwayat(current_user_id, data_riwayat)

# chiperDecript(chiperEncript('123_!#@chaos_membuat-dasPrO0!'),
#            'tahusah!')


print('=== SELAMAT DATANG dI BINOMO ===')
user = login(data_user)
current_user_id = user[1]
current_user_role = user[0]

while(True):
    cmd = input('>> ')
    # pilih cmd
    if current_user_role == 'Admin':
        if cmd == 'register':
            pass
        elif cmd == 'tambah_game':
            pass
        elif cmd == 'ubah_game':
            pass
        elif cmd == 'ubah_stok':
            pass
        elif cmd == 'list_game_toko':
            pass
        elif cmd == 'search_game_at_store':
            pass
        elif cmd == 'topup':
            pass
        elif cmd == 'help':
            pass
        elif cmd == 'save':
            pass
        elif cmd == 'exit':
            break
        else:
            print('Perintah salah!!.')
    else:
        if cmd == 'list_game_toko':
            pass
        elif cmd == 'buy_game':
            pass
        elif cmd == 'list_game':
            pass
        elif cmd == 'search_my_game':
            pass
        elif cmd == 'search_game_at_store':
            pass
        elif cmd == 'riwayat':
            pass
        elif cmd == 'help':
            pass
        elif cmd == 'save':
            pass
        elif cmd == 'exit':
            break
        else:
            print('Perintah salah!!.')
