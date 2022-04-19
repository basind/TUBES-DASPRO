"""
Program utama binomo
"""
from f2_5 import *
from f6_9 import *
from f10_13 import *
from b01_chiper import *
from helper import *

# Fetch data dari database
data_game = potongDataCSV('game.csv')
data_user = potongDataCSV('user.csv')
data_kepemilikan = potongDataCSV('kepemilikan.csv')
data_riwayat = potongDataCSV('riwayat.csv')


# Dummy data
current_user_id = 1

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

chiperDecript(chiperEncript('123_!#@chaos_membuat-dasPrO0!'),
              'tahusah!')
