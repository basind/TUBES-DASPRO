# -*- coding: utf-8 -*-
"""help

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mdolywIm0t0xuxQSQBf0UWO8uqGR7uRa
"""

def help (isAdmin): #bisa dipanggil di setiap momen dengan kode '-help'
  
  if isAdmin:
    print('============ HELP ============')
    print('1. register - Untuk melakukan registrasi user baru')    
    print('2. login - Untuk melakukan login ke dalam sistem')    
    print('3. tambah_game - Untuk menambah game yang dijual pada toko')    
    print('4. list_game_toko - Untuk melihat list game yang dijual pada toko')    
    print('5. exit')
    number = int(input())
    if number == 1:
      print('')
    elif number == 2:
      print('')
    elif number == 3:
      print('')
    elif number == 4:
      print('')

  else:
    print('============ HELP ============')
    print('1. login - Untuk melakukan login ke dalam sistem')
    print('2. list_game_toko - Untuk melihat list game yang dijual pada toko')    
    print('3. exit')
    number = int(input())
    if number == 1:
      print('')
    elif number == 2:
      print('')
    
