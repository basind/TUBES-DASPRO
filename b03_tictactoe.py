"""
Bonus 03 - Tic Tac Toe Game
!! 
"""

from helper import *

# define global variable
global table_status

# print table_status
def printTable(table_status):
    for item in table_status:
        for ite in item:
            print(ite, end='')
        print()
    print()

# cek apakah ada pemenang
def isWinner(table_status):
    # by default ada 3 case kondisi menang:
    # -> Horizontal
    # -> Vertical
    # -> Diagonal

    # cek Horizontal
    for i in range(3):
        first_char = table_status[i][0]
        if first_char == '#':
            continue
        ada_pemenang = True
        for j in range(1,3):
            if table_status[i][j] != first_char:
                ada_pemenang = False
                break
        if ada_pemenang: 
            printTable(table_status)
            if first_char == 'X':
                print('Pemenangnya adalah pemain 1')
            else:
                print('Pemenangnya adalah pemain 2')
            print()
            return True

    # cek Vertical
    for j in range(3):
        first_char = table_status[0][j]
        if first_char == '#':
            continue
        ada_pemenang = True
        for i in range(1,3):
            if table_status[i][j] != first_char:
                ada_pemenang = False
                break
        if ada_pemenang:
            printTable(table_status)
            if first_char == 'X':
                print('Pemenangnya adalah pemain 1')
            else:
                print('Pemenangnya adalah pemain 2')
            print()
            return True

    # cek Diagonal kiri atas -> kanan bawah
    counter = 1
    ada_pemenang = True
    first_char = table_status[0][0]
    for j in range(1,3):
        if first_char == '#' or first_char != table_status[counter][counter]:
            ada_pemenang = False
            break
        counter += 1
    if ada_pemenang:
        printTable(table_status)
        if first_char == 'X':
            print('Pemenangnya adalah pemain 1')
        else:
            print('Pemenangnya adalah pemain 2')
        print()
        return True 

    # cek Diagonal kanan atas -> kiri bawah
    counter = 2
    ada_pemenang = True
    first_char = table_status[0][2]
    for j in range(1,3):
        if first_char == '#' or first_char != table_status[j][counter-1]:
            ada_pemenang = False
            break
        counter -= 1
    if ada_pemenang:
        printTable(table_status)
        if first_char == 'X':
            print('Pemenangnya adalah pemain 1')
        else:
            print('Pemenangnya adalah pemain 2')
        print()
        return True

    # cek apakah masih ada yang kosong
    for item in table_status:
        for ite in item:
            if ite == '#':
                return False
    printTable(table_status)
    print('Seri\n')
    return True

def tictactoe():
    print('Legenda:')
    print('# kosong')
    print('X pemain 1')
    print('O pemain 2\n')
    # membuat tabel status papan
    table_status = []
    for _ in range(3):
        temp = []
        for _ in range(3):
            temp = tambahArray(temp, ['#'])
        table_status = tambahArray(table_status, [temp])

    # loop game
    last_player = 'X'
    while not isWinner(table_status):
        printTable(table_status)
        print(f'Giliran pemain "{last_player}"')
        print('X: ', end='')
        coor_x = input()
        print('Y: ', end='')
        coor_y = input()
        print()
        try:
            coor_x = int(coor_x)
            coor_y = int(coor_y)
            if (coor_x < 1 and coor_x > 3) or (coor_y < 1 and coor_y > 3) or (table_status[coor_x - 1][coor_y - 1] != '#'):
                print('Input tidak valid')
                continue
            else:
                table_status[coor_x-1][coor_y-1] = last_player
                if last_player == 'X':
                    last_player = 'O'
                else:
                    last_player = 'X'
        except:
            print('Input tidak valid')
        
