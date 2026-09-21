board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def printBoard():
   print(board[1] + '|'+ board[2]+'|'+board[3])
   print('-----')
   print(board[4] + '|'+board[5]+'|' + board[6])
   print('-----')
   print(board[7] + '|'+board[8]+'|' + board[9])
   print()
   return

def check(i):
    return board.get(i) == " "

def checkWin(player):
    if board[1] == board[2] == board[3] == player: return True
    if board[4] == board[5] == board[6] == player: return True
    if board[7] == board[8] == board[9] == player: return True
    if board[1] == board[4] == board[7] == player: return True
    if board[2] == board[5] == board[8] == player: return True
    if board[3] == board[6] == board[9] == player: return True
    if board[1] == board[5] == board[9] == player: return True
    if board[3] == board[5] == board[7] == player: return True
    return False

def checkFull():
    for key in board:
        if board[key] == ' ':
            return False
    return True

print("X starts first and you can choose from 1 to 9 to place\n")
printBoard()
turn = 'X'

while True:
    if turn == 'X':
        while True:
            i = int(input("Player 1 (X): ").strip())
            if i in board and check(i):
                board[i] = "X"
                printBoard()
                break
            else:
                print("Occupied\n")
        if checkWin('X'):
            print("Player 1 wins")
            break
        if checkFull():
            print("Draw")
            break
        turn = 'O'
    else:
        while True:
            i = int(input("Player 2 (O): ").strip())
            if i in board and check(i):
                board[i] = "O"
                printBoard()
                break
            else:
                print("Occupied\n")
        if checkWin('O'):
            print("Player 2 wins")
            break
        if checkFull():
            print("Draw")
            break
        turn = 'X'
