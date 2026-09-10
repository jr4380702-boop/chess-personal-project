import os
import time
import threading
import colors
import random

def printBoard(board,a,b,d):
    global colors
    for r in board:
        for c in r:
            if c == "O":
                print(a, end="")
            if c == "X":
                print(b, end="")
            print(c, end="")
            print(d, end="")
        print()
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
ROWS = 8
COLS = 8
board = []
for r in range(ROWS):
    board.append([])
    for c in range(COLS):
        board[-1].append("#")
clear()
x = 1
y = 1
board[x][y] = "#"
printBoard(board,colors.CGREEN,colors.CBLUE,colors.CWHITE)
