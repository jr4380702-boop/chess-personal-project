
import os
import time
import threading
import colors
import random

def clear():
    os.system('clr')

def printBoard(board):
    global colors
    for r in board:
        for c in r:
            if c == "O":
                print(end="")
            if c == "X":
                print(end="")
            print(c, end="")
            print(end="")
        print()
x = ""
y = ""
axis = ""

user = ""
white_input = True
wk_x = 4
wk_y = 0
wk_axis = f"({wk_x},{wk_y})"

black_input = True
bk_x = 4
bk_y = 7
bk_axis = f"({bk_x},{bk_y})"

class piece:
    def __init__(self,x,y,xy, color="white"):
        self.color = color
        self.x = x
        self.y = y
        
    def axis(self):
        return (self.x, self.y)

class king(piece):
    def __init__(self,x,y,xy, color="white"):
        super(). __init__ (x,y,xy, color)

    def right(self):
        self.x += 1
        self.y = self.y
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def left(self):
        self.x -= 1
        self.y = self.y
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def up(self):
        self.y += 1
        self.x = self.x
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def down(self):
        self.y -= 1
        self.x = self.x
        self.xy = f"({self.x}, {self.y})"
        return self.xy

    def ur(self):
        self.x += 1
        self.y += 1
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def ul(self):
        self.x -= 1
        self.y += 1
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def dr(self):
        self.x += 1
        self.y -= 1
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def dl(self):
        self.x -= 1
        self.y -= 1
        self.xy = f"({self.x}, {self.y})"
        return self.xy
    def __str__(self):
        return f"({self.axis()[0]}, {self.axis()[1]})"

wk = king(wk_x,wk_y,wk_axis)
bk = king(bk_x,bk_y,bk_axis)
k = king(x,y,axis)

print(wk.ur())

def king_move(color):
    global wk_x
    global wk_y
    global wk_axis
    global bk_x
    global bk_y
    global bk_axis
    if color == "white":
        x = wk_x
        y = wk_y
        axis = wk_axis
    elif color == "black":
        x = bk_x
        y = bk_y
        axis = bk_axis
    valid_input = True
    user = input(f"{color} where would you like to move your king: ")
    axis = f"({x}, {y})"
    if user == "up":
        axis = k.up()
    elif user == "down":
        axis = k.down()
    elif user == "left":
        axis = k.left()
    elif user == "right":
        axis = k.right()
    elif user == "ul":
        axis = k.ul()
    elif user == "ur":
        axis = k.ur()
    elif user == "dl":
        axis = k.dl()
    elif user == "dr":
        axis = k.dr()
    else:
        valid_input = False
    if valid_input == True:
        return axis
    else:
        return False
ROWS = 8
COLS = 8
board = []
for r in range(ROWS):
    board.append([])
    for c in range(COLS):
        board[-1].append("#")

board[wk_y][wk_x] = "k"
board[bk_y][bk_x] = "k"

