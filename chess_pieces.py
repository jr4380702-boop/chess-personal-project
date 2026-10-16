from chess_board_module import board, root, placeholder
import json
import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image

wk_x = 5
wk_y = 1
wk_axis = f"({wk_x},{wk_y})"

bk_x = 5
bk_y = 8
bk_axis = f"({bk_x},{bk_y})"

board_color = []
color_row = []
c = 0
for x in range(8):
    for i in range(8):
        color_row.append(c % 2)
        c += 1
    board_color.append(color_row)
    color_row = []
    c -= 1
for x in range(8):
    for i in range(8):
        if board_color[x][i] == 1:
            board_color[x][i] = "green"
        if board_color[x][i] == 0:
            board_color[x][i] = "white"

def define_grid(x_axis,y_axis,r):
    x = 9
    y = 9
    if x_axis == "a":
        x = 0
    elif x_axis == "b":
        x = 1
    elif x_axis == "c":
        x = 2
    elif x_axis == "d":
        x = 3
    elif x_axis == "e":
        x = 4
    elif x_axis == "f":
        x = 5
    elif x_axis == "g":
        x = 6
    elif x_axis == "h":
        x = 7

    if y_axis > 0 and y_axis < 9:
        y = y_axis - 1

    full_axis = f"{x}{y}"
    if r == "":
        return full_axis
    elif r == "x":
        return x
    elif r == "y":
        return y

def set_grid(x_axis,y_axis,r):
    x = 0
    y = 0
    if x_axis == 1:
        x = "a"
    elif x_axis == 2:
        x = "b"
    elif x_axis == 3:
        x = "c"
    elif x_axis == 4:
        x = "d"
    elif x_axis == 5:
        x = "e"
    elif x_axis == 6:
         x = "f"
    elif x_axis == 7:
        x = "g"
    elif x_axis == 8:
        x = "h"
    
    if y_axis == 1:
        y = "1"
    elif y_axis == 2:
        y = "2"
    elif y_axis == 3:
        y = "3"
    elif y_axis == 4:
        y = "4"
    elif y_axis == 5:
        y = "5"
    elif y_axis == 6:
        y = "6"
    elif y_axis == 7:
        y = "7"
    elif y_axis == 8:
        y = "8"
    full_axis = f"{x}{y}"
    if r == "":
        return full_axis
    elif r == "x":
        return x
    elif r == "y":
        return y

class piece:
    def __init__(self,x,y,xy, color="white"):
        self.color = color
        self.x = x
        self.y = y
        self.xy = f"{self.x} {self.y}"
        
    def axis(self):
        return (self.x, self.y)

class king(piece):
    def __init__(self,x,y,xy, color="white"):
        super(). __init__ (x,y,xy, color)

    def up(self):
        if self.y > 1:
            self.y += 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def down(self):
        if self.y < 8:
            self.y -= 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def left(self):
        if self.x > 1:
            self.x -= 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def right(self):
        if self.x > 1:
            self.x += 1
            self.xy = f"{self.x} {self.y}"
            return self.xy

    def ul(self):
        if self.y < 8 and self.x > 1:
            self.y += 1
            self.x -= 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def dl(self):
        if self.y < 8:
            self.y -= 1
            self.x -= 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def ur(self):
        if self.x > 1:
            self.y += 1
            self.x += 1
            self.xy = f"{self.x} {self.y}"
            return self.xy
    def dr(self):
        if self.x > 1:
            self.y -= 1
            self.x += 1
            self.xy = f"{self.x} {self.y}"
            return self.xy

        #abstract in parent class?
    def move(self, newspace=(4,5)):
        #make sure tuple is in movable range (eg. x is within 1, y is within 1, both are on board)
        #return true or false
        pass

        #abstract in parent class?
    def list_possible_moves(self , forbidden = []):
        moves = []
        moves.append((self.x+1, self.y)) #right
        moves.append((self.x-1, self.y)) #left
        moves.append((self.x-1, self.y+1)) #up left
        moves.append((self.x, self.y+1)) #up middle
        moves.append((self.x+1, self.y+1)) #up right
        moves.append((self.x-1, self.y-1)) #down left
        moves.append((self.x, self.y-1)) #down middle
        moves.append((self.x+1, self.y-1)) #down right

        possible_moves = [move for move in moves if 0 < move[0] <= 8 and 0 < move[1] <= 8 and move not in forbidden]
        return possible_moves
    
    def __str__(self):
        return json.dumps({"x": self.x, "y": self.y, "type": "King", "color": self.color})

wk = king(wk_x,wk_y,wk_axis)
bk = king(bk_x,bk_y,bk_axis)

white_pieces = [wk_axis]
black_pieces = [bk_axis]

wk_attack_spaces = wk.list_possible_moves()
bk_attack_spaces = bk.list_possible_moves()

white_attack_spaces = [wk_attack_spaces]
black_attack_spaces = [bk_attack_spaces]

wk_possible_moves = wk.list_possible_moves([black_attack_spaces,white_pieces])
bk_possible_moves = bk.list_possible_moves([white_attack_spaces,black_pieces])


grey_dot = ImageTk.PhotoImage(Image.open("./images/grey_dot.png"))
gd_img = Image.open("./images/grey_dot.png")
gd_width = 50
gd_height = 50
gd_resize = gd_img.resize((gd_width,gd_height), Image.Resampling.LANCZOS)
grey_dot = ImageTk.PhotoImage(gd_resize)

white_king_icon = ImageTk.PhotoImage(Image.open("./images/white_king.png"))
wk_img = Image.open("./images/white_king.png")
wk_width = 120
wk_height = 120
wk_resize = wk_img.resize((wk_width, wk_height), Image.Resampling.LANCZOS)
white_king_icon = ImageTk.PhotoImage(wk_resize)

black_king_icon = ImageTk.PhotoImage(Image.open("./images/black_king.png"))
bk_img = Image.open("./images/black_king.png")
bk_width = 100
bk_height = 100
bk_resize = bk_img.resize((bk_width, bk_height), Image.Resampling.LANCZOS)
black_king_icon = ImageTk.PhotoImage(bk_resize)


def move_king(x,y,color):
    global wk_x, wk_y, bk_x, bk_y
    if color == "white":
        if x == wk_x and y == wk_y:
            for i in range(len(wk_possible_moves)):
                if board_color[wk_possible_moves[i][0]][wk_possible_moves[i][1]] == 0:
                    board[wk_possible_moves[i][0]][wk_possible_moves[i][1]] = ttk.Button(root, text="", style="white.TButton", command=move_piece, image=grey_dot, padding=(10,10))
                if board_color[wk_possible_moves[i][0]][wk_possible_moves[i][1]] == 1:
                    board[wk_possible_moves[i][0]][wk_possible_moves[i][1]] = ttk.Button(root, text="", style="green.TButton", command=move_piece, image=grey_dot, padding=(10,10))

    elif color == "black":
        if x == bk_x and y == bk_y:
            pass

def move_piece(x,y,color):
    move_king(x,y,color)

move_king(wk_x,wk_y,"white")