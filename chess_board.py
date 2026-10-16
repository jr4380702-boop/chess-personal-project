import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image
import chess_pieces as pieces

turn = "white"

board = []
rows = []

axis = []
axis_row = [False, False, False, False, False, False, False, False]
for i in range(8):
    axis.append(axis_row)



def find_axis(axis,xy):
    x = axis[1]
    y = axis[4]
    if xy == "y":
        return y
    if xy == "x":
        return x

def set_grid(x_axis,y_axis):
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
    return full_axis

def find_button(axis):
    x = axis[1]
    y = axis[4]
    btn = set_grid(x,y)
    return btn

root = tk.Tk()
root.title("TTK Button Press Styling")
root.geometry("1000x1000")

style = ttk.Style()
style.theme_use("clam")
style.configure("green.TButton",
                font=("Arial", 12),
                padding=(10, 50),
                background="GREEN")
style.map("green.TButton",
          background=[("pressed", "green"), ("active", "darkgreen")],
          foreground=[("pressed", "green"), ("active", "black")])
style.configure("white.TButton",
                font=("Arial", 12),
                padding=(10, 50),
                background="WHITE")
style.map("white.TButton",
          background=[("pressed", "white"), ("active", "lightgray")],
          foreground=[("pressed", "white"), ("active", "black")])

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


c = 0
x_value = 1
y_value = 1
for i in range(9):
    x_value = 1
    for x in range(9):
        c += 1
        if i == 0 or x == 0:
            pass
        else:
            value_axis = set_grid(x_value,y_value)
            white_king_axis = set_grid(pieces.wk_x,pieces.wk_y)
            black_king_axis = set_grid(pieces.bk_x,pieces.bk_y)
            if c % 2 == 1:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="white.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn), image=white_king_icon, padding=(0,0))
                elif value_axis == black_king_axis:
                    btn = ttk.Button(root, text="", style="white.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn), image=black_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="white.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn))
                btn.grid(row= 8 - y_value, column= x_value)
                rows.append(btn)
            else:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="green.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn), image=white_king_icon, padding=(0,0))
                elif value_axis == black_king_axis:
                    btn = ttk.Button(root, text="", style="green.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn), image=black_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="green.TButton", command=pieces.move_piece(pieces.define_grid(value_axis[0],value_axis[1],"x"),pieces.define_grid(value_axis[0],value_axis[1],"y"),turn))
                btn.grid(row= 8 - y_value, column= x_value)
                rows.append(btn)
            x_value += 1
    if i == 0 or x == 0:
        pass
    else:
        board.append(rows)
        rows = []
        y_value += 1

print(board)
root.mainloop()