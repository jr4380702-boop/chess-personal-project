import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image

turn = "white"

board = []
rows = []

axis = []
axis_row = []

def placeholder():
    print("placeholder")

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

def move_piece():
    if turn == "white":
        pass

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
            white_king_axis = set_grid(5,1)
            black_king_axis = set_grid(5,8)
            if c % 2 == 1:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="white.TButton", command=placeholder, image=white_king_icon, padding=(0,0))
                elif value_axis == black_king_axis:
                    btn = ttk.Button(root, text="", style="white.TButton", command=placeholder, image=black_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="white.TButton", command=placeholder)
                btn.grid(row= 8 - y_value, column= x_value)
                rows.append(btn)
                axis_row.append(set_grid(x,i))
            else:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="green.TButton", command=placeholder, image=white_king_icon, padding=(0,0))
                elif value_axis == black_king_axis:
                    btn = ttk.Button(root, text="", style="green.TButton", command=placeholder, image=black_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="green.TButton", command=placeholder)
                btn.grid(row= 8 - y_value, column= x_value)
                rows.append(btn)
                axis_row.append(set_grid(x,i))
            x_value += 1
    if i == 0 or x == 0:
        pass
    else:
        board.append(rows)
        axis.append(axis_row)
        rows = []
        axis_row = []
        y_value += 1
x_axis = 0
y_axis = 0
for i in range(9):
    x_axis = 0
    for x in range(9):
        if i == 0 or x == 0:
            pass
        else:
            axis[y_axis][x_axis] = set_grid(x,i)
            x_axis += 1
    if i == 0 or x == 0:
        pass
    else:
        y_axis += 1

root.mainloop()