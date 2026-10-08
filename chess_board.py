import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image
import chess_pieces as pieces

board = []
rows = []

axis = []
axis_row = []

def find_axis(axis,xy):
    x = axis[1]
    y = axis[4]
    if xy == "y":
        return y
    if xy == "x":
        return x

def set_grid(x_axis,y_axis):
    global x
    global y
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

def on_click():
    print("TTK Button pressed!")

root = tk.Tk()
root.title("TTK Button Press Styling")
root.geometry("1000x1000")

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TButton",
                font=("Arial", 12),
                padding=(10, 50),
                background="GREEN")
style.map("Custom.TButton",
          background=[("pressed", "green"), ("active", "darkgreen")],
          foreground=[("pressed", "green"), ("active", "black")])
style.configure("white.TButton",
                font=("Arial", 12),
                padding=(10, 50),
                background="WHITE")
style.map("white.TButton",
          background=[("pressed", "white"), ("active", "lightgray")],
          foreground=[("pressed", "white"), ("active", "black")])
# Create a ttk button with custom style

white_king_icon = ImageTk.PhotoImage(Image.open("./images/whiteking.png"))
wk_img = Image.open("./images/whiteking.png")
wk_width = 100
wk_height = 100
wk_resize = wk_img.resize((wk_width, wk_height), Image.LANCZOS)
white_king_icon = ImageTk.PhotoImage(wk_resize)
tk.Label(root,image=white_king_icon, bg="green")

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
            if c % 2 == 1:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="white.TButton", command=on_click, image=white_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="white.TButton", command=on_click)
                btn.grid(row= y_value, column= x_value)
                rows.append(btn)
                axis_row.append(set_grid(x,i))
            else:
                if value_axis == white_king_axis:
                    btn = ttk.Button(root, text="", style="Custom.TButton", command=on_click, image=white_king_icon, padding=(9,9))
                else:
                    btn = ttk.Button(root, text="", style="Custom.TButton", command=on_click)
                btn.grid(row= y_value, column= x_value)
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
            board[y_axis][x_axis] = set_grid(x,i)
            x_axis += 1
    if i == 0 or x == 0:
        pass
    else:
        y_axis += 1

root.mainloop()