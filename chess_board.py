import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image
import chess_pieces as pieces
import os

def placeholer():
    pass

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

if __name__ == "__main__":
    pieces.root.mainloop()