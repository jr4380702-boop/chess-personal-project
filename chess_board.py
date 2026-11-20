import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image
import chess_pieces as pieces
import os

def placeholer():
    pass

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