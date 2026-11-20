import json
import tkinter as tk
from tkinter import ttk
import colors
from PIL import ImageTk, Image
from functools import partial

def placeholder():
    pass

boolean = False

turn = "white"

board = {}

root = tk.Tk()
root.geometry("1000x1000")

wk_x = 4
wk_y = 3
wk_axis = f"({wk_x},{wk_y})"

bk_x = 4
bk_y = 5
bk_axis = f"({bk_x},{bk_y})"

board_color = {}
c = 0
for x in range(8):
    for i in range(8):
        key = f"{x}{i}"
        if c % 2 == 1:
            board_color[key] = "green"
        else:
            board_color[key] = "white"
        c += 1
    c -= 1

for i in range(8):
    for x in range(8):
        if board_color[f"{x}{i}"] == "white":
            key = f"{x}{i}"
            board[key] = ttk.Button(root, text="", style="white.TButton", command=placeholder())
            board[key].grid(row= 7 - i, column= x)
        else:
            key = f"{x}{i}"
            board[key] = ttk.Button(root, text="", style="green.TButton", command=placeholder())
            board[key].grid(row= 7 - i, column= x)

def set_piece(x,y,image_icon):
    board[f"{x}{y}"].config(image=image_icon, padding=(0,0))

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

        #abstract in parent class?
    def move(self, newspace=(4,5)):
        #make sure tuple is in movable range (eg. x is within 1, y is within 1, both are on board)
        #return true or false
        pass

        #abstract in parent class?
    def list_possible_moves(self , forbidden = []):
        unlisted_forbidden = []
        moves = []
        moves.append((self.x+1, self.y)) #right
        moves.append((self.x-1, self.y)) #left
        moves.append((self.x-1, self.y+1)) #up left
        moves.append((self.x, self.y+1)) #up middle
        moves.append((self.x+1, self.y+1)) #up right
        moves.append((self.x-1, self.y-1)) #down left
        moves.append((self.x, self.y-1)) #down middle
        moves.append((self.x+1, self.y-1)) #down right

        if forbidden != []:
            for i in range(len(forbidden)):
                if isinstance(forbidden[i], list):
                    for x in range(len(forbidden[i])):
                        print(len(forbidden[i]))
                        if isinstance(forbidden[i][x], list):
                            for y in range(len(forbidden[i][x])):
                                unlisted_forbidden.append(forbidden[i][x][y])
                                print(f"appened 2D list value {forbidden[i][x][y]}")
                        else:
                            unlisted_forbidden.append(forbidden[i][x])
                            print(f"appened list value {forbidden[i][x]}")
                else:
                    unlisted_forbidden.append(forbidden[i])
                    print(f"appened {forbidden[i]}")
        print(f"unlisted fobidden: {unlisted_forbidden}")

        possible_moves = [move for move in moves if 0 <= move[0] < 8 and 0 <= move[1] < 8 and move not in unlisted_forbidden]
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
print(f"wk: {wk_possible_moves}")
gd_path = r"./images/grey_dot.png"
wk_path = r"./images/white_king.png"
bk_path = r"./images/black_king.png"

grey_dot = ImageTk.PhotoImage(Image.open(gd_path), master=root)
gd_img = Image.open(gd_path)
gd_width = 50
gd_height = 50
gd_resize = gd_img.resize((gd_width,gd_height), Image.Resampling.LANCZOS)
grey_dot = ImageTk.PhotoImage(gd_resize)

white_king_icon = ImageTk.PhotoImage(Image.open(wk_path), master=root)
wk_img = Image.open(wk_path)
wk_width = 120
wk_height = 120
wk_resize = wk_img.resize((wk_width, wk_height), Image.Resampling.LANCZOS)
white_king_icon = ImageTk.PhotoImage(wk_resize)

black_king_icon = ImageTk.PhotoImage(Image.open(bk_path), master=root)
bk_img = Image.open(bk_path)
bk_width = 120
bk_height = 120
bk_resize = bk_img.resize((bk_width, bk_height), Image.Resampling.LANCZOS)
black_king_icon = ImageTk.PhotoImage(bk_resize)

def set_all_pieces():
    for i in range(8):
        for e in range(8):
            board[f"{e}{i}"].config(image="", padding=(10,50))
    set_piece(wk_x,wk_y,white_king_icon)
    set_piece(bk_x,bk_y,black_king_icon)

def wk_refresh_moves():
    global wk_x, wk_y, wk_axis, wk_attack_spaces, wk_possible_moves, black_attack_spaces, white_attack_spaces
    wk_axis = wk_x,wk_y
    wk = king(wk_x,wk_y,wk_axis)
    wk_attack_spaces = wk.list_possible_moves()
    white_attack_spaces = [wk_attack_spaces]
    black_attack_spaces = [bk_attack_spaces]
    wk_possible_moves = wk.list_possible_moves([black_attack_spaces,white_pieces])
    print(wk_attack_spaces)
    print(wk_possible_moves)
    return wk_possible_moves

def bk_refresh_moves():
    global bk_x, bk_y, bk_axis, bk_attack_spaces, bk_possible_moves, white_attack_spaces, black_attack_spaces
    bk_axis = bk_x,bk_y
    bk = king(bk_x,bk_y,bk_axis)
    bk_attack_spaces = bk.list_possible_moves()
    black_attack_spaces = [bk_attack_spaces]
    white_attack_spaces = [wk_attack_spaces]
    bk_possible_moves = bk.list_possible_moves([white_attack_spaces,black_pieces])
    return bk_possible_moves

def refresh_moves():
    wk_refresh_moves()
    bk_refresh_moves()
    
def wk_move(new_x,new_y):
    global wk_x, wk_y, turn
    wk_x = new_x
    wk_y = new_y
    refresh_moves()
    set_all_to_move_piece()
    set_all_pieces()
    if turn == "white":
        turn = "black"
    else:
        turn = "white"

def bk_move(new_x,new_y):
    global bk_x, bk_y, turn
    bk_x = new_x
    bk_y = new_y
    refresh_moves()
    set_all_to_move_piece()
    set_all_pieces()
    if turn == "white":
        turn = "black"
    else:
        turn = "white"

def move_king(x,y):
    if turn == "white":
        if board[f"{y}{x}"] == board[f"{wk_y}{wk_x}"]:
            for i in range(len(wk_possible_moves)):
                if board_color[f"{wk_possible_moves[i][0]}{wk_possible_moves[i][1]}"] == "white":
                    board[f"{wk_possible_moves[i][0]}{wk_possible_moves[i][1]}"].config(image=grey_dot, style="white.TButton", command=partial(wk_move, wk_possible_moves[i][0], wk_possible_moves[i][1]), padding=(34,34))
                if board_color[f"{wk_possible_moves[i][0]}{wk_possible_moves[i][1]}"] == "green":
                    board[f"{wk_possible_moves[i][0]}{wk_possible_moves[i][1]}"].config(image=grey_dot, style="green.TButton", command=partial(wk_move, wk_possible_moves[i][0], wk_possible_moves[i][1]), padding=(34,34))
    elif turn == "black":
        if board[f"{y}{x}"] == board[f"{bk_y}{bk_x}"]:
            for i in range(len(bk_possible_moves)):
                if board_color[f"{bk_possible_moves[i][0]}{bk_possible_moves[i][1]}"] == "white":
                    board[f"{bk_possible_moves[i][0]}{bk_possible_moves[i][1]}"].config(image=grey_dot, style="white.TButton", command=partial(bk_move, bk_possible_moves[i][0], bk_possible_moves[i][1]), padding=(34,34))
                if board_color[f"{bk_possible_moves[i][0]}{bk_possible_moves[i][1]}"] == "green":
                    board[f"{bk_possible_moves[i][0]}{bk_possible_moves[i][1]}"].config(image=grey_dot, style="green.TButton", command=partial(bk_move, bk_possible_moves[i][0], bk_possible_moves[i][1]), padding=(34,34))

def move_piece(x,y):
    if boolean == True:
        move_king(x,y)

def set_all_to_move_piece():
    for i in range(8):
        for e in range(8):
            board[f"{e}{i}"].config(command=partial(move_piece, e,i))

def change_opacity(image_path, alpha):
    """
    Change the opacity of an image.
    alpha: float between 0.0 (transparent) and 1.0 (opaque)
    """
    # Open the image with Pillow
    img = Image.open(image_path).convert("RGBA")
    
    # Extract the alpha channel
    r, g, b, a = img.split()
    
    # Apply new alpha
    new_alpha = a.point(lambda p: int(p * alpha))
    
    # Merge channels back
    img = Image.merge("RGBA", (r, g, b, new_alpha))
    return img

def resize_image(path, target_width, target_height):
    """
    Resize an image to fit within target dimensions while keeping aspect ratio.
    Returns a PhotoImage object for Tkinter.
    """
    try:
        # Open the image
        img = Image.open(path)

        # Calculate aspect ratio preserving size
        img.thumbnail((target_width, target_height), Image.LANCZOS)

        # Convert to Tkinter-compatible PhotoImage
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {path}")
    except Exception as e:
        raise RuntimeError(f"Error processing image: {e}")

set_all_to_move_piece()
boolean = True

set_all_pieces()

if __name__ == "__main__":
    root.mainloop()