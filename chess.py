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

x = 5
class white_king:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class white_king_x(white_king):
    def speak(self):
        return self.x + 1
