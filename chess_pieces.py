
wk_x = 4
wk_y = 0
wk_axis = f"({wk_x},{wk_y})"

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