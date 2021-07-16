class Object():

    def __init__(self, x, y, w, h, speedx, speedy, acel):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speedx = speedx
        self.speedy = speedy
        self.acel = acel

    def show(self):
        fill(255,255,255)
        rect(self.x, self.y, self.w, self.h)
