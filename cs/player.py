from object import Object

class Player(Object):

    def __init__(self, x, y, w, h, speedx, speedy, acel):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)

        self.boxs = None

    def run(self):    
        self.fall()
        self.stay_on_ground()
        self.touch_to_box()
        Object.show(self)

    def stay_on_ground(self):
        if self.y > height/2:
            self.y = height/2
            self.speedy = 0

    def fall(self):
        self.speedy += self.acel
        self.y += self.speedy

    def load_box(self, item):
        self.boxs = item

    def build_box(self):
        pass

    def touch_to_box(self):
        for item in self.boxs:
            if abs(self.x-self.w/2 - (item.x + item.w/2)) <= self.speedx and item.y - item.h/2 < self.y + self.h/2 and self.x > item.x:
                self.x = item.x + item.w/2 + self.w/2 + 0.1
            elif abs(self.x+self.w/2 - (item.x - item.w/2)) <= self.speedx and item.y - item.h/2 < self.y + self.h/2 and self.x < item.x:
                self.x = item.x - item.w/2 - self.w/2 - 0.1
    
            if item.x - item.w/2 < self.x + self.w/2 and self.x - self.w/2 < item.x + item.w/2 and abs((self.y + self.h/2) - (item.y - item.h/2)) < self.speedy:
                self.y = item.y - item.h/2 - self.h/2
                self.speedy = 0

    def move(self, dir):
        if dir == 'LEFT':
            self.x -= self.speedx
        elif dir == 'RIGHT':
            self.x += self.speedx
        elif dir == 'UP' and self.speedy == 0:
            self.speedy = -5
