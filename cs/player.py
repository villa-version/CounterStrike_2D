from object import Object
from box_ import Box

class Player(Object):

    def __init__(self, x, y, w, h, speedx, speedy, acel):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)

        self.boxs = None
        self.money = None

    def run(self):
        self.fall()
        self.stay_on_ground()
        self.touch_to_box()
        self.outline()
        Object.show(self)

    def stay_on_ground(self):
        if self.y >= height/2:
            self.y = height/2
            self.speedy = 0
            self.acel = 0
        else:
            self.acel = 0.2

    def fall(self):
        self.speedy += self.acel
        self.y += self.speedy

    def load_box(self, item):
        self.boxs = item

    def load_money(self, item):
        self.money = item

    def buy_box(self):
        if self.money.score >= Box.cost_box:
            self.money.score -= Box.cost_box
        elif self.money.score < Box.cost_box:
            self.money.score = 0

    def build_box(self):
        if self.money.score >= Box.cost_box:
            for item in self.boxs:
                if (mouseX > item.x + item.w/2 and mouseX < item.x + item.w/2*3 and 
                    mouseY > item.y - item.h/2 and mouseY < item.y + item.h/2):
                    self.boxs.append(Box(item.x + item.w, item.y, 35, 35, 0, 0, '', 0))
                elif (mouseX > item.x - item.w/2 - item.w and mouseX < item.x - item.w/2 and 
                      mouseY > item.y - item.h/2 and mouseY < item.y + item.h/2):
                    self.boxs.append(Box(item.x - item.w, item.y, 35, 35, 0, 0, '', 0))
                elif (mouseX > item.x - item.w/2 and mouseX < item.x + item.w/2 and 
                      mouseY > item.y - item.h/2 - item.h and mouseY < item.y - item.h/2):
                    self.boxs.append(Box(item.x, item.y - item.h, 35, 35, 0, 0, '', 0))

    def outline(self):
        for item in self.boxs:
            if (mouseX > item.x + item.w/2 and mouseX < item.x + item.w/2*3 and 
                mouseY > item.y - item.h/2 and mouseY < item.y + item.h/2):
                noFill()
                rect(item.x + item.w, item.y, 35, 35)
            elif (mouseX > item.x - item.w/2 - item.w and mouseX < item.x - item.w/2 and 
                  mouseY > item.y - item.h/2 and mouseY < item.y + item.h/2):
                noFill()
                rect(item.x - item.w, item.y, 35, 35)
            elif (mouseX > item.x - item.w/2 and mouseX < item.x + item.w/2 and 
                  mouseY > item.y - item.h/2 - item.h and mouseY < item.y - item.h/2):
                noFill()
                rect(item.x, item.y - item.h, 35, 35)

    def touch_to_box(self):
        for item in self.boxs:
            if abs(self.x-self.w/2 - (item.x + item.w/2)) <= self.speedx and item.y - item.h/2 < self.y + self.h/2 and self.x > item.x:
                self.x = item.x + item.w/2 + self.w/2 + 0.1
            elif abs(self.x+self.w/2 - (item.x - item.w/2)) <= self.speedx and item.y - item.h/2 < self.y + self.h/2 and self.x < item.x:
                self.x = item.x - item.w/2 - self.w/2 - 0.1
    
            if item.x - item.w/2 < self.x + self.w/2 and self.x - self.w/2 < item.x + item.w/2 and abs((self.y + self.h/2) - (item.y - item.h/2)) < self.speedy:
                self.y = item.y - item.h/2 - self.h/2 - 0.2
                self.speedy = 0

    def move(self, dir):
        if dir == 'LEFT':
            self.x -= self.speedx
        elif dir == 'RIGHT':
            self.x += self.speedx
        elif dir == 'UP' and self.speedy == 0:
            self.speedy = -5
