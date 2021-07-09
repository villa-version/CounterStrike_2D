from object import Object

class Player(Object):

    def __init__(self, x, y, w, h, speedx, speedy):
        Object.__init__(self, x, y, w, h, speedx, speedy)

    def run(self):
        Object.show(self)
        self.stay_on_ground()

    def stay_on_ground(self):
        self.speedy += 0.2
        self.y += self.speedy
        if self.y > height/2 - self.speedy:
            self.y = height/2
            self.speedy = 0

    def move(self, dir):
        if dir == 'LEFT':
            self.x -= self.speedx
        elif dir == 'RIGHT':
            self.x += self.speedx
        elif dir == 'UP' and self.speedy == 0:
            self.speedy = -5
