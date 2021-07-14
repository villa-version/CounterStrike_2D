from object import Object

class Bullet(Object):

    damage = 15

    def __init__(self, x, y, w, h, speedx, speedy, acel, speed_vector, allow, player):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)
        self.allow = allow
        self.speed_vector = speed_vector
        self.player = player

    def run(self):
        Object.show(self)
        self.dir()
        self.move()

    def move(self):
        self.x += self.speedx
        self.y += self.speedy

    def dir(self):
        if self.allow:
            self.allow = False
            dx = mouseX - self.player.x
            dy = mouseY - self.player.y

            d = sqrt(dx**2+dy**2)

            self.speedx = self.speed_vector * (float(dx)/float(d))
            self.speedy = self.speed_vector * (float(dy)/float(d))
