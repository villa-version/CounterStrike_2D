from object import Object
from bullet import Bullet

class Pistol(Object):

    def __init__(self, x, y, w, h, player):
        Object.__init__(self, x, y, w, h, 0, 0, 0)
        self.bullets = []
        self.player = player
        self.skin = loadImage('image/pistol.png')

    def run(self):
        self.del_bullet()

        for bullet in self.bullets:
            bullet.run()

        self.x = self.player.x
        self.y = self.player.y

    def del_bullet(self):
        for bullet in self.bullets[:]:
            if bullet.x < 0 or bullet.x > width or bullet.y < 0 or bullet.y > height:
                self.bullets.remove(bullet)

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)

    def shoot(self):
        self.bullets.append(Bullet(self.player.x, self.player.y, 5, 5, 0, 0, 0, 15, True, self.player))
