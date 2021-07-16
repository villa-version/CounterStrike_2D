from object import Object

class Box(Object):

    cost_box = 50

    def __init__(self, x, y, w, h, speedx, speedy, acel):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)
        self.skin = loadImage('images/box.jpg')

    def run(self):
        self.show()

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)
