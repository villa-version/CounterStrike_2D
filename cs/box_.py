from object import Object

class Box(Object):

    cost_box = 50

    def __init__(self, x, y, w, h, speedx, speedy, img, acel):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)
        self.skin = img

    def run(self):
        Object.show(self)
