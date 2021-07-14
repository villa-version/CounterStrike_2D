from object import Object

class Box(Object):

    def __init__(self, x, y, w, h, speedx, speedy, img, acel):
        Object.__init__(self, x, y, w, h, speedx, speedy, acel)
        self.skin = img

    def run(self):
        self.show()

    def show(self):
        rect(self.x, self.y, self.w, self.h)
        #image(self.skin, self.x, self.y, self.w, self.h)
