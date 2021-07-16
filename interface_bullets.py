from Object_interface import ObjectInterFace

class InterFaceBullets(ObjectInterFace):

    def __init__(self, x, y, xt, yt, w, h, score, score2, quantity_spent_bullets):
        ObjectInterFace.__init__(self, x, y, xt, yt, w, h, score, score2)
        self.quantity_spent_bullets = quantity_spent_bullets

    def run(self):
        ObjectInterFace.run(self)
