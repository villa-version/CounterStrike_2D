class ObjectMSG():

    def __init__(self, x, y, msg, score):
        self.x = x
        self.y = y
        self.msg = msg
        self.score = score

    def show(self):
        fill(0,0,0)
        text(self.msg + str(self.score), self.x, self.y)
