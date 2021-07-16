class ObjectInterFace():

    def __init__(self, x, y, xt, yt, w, h, score, score2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.score = score
        self.score2 = score2
        self.xt = xt
        self.yt = yt

    def run(self):
        self.show()
        self.show_text()

    def show(self):
        fill(0,0,0)
        rect(self.x, self.y, self.w, self.h)

    def show_text(self):
        fill(0,0,0)
        text(str(self.score) +'/'+ str(self.score2) , self.xt, self.yt)
