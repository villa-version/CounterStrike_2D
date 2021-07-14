from player import Player
from box_ import Box

class Main():

    def __init__(self, box_img):
        self.player = Player(700, 100, 50, 75, 5, 0, 0.2)
        self.box_list = []
        for i in range(0,3):
            self.box_list.append(Box(width/2-100, height/2+20-i*35, 35, 35, 0, 0, box_img, 0))
        self.player.load_box(self.box_list)

    def run(self):
        self.player.run()
        for item in self.box_list:
            item.run()

    def dir_player(self, dir):
        self.player.move(dir)
