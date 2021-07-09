from player import Player

class Main():

    def __init__(self):
        self.player = Player(width/2, 100, 50, 75, 5, 0)

    def run(self):
        self.player.run()

    def dir_player(self, dir):
        self.player.move(dir)
