from player import Player
from box_ import Box
from money import Money
from pistol import Pistol

class Main():

    def __init__(self):
        self.player = Player(700, 100, 50, 75, 5, 0, 0.2)
        self.box_list = []
#        for i in range(0,3):
        self.box_list.append(Box(width/2-100, height/2+20, 35, 35, 0, 0, 0))
        self.player.load_box(self.box_list)
        self.money = Money(width/2-100, height-100, 'Balance:', 100)
        self.player.load_money(self.money)
        self.pistol = Pistol(0, 0, 100, 100, self.player)

    def run(self):
        self.player.run()
        self.money.run()
        self.pistol.run()
        for item in self.box_list:
            item.run()

    def dir_player(self, dir):
        self.player.move(dir)

    def shoot(self):
        self.pistol.shoot()

    def delete_box(self):
        self.player.del_box()

    def build_box(self):
        self.player.build_box()
        self.player.buy_box()
