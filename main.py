from player import Player
from box_ import Box
from money import Money
from pistol import Pistol
from interface_bullets import InterFaceBullets

class Main():

    def __init__(self):
        self.player = Player(700, 100, 50, 75, 5, 0, 0.4)
        self.box_list = []
#        for i in range(0,3):
        self.box_list.append(Box(width/2-100, height/2+20, 35, 35, 0, 0, 0))
        self.player.load_box(self.box_list)
        #self.money = Money(width-150, 100, '$', 100)
        #self.player.load_money(self.money)
        #self.pistol = Pistol(0, 0, 100, 100, self.player)
        #self.intBullets = InterFaceBullets(0, 0, width-150, height-100, 0, 0, 11, 30, 0)
        #self.pistol.load_intBullets(self.intBullets)

    def run(self):
        self.player.run()
        #self.money.run()
        #self.pistol.run()
        #self.intBullets.run()
        for item in self.box_list:
            item.run()

    def dir_player(self, dir):
        self.player.move(dir)

#    def reload(self):
#        self.pistol.reload()

#    def shoot(self):
#        self.pistol.shoot()

    def delete_box(self):
        self.player.del_box()

    def build_box(self):
        self.player.build_box()
