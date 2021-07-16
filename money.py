from object_msg import ObjectMSG

class Money(ObjectMSG):

    def __init__(self, x, y, msg, score):
        ObjectMSG.__init__(self, x, y, msg, score)

    def run(self):
        ObjectMSG.show(self)
