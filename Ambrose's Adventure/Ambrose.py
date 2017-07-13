import ccircle
import time

North = 0
East = 1
South = 2
West = 3

class Ambrose:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tx = x
        self.ty = y
        self.image = [

                ccircle.Image('AA_AmbroseBehind.png'),
                ccircle.Image('AA_AmbroseCharModel(3).png'),
                ccircle.Image('AA_AmbroseCharModel.png'),
                ccircle.Image('AA_AmbroseSideStop.png'),
        ]
        self.facing = West

    def draw(self, x, y, s, window):
        self.image[self.facing].draw(x, y, s, s)

    def getName(self):
            return 'pusheen'

    def update(self, dt):
            pass