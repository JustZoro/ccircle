import ccircle
North = 0
East = 1
South = 2
West = 3

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tx = x
        self.ty = y
        self.image = [
            ccircle.Image("image/AA_AmbroseCharModel.png"),
            ccircle.Image("image/AA_AmbroseCharModel(2).png"),
            ccircle.Image("image/AA_AmbroseCharModel(6).png"),
            ccircle.Image("image/AA_AmbroseCharModel(3).png"),
            ccircle.Image("image/AA_AmbroseCharModel(4).png"),
            ccircle.Image("image/AA_AmbroseCharModel(5).png"),
            ccircle.Image("image/AA_AmbroseSideStop.png"),
            ccircle.Image("image/AA_AmbroseSideW.png"),
            ccircle.Image("image/AA_AmbroseSideW(2).png"),
            ccircle.Image("image/AA_AmbroseBehind.png"),
            ccircle.Image("image/AA_AmbroseBehind(W).png"),
            ccircle.Image("image/AA_AmbroseBehind(W2).png"),
        ]

    if Player.isFacingE():
        image.draw("")

    def draw(self):
        self.image[self.facing].draw(900, 240, 89, 109)

    def getName(self):
        return 'pusheen'

    def update(self, dt):
        if ccircle.isKeyDown('left'):
            self.y = 0
            self.x = -50
        if ccircle.isKeyDown('right'):
            self.y = 0
            self.x = 50
        if ccircle.isKeyDown('up'):
            self.y = -50
            self.x = 0
        if ccircle.isKeyDown('down'):
            self.y = 50
            self.x = 0



