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
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel.png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel(2).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel(6).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel(3).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel(4).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseCharModel(5).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseSideStop.png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseSideW.png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseSideW(2).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseBehind.png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseBehind(W).png"),
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseBehind(W2).png"),
        ]
        self.facing = West

    def draw(self, x, y, s, window):
        self.image[self.facing].draw(x, y, s, s)

    def getName(self):
        return 'pusheen'

    def update(self, dt):
        pass

    def Player(self):
        return
        if ccircle.isKeyDown('left'):
            args['vy'] = 0
            args['vx'] = -50
        if ccircle.isKeyDown('right'):
            args['vy'] = 0
            args['vx'] = 50
        if ccircle.isKeyDown('up'):
            args['vy'] = -50
            args['vx'] = 0
        if ccircle.isKeyDown('down'):
            args['vy'] = 50
            args['vx'] = 0



