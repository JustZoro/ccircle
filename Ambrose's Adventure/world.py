import ccircle

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
            ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/")
        ]