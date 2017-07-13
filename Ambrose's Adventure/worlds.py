import ccircle
class worlds:
    def __init__(self, **kwargs):
        self.imageBG = ccircle.Image('AA_Cabin(Inside).png')

window = ccircle.Window("Cabin", 2021, 2021)
while window.isOpen():
        window.clear(0, 0, 0)
