class eevee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tx = x
        self.ty = y
        self.image = [

            ccircle.Image('eevee.png'),
            ccircle.Image('eevee.png'),
            ccircle.Image('eevee.png'),
        ]
        self.facing = South


    def draw(self, window):
        window.draw(788, 1000, 566, 300)
        self.image[self.facing].draw(788, 1000, 566, 300)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)