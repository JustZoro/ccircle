import ccircle
class World:
    def __init__(self, name):
        self.name = name
        self.objects = []
        self.bg = ccircle.Image('eevee.png')


    def add(self, obj):
        self.objects.append(obj)
        obj.world = self

    def draw(self, window):
        maxX, maxY = window.getSize()
        self.bg.draw(0, 0, maxX, maxY)
        window.drawRect(0, maxY - 100, maxX, 100, 0.1, 0.15, 0.2)
        for obj in self.objects:
            obj.draw(window)

    def update(self):
        for obj in self.objects:
            obj.update(dt)


