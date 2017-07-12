import ccircle

class Cabin:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)
        obj.world = self

    def draw(self, window):
        maxX, maxY = window.getSize()
        window.drawRect(990, 560, 1100, 1100)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)