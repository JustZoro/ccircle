import ccircle
class world:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)
        obj.world = self

    def draw(self, window):
        maxX, maxY = window.getSize()
        window.drawRect(0, 0, maxX, maxY, 0, 0.9, 1)
        window.drawRect(0, maxY - 100, maxX, 100, 0, 1, 0)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

