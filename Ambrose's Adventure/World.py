class World:
    def __init__(self, bg, collision):
        self.bg = bg
        self.width, self.height = bg.getSize()
        self.collision = collision
        self.objects = []

    def add(self, obj):
        obj.world = self
        self.objects.append(obj)

    def remove(self, obj):
        self.objects.remove(obj)

    def draw(self, window):
        sx, sy = window.getSize()
        window.drawRect(0, 0, sx, sy, 0, 0, 0)
        self.bg.draw(0, 0, self.width, self.height)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
