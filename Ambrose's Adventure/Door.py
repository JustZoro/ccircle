class Door:
    def __init__(self, x, y, width, height, link, linkx, linky):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.link = link
        self.linkx = linkx
        self.linky = linky

    def getType(self):
        return "door"

    def draw(self, window):
        window.drawRect(self.x, self.y, self.width, self.height, 1, 0, 0, 0.25)

    def update(self, dt):
        pass