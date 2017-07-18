import ccircle
from math import*

window = ccircle.Window("Tic Tac Toe",600,600)
window.toggleMaximized()


image = ccircle.Image("C:/Users/FLL234-06/Downloads/adorable.jpg")

while window.isOpen():
    window.clear(1, 1, 1)
    image.draw(200, 30, 1266, 1266)
    window.drawLine(700, 100, 700, 700, 20, 0, 0, 0)
    window.drawLine(900, 100, 900, 700, 20, 0, 0, 0)
    window.drawLine(500, 300, 1100, 300, 20, 0, 0, 0)
    window.drawLine(500, 500, 1100, 500, 20, 0, 0, 0)

    mx, my = window.getMousePos()
    if ccircle.isMouseDown('left'):
        print(window.getMousePos())
    window.update()