import ccircle
from math import*

window = ccircle.Window()
window.toggleMaximized()
window.hideMouse()

points = []

while window.isOpen():
    window.clear(0.2, 0.2, 0.2)
    mx, my = window.getMousePos()

    if ccircle.isMouseDown('left'):
        points.append((mx, my))

    for point in points:
        window.drawCircle(point[0], point[1], 8, 0.1, 0.5, 1.0)
    # == -> equal to
    #!= -> not equal to
    # > -> greater than
    # >= -> greater than or equal to
    # if len(points) >= 21:
    #    window.drawCircle(points[20][0], points[20][1], 16, 1.0, 0.5, 0.1)

    window.drawCircle(mx, my, 8, 0.1, 0.5, 1.0)
    window.drawCircle(777, 455, 88, 0.788, 0.799, 0.566)
    window.drawTri(455, 488, 430, 487, 490, 488, 0.2, 0.2, 0.99)
    window.update()
