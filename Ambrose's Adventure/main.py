import ccircle
from Ambrose import*
import time

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()
size = window.getSize()
imageBG = ccircle.Image("image/AA_Cabin(Inside).png")

ambrose = Ambrose(678, 109)
last = time.perf_counter()
dt = 1 / 60
while window.isOpen():
    window.clear(1, 1, 1)
    imageBG.draw(0, 2, 1630, 830)

    ambrose.update(dt)
    ambrose.draw()

    window.update()

    now = time.perf_counter()
    dt = now - last
    last = now