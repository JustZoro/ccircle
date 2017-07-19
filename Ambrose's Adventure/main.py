import ccircle
import world

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()
imageBG = ccircle.Image("image/AA_Cabin(Inside).png")

ambrose = world.Ambrose(678, 109)
while window.isOpen():
    window.clear(1, 1, 1)
    dt = 1/60
    imageBG.draw(2, 0, 1400, 730)

    ambrose.update(dt)
    ambrose.draw()

    window.update()