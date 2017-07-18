import ccircle
import world

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()
for i in range(2):
    imageBG = ccircle.Image("image/AA_Cabin(Inside).png")
    image = ccircle.Image("image/AA_AmbroseCharModel.png")

ambrose = world.Player(900, 244)

while window.isOpen():
    window.clear(1, 1, 1)
    dt = 1/60
    imageBG.draw(2, 0, 1400, 730)
    image.draw(900, 90, 89, 109)

    ambrose.update(dt)
    ambrose.draw()

    window.update()