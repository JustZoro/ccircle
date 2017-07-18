import ccircle
import world

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()

for i in range(2):
    imageBG = ccircle.Image("image/AA_Cabin(Inside).png")
while window.isOpen():
    window.clear(1, 1, 1)
    imageBG.draw(2, 0, 1400, 730)

    dt = 1.0 / 60.0
    args = {
        'vx': -43,
        'vy': -24,
    }

    if ccircle.isKeyDown('left'):
        args['vy'] = 0
        args['vx'] = -50
    if ccircle.isKeyDown('right'):
        args['vy'] = 0
        args['vx'] = 50
    if ccircle.isKeyDown('up'):
        args['vy'] = -50
        args['vx'] = 0
    if ccircle.isKeyDown('down'):
        args['vy'] = 50
        args['vx'] = 0
    window.update()