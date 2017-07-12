import ccircle
import worlds
import time
import Cabin

window = ccircle.Window('Ambroses Adventure', 1200, 1200)
my_world = world.World('Cabin')


while window.isOpen:
    window.clear(0,0,0)
    window.drawRect(990, 560, 1100, 1100)

    my_world.update(dt)
    window.update()
