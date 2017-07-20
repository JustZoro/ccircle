import ccircle
from Ambrose import*
import time
from World import*
from Door import*

# Fix door in cabin
# Fix Ambrose starting pos
# Add door from outside to cabin
# Create mask for outside

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()
size = window.getSize()
imageBG = ccircle.Image("image/AA_Cabin(Inside).png")
Cabin = World(ccircle.Image("image/AA_Cabin(Inside).png"), ccircle.Image("image/AA_Cabin(Inside)_mask.png"))
Outside = World(ccircle.Image("image/AA_Outside.png"), ccircle.Image("image/AA_Cabin(Inside)_mask.png"))
Upstairs = World(ccircle.Image(""))
Cabin.add(Door(522, 635, 90, 45, Outside, 108, 158))
Outside.add(Door(100, 34, 34, 34, Cabin, 530, 625))
Cabin.add(Door(125, 210, 95, 34, Upstairs,))

ambrose = Ambrose(1285, 235)
Cabin.add(ambrose)
last = time.perf_counter()
dt = 1 / 60
while window.isOpen():
    window.clear(1, 1, 1)
    ambrose.world.draw(window)
    ambrose.world.update(dt)
    window.update()

    now = time.perf_counter()
    dt = now - last
    last = now