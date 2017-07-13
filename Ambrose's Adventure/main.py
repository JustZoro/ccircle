import ccircle
import rooms
import Ambrose

window = ccircle.Window("Ambroses Adventure", 2021, 2021)
rooms = Ambrose.Rooms(place.Player)

time = 0
while window.isOpen():
    window.clear(0, 0, 0)
    window.update()
    room.update(dt)


