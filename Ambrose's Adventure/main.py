import ccircle
import worlds

window = ccircle.Window("Ambroses Adventure")
my_world = worlds.World('AA_Coty(2).gif')
window.toggleMaximized()
print(dir(my_world))

for i in range(2):
    image = ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseBehind.png")
while window.isOpen():
    my_world.draw(window)
    image.draw(2, 0, 1599, 900)

    dt = 1.0 / 60.0

    my_world.update(dt)
    window.update()