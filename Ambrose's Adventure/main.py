import ccircle

window = ccircle.Window("Ambroses Adventure")
window.toggleMaximized()

for i in range(2):
    imageBG = ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_Coty(2).gif")
    image = ccircle.Image("C:/Users/FLL234-06/PycharmProjects/ccircle/Ambrose's Adventure/image/AA_AmbroseBehind.png")
while window.isOpen():
    window.clear(1, 1, 1)
    imageBG.draw(2, 0, 1599, 920)
    image.draw(470, 450, 199, 229)

    dt = 1.0 / 60.0

    window.update()