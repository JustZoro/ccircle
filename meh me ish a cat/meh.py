import ccircle
import world
import random
import Ball
import time
import eevee

window = ccircle.Window('Ambroses Adventure', 800, 600)
my_world = world.World('city')
print(dir(my_world))

for i in range(10):
    my_ball = Ball.Ball(random.randint(0, 800), random.randint(100, 150))
    my_world.add(my_ball)

my_ball = Ball.Ball(100, 100)
my_world.add(my_ball)

while window.isOpen():
    my_world.draw(window)

    start = time.time()
    dt = 1.0 / 60.0

    my_world.update(dt)
    window.update()