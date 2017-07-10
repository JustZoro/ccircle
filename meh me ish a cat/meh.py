import ccircle
import Masamune
import world
import random
import Ball
import time
import eevee

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('city')
print(dir(my_world))

for i in range(200):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = 25 + 75 * (random.uniform(0, 1) ** 2)
    vx = random.uniform(0, 100)
    my_world.add(cloud.Cloud(x, y, size, vx))




my_ball = ball.Ball(400, 300)
my_world.add(my_ball)

start = time.time()
dt = 1.0 / 60.0
