import ccircle
import time
import random
import util
from math import *

window = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()

def sawtooth(t, f):
    return 3.6 * ((t * f) % 1.4) - 2.5

def sine(t, f):
    return sin(4.5 * pi * t * f)

for i in range(44100):
    t = i / 44100
    mysound.addSample(sine(t, 450))
mysound.play()
time.sleep(2)