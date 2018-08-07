#!/usr/bin/env python
import logging
import os

from pngcanvas import *

logging.getLogger().setLevel(logging.DEBUG)

HEIGHT = WIDTH = 500
STEP = 50

logging.debug("Creating canvas: %d, %d", WIDTH, HEIGHT)
c = PNGCanvas(WIDTH, HEIGHT, color=(0xff, 0, 0, 0xff))

logging.debug("Drawing grid...")
c.color = bytearray((0, 0, 0, 0xff))

for i in range(0, WIDTH, STEP):
    c.line(i, 0, i, HEIGHT)

for j in range(0, HEIGHT, STEP):
    c.line(0, j, WIDTH, j)


def draw_dot(x, y, size=10, color=(0, 0, 0)):
    c.color = toByteArray(color)
    c.filled_rectangle(x * STEP - size / 2, HEIGHT - y * STEP - size / 2, x * STEP + size / 2,
                       HEIGHT - y * STEP + size / 2)


def toByteArray(triplet):
    return bytearray((triplet[0], triplet[1], triplet[2], 0xff))


def draw_line(x1, y1, x2, y2, color=(0, 0, 0)):
    c.color = toByteArray(color)
    c.line(x1 * STEP, HEIGHT - y1 * STEP, x2 * STEP, HEIGHT - y2 * STEP)


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

draw_dot(0, 0)
draw_dot(1, 2, color=blue)
draw_dot(10, 10, size=20, color=red)

draw_line(1, 0, 0, 1)
draw_line(2, 3, 5, 7, color=red)
draw_line(0, 5, 5, 2, green)
draw_line(2, 8, 9, 10, blue)

with open("image.png", "wb") as png_fil:
    logging.debug("Writing to file...")
    png_fil.write(c.dump())

cmd = 'cmd /c' if os.name == 'nt' else 'xdg-open'
os.system('%s image.png' % cmd)
