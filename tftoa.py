#!/usr/bin/env python

import os
import io
import logging

logging.getLogger().setLevel(logging.DEBUG)

from pngcanvas import *

HEIGHT = WIDTH = 512

logging.debug("Creating canvas: %d, %d", WIDTH, HEIGHT)
c = PNGCanvas(WIDTH, HEIGHT, color=(0xff, 0, 0, 0xff))
c.rectangle(0, 0, WIDTH - 1, HEIGHT - 1)

#logging.debug("Generating gradient...")
#c.vertical_gradient(1, 1, WIDTH - 2, HEIGHT - 2,
#    (0xff, 0, 0, 0xff), (0x20, 0, 0xff, 0x80))

logging.debug("Drawing some lines...")
c.color = bytearray((0, 0, 0, 0xff))

STEP = 10

for i in range(0, WIDTH, STEP):
    c.line(i, 0, i, HEIGHT)

for j in range(0, HEIGHT, STEP):
    c.line(0, j, WIDTH, j)

with open("try_pngcanvas.png", "wb") as png_fil:
    logging.debug("Writing to file...")
    png_fil.write(c.dump())

os.system('xdg-open try_pngcanvas.png')

