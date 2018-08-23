from pngcanvas import *
import logging
import os


class Graph(object):

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, width=500, height=500, step=50):
        self.width = width
        self.height = height
        self.step = step
        self.create_canvas()
        self.create_grid()

    def create_canvas(self):
        logging.debug("Creating canvas: %d, %d", self.width, self.height)
        self.canvas = PNGCanvas(self.width, self.height, color=(0xff, 0, 0, 0xff))

    def create_grid(self):
        logging.debug("Drawing grid...")
        self.canvas.color = bytearray((0, 0, 0, 0xff))
        for i in range(0, self.width, self.step):
            self.canvas.line(i, 0, i, self.height)

        for j in range(0, self.height, self.step):
            self.canvas.line(0, j, self.width, j)

    def draw_dot(self, x, y, size=10, color=(0, 0, 0)):
        self.canvas.color = self.to_byte_array(color)
        self.canvas.filled_rectangle(x * self.step - size / 2, self.height - y * self.step - size / 2, x * self.step + size / 2,
                       self.height - y * self.step + size / 2)

    @staticmethod
    def to_byte_array(triplet):
        return bytearray((triplet[0], triplet[1], triplet[2], 0xff))

    def draw_line(self, x1, y1, x2, y2, color=(0, 0, 0)):
        self.canvas.color = self.to_byte_array(color)
        self.canvas.line(x1 * self.step, self.height - y1 * self.step, x2 * self.step, self.height - y2 * self.step)

    def save(self):
        logging.debug("Writing to file...")
        with open("image.png", "wb") as png_fil:
            png_fil.write(self.canvas.dump())

        cmd = 'cmd /c' if os.name == 'nt' else 'xdg-open'
        os.system('%s image.png' % cmd)


