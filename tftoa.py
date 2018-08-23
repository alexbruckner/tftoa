#!/usr/bin/env python
import sys
sys.path.append('./lib')
import logging
from graph import Graph
sys.path.append("./lib")
logging.getLogger().setLevel(logging.DEBUG)


graph = Graph(500, 500, 50)

graph.draw_dot(0, 0)
graph.draw_dot(1, 2, color=graph.BLUE)
graph.draw_dot(10, 10, size=20, color=graph.RED)

graph.draw_line(1, 0, 0, 1)
graph.draw_line(2, 3, 5, 7, color=graph.RED)
graph.draw_line(0, 5, 5, 2, graph.GREEN)
graph.draw_line(2, 8, 9, 10, graph.BLUE)

graph.save()
