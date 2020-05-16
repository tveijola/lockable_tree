from graphics import *
from node import Node

def draw_node(coord=Point(0,0), win=None):
    circle = Circle(coord, radius=5)
    circle.draw(win)

nodes = []
rootNode = Node()

win = GraphWin(width=200, height=200)
draw_node()
win.getMouse()

