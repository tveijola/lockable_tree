from graphics import *
import math
from node import Node

def draw_node(n, win=None):
    circle = Circle(Point(n.x, n.y), radius=n.r)
    circle.draw(win)
    conn_parent(n, win)

def conn_parent(n, win=None):
    if n.parent is not None:
        alpha = math.atan((n.y - n.parent.y) / abs(n.x - n.parent.x))
        if n.x < n.parent.x:
            p1 = Point(n.x + n.r * math.cos(alpha), n.y - n.r * math.sin(alpha))
            p2 = Point(n.parent.x - n.parent.r * math.cos(alpha), n.parent.y + n.parent.r * math.sin(alpha))
        else:
            p1 = Point(n.x - n.r * math.cos(alpha), n.y - n.r * math.sin(alpha))
            p2 = Point(n.parent.x + n.parent.r * math.cos(alpha), n.parent.y + n.parent.r * math.sin(alpha))
        line = Line(p1, p2)
        line.draw(win)


w, h = 1000, 1000

rootNode = Node(w/2, 20, 20)
nodes = [rootNode]
# Create nodes
for i in range(9):
    node = nodes[i]
    print("Creating children for node num: {} [depth {}]".format(i, node.depth))
    nodes.append(node.create_left_child())
    nodes.append(node.create_right_child())

window = GraphWin(width=w, height=h)
for node in nodes:
    draw_node(node, window)

window.getMouse()
