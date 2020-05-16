from graphics import *
import math
from node import Node

def draw_node(n, win=None):
    circle = Circle(Point(n.x, n.y), radius=n.r)
    circle.setFill("gray")
    circle.draw(win)
    connect(n, win)
    return circle

def connect(n, win=None):
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

def getClickedNode(nodes, p):
    for node in nodes:
        if math.sqrt((node.x - p.x) ** 2 + (node.y - p.y) ** 2) < node.r:
            return node
    return None

w, h = 1500, 1000

rootNode = Node(w/2, 60, 20)
nodes = [rootNode]
# Create nodes
for i in range(31):
    node = nodes[i]
    print("Creating children for node num: {} [depth {}]".format(i, node.depth))
    nodes.append(node.create_left_child())
    nodes.append(node.create_right_child())

window = GraphWin(width=w, height=h)
graph_nodes = {}
# Draw nodes
for node in nodes:
    circle = draw_node(node, window)
    graph_nodes[node] = circle

unlock_all_button = Rectangle(Point(50, 50), Point(150, 100))
unlock_all_button.draw(window)
label = Text(unlock_all_button.getCenter(), "UNLOCK ALL")
label.draw(window)

try:
    while True:
        point = window.getMouse()
        node = getClickedNode(nodes, point)
        if node is None:
            p1 = unlock_all_button.getP1()
            p2 = unlock_all_button.getP2()
            if p1.x < point.x < p2.x and p1.y < point.y < p2.y:
                for node in nodes:
                    node.unlock()
                    graph_nodes[node].setFill("gray")
            continue
        if not node.is_locked:
            success = node.lock()
            if success:
                graph_nodes[node].setFill("red")
        elif node.is_locked:
            node.unlock()
            graph_nodes[node].setFill("gray")

except GraphicsError:
    window.close()
finally:
    window.close()


