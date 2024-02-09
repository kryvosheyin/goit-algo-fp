import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def bfs_traversal(root, colors):
    global color_index
    queue = deque([root])
    color_index = 0
    while queue and color_index < len(colors):
        current_node = queue.popleft()
        current_node.color = colors[color_index]
        color_index += 1

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def dfs_traversal(node, colors):
    global color_index
    if node is None or color_index >= len(colors):
        return

    node.color = colors[color_index]
    color_index += 1

    if node.left:
        dfs_traversal(node.left, colors)
    if node.right:
        dfs_traversal(node.right, colors)


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def generate_color_gradient(start_color, end_color, steps):
    start = [int(start_color[i : i + 2], 16) for i in (1, 3, 5)]
    end = [int(end_color[i : i + 2], 16) for i in (1, 3, 5)]
    gradient = []

    for i in range(steps):
        intermediate_color = [
            start[j] + (end[j] - start[j]) * i // (steps - 1) for j in range(3)
        ]
        gradient.append(
            "#" + "".join(["{:02x}".format(int(x)) for x in intermediate_color])
        )

    return gradient


color_index = 0


def main():
    colors = generate_color_gradient("#003366", "#99CCFF", 15)

    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)

    draw_tree(root)
    dfs_traversal(root, colors)
    draw_tree(root)
    bfs_traversal(root, colors)
    draw_tree(root)


if __name__ == "__main__":
    main()
