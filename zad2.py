#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()

nodes = random.randint(1,10)
G.add_node(nodes)

for (a, b) in ((1, 4), (1, 2), (2, 5), (3, 6), (4, 2), (4, 5), (4, 6), (5, 6), (7, 2), (7, 9), (8, 1), (8, 4), (9, 2), (9, 10), (9, 1), (10, 5)):
    G.add_edge(a, b)

G.nodes(data=True)

G.edges(data=True)

nx.draw(G, with_labels=True, font_weight='bold', node_size=300, node_shape='o', node_color='red', edge_color='blue', style='dotted')

plt.show()
