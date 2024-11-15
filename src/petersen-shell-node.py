import networkx as nx
import matplotlib.pyplot as plt

import listcolouring

from listcolouring import list_init_node, greedy_list_node_colouring

G = nx.petersen_graph()
G = list_init_node(G, range(0, 6), 3, 0)

G = greedy_list_node_colouring(G)

colors = nx.get_node_attributes(G, 'colour').values()

options = {'with_labels': False, "edge_cmap": plt.cm.tab10}

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)
nx.draw(G, G_layout, edge_color = "grey", node_color = list(colors), width = 5, node_size = 250, **options)

plt.savefig("png/petersen-shell-node.png", format = "PNG")
