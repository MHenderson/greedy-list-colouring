import networkx as nx
import matplotlib.pyplot as plt

import listcolouring
from listcolouring import list_init, greedy_list_edge_colouring

G = nx.erdos_renyi_graph(10, 0.5, 0)

G = list_init(G, range(0, 20), 3, 0)
G = greedy_list_edge_colouring(G)

colors = nx.get_edge_attributes(G,'colour').values()

options = {'with_labels': True, "edge_cmap": plt.cm.tab20}
G_layout = nx.circular_layout(G)
nx.draw(G, G_layout, edge_color = colors, width = 5, node_size = 150, node_color = 'grey', **options)
edge_labels = dict([((n1, n2), str(d['colour']) + ': ' + str(d['permissible'])) for n1, n2, d in G.edges(data = True)])

nx.draw_networkx_edge_labels(G, pos = G_layout, edge_labels = edge_labels, font_size = 6)

plt.savefig("png/random-graph.png", format = "PNG")

