import networkx as nx
import matplotlib.pyplot as plt

import listcolouring
from listcolouring import list_init, greedy_list_edge_colouring, print_list_edge_colouring

G = nx.petersen_graph()

G = list_init(G, range(0, 10), 3, 0)
G = greedy_list_edge_colouring(G)
    
colors = nx.get_edge_attributes(G,'colour').values()

options = {'with_labels': False, "edge_cmap": plt.cm.tab10}

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)
nx.draw(G, G_layout, edge_color = colors, width = 5, node_size = 150, node_color = 'grey', **options)
edge_labels = dict([((n1, n2), str(d['colour']) + ': ' + str(d['permissible'])) for n1, n2, d in G.edges(data = True)])

nx.draw_networkx_edge_labels(G, pos = G_layout, edge_labels = edge_labels, font_size = 6)

plt.savefig("png/petersen-shell.png", format = "PNG")
