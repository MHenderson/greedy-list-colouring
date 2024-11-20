import networkx as nx
import matplotlib.pyplot as plt

import listcolouring

from listcolouring import list_init, list_init_node, greedy_list_total_colouring

G = nx.petersen_graph()

G = list_init_node(G, range(0, 9), 3, 0)
G = list_init(G, range(0, 9), 3, 0)

G = greedy_list_total_colouring(G)

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)

edge_labels = dict([((n1, n2), str(d['colour']) + ': ' + str(d['permissible'])) for n1, n2, d in G.edges(data = True)])
node_labels = dict([(n, str(d['colour']) + ': ' + str(d['permissible'])) for n, d in G.nodes(data = True)])

nx.draw(G,      
          pos = G_layout,
   edge_color = nx.get_edge_attributes(G,'colour').values(),
   node_color = list(nx.get_node_attributes(G, 'colour').values()),
        width = 10,
    node_size = 1300,
         cmap = plt.cm.tab10,
    edge_cmap = plt.cm.tab10,
  with_labels = False
)

edge_labels_ = nx.draw_networkx_edge_labels(G, pos = G_layout, edge_labels = edge_labels, font_size = 6)
node_labels_ = nx.draw_networkx_labels(G, pos = G_layout, labels = node_labels, font_size = 6)

plt.savefig("png/petersen-shell-total.png", format = "PNG")
