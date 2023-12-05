import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

G = ox.graph_from_bbox(
    21.02743,
    21.02221,
    105.83977,
    105.82522,
    network_type="all_private",
    retain_all=True,
)
nx.draw(G)
plt.show()
