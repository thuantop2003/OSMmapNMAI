import getfromgraph as gfg
import DijkstraAlgorithm as DA
import searchNode as SN
import osmnx as ox

path = "data\\QTGfull.graphml"
osmpath = "data\\map.osm"
G = ox.graph_from_bbox(
    21.02743,
    21.02221,
    105.83977,
    105.82522,
    network_type="all_private",
    retain_all=True,
)
print(DA.DSearch(G, "1497544796", "5704011550"))
print(SN.findNearNodeid("1497544796", osmpath, G))
