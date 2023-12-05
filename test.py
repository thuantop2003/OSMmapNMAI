import getfromgraph as gfg
import DijkstraAlgorithm as DA
import searchNode as SN
import osmnx as ox
path=r'data\QTGfull.graphml'
osmpath=r'data\map.osm'
G=gfg.getgraph(path)
print(SN.findNearEdgeId("11059028947",osmpath))
print(SN.findNearNodeid("11059028947",osmpath,G))
print(DA.DSearch(G,"1497544796","5704011550"))

