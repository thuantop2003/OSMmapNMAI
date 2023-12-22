
import getfromgraph as gfg
import DijkstraAlgorithm as DA
import searchNode as SN
import osmnx as ox
import GBFSAlgorithm as GBF
path=r'data\QTGfull.graphml'
osmpath=r'data\map.osm'
G=gfg.getgraph(path)
print(SN.findNearNodeidForfinish(21.0295689,105.8273507,G))
#print(SN.distance_from_point_to_line(21.0244681,105.8244233,21.0244681,105.8244233,21.0244681,105.8244233))
