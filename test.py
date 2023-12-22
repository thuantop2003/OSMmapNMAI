
import getfromgraph as gfg
import DijkstraAlgorithm as DA
import searchNode as SN
import osmnx as ox
import GBFSAlgorithm as GBF
path=r'data\QTGfull.graphml'
osmpath=r'data\map.osm'
G=gfg.getgraph(path)
print(SN.findNearNodeid(21.0240336,105.8291179,G))
#print(SN.distance_from_point_to_line(21.0244681,105.8244233,21.0244681,105.8244233,21.0244681,105.8244233))
