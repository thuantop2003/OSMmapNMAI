
import getfromgraph as gfg
import DijkstraAlgorithm as DA
import searchNode as SN
import osmnx as ox
import GBFSAlgorithm as GBF
path=r'data\QTGfull.graphml'
osmpath=r'data\map.osm'
G=gfg.getgraph(path)
print(GBF.GBFSearch(G,"11059028995","10904656406"))
print(DA.DSearch(G,"11059028995","10904656406"))
