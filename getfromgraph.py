import osmnx as ox
import networkx as nx
#lấy đồ thị ra khỏi file
def getgraph(filepath):
    try:
        G = ox.load_graphml(filepath)
        return G
    except Exception as e:
        print(f"Error: {e}")
        return None