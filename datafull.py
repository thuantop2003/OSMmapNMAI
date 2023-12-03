import osmium

class OSMHandler(osmium.SimpleHandler):
    def node(self, n):
        print(f"Node {n.id} at lon={n.location.lon}, lat={n.location.lat}")

    def way(self, w):
        print(f"Way {w.id} with nodes {', '.join(map(str, w.nodes))}")

if __name__ == '__main__':
    osm_file = r'C:\Users\Lenovo\Downloads\map.osm'
    handler = OSMHandler()
    handler.apply_file(osm_file)
