import heapq as heap
import time
import xmltodict
from haversine import haversine
from searchNode import *

doc = {}
with open("data\QTGfull.graphml", "r", encoding="utf-8") as fd:
    doc = xmltodict.parse(fd.read())


def calculateHeuristic(curr, destination):
    return haversine(curr, destination)


def getNeighbours(OSMId, destinationLatLon):
    neighbourDict = {}
    tempList = []
    edges = doc["graphml"]["graph"]["edge"]
    for eachEdge in range(len(edges)):
        if edges[eachEdge]["@source"] == str(OSMId):
            temp_nbr = {}

            neighbourCost = 0
            neighbourId = edges[eachEdge]["@target"]
            neighbourLatLon = getLatLon(neighbourId)

            dataPoints = edges[eachEdge]["data"]
            for eachData in range(len(dataPoints)):
                if dataPoints[eachData]["@key"] == "d13":
                    neighbourCost = dataPoints[eachData]["#text"]

            neighborHeuristic = calculateHeuristic(neighbourLatLon, destinationLatLon)

            temp_nbr[neighbourId] = [neighbourLatLon, neighbourCost, neighborHeuristic]
            tempList.append(temp_nbr)

    neighbourDict[OSMId] = tempList
    return neighbourDict


def getNeighbourInfo(neighbourDict):
    neighbourId = 0
    neighbourHeuristic = 0
    neighbourCost = 0
    for key, value in neighbourDict.items():
        neighbourId = key
        neighbourHeuristic = float(value[2])
        neighbourCost = float(value[1]) / 1000
        neighbourLatLon = value[0]

    return neighbourId, neighbourHeuristic, neighbourCost, neighbourLatLon


def getLatLon(OSMId):
    lat, lon = 0, 0
    nodes = doc["graphml"]["graph"]["node"]
    for eachNode in range(len(nodes)):
        if nodes[eachNode]["@id"] == str(OSMId):
            lat = float(nodes[eachNode]["data"][0]["#text"])
            lon = float(nodes[eachNode]["data"][1]["#text"])
    return (lat, lon)


def aStar(sourceID, destinationID):
    open_list = []
    g_values = {}

    path = {}
    closed_list = {}

    source = getLatLon(sourceID)
    destination = getLatLon(destinationID)
    g_values[sourceID] = 0
    h_source = calculateHeuristic(source, destination)

    open_list.append((h_source, sourceID))

    s = time.time()
    while len(open_list) > 0:
        curr_state = open_list[0][1]

        # print(curr_state)
        heap.heappop(open_list)
        closed_list[curr_state] = ""

        if curr_state == destinationID:
            print("We have reached to the goal")
            break

        nbrs = getNeighbours(curr_state, destination)
        values = nbrs[curr_state]
        for eachNeighbour in values:
            (
                neighbourId,
                neighbourHeuristic,
                neighbourCost,
                neighbourLatLon,
            ) = getNeighbourInfo(eachNeighbour)
            current_inherited_cost = g_values[curr_state] + neighbourCost

            if neighbourId in closed_list:
                continue
            else:
                g_values[neighbourId] = current_inherited_cost
                neighbourFvalue = neighbourHeuristic + current_inherited_cost

                open_list.append((neighbourFvalue, neighbourId))

            path[str(neighbourLatLon)] = {
                "parent": str(getLatLon(destinationID)),
                "cost": neighbourCost,
            }

        open_list = list(set(open_list))
        heap.heapify(open_list)

    print("Time taken to find path(in second): " + str(time.time() - s))
    return path
