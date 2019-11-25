import random
import math
from tsplib95 import distances
import networkx
import Graph, Node, Edge
from typing import List

class Utils:

    INITIALPOINT = "nodoInicial"
    FINALPOINT = "nodoFinal"
    FEROMONERATE = "taxaFeromona"
    DISTANCE = "distancia"
    EDGES = "edges"
    EDGE1 = "edge1"
    EDGE2 = "edge2"
    EDGE3 = "edge3"
    EDGE4 = "edge4"
    NODEA = "nodeA"
    NODEB = "nodeB"
    NODEC = "nodeC"
    NODED = "nodeD"
    NODEE = "nodeE"

    dictA = {INITIALPOINT : 'A', EDGE1 : {INITIALPOINT: 'A', FINALPOINT: 'B', DISTANCE: 2, FEROMONERATE : 0.1},
                               EDGE2 : {INITIALPOINT: 'A', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.1},
                               EDGE3 : {INITIALPOINT: 'A', FINALPOINT: 'D', DISTANCE: 5, FEROMONERATE: 0.2},
                               EDGE4 : {INITIALPOINT: 'A', FINALPOINT: 'E', DISTANCE: 5, FEROMONERATE: 0.2}
    }

    dictB = {INITIALPOINT: 'B', EDGE1: {INITIALPOINT: 'B', FINALPOINT: 'A', DISTANCE: 2, FEROMONERATE: 0.1},
                                EDGE2 : {INITIALPOINT: 'B', FINALPOINT: 'C', DISTANCE: 2, FEROMONERATE: 0.1},
                                EDGE3 : {INITIALPOINT: 'B', FINALPOINT: 'D', DISTANCE: 4, FEROMONERATE: 0.2},
                                EDGE4 : {INITIALPOINT: 'B', FINALPOINT: 'E', DISTANCE: 6, FEROMONERATE: 0.3}
    }

    dictC = {INITIALPOINT: 'C', EDGE1: {INITIALPOINT: 'C', FINALPOINT: 'A', DISTANCE: 5, FEROMONERATE: 0.1},
                                EDGE2 :  {INITIALPOINT: 'C', FINALPOINT: 'B', DISTANCE: 2, FEROMONERATE: 0.1},
                                EDGE3 : {INITIALPOINT: 'C', FINALPOINT: 'D', DISTANCE: 5, FEROMONERATE: 0.5},
                                EDGE4 :  {INITIALPOINT: 'C', FINALPOINT: 'E', DISTANCE: 5, FEROMONERATE: 0.1}
    }

    dictD = {INITIALPOINT: 'D', EDGE1: {INITIALPOINT: 'D', FINALPOINT: 'A', DISTANCE: 5, FEROMONERATE: 0.2},
                                EDGE2 : {INITIALPOINT: 'D', FINALPOINT: 'B', DISTANCE: 4, FEROMONERATE: 0.2},
                                EDGE3 : {INITIALPOINT: 'D', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.5},
                                EDGE4 : {INITIALPOINT: 'D', FINALPOINT: 'E', DISTANCE: 6, FEROMONERATE: 0.6}
    }

    dictE = {INITIALPOINT: 'E', EDGE1: {INITIALPOINT: 'E', FINALPOINT: 'A', DISTANCE: 3, FEROMONERATE: 0.2},
                                EDGE2 : {INITIALPOINT: 'E', FINALPOINT: 'B', DISTANCE: 6, FEROMONERATE: 0.3},
                                EDGE3 : {INITIALPOINT: 'E', FINALPOINT: 'C', DISTANCE: 5, FEROMONERATE: 0.1},
                                EDGE4 : {INITIALPOINT: 'E', FINALPOINT: 'D', DISTANCE: 6, FEROMONERATE: 0.6}
    }

    dictOfNodes = {
        NODEA: dictA,
        NODEB: dictB,
        NODEC: dictC,
        NODED: dictD,
        NODEE: dictE,
    }

def euclidean_jitter(a, b):
    dist = distances.euclidean(a, b) # works for n-dimensions
    return dist * random.random() * 2

def putAsciiValues(value, numberNodes):

    '''
    :param value: value of Node
    :param numberNodes: nº de nós existente no grafo
    :return: ascii correspondente, começando na letra A--> 1 é A, 2 é B, e por aí fora
    '''

    initialValue = 65 # ascii number of 'A'

    return chr(initialValue+value)

def getConvertedEdges(graph : networkx.Graph):

    convertedEdges = [[0] * (graph.number_of_nodes()-i) for i in range(graph.number_of_nodes())] #--> Desta forma para evitar que as linhas sejam todas a msm referencia --> https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly

    counter = 0
    for i in range(len(graph.nodes)):
        counter = 0
        for u, v, data in graph.edges(data=True):
            if i == u:
                itemArgs = { Utils.INITIALPOINT : putAsciiValues(u, graph.number_of_nodes()), Utils.FINALPOINT : putAsciiValues(v, graph.number_of_nodes()), Utils.DISTANCE : data['weight']}
                convertedEdges[i][counter] = Edge.Edge(**itemArgs)
                counter = counter + 1

    return convertedEdges

def getConvertedNodes(graph : networkx.Graph):

    convertedNodes = [0] * graph.number_of_nodes()

    convertedEdges = getConvertedEdges(graph)

    for i in range(graph.number_of_nodes()):
        convertedNodes[i] = Node.Node(putAsciiValues(i, graph.number_of_nodes()), convertedEdges[i])

    return convertedNodes

def convertNetworkxToGraphObject(graph : networkx.Graph):

    '''

    :param graph: Networkx Graph
    :return: Graph Object converted from Networkx Graph
    '''

    try:

        convertedNodes = getConvertedNodes(graph)

        #CRIACAO DO GRAFO
        convertedGraph = Graph.Graph(convertedNodes)

        return convertedGraph
    except:
        raise