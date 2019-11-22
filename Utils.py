from typing import List
import Main

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
