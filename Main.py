import acopy
import Utils
import networkx as nx
import Graph,Node,Edge

def createGraph():

    edgesA = [Edge.Edge(**{Utils.Utils.INITIALPOINT : Utils.Utils.dictA.get(Utils.Utils.EDGE1).get(Utils.Utils.INITIALPOINT),
                         Utils.Utils.FINALPOINT : Utils.Utils.dictA.get(Utils.Utils.EDGE1).get(Utils.Utils.FINALPOINT),
                         Utils.Utils.DISTANCE : Utils.Utils.dictA.get(Utils.Utils.EDGE1).get(Utils.Utils.DISTANCE),
                         Utils.Utils.FEROMONERATE : Utils.Utils.dictA.get(Utils.Utils.EDGE1).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE2).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE2).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictA.get(Utils.Utils.EDGE2).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictA.get(Utils.Utils.EDGE2).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE3).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE3).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictA.get(Utils.Utils.EDGE3).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictA.get(Utils.Utils.EDGE3).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE4).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictA.get(Utils.Utils.EDGE4).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictA.get(Utils.Utils.EDGE4).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictA.get(Utils.Utils.EDGE4).get(Utils.Utils.FEROMONERATE)}),
    ]

    edgesB = [Edge.Edge(**{Utils.Utils.INITIALPOINT : Utils.Utils.dictB.get(Utils.Utils.EDGE1).get(Utils.Utils.INITIALPOINT),
                         Utils.Utils.FINALPOINT : Utils.Utils.dictB.get(Utils.Utils.EDGE1).get(Utils.Utils.FINALPOINT),
                         Utils.Utils.DISTANCE : Utils.Utils.dictB.get(Utils.Utils.EDGE1).get(Utils.Utils.DISTANCE),
                         Utils.Utils.FEROMONERATE : Utils.Utils.dictB.get(Utils.Utils.EDGE1).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE2).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE2).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictB.get(Utils.Utils.EDGE2).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictB.get(Utils.Utils.EDGE2).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE3).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE3).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictB.get(Utils.Utils.EDGE3).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictB.get(Utils.Utils.EDGE3).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE4).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictB.get(Utils.Utils.EDGE4).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictB.get(Utils.Utils.EDGE4).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictB.get(Utils.Utils.EDGE4).get(Utils.Utils.FEROMONERATE)}),
    ]

    edgesC = [Edge.Edge(**{Utils.Utils.INITIALPOINT : Utils.Utils.dictC.get(Utils.Utils.EDGE1).get(Utils.Utils.INITIALPOINT),
                         Utils.Utils.FINALPOINT : Utils.Utils.dictC.get(Utils.Utils.EDGE1).get(Utils.Utils.FINALPOINT),
                         Utils.Utils.DISTANCE : Utils.Utils.dictC.get(Utils.Utils.EDGE1).get(Utils.Utils.DISTANCE),
                         Utils.Utils.FEROMONERATE : Utils.Utils.dictC.get(Utils.Utils.EDGE1).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE2).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE2).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictC.get(Utils.Utils.EDGE2).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictC.get(Utils.Utils.EDGE2).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE3).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE3).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictC.get(Utils.Utils.EDGE3).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictC.get(Utils.Utils.EDGE3).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE4).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictC.get(Utils.Utils.EDGE4).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictC.get(Utils.Utils.EDGE4).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictC.get(Utils.Utils.EDGE4).get(Utils.Utils.FEROMONERATE)}),
    ]

    edgesD = [Edge.Edge(**{Utils.Utils.INITIALPOINT : Utils.Utils.dictD.get(Utils.Utils.EDGE1).get(Utils.Utils.INITIALPOINT),
                         Utils.Utils.FINALPOINT : Utils.Utils.dictD.get(Utils.Utils.EDGE1).get(Utils.Utils.FINALPOINT),
                         Utils.Utils.DISTANCE : Utils.Utils.dictD.get(Utils.Utils.EDGE1).get(Utils.Utils.DISTANCE),
                         Utils.Utils.FEROMONERATE : Utils.Utils.dictD.get(Utils.Utils.EDGE1).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE2).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE2).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictD.get(Utils.Utils.EDGE2).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictD.get(Utils.Utils.EDGE2).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE3).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE3).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictD.get(Utils.Utils.EDGE3).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictD.get(Utils.Utils.EDGE3).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE4).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictD.get(Utils.Utils.EDGE4).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictD.get(Utils.Utils.EDGE4).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictD.get(Utils.Utils.EDGE4).get(Utils.Utils.FEROMONERATE)}),
    ]

    edgesE = [Edge.Edge(**{Utils.Utils.INITIALPOINT : Utils.Utils.dictE.get(Utils.Utils.EDGE1).get(Utils.Utils.INITIALPOINT),
                         Utils.Utils.FINALPOINT : Utils.Utils.dictE.get(Utils.Utils.EDGE1).get(Utils.Utils.FINALPOINT),
                         Utils.Utils.DISTANCE : Utils.Utils.dictE.get(Utils.Utils.EDGE1).get(Utils.Utils.DISTANCE),
                         Utils.Utils.FEROMONERATE : Utils.Utils.dictE.get(Utils.Utils.EDGE1).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE2).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE2).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictE.get(Utils.Utils.EDGE2).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictE.get(Utils.Utils.EDGE2).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE3).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE3).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictE.get(Utils.Utils.EDGE3).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictE.get(Utils.Utils.EDGE3).get(Utils.Utils.FEROMONERATE)}),
              Edge.Edge(**
                  {Utils.Utils.INITIALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE4).get(Utils.Utils.INITIALPOINT),
                   Utils.Utils.FINALPOINT: Utils.Utils.dictE.get(Utils.Utils.EDGE4).get(Utils.Utils.FINALPOINT),
                   Utils.Utils.DISTANCE: Utils.Utils.dictE.get(Utils.Utils.EDGE4).get(Utils.Utils.DISTANCE),
                   Utils.Utils.FEROMONERATE: Utils.Utils.dictE.get(Utils.Utils.EDGE4).get(Utils.Utils.FEROMONERATE)}),
    ]

    nodesList = [Node.Node("A", edgesA), Node.Node("B", edgesB), Node.Node("C" ,edgesC), Node.Node("D", edgesD), Node.Node("E" ,edgesE)]

    grafo = Graph.Graph(nodesList)

    return grafo

def main():

    print(Utils.Utils.dictOfNodes)
    grafo = createGraph()

if __name__ == "__main__":
    main()