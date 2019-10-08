import Node
from typing import List

class Graph:

    def __init__(self, nodes : List[Node.Node]):

        self.nodes = nodes

    def getNodes(self):
        return self.nodes