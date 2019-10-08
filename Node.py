import Edge
from typing import List

class Node:

    def __init__(self, edges : List[Edge.Edge]):

        self.edges=edges

    def getEdges(self):
        return self.edges