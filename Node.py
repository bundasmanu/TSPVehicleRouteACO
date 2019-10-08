import Edge
from typing import List

class Node:

    def __init__(self, name, edges : List[Edge.Edge]):
        self.name = name
        self.edges = edges

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getEdges(self):
        return self.edges