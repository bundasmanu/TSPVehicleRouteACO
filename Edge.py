import Utils

class Edge:

    '''
    Esta classe representa, as arestas inerentes à ligacao
    entre os vários nodos, de um grafo
    '''

    def __init__(self, **kwargs):

        '''
        4 atributos
        :param kwargs:
            - Ponto Inicial --> Representa o nodo inicial da aresta;
            - Ponto Final --> Representa o nodo final da aresta;
            - Distancia --> Representa a distancia entre os nodos
            - Taxa de Feromonas --> na aresta
        '''

        self.pInicial = kwargs.get(Utils.Utils.INITIALPOINT)
        self.pFinal = kwargs.get(Utils.Utils.FINALPOINT)
        self.distance = kwargs.get(Utils.Utils.DISTANCE)
        self.pheromoneTax = kwargs.get(Utils.Utils.FEROMONERATE)


    def getPInicial(self):
        return self.pInicial

    def setPInicial(self, newPInicial):
        self.pInicial=newPInicial

    def getPFinal(self):
        return self.pFinal

    def setPFinal(self, newPFinal):
        self.pFinal=newPFinal

    def getDistance(self):
        return self.distance

    def setDistance(self, newDistance):
        self.distance=newDistance

    def getPheromoneTax(self):
        return self.pheromoneTax

    def setPheromoneTax(self, newPheromoneTax):
        self.pheromoneTax= newPheromoneTax

    def __str__(self):
        return "\n"+self.pInicial+"\t"+self.pFinal+"\t"+str(self.distance)+"\t"+str(self.pheromoneTax)+"\n"