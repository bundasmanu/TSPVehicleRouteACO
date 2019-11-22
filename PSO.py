import networkx as nx
import Graph,Node,Edge
import numpy

def valueToPredict(value):

    if value <= 0.2:
        return 'A'
    elif value > 0.2 and value <= 0.4:
        return 'B'
    elif value > 0.4 and value <= 0.6:
        return 'C'
    elif value > 0.6 and value <= 0.8:
        return 'D'
    else:
        return 'E'

def getSpaceBetweenNodes(numberNodes):

    return 1/numberNodes #--> Max Boundary é sempre 1, visto que divido por 1, na definicao do espaço entre cada nó do problema

def simuleNumpyOfNodeProbabilities(numberNodes):

    spaceBetweenNodes = getSpaceBetweenNodes(numberNodes)

    numpyArray = numpy.zeros(shape=(1, numberNodes))

    numpyArray = [spaceBetweenNodes+(i*spaceBetweenNodes) for i in range(numberNodes)]

    return numpyArray

def getSpecificNode(value, graph: Graph.Graph):

    for i in range(len(graph.getNodes())):
        if graph.getNodes()[i].getName() == value:
            return graph.getNodes()[i]

def getDistanceTwoNodes(vInicial, vFinal, graph: Graph.Graph):

    counter = -1

    for i in graph.getNodes():
        counter = counter + 1
        if i.getName() == vInicial.getName():
            tamEdges = len(graph.getNodes()[counter].getEdges())
            for j in range(tamEdges):
                if graph.getNodes()[counter].getEdges()[j].getPFinal() == vFinal.getName():
                    return graph.getNodes()[counter].getEdges()[j].getDistance()

    return 0

def countErrors(numpyValues):

    unique_elements, counts_elements = numpy.unique(numpyValues, return_counts=True)

    numberErrors = len(numpyValues) - len(counts_elements)

    return numberErrors

def costFunction(particles, graph : Graph.Graph):

    numberOfNodes = len(graph.getNodes())

    spaceBetweenNodes = getSpaceBetweenNodes(len(graph.getNodes()))

    nP = len(particles)
    quantos = -1
    nValues = 0
    realCounter = 0
    firstDimensionValue = particles[0]

    '''for i in range(len(graph.getNodes())):
        for x in range(nP):
            quantos = quantos + 1
            for j in range(nP-quantos):
                if x != j :
                    val = abs(particles[x]-particles[j])
                    if val > spaceBetweenNodes:
                        nValues = nValues + 1
                    if nValues == (nP- quantos):
                        realCounter = realCounter + 1'''

    vals = [valueToPredict(particles[i]) for i in range(nP)]

    numberOfErrors = countErrors(vals)

    cost = 0
    increase = 500

    cost = cost + (increase*numberOfErrors)

    numpyArr = simuleNumpyOfNodeProbabilities(len(graph.getNodes()))

    onlyOnce = 0
    for i in range(len(particles)-1):
        onlyOnce = onlyOnce + 1
        for j in range(len(numpyArr)):
            if particles[i] < j:
                vInicial = valueToPredict(particles[i])
                nInicial = getSpecificNode(vInicial,graph)
                vFinal = valueToPredict(particles[i+1])
                nFinal = getSpecificNode(vFinal, graph)
                cost = cost + getDistanceTwoNodes(nInicial, nFinal, graph)
                break


    backToInitialNode = valueToPredict(particles[len(particles)-1])
    finalNode = getSpecificNode(backToInitialNode, graph)
    backToFinalNode = valueToPredict(particles[0])
    sourceNode = getSpecificNode(backToFinalNode, graph)
    cost = cost + getDistanceTwoNodes(finalNode, sourceNode, graph)

    return cost

def aplicarFuncaoObjetivoTodasParticulas(arrayParticulasDimensao, graph : Graph.Graph):

    nParticles = arrayParticulasDimensao.shape[0]

    lossOfEveryParticle = [costFunction(arrayParticulasDimensao[i], graph) for i in range(nParticles)]

    return lossOfEveryParticle
