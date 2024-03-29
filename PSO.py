import networkx as nx
import Graph,Node,Edge
import numpy
import random

def generateRandomNumbers(numberNodes):

    valueBetweenValues = getSpaceBetweenNodes(numberNodes)

    k =[(i*valueBetweenValues) for i in range(numberNodes+1)]# GAMA DE VALORES POSSIVEIS PARA CADA CIDADE--> 0--0.05 ('A'), 0.05--0,10('B')

    randomValues = []

    for i in range(numberNodes):
        randomValues.append(random.uniform(k[i],k[i+1]))

    toShuffle = [randomValues[i] for i in range(1,len(randomValues)-1)]
    numpy.random.permutation(toShuffle)

    intermidiatte = [toShuffle[i] for i in range(len(toShuffle))]

    intermidiatte = numpy.asarray(intermidiatte)
    intermidiatte = numpy.random.permutation(intermidiatte)

    for i in range(1,len(randomValues)-1):
        randomValues[i] = intermidiatte[i-1]

    return randomValues

def initPos(numberParticles, numberNodes):

    try:

        valueBetweenValues = getSpaceBetweenNodes(numberNodes)

        initPosArray = generateRandomNumbers(numberNodes)

        for i in range(numberParticles-1):
            initPosArray = numpy.vstack((initPosArray,generateRandomNumbers(numberNodes)))

        return initPosArray
    except:
        raise

def valueToPredict(value, numberNodes):

    #ESTE CODIGO EM PRINCIPIO FUNCIONA
    val = getSpaceBetweenNodes(numberNodes)
    initialValue = 65  # ascii number of 'A'

    for i in range(numberNodes):
        if float((i*val)) < value and value <= float((val * (i+1))):
            return chr(initialValue+i)

    return 0


def getSpaceBetweenNodes(numberNodes):

    return 1 / numberNodes  # --> Max Boundary é sempre 1, visto que divido por 1, na definicao do espaço entre cada nó do problema

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

    vals = [valueToPredict(particles[i], len(graph.getNodes())) for i in range(nP)]

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
                vInicial = valueToPredict(particles[i], len(graph.getNodes()))
                nInicial = getSpecificNode(vInicial,graph)
                vFinal = valueToPredict(particles[i+1], len(graph.getNodes()))
                nFinal = getSpecificNode(vFinal, graph)
                cost = cost + getDistanceTwoNodes(nInicial, nFinal, graph)
                break


    backToInitialNode = valueToPredict(particles[len(particles)-1], len(graph.getNodes()))
    finalNode = getSpecificNode(backToInitialNode, graph)
    backToFinalNode = valueToPredict(particles[0], len(graph.getNodes()))
    sourceNode = getSpecificNode(backToFinalNode, graph)
    cost = cost + getDistanceTwoNodes(finalNode, sourceNode, graph)

    return cost

def aplicarFuncaoObjetivoTodasParticulas(arrayParticulasDimensao, graph : Graph.Graph):

    nParticles = arrayParticulasDimensao.shape[0]

    lossOfEveryParticle = [costFunction(arrayParticulasDimensao[i], graph) for i in range(nParticles)]

    return lossOfEveryParticle
