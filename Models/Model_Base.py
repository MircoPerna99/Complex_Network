from adjacencyMatrix import AdjacencyMatrix
class ModelBase():
    def __init__(self):
        self.adjacencyMatrix : AdjacencyMatrix
        self.nameGraph = "Model"
            
    def printAdjacencyMatrix(self):
        self.adjacencyMatrix.print()
    
    def _initAdjacencyMatrix(self, amountNodes, edges):
        self.adjacencyMatrix = AdjacencyMatrix(False, amountNodes, edges, False)
    
    def printDegreesNodeDistribution(self):
        self.adjacencyMatrix.printDegreeNodesDistribution()
    
    def calculateAverageDegree(self, recalculateDegrees = True):
        if(self.areDegreeNodesNull() or recalculateDegrees):
            self.adjacencyMatrix.calculate_degree()
            
        return float(sum(self.adjacencyMatrix.degree_nodes.values())/self.adjacencyMatrix.getAmountEdges())
    
    def areDegreeNodesNull(self):
        return self.adjacencyMatrix.degree_nodes == None or len(self.adjacencyMatrix.degree_nodes) == 0
    
    def printGraph(self):
        self.adjacencyMatrix.printGraph("Model")

        
        