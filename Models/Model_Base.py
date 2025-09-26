from adjacencyMatrix import AdjacencyMatrix
class ModelBase():
    def __init__(self):
        self.adjancencyMatrix : AdjacencyMatrix
        
    def printAdjancencyMatrix(self):
        self.adjancencyMatrix.print()
    
    def _initAdjancencyMatrix(self, amountNodes, edges):
        self.adjancencyMatrix = AdjacencyMatrix(False, amountNodes, edges, False)