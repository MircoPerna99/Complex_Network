from adjacencyMatrix import AdjacencyMatrix
from Models.Model_Base import ModelBase
import random
from random import sample, uniform
class BarabasiAlbert(ModelBase):
    def __init__(self, initNodes: int, initEdges :list, m:int):
        self.initNodes = initNodes
        self.initEdges = initEdges
        
        if(not self._checkParameters(m)):
            print("m must be 0 < m < |n0|")
            exit()
            
        self.amountNewConnections = m
        
        self._initAdjancencyMatrix(initNodes,initEdges)
    
    def addNode(self):
        self.adjancencyMatrix.addNodes(1)
        degreeNodes =  self.adjancencyMatrix.calculate_degree()
      
        edgesToAdd = []
        while(len(edgesToAdd) != self.amountNewConnections):
            for node in range(len(degreeNodes)):
                p = float(degreeNodes[node] / (2 * self.adjancencyMatrix.getAmountEdges()))
            
                if (uniform(0,1) <= p):
                    edgesToAdd.append((self.adjancencyMatrix._amountNodes-1, node))
                if(len(edgesToAdd) == self.amountNewConnections):
                    break
        
        self.adjancencyMatrix.addEdges(edgesToAdd)
              
    
    def _checkParameters(self, m):
        return m > 0 and m < self.initNodes
    
    
    