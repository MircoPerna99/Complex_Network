from adjacencyMatrix import AdjacencyMatrix
from Models.Model_Base import ModelBase
import random
from random import sample, uniform
from histogram import Histogram
class BarabasiAlbert(ModelBase):
    def __init__(self, initNodes: int, initEdges :list, m:int):
        self.initNodes = initNodes
        self.initEdges = initEdges
                
        if(not self._checkParameters(m)):
            print("m must be 0 < m < |n0|")
            exit()
            
        self.amountNewConnections = m
        
        self._initAdjacencyMatrix(initNodes,initEdges)
        self.degreeInTime = {}
        self.degreeInTime[0] = self.calculateAverageDegree()
    
    def _checkParameters(self, m):
        return m > 0 and m < self.initNodes
    
    def addNode(self):
        if(self.areDegreeNodesNull()):
            self.adjacencyMatrix.calculate_degree()
            
        self.adjacencyMatrix.addNodes(1)
        edgesToAdd = []
        while(len(edgesToAdd) != self.amountNewConnections):
            for node in range(len(self.adjacencyMatrix.degree_nodes)):
                p = float(self.adjacencyMatrix.degree_nodes[node] / (2 * self.adjacencyMatrix.getAmountEdges()))
            
                if (uniform(0,1) <= p and (self.adjacencyMatrix.getAmountNodes()-1, node) not in edgesToAdd):
                    edgesToAdd.append((self.adjacencyMatrix.getAmountNodes()-1, node))
                if(len(edgesToAdd) == self.amountNewConnections):
                    break
                
        self.adjacencyMatrix.addEdges(edgesToAdd)
    
    def addNodes(self, amountNewNodes, calculateAverageDegreeInTime = False):
        for i in range(amountNewNodes):
            self.addNode()
            if(calculateAverageDegreeInTime):
                self.degreeInTime[i+1] = self.calculateAverageDegree(False) 
    
    
    def printAverageDegreeInTime(self):
        AdjacencyMatrix._print_dictionary("Average Degree In Time",self.degreeInTime, "Time", "Average Degree")  
