from Adjacency_Matrix import AdjacencyMatrix
from Models.Model_Base import ModelBase
import random
from random import sample, uniform
from Histogram import Histogram

class BarabasiAlbert(ModelBase):
    def __init__(self, initNodes: int, m:int):
        self.initNodes = initNodes
        self.initEdges = [] 
                
        if(not self._check_parameters(m)):
            print("m must be 0 < m < |n0|")
            exit()
            
        self.amountNewConnections = m
        
        self.create_full_edges()
        
        self._init_adjacency_matrix(self.initNodes,self.initEdges)
        self.degreeInTime = {}
        self.degreeInTime[0] = self.calculate_average_degree()
        
    def create_full_edges(self):
        for i in range(self.initNodes):
            for j in range(i+1, self.initNodes):
                self.initEdges.append((i,j))
    
    def _check_parameters(self, m):
        return m > 0 and m < self.initNodes
    
    def add_node(self):
        if(self.are_degree_nodes_null()):
            self.adjacencyMatrix.calculate_degree()
            
        self.adjacencyMatrix.add_nodes(1)
        edgesToAdd = []
        while(len(edgesToAdd) != self.amountNewConnections):
            for node in range(len(self.adjacencyMatrix.degree_nodes)):
                p = float(self.adjacencyMatrix.degree_nodes[node] / (2 * self.adjacencyMatrix.get_amount_edges()))
            
                if (uniform(0,1) <= p and (self.adjacencyMatrix.get_amount_nodes()-1, node) not in edgesToAdd):
                    self.adjacencyMatrix.add_edges([(self.adjacencyMatrix.get_amount_nodes()-1, node)])
                    edgesToAdd.append((self.adjacencyMatrix.get_amount_nodes()-1, node))
                if(len(edgesToAdd) == self.amountNewConnections):
                    break
                

    
    def add_nodes(self, amountNewNodes, calculateAverageDegreeInTime = False):
        for i in range(amountNewNodes):
            self.add_node()
            if(calculateAverageDegreeInTime):
                self.degreeInTime[i+1] = self.calculate_average_degree(True) 
    
    def print_average_degree_in_time(self):
        AdjacencyMatrix._print_dictionary("Average Degree In Time",self.degreeInTime, "Time", "Average Degree")  
