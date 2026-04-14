from Models.Model_Base import ModelBase
import random
from random import sample, uniform

class WattsStrogatzModel(ModelBase):
    def __init__(self, amountNodes, initialDegree, probRewining = 0.0):
        super().__init__()
        if(not self._check_parameters(amountNodes, initialDegree,probRewining)):
            exit()
            
        self._amountNodes = amountNodes
        self._initialDegree = initialDegree
        self._probRewining : float = probRewining 
        self._generate_regular_cirucalar_network()

    def _check_parameters(self, amountNodes, initialDegree,probRewining):
        if(amountNodes < 2):
            print("The numbers of nodes must be higher than 2")
            return False
        if(initialDegree < 1):
            print("The initial degree must be higher than 0")
            return False
        if(initialDegree % 2 > 0):
            print("The initial degree must be even")
            return False
        if(probRewining<0 or probRewining > 1):
            print("The probabilities must be between 0 and 1")
            return False
        return True
    
    def _generate_regular_cirucalar_network(self):
        def calculate_right_edges(amountEdges, amountNodes, node, edges):
            for i in range(1, amountEdges+1):      
                vertexOne = node
                vertexTwo = (node + i) % amountNodes
                
                if((vertexTwo, vertexOne) not in edges):
                    edges.append((vertexOne,vertexTwo))
            
        
        def calculate_left_edges(amountEdges, amountNodes, node,edges):
            for i in range(1, amountEdges+1):
                vertexOne = node
                vertexTwo = (node - i) % amountNodes
            
                if((vertexTwo, vertexOne) not in edges):
                    edges.append((vertexOne,vertexTwo))

            
        nodeForSide = int(self._initialDegree / 2)
        
        edges = []
        
        for i in range(self._amountNodes):
            calculate_right_edges(nodeForSide, self._amountNodes, i,edges) 
            calculate_left_edges(nodeForSide, self._amountNodes, i, edges)
        
        self._init_adjacency_matrix(self._amountNodes, edges)
    
    def rewing(self):
            def is_to_change():
                return uniform(0,1) < self._probRewining
            
            def apply_rewing(i, amountNodes, node):
                    vertexOne = node
                    vertexTwo = (node+i) % amountNodes

                    if(is_to_change()):
                        newNode = random.randint(0, amountNodes-1)
                        while newNode == vertexOne or newNode == vertexTwo or self.adjacencyMatrix.is_a_link(vertexOne,newNode):
                            newNode = random.randint(0, amountNodes-1)
                        
                        self.adjacencyMatrix.remove_edges([(vertexOne, vertexTwo)])
                        self.adjacencyMatrix.add_edges([(vertexOne, newNode)])
                    

                        
            if(self._probRewining == 0.0):
                return
            
            nodeForSide = self._initialDegree // 2

            for i in range(self._amountNodes):
                for j in range(1,nodeForSide+1):
                    apply_rewing(j,self._amountNodes, i)
                    
    