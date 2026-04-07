from Models.Model_Base import ModelBase
import random
from random import sample, uniform
class ErdosRenjiTypeA(ModelBase):
    
    def __init__(self, N : int , K: int):
        super().__init__()
        self._amountOfNodes = N
        self._amountOfPairs = int(((self._amountOfNodes-1)*self._amountOfNodes)/2)
        if(not self._check_parameters(K)):
            print("K must be K > 0 and K < M, where M is equal to (N-1)/N and it is the amount of possible pairs")
            exit()
        
        self._amountOfEdges = K
        self.probNewNodeLink = self._amountOfEdges / self._amountOfPairs
        self._calculate_edges()
         
    def _check_parameters(self,K):
        return K > 0 and K < self._amountOfPairs
    
    def _calculate_edges(self):
        possibleEdges = []
        for i in range(0,self._amountOfNodes):
            for j in range(i+1, self._amountOfNodes):
                possibleEdges.append((i,j))
            
        selectedEdges = sample(possibleEdges, self._amountOfEdges)
        
        self._init_adjacency_matrix(self._amountOfNodes,selectedEdges)
        
        
class ErdosRenjiTypeB(ModelBase):
    
    def __init__(self, N : int , p: float):
        super().__init__()
        self._amountOfNodes = N
        self._amountOfPairs = int(((self._amountOfNodes-1)*self._amountOfNodes)/2)
        if(not self._check_parameters(p)):
            print("p must be p > 0 and p < 1")
            exit()
            
        self._amountOfEdges = p*self._amountOfPairs
        self.probNewNodeLink = p
        self._calculate_edges()
    
    def _check_parameters(self,p):
        return p > 0 and p < 1
    
    def _calculate_edges(self):
        edgesToAdd = []
        for i in range(0,self._amountOfNodes):
            for j in range(i+1, self._amountOfNodes):
                if(uniform(0.0, 1.0) < self.probNewNodeLink):
                    edgesToAdd.append((i,j))
                
        self._init_adjacency_matrix(self._amountOfNodes,edgesToAdd)


        