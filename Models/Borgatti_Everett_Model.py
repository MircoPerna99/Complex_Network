from Models.Model_Base import ModelBase
import random
from random import sample, uniform

class BorgattiEverettModel(ModelBase):
    def __init__(self, amountNodes:int, connectedComponentSize :int = 0):
        super().__init__()
        if(not self._check_parameters(amountNodes, connectedComponentSize)):
            exit()

        self._amountNodes = amountNodes
        
        if(connectedComponentSize == 0):
            connectedComponentSize = random.randint(2, amountNodes-1)
            
        self._connectedComponentSize = connectedComponentSize
        self._init_core_component()
        self._init_periphery_component()

    def _check_parameters(self, amountNodes, connectedComponentSize):
        if(amountNodes < 4):
            print("The amount of nodes must be higher than or equal to 4")
            return False
        
        if(connectedComponentSize > 0 and connectedComponentSize < 2):
            print("The size of the connected component must be higher than or equal to 2")
            return False
            
        return True
    
    def _init_core_component(self):
        edgesCoreComponent = []
        for i in range(0, self._connectedComponentSize):
            for j in range(i+1, self._connectedComponentSize):
                edgesCoreComponent.append((i,j))
        
        self._init_adjacency_matrix(self._amountNodes, edgesCoreComponent)
        
    def _init_periphery_component(self):
        edgesPeripheryComponent = []
        for i in range(self._connectedComponentSize, self._amountNodes):
            isInsterted = False
            while(not isInsterted):
                for j in range(0, self._connectedComponentSize):
                    if(uniform(0,1) < 0.4) :
                        edgesPeripheryComponent.append((i,j))
                        isInsterted = True
                    
        
        self.adjacencyMatrix.add_edges(edgesPeripheryComponent)
                
        