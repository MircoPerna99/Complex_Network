from adjacencyMatrix import AdjacencyMatrix
class DFS():
    def __init__(self, adjancecyMatrix: AdjacencyMatrix = None):
        self._adjancecyMatrix = adjancecyMatrix
    
    def _apply_dfs(self, node, visitedNodes, component):
        visitedNodes[node] = True
        component.append(node)
        neighbors =  self._adjancecyMatrix.takeNeighbors(node)
        for neighbor in neighbors:
            if(not visitedNodes[neighbor]):
                self._apply_dfs(neighbor, visitedNodes, component)
                
    
    def apply(self):
        visitedNodes = [False] * self._adjancecyMatrix._amountNodes
        components = []
        
        for node in range(0,self._adjancecyMatrix._amountNodes):
            component = []
            if(not visitedNodes[node]):
                self._apply_dfs(node, visitedNodes, component)
                components.append(component)
        
        return components
        
        
                    
                
                
                
                
            
          
        