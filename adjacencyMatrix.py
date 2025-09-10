class AdjacencyMatrix():
    def __init__(self, isDirected = True, amountNodes = 3, edges = []):
        self._isDirected = isDirected
        if(not AdjacencyMatrix._check_edges(edges)):
            exit()
        self._amountNodes = amountNodes
        self._init_adjacency_matrix(edges)
    
    def _fill_metrix(self, edges):
        if(edges != None):
            if(self._isDirected):
                for edge in edges:
                    self._adjacency_matrix[edge[0]][edge[1]] = 1
            else:
                for edge in edges:
                    self._adjacency_matrix[edge[0]][edge[1]] = 1
                    self._adjacency_matrix[edge[1]][edge[0]] = 1

        
    def _init_adjacency_matrix(self, edges):
        self._adjacency_matrix = []
        for i in range(0,self._amountNodes):
            row = []
            for j in range(0,self._amountNodes):
                row.append(0)
            self._adjacency_matrix.append(row)
        
        self._fill_metrix(edges)


                
    def _check_edges(edges):
        def _check_edge(edge):
            return isinstance(edge,tuple) and len(edge) == 2
        
        if(edges == None):
            print("The list of edges is empty")
            return False
        if(not all(_check_edge(edge) for edge in edges)):
            print("The edges are not tuple with length 2")
            return False
        
        return True
    
    def _calculate_degree_undirected(self):
        degree_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            degree = 0
            for column in self._adjacency_matrix[row]:
                if(column > 0):
                    degree += 1
            
            degree_nodes[row] =  degree
        
        print("Degree node:")
        for node in degree_nodes.keys():
            print(node, degree_nodes[node])
        
    def _calculate_degree_directed(self):
        degree_nodes_out = dict.fromkeys(range(0,self._amountNodes), 0)
        degree_nodes_input = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                if(self._adjacency_matrix[row][column] > 0):
                    degree_nodes_input[column] +=1
                    degree_nodes_out[row] +=1
        
        print("Degree node out:")
        for node in degree_nodes_out.keys():
            print(node, degree_nodes_out[node])
        
        print("Degree node input:")
        for node in degree_nodes_input.keys():
            print(node, degree_nodes_input[node])
            
    def calculate_degree(self):
        if(self._isDirected):
            self._calculate_degree_directed()
        else:
            self._calculate_degree_undirected()

            
    def print(self):
        for row in self._adjacency_matrix:
            for column in row:
                print(column,  end =" ")
            print("")
    
edges = [(0,1),(0,2),(1,2), (2,3)]

am = AdjacencyMatrix(True, 4, edges)
am.print()
am.calculate_degree()

            
            
        