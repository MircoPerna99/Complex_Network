from histogram import Histogram
class AdjacencyMatrix():
    def __init__(self, isDirected = True, amountNodes = 3, edges = [], isWeighted = True):
        self._isDirected = isDirected
        self._amountNodes = amountNodes
        self._isWeighted = isWeighted
       
        if(not self._check_edges(edges)):
            exit()

        self._init_adjacency_matrix(edges)
                
    
    def _fill_metrix(self, edges):
        if(edges != None):
            if(self._isDirected):
                if(self._isWeighted):
                    for edge in edges:
                        self._adjacency_matrix[edge[0]][edge[1]] = edge[2]
                else:
                    for edge in edges:
                        self._adjacency_matrix[edge[0]][edge[1]] = 1
            else:
                if(self._isWeighted):
                    for edge in edges:
                        self._adjacency_matrix[edge[0]][edge[1]] = edge[2]
                        self._adjacency_matrix[edge[1]][edge[0]] = edge[2]
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


                
    def _check_edges(self, edges):
        def generate_error_message_not_valid_edges(isWeighted):
            return "The edges are not tuple with length 3" if isWeighted else "The edges are not tuple with length 2"
        
        def _check_edge(isWeighted, edge):
            lenTuple = 3 if isWeighted else 2
            return isinstance(edge,tuple) and len(edge) == lenTuple
        
        if(edges == None):
            print("The list of edges is empty")
            return False
        
        if(not all(_check_edge(self._isWeighted,edge) for edge in edges)):
            print(generate_error_message_not_valid_edges(self._isWeighted))
            return False
        
        return True
    
    def _print_dictionary(title, dictionary, labelKeys, labelValues):
        print(title)
        for node in dictionary.keys():
            print(node, dictionary[node])
        Histogram.show(title, labelKeys, labelValues, dictionary.keys(), dictionary.values())
    
    def _calculate_degree_undirected(self):
        degree_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            degree = 0
            for column in self._adjacency_matrix[row]:
                if(column > 0):
                    degree += 1
            
            degree_nodes[row] =  degree
        
        AdjacencyMatrix._print_dictionary("Degree node",degree_nodes, "Node", "Degree")

        
    def _calculate_degree_directed(self):
        degree_nodes_out = dict.fromkeys(range(0,self._amountNodes), 0)
        degree_nodes_input = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                if(self._adjacency_matrix[row][column] > 0):
                    degree_nodes_input[column] +=1
                    degree_nodes_out[row] +=1
        
        AdjacencyMatrix._print_dictionary("Degree node out",degree_nodes_out, "Node", "Degree")
        AdjacencyMatrix._print_dictionary("Degree node input",degree_nodes_input, "Node", "Degree")
    
    
    def _calculate_strength_undirected(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in self._adjacency_matrix[row]:
                strength_nodes[row] += column
        
        AdjacencyMatrix._print_dictionary("Strength node",strength_nodes, "Node", "Strength")
    
    def _calculate_strength_directed(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                strength_nodes[column] +=self._adjacency_matrix[row][column]
                strength_nodes[row] +=self._adjacency_matrix[row][column]
                
        AdjacencyMatrix._print_dictionary("Strength node",strength_nodes, "Node", "Strength")

        
    def calculate_strength(self):
        if(not self._isWeighted):
            print("The graph is not weighted")
        else:
            if(self._isDirected):
                self._calculate_strength_directed()
            else:
                self._calculate_strength_undirected()
            
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
    
edges = [(0,1,0.3),(0,2, 0.2),(1,2,0.2), (2,3,0.1)]

am = AdjacencyMatrix(True, 4, edges, True)
am.print()
am.calculate_degree()
am.calculate_strength()



            
            
        