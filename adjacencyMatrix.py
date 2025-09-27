from histogram import Histogram
import numpy as np
class AdjacencyMatrix():
    def __init__(self, isDirected = True, amountNodes = 3, edges = [], isWeighted = True):
        self._isDirected = isDirected
        self._amountNodes = amountNodes
        self._isWeighted = isWeighted
        self.degree_nodes : dict = None
        self.degree_nodes_input  : dict = None
        self.degree_nodes_out : dict = None
        self.strength_nodes : dict = None
       
        if(not self._check_edges(edges)):
            exit()
        
        self._edges = edges

        self._init_adjacency_matrix()
    
    def getAmountNodes(self):
        return self._amountNodes
    
    def getAmountEdges(self):
        return len(self._edges)            
    
    def _fill_metrix(self, edgesToAdd : list = []):
        if(edgesToAdd == None or len(edgesToAdd) == 0):
            edgesToAdd = self._edges
        if(edgesToAdd != None):
            if(self._isDirected):
                if(self._isWeighted):
                    for edge in edgesToAdd:
                        self._adjacency_matrix[edge[0],edge[1]] = edge[2]
                else:
                    for edge in edgesToAdd:
                        self._adjacency_matrix[edge[0],edge[1]] = 1
            else:
                if(self._isWeighted):
                    for edge in edgesToAdd:
                        self._adjacency_matrix[edge[0],edge[1]] = edge[2]
                        self._adjacency_matrix[edge[1],edge[0]] = edge[2]
                else:
                    for edge in edgesToAdd:
                        self._adjacency_matrix[edge[0],edge[1]] = 1
                        self._adjacency_matrix[edge[1],edge[0]] = 1

        
    def _init_adjacency_matrix(self):
        self._adjacency_matrix = np.zeros(shape=(self._amountNodes,self._amountNodes))    
        self._fill_metrix()


                
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
        
        self.degree_nodes = degree_nodes
        
    def printDegreeNodesDistribution(self):
        if(self._isDirected):
            print("The graph is directed, use the other methods")
            exit()
        
        if(self.degree_nodes == None or len(self.degree_nodes) == 0):
            self._calculate_degree_undirected()
            
        AdjacencyMatrix._print_dictionary("Degree node",self.degree_nodes, "Node", "Degree")

        
    def _calculate_degree_directed(self):
        degree_nodes_out = dict.fromkeys(range(0,self._amountNodes), 0)
        degree_nodes_input = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                if(self._adjacency_matrix[row][column] > 0):
                    degree_nodes_input[column] +=1
                    degree_nodes_out[row] +=1
        
        self.degree_nodes_input = degree_nodes_input
        self.degree_nodes_out = degree_nodes_out
        
    def printDegreeNodesOutDistribution(self):
        if(not self._isDirected):
            print("The graph is undirected, use the other methods")
            exit()
        
        if(self.degree_nodes_out == None or len(self.degree_nodes_out) == 0):
            self._calculate_degree_undirected()
            
        AdjacencyMatrix._print_dictionary("Degree node out",self.degree_nodes_out, "Node", "Degree")
    
    def printDegreeNodesInputDistribution(self):
        if(not self._isDirected):
            print("The graph is undirected, use the other methods")
            exit()
        
        if(self.degree_nodes_input == None or len(self.degree_nodes_input) == 0):
            self._calculate_degree_undirected()
            
        AdjacencyMatrix._print_dictionary("Degree node input",self.degree_nodes_input, "Node", "Degree")    
    
    def _calculate_strength_undirected(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in self._adjacency_matrix[row]:
                strength_nodes[row] += column
        
        self.strength_nodes = strength_nodes
        
    def printStrengthUndirectedDistribution(self):
        if(self._isDirected):
            print("The graph is directed, use the other methods")
            exit()
        
        if(self.strength_nodes == None or len(self.strength_nodes) == 0):
            self._calculate_strength_undirected()
            
        AdjacencyMatrix._print_dictionary("Strength ",self.strength_nodes, "Node", "Strength")  
    
    def _calculate_strength_directed(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                strength_nodes[column] +=self._adjacency_matrix[row][column]
                strength_nodes[row] +=self._adjacency_matrix[row][column]
                
        self.strength_nodes = strength_nodes

    def printStrengthUndirectedDistribution(self):
        if(not self._isDirected):
            print("The graph is undirected, use the other methods")
            exit()
        
        if(self.strength_nodes == None or len(self.strength_nodes) == 0):
            self._calculate_strength_directed()
            
        AdjacencyMatrix._print_dictionary("Strength ",self.strength_nodes, "Node", "Strength")  
        
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
    
    def takeNeighbors(self, node):
        neighbors = []
        for column in range(0,self._amountNodes):
            if(self._adjacency_matrix[node][column] > 0):
                neighbors.append(column)
        
        return neighbors
    
    def _addColumn(self, newNode:int):
        nodeToAdd = np.zeros(shape=(self._amountNodes, newNode))
        self._adjacency_matrix = np.append(self._adjacency_matrix, nodeToAdd, axis = 1)
        
    def _addRow(self):
        nodeToAdd =  np.zeros( (1, self._amountNodes))
        self._adjacency_matrix = np.append(self._adjacency_matrix, nodeToAdd, axis=0)
        
    def addNodes(self, newNode:int):
        self._addColumn(newNode)
        
        self._amountNodes = self._amountNodes + newNode
        self._addRow()
    
    def addEdges(self, newEdges):
        if(not self._check_edges(newEdges)):
            exit()
        self._fill_metrix(newEdges)
        self._edges.append(newEdges)
        
        



            
            
        