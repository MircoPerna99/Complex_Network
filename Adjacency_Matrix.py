from Histogram import Histogram
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

class AdjacencyMatrix():
    def __init__(self, amountNodes = 3, edges = [], isDirected = False, isWeighted = False):
        self._amountNodes = amountNodes
        self._isDirected = isDirected
        self._isWeighted = isWeighted
        self.degree_nodes : dict = None
        self.degree_nodes_input  : dict = None
        self.degree_nodes_out : dict = None
        self.strength_nodes : dict = None
        self.degree_distribution : dict = None
       
        if(not self._check_edges(edges)):
            exit()
        
        if(not self._isDirected):
            edges = self._create_edges_for_undirect(edges)
            
        self._edges : list = edges 

        self._init_adjacency_matrix()
    
    def get_amount_nodes(self):
        return self._amountNodes
    
    def get_amount_edges(self):
        return len(self._edges)  
    
    def get_edges(self):
        return self._edges   
    
    def is_a_link(self, nodeOne, nodeTwo):
        return self._adjacency_matrix[nodeOne, nodeTwo]      
    
    def _fill_metrix(self, edges_to_add = None):
        if(edges_to_add == None):
            edges_to_add = self._edges
            
        for edge in edges_to_add:
            self._adjacency_matrix[edge[0],edge[1]] = edge[2] if self._isWeighted else 1
                          
    def _init_adjacency_matrix(self):
        self._adjacency_matrix = np.zeros(shape=(self._amountNodes,self._amountNodes))    
        self._fill_metrix()
           
    def _check_edges(self, edges):
        def _generate_error_message_not_valid_edges(isWeighted):
            return "The edges are not tuple with length 3" if isWeighted else "The edges are not tuple with length 2"
        
        def _check_edge(isWeighted, edge):
            lenTuple = 3 if isWeighted else 2
            return isinstance(edge,tuple) and len(edge) == lenTuple
        
        if(edges == None):
            print("The list of edges is empty")
            return False
        
        if(not all(_check_edge(self._isWeighted,edge) for edge in edges)):
            print(_generate_error_message_not_valid_edges(self._isWeighted))
            return False
        
        return True
    
    def _create_edges_for_undirect(self,edges):
        edges_to_add = []
        for edge in edges:
            new_edge = (edge[1],edge[0], edge[2]) if self._isWeighted else (edge[1],edge[0])
            edges_to_add.append(new_edge)
            
        return edges + edges_to_add
    
    def _removes_edges_metrix(self, edgesToRemove : list = []):
        if(edgesToRemove == None or len(edgesToRemove) == 0):
            return
        if(edgesToRemove != None):
            if(self._isDirected):
                for edge in edgesToRemove:
                    self._adjacency_matrix[edge[0],edge[1]] = 0
            else:
                for edge in edgesToRemove:
                    self._adjacency_matrix[edge[0],edge[1]] = 0
                    self._adjacency_matrix[edge[1],edge[0]] = 0
    
    def _print_dictionary(title, dictionary, labelKeys, labelValues):
        Histogram.show(title, labelKeys, labelValues, dictionary.keys(), dictionary.values())
    
    def takeNeighbors(self, node):
        neighbors = []
        for column in range(0,self._amountNodes):
            if(self._adjacency_matrix[node][column] > 0):
                neighbors.append(column)
        
        return neighbors
    
    def _add_column(self, newNode:int):
        nodeToAdd = np.zeros(shape=(self._amountNodes, newNode))
        self._adjacency_matrix = np.append(self._adjacency_matrix, nodeToAdd, axis = 1)
        
    def _add_row(self):
        nodeToAdd =  np.zeros((1, self._amountNodes))
        self._adjacency_matrix = np.append(self._adjacency_matrix, nodeToAdd, axis=0)
        
    def add_nodes(self, newNode:int):
        self._add_column(newNode)      
        self._amountNodes = self._amountNodes + newNode
        self._add_row()
        
    def remove_edges(self, edgesToRemove):
        if(not self._check_edges(edgesToRemove)):
            exit()
        self._removes_edges_metrix(edgesToRemove)
        for edge in edgesToRemove:
            if(edge in self._edges):
                self._edges.remove(edge)
            else:
                self._edges.remove((edge[1], edge[0]))
        self.calculate_degree()
        

    def add_edges(self, newEdges):
        if(not self._check_edges(newEdges)):
            exit()
        
        if(not self._isDirected):
            newEdges = self._create_edges_for_undirect(newEdges)
        
        self._fill_metrix(newEdges)
        self._edges = self._edges + newEdges
        self.calculate_degree()
    
    def print(self):
        for row in self._adjacency_matrix:
            for column in row:
                print(column,  end =" ")
            print("")  
      
    def print_graph(self, title = "Graph"):        
        network = ig.Graph.TupleList(self._edges,weights=self._isWeighted, directed=self._isDirected)
        network["title"] = title

        if(not self._isDirected):
           network = network.simplify(combine_edges=dict(weight="first"))
        
        fig, ax = plt.subplots( figsize= (10,10) )
        ig.plot(
            network,
            target= ax,
            vertex_size= 30,
            vertex_color= "purple",
            vertex_frame_width= 0,
            edge_color= "black",
            edge_width= 1.0,
            layout= "fr"
        )
        ax.set_title(title)

        plt.show()
    
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
    
    def _calculate_degree_undirected(self):
        degree_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            degree = 0
            for column in self._adjacency_matrix[row]:
                degree += column           
            degree_nodes[row] =  degree   
        self.degree_nodes = degree_nodes

    def calculate_degree(self):
        if(self._isDirected):
            self._calculate_degree_directed() 
        else:
            self._calculate_degree_undirected()
            self.calculate_degree_distribution()  
    
    def print_degree_nodes(self):
        if(self._isDirected):
            print("The graph is directed, use the other methods")
            exit()
        
        if(self.degree_nodes == None or len(self.degree_nodes) == 0):
            self._calculate_degree_undirected()
            
        AdjacencyMatrix._print_dictionary("Degree node",self.degree_nodes, "Node", "Degree")
        
    def print_degree_nodes_out(self):
        if(not self._isDirected):
            print("The graph is undirected, use the other methods")
            exit()
        
        if(self.degree_nodes_out == None or len(self.degree_nodes_out) == 0):
            self._calculate_degree_directed()
            
        AdjacencyMatrix._print_dictionary("Degree node out",self.degree_nodes_out, "Node", "Degree")
    
    def print_degree_nodes_input(self):
        if(not self._isDirected):
            print("The graph is undirected, use the other methods")
            exit()
        
        if(self.degree_nodes_input == None or len(self.degree_nodes_input) == 0):
            self._calculate_degree_directed()
            
        AdjacencyMatrix._print_dictionary("Degree node input",self.degree_nodes_input, "Node", "Degree")  
        
    def calculate_degree_distribution(self):
        if(self._isDirected):
            print("The graph is directed, use the other methods")
            exit()
        
        self.degree_distribution = {}
        
        if(self.degree_nodes == None or len(self.degree_nodes) == 0):
            self._calculate_degree_undirected()
        
        for node in self.degree_nodes.keys():
            if(not (self.degree_nodes[node] in self.degree_distribution)):
                self.degree_distribution[self.degree_nodes[node]] = 1
            else:
                self.degree_distribution[self.degree_nodes[node]] += 1
                
    def print_degree_distribution(self):
        if(self.degree_distribution == None or len(self.degree_distribution) == 0):
            self.calculate_degree_distribution()   
        
        AdjacencyMatrix._print_dictionary("Degree distribution",self.degree_distribution, "Degree", "Value")  
        
    def print_degree_distribution_normalized(self):
        if(self.degree_distribution == None or len(self.degree_distribution) == 0):
            self.calculate_degree_distribution()  
            
        degree_distribution_normalize = {k: v / self._amountNodes for k, v in self.degree_distribution.items()}
        
        AdjacencyMatrix._print_dictionary("Degree distribution",degree_distribution_normalize, "Degree", "Value") 
   
        

    def _calculate_strength_directed(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in range(0, self._amountNodes):
                strength_nodes[column] +=self._adjacency_matrix[row][column]
                strength_nodes[row] +=self._adjacency_matrix[row][column]
                
        self.strength_nodes = strength_nodes
    
    def _calculate_strength_undirected(self):
        strength_nodes = dict.fromkeys(range(0,self._amountNodes), 0)
        for row in range(0, self._amountNodes):
            for column in self._adjacency_matrix[row]:
                strength_nodes[row] += column
        
        self.strength_nodes = strength_nodes 


    def calculate_strength(self):
        if(not self._isWeighted):
            print("The graph is not weighted")
        else:
            if(self._isDirected):
                self._calculate_strength_directed()
            else:
                self._calculate_strength_undirected()        
    
    def print_strength_distrubution(self):
        
        if(self.strength_nodes == None or len(self.strength_nodes) == 0):
            self.calculate_strength()
            
        AdjacencyMatrix._print_dictionary("Strength ",self.strength_nodes, "Node", "Strength")  
            