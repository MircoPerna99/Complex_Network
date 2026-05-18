from Adjacency_Matrix import AdjacencyMatrix
import igraph as ig
import matplotlib.pyplot as plt
from random import uniform

class SIR():
    def __init__(self,adjacencyMatrix : AdjacencyMatrix, probability_infection : float, probability_recovery):
        self._adjacencyMatrix = adjacencyMatrix
        self._nodes_status = [0] * adjacencyMatrix._amountNodes
        self._probability_infection = probability_infection
        self._probability_recovery = probability_recovery
        self._edges = adjacencyMatrix.get_edges_dictionary()
    
    def init_infection(self):
        for node in range(len(self._nodes_status)):
            if(uniform(0.0, 1.0) < self._probability_infection):
               self._nodes_status[node] = 1
    
    def evalute_step(self):
        new_nodes_status = [0] * len(self._nodes_status)
        for node in range(len(self._nodes_status)):
            if(self._nodes_status[node] == 2):
                new_nodes_status[node] = 2
                
            if(self._nodes_status[node] == 1):
                for node_neigh in self._edges[node]:
                    if(self._nodes_status[node_neigh] == 0):
                           if(uniform(0.0, 1.0) < self._probability_infection):
                                new_nodes_status[node_neigh] = 1
                                
                if(uniform(0.0, 1.0) < self._probability_recovery):
                    new_nodes_status[node] = 2
                else:
                    new_nodes_status[node] = 1
        
        self._nodes_status = new_nodes_status
    
    def print_graph(self, title = "Graph"):    
        colour_map = {
            0:"green",
            1:"red",
            2:"blue"
        }
        
        network = ig.Graph.TupleList(self._adjacencyMatrix.get_edges() ,weights=False, directed=False)
        network = network.simplify(combine_edges=dict(weight="first"))
        network["title"] = title
        
        
        colour_nodes  = [colour_map[self._nodes_status[node]] for node in range(len(self._nodes_status))]
        fig, ax = plt.subplots( figsize= (10,10) )
        ig.plot(
            network,
            target= ax,
            vertex_size= 30,
            vertex_color = colour_nodes,
            vertex_frame_width= 0,
            edge_color= "black",
            edge_width= 1.0,
            layout= "fr"
        )
        ax.set_title(title)

        plt.show()            

    