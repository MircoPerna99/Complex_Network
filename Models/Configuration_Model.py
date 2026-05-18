import networkx as nx
from Models.Model_Base import ModelBase

class ConfigurationModel(ModelBase):
    def __init__(self, degree_sequence):
        self._degree_sequence = degree_sequence
        

    def generate_model(self):
        G = nx.configuration_model(self._degree_sequence)
        G = nx.Graph(G)
        G.remove_edges_from(nx.selfloop_edges(G))
        self.edge_list = list(G.edges())
        self._init_adjacency_matrix(len(self._degree_sequence),self.edge_list)
    
    def is_edge_in_graph(self, edge):
        return edge in self.edge_list
    
