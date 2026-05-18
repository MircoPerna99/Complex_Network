import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import csv

class Percolation():
    def __init__(self):
        self.adjacency_matrix : list = None
        self.dims : tuple = None
        self.p : float = 0.5
        self.graph_type = '2D'
        
    def init_graph_from_adjacency_matrix(self, adjacency_matrix : list, p):
        A = np.array(adjacency_matrix) 
        self.network = nx.from_numpy_array(A)
        self.dims = A.shape
        self.graph_type = '2D'
        self.p = p
        self.define_open_sites()
        
    def apply_percolation(self):
        nodes_to_remove = [node for node in self.network.nodes if not self.open_sites[node]]
        self.network.remove_nodes_from(nodes_to_remove)
        
    def define_open_sites(self):
        if (self.graph_type == '2D'):
            N, M = self.dims
            self.open_sites = np.random.rand(N, M) < self.p
        elif (self.graph_type == 'cayley'):
            self.open_sites = np.random.rand(self.network.number_of_nodes()) < self.p
        else:
            N = self.dims[0]
            self.open_sites = np.random.rand(N) < self.p
            
    def generate_cayley_tree(self,k, h):
        self.network = nx.Graph()
        if h == 0:
            self.network.add_node(0)
        else:    
            self.network.add_node(0)
            node_id = 1
            # Coda per la Breadth-First Search: memorizza (nodo_corrente, livello)
            queue = [(0, 0)]
            
            while queue:
                current, level = queue.pop(0)
                
                if level < h:
                    # Il nodo centrale ha k figli. Gli altri hanno k-1 figli.
                    num_children = k if current == 0 else (k - 1)
                    
                    for _ in range(num_children):
                        self.network.add_edge(current, node_id)
                        queue.append((node_id, level + 1))
                        node_id += 1
                
    
    def generate_graph(self):
        if self.graph_type == '1D':
            N = self.dims[0]
            self.network = nx.path_graph(N)   
        elif self.graph_type == '2D':
            N, M = self.dims
            self.network = nx.grid_2d_graph(N, M)
        elif self.graph_type == 'cayley':
            K, M = self.dims
            self.generate_cayley_tree(K,M)
        elif self.graph_type == 'random':
            N = self.dims
            self.network = nx.erdos_renyi_graph(N, self.p)
        elif self.graph_type == 'small_world':
            N, k, prob_rewire = self.dims
            self.network = nx.watts_strogatz_graph(N, k, prob_rewire)
        elif self.graph_type == 'scale_free':
            N, m = self.dims
            self.network = nx.barabasi_albert_graph(N, m=m)
        else:
            raise ValueError("graph_type non valido. Usa '1D', '2D', 'cayley', 'random', 'small_world' o 'scale_free'.")
            
    def init_graph(self, dims, p, graph_type='2D'):
        '''
        Genera un lattice con siti aperti e chiusi, basato su diverse tipologie di grafi.

        Input:
            - dims: dimensione del reticolo (int o tuple).
                    Se 'graph_type' è '1D', dims è un intero N.
                    Se 'graph_type' è '2D', dims è una tupla (N, M).
                    Se 'graph_type' è '3D', dims è una tupla (N, M, L).
            - p: probabilità che un sito sia aperto.
            - graph_type: tipo di grafo ('1D', '2D', '3D', 'random', 'small_world', 'scale_free').

        Output:
            - G: grafo con nodi aperti e bordi connessi tra siti aperti.
            - open_sites: array booleano che indica i siti aperti.
        '''
        self.dims = dims
        self.graph_type= graph_type
        self.p = p
        self.generate_graph()
        self.define_open_sites()
        # if(self.graph_type != '1D'):
        #     self.apply_percolation()
    
    def print_adj_matrix(self):
        A = nx.to_numpy_array(self.network, dtype=int)
        print(A)
        
    def plot_lattice(self):
        '''
        Visualizza il lattice generato.

        Input:
            - open_sites: matrice booleana che indica i siti aperti.
            - G: grafo generato.
            - graph_type: tipo di grafo ('1D', '2D', '3D', 'random', 'small_world', 'scale_free').
        '''
        if self.graph_type == '1D':
            plt.figure(figsize=(10, 1))
            pos = {i: (i, 0) for i in range(len(self.open_sites))}
            
            # Disegna i nodi
            nx.draw(self.network, pos, with_labels=False, node_size=300, node_color=['grey' if self.open_sites[i] else 'blue' for i in range(len(self.open_sites))], edge_color='black')

            plt.title('Lattice 1D')
            plt.show()
        
        elif self.graph_type == '2D':
            plt.figure(figsize=(6, 6))
            plt.imshow(self.open_sites, cmap='binary', interpolation='nearest')
            pos = {(x, y): (y, x) for x, y in self.network.nodes()}
            nx.draw(self.network, pos=pos, with_labels=False, node_size=10, edge_color='blue')
            plt.title('Lattice 2D')
            plt.show()

        else:
            nx.draw(self.network, with_labels=False, node_size=50,node_color=['grey' if self.open_sites[i] else 'blue' for i in range(len(self.open_sites))], edge_color='blue')
            plt.title(f'Lattice {self.graph_type}')
            plt.show()