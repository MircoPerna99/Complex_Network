from Adjacency_Matrix import AdjacencyMatrix
import igraph as ig
import matplotlib.pyplot as plt
class GirvanNewmann():
    def __init__(self,adjacencyMatrix : AdjacencyMatrix):
        self._adjacencyMatrix = adjacencyMatrix
    
    def apply(self):
        while(len(self._adjacencyMatrix._edges) != 0):
            edges_betweenness = self._adjacencyMatrix.get_edge_betweenness()
            print(edges_betweenness)
            res = max(edges_betweenness, key=edges_betweenness.get)
            print(f"The edges deleted is {res}")
            self._adjacencyMatrix.remove_edges([res])
            self._adjacencyMatrix.print_graph()


    