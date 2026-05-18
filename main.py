from Adjacency_Matrix import AdjacencyMatrix
from DFS import DFS
from Models.Erdos_Renji_Model import ErdosRenjiTypeA, ErdosRenjiTypeB
from Models.Barabasi_Albert_Model import BarabasiAlbert
from Models.Watts_Strogatz_Model import WattsStrogatzModel
from Models.Borgatti_Everett_Model import BorgattiEverettModel
from Models.Configuration_Model import ConfigurationModel
from Percolation.Percolation import Percolation
from Girvan_Newmann import GirvanNewmann
from SIR import SIR


# edges = [(0,1), (2,3), (1,2)]
# am = AdjacencyMatrix(4, edges, isWeighted=False, isDirected=False)
# am.print()
# # am.print_degree_distribution_normalized()
# print(am.get_edges_dictionary())
# print(am.get_edge_betweenness())

# components = DFS(am).apply()
# print(components)
# print("Erdos-Renji Type A")
# model = ErdosRenjiTypeA(5, 6)
# model.print_adjacency_matrix()
# model.print_degree_distribution_normalized()
# model.print_graph()

# print("Erdos-Renji Type B")
# model = ErdosRenjiTypeB(5, 0.7)
# model.print_adjacency_matrix()
# model.print_degree_distribution_normalized()
# model.print_graph()

# print("Barabasi-Albert Model")
# modelBA = BarabasiAlbert(11, 4)
# modelBA.print_adjacency_matrix()
# modelBA.print_degree_distribution_normalized()
# modelBA.add_nodes(100, True)
# # modelBA.print_adjacency_matrix()
# modelBA.print_degree_distribution()


# print("Watts-Strogatz Model")
# modelWS = WattsStrogatzModel(12, 4,0.5)
# modelWS.print_adjacency_matrix()
# modelWS.print_degree_distribution()
# modelWS.print_graph()
# modelWS.rewing()
# modelWS.print_degree_distribution()
# modelWS.print_graph()

# print("Borgatti-Everett Model")
# modelBE = BorgattiEverettModel(20, 8)
# modelBE.print_adjacency_matrix()
# modelBE.print_graph()
# modelBE.print_degree_distribution()

# print("Percolation 1D")
# percolation = Percolation()
# percolation.init_graph((10,), 1, '1D')
# percolation.plot_lattice()

# print("Percolation 2D")
# percolation = Percolation()
# percolation.init_graph((5,5), 0.50, '2D')
# percolation.plot_lattice()

# print("Percolation 3D")
# percolation = Percolation()
# percolation.init_graph((3,3), 0.60, 'cayley')
# percolation.plot_lattice()

print("Erdos-Renji Type A")
model = ErdosRenjiTypeA(5, 6)
model.print_adjacency_matrix()
model.print_graph()


list_model_con = []

degree_sequences = model.get_degree_sequences()
print(degree_sequences)
for i in range(100):
    model_con = ConfigurationModel(degree_sequences)
    model_con.generate_model()
    list_model_con.append(model_con)

degree_equal = {i: 0 for i in range(len(degree_sequences))}
for model_to_check in list_model_con:
        degree_sequences_to_check = model_to_check.get_degree_sequences()
        for node in range(len(degree_sequences)):
            if(degree_sequences[node] == degree_sequences_to_check[node]):
                degree_equal[node] = degree_equal[node] + 1

print(degree_equal)
# Calcolare quante volte un dato link da due nodi i e j è presente nelle 100
# copie realizzate. Cosa ci si aspetta che avvenga?
freq = {}
for edge in model.adjacencyMatrix.get_edges():
    if edge not in freq:
        freq[edge] = 0
   
    for model_to_check in list_model_con:
        if(model_to_check.is_edge_in_graph(edge)):
            freq[edge] = freq[edge] + 1 

print(freq)

# GirvanNewmann(model.adjacencyMatrix).apply()
# edges_betweenness = model.get_edge_betweenness()
# print(edges_betweenness)
# res = max(edges_betweenness, key=edges_betweenness.get)
# print(res)
# model.adjacencyMatrix.remove_edges([res])
# model.print_graph()

# print("Barabasi-Albert Model")
# model = BarabasiAlbert(5, 4)
# model.add_nodes(20, True)

# print("Watts-Strogatz Model")
# model = WattsStrogatzModel(12, 4,0.5)
# model.print_graph()
# model.rewing()
# model.print_graph()

# print("Borgatti-Everett Model")
# model = BorgattiEverettModel(30, 5)
# model.print_graph()

# sir_model = SIR(model.adjacencyMatrix, 0.3, 0.4)
# sir_model.init_infection()
# sir_model.print_graph()
# print(sir_model._nodes_status)

# for i in range(10):
#     sir_model.evalute_step()
#     sir_model.print_graph()
#     print(sir_model._nodes_status)