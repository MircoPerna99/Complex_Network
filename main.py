from Adjacency_Matrix import AdjacencyMatrix
from DFS import DFS
from Models.Erdos_Renji_Model import ErdosRenjiTypeA, ErdosRenjiTypeB
from Models.Barabasi_Albert_Model import BarabasiAlbert
from Models.Watts_Strogatz_Model import WattsStrogatzModel
from Models.Borgatti_Everett_Model import BorgattiEverettModel
# edges = [(0,1), (2,3), (1,2)]
# am = AdjacencyMatrix(4, edges, isWeighted=False, isDirected=False)
# am.print()
# am.print_degree_distribution_normalized()

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

print("Barabasi-Albert Model")
modelBA = BarabasiAlbert(10, 4)
modelBA.print_adjacency_matrix()
modelBA.print_degree_distribution_normalized()
modelBA.add_nodes(100, True)
# modelBA.print_adjacency_matrix()
modelBA.print_degree_distribution()


# print("Erdos-Renji Type B")
# model = ErdosRenjiTypeB(10000, 0.2)
# # model.adjacencyMatrix.print()
# model.adjacencyMatrix.calculate_degree()

# print("Watts-Strogatz Model")
# modelWS = WattsStrogatzModel(12, 4,0.5)
# modelWS.printAdjacencyMatrix()
# modelWS.printDegreesNodeDistribution()
# modelWS.printGraph()
# modelWS.rewing()
# modelWS.printDegreesNodeDistribution()
# modelWS.printGraph()

# print("Borgatti-Everett Model")
# modelBE = BorgattiEverettModel(20, 5)
# modelBE.printAdjacencyMatrix()
# modelBE.printGraph()
# modelBE.printDegreesNodeDistribution()
