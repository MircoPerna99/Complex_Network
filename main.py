from adjacencyMatrix import AdjacencyMatrix
from DFS import DFS
from Models.Erdos_Renji_Model import ErdosRenjiTypeA, ErdosRenjiTypeB
from Models.Barabasi_Albert_Model import BarabasiAlbert
# edges = [(0,1), (2,3)]
# am = AdjacencyMatrix(False, 4, edges, False)
# components = DFS(am).apply()
# print(components)
print("Erdos-Renji Type A")
model = ErdosRenjiTypeA(5, 6)
model.printAdjancencyMatrix()
# modelBA = BarabasiAlbert(model.adjacencyMatrix._amountNodes, model.adjacencyMatrix._edges, 2)

# modelBA.adjancencyMatrix.print()
# modelBA.addNode()
# modelBA.adjancencyMatrix.print()
# # model.adjacencyMatrix.calculate_degree()

# print("Erdos-Renji Type B")
# model = ErdosRenjiTypeB(10000, 0.2)
# # model.adjacencyMatrix.print()
# model.adjacencyMatrix.calculate_degree()