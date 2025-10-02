from adjacencyMatrix import AdjacencyMatrix
from DFS import DFS
from Models.Erdos_Renji_Model import ErdosRenjiTypeA, ErdosRenjiTypeB
from Models.Barabasi_Albert_Model import BarabasiAlbert
from Models.Watts_Strogatz_Model import WattsStrogatzModel
# edges = [(0,1), (2,3)]
# am = AdjacencyMatrix(False, 4, edges, False)
# components = DFS(am).apply()
# print(components)
# print("Erdos-Renji Type A")
# model = ErdosRenjiTypeA(5, 6)
# model.printAdjacencyMatrix()
# model.printGraph()

# model.printDegreesNodeDistribution()
# print("Barabasi-Albert Model")
# modelBA = BarabasiAlbert(model.adjacencyMatrix.getAmountNodes(), model.adjacencyMatrix.getEdges(), 2)
# modelBA.addNodes(10, True)
# modelBA.printAdjacencyMatrix()
# modelBA.printDegreesNodeDistribution()
# modelBA.printGraph()
# modelBA.printAverageDegreeInTime()
# modelBA.adjancencyMatrix.print()
# # model.adjacencyMatrix.calculate_degree()

# print("Erdos-Renji Type B")
# model = ErdosRenjiTypeB(10000, 0.2)
# # model.adjacencyMatrix.print()
# model.adjacencyMatrix.calculate_degree()

print("Watts-Strogatz Model")
modelWS = WattsStrogatzModel(12, 4,0.5)
modelWS.printAdjacencyMatrix()
modelWS.printDegreesNodeDistribution()
modelWS.printGraph()
modelWS.rewing()
modelWS.printDegreesNodeDistribution()
modelWS.printGraph()
