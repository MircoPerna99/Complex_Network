from Adjacency_Matrix import AdjacencyMatrix

class ModelBase():
    def __init__(self):
        self.adjacencyMatrix : AdjacencyMatrix
        self.nameGraph = "Model"
            
    def print_adjacency_matrix(self):
        self.adjacencyMatrix.print()
    
    def _init_adjacency_matrix(self, amountNodes, edges):
        self.adjacencyMatrix = AdjacencyMatrix(amountNodes, edges)
    
    def print_degrees_node(self):
        self.adjacencyMatrix.printDegreeNodes()
    
    def calculate_average_degree(self, recalculateDegrees = True):
        if(self.are_degree_nodes_null() or recalculateDegrees):
            self.adjacencyMatrix.calculate_degree()
            
        return float(sum(self.adjacencyMatrix.degree_nodes.values())/self.adjacencyMatrix.get_amount_edges())
    
    def are_degree_nodes_null(self):
        return self.adjacencyMatrix.degree_nodes == None or len(self.adjacencyMatrix.degree_nodes) == 0
    
    def print_graph(self):
        self.adjacencyMatrix.print_graph("Model")
        
    def print_degree_distribution(self):
        self.adjacencyMatrix.print_degree_distribution()
    
    def print_degree_distribution_normalized(self):
        self.adjacencyMatrix.print_degree_distribution_normalized()

        
        