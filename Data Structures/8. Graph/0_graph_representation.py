from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)     # If undirected
    
    def print_graph(self):
        # print the vertex
        for vertex in self.graph:
            print("[{}]".format(vertex), end="")
            # print the connected_vertices to this vertex
            for connected_vertex in self.graph[vertex]:
                print("-->{}".format(connected_vertex), end="")
            print()



print("Example-1: Graph Representation")
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()
