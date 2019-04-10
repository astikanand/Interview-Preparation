class Graph:
    def  __init__(self):
        self.graph = {}
 
 
    def addEdge(self, u, v):
        if(u not in self.graph):
            self.graph[u]=[]
 
        self.graph[u].append(v)
 
        # For undirected graph
        if(v not in self.graph):
            self.graph[v]=[]
 
        self.graph[v].append(u)
 
 
    def printGraph(self):
        for vertex in self.graph:
            print("{}".format(vertex), end="")
 
            for connected_vertex in self.graph[vertex]:
                print("--->{}".format(connected_vertex), end="")
            print()
 
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
 
 
print("Here is the graph")
g.printGraph()
