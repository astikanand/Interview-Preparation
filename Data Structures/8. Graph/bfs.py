from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def printGraph(self):
        for vertex in self.graph:
            print("[%d]" %(vertex), end="")

            for connected_vertices in self.graph[vertex]:
                print("--->%d" %(connected_vertices), end="")
            print()


    def BFS(self, s):
        visited = [False]*(len(self.graph))
        queue = []

        queue.append(s)
        visited[s] = True

        while(queue):
            s = queue.pop(0)
            print(s, end=" ")
            connected_vertices = self.graph[s]

            for vertex in connected_vertices:
                if(visited[vertex]==False):
                    queue.append(vertex)
                    visited[vertex] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.printGraph()
 
print ("Following is Breadth First Traversal starting from vertex 2: ")
g.BFS(2)

 
