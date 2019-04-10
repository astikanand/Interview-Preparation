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


    def DFSIterative(self, s):
        visited = [False]*(len(self.graph))
        stack = []

        stack.append(s)

        while(stack):
            s = stack.pop()

            if(visited[s]==False):
                visited[s] = True
                print(s, end=" ")

            connected_vertices = self.graph[s]

            for vertex in connected_vertices:
                if(visited[vertex]==False):
                    stack.append(vertex)


    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        connected_vertices = self.graph[v]

        for vertex in connected_vertices:
                if(visited[vertex]==False):
                    self.DFSUtil(vertex, visited)


    def DFS(self, s):
        visited = [False]*(len(self.graph))

        self.DFSUtil(s, visited)




g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.printGraph()
 
print ("Following is Iterative Depth First Traversal starting from vertex 2: ")
g.DFSIterative(2)


print ("Following is Recursive Depth First Traversal starting from vertex 2: ")
g.DFS(2)


 
