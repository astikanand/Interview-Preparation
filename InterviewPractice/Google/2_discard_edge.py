# Q: A graph has N vertices numbered from 1 to N. We have two lists. 
# One list M consisted of edges between vertices. The other list K consists of restricted paths. 
# We have to add edges one by one from M and check whether the addition of the particular edge 
# leads to a path between the restricted edges given in K. If it creates a path, we have to discard the edge.
# Example: N = 4; K = {(1, 4)}; M = {(1, 2), (2, 3), (3, 4)}. 
# Here, addition of edge (3, 4) will create a path between 1 and 4. Hence we discard edge (3, 4)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For Undirected Graph
    
    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def bfs(self, start_vertex, visited):
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True

        while(queue):
            current_vertex = queue.pop()
            for connected_vertex in self.graph[current_vertex]:
                if not visited[connected_vertex]:
                    queue.append(connected_vertex)
                    visited[connected_vertex] = True
    
    def is_reachable(self, source, destination):
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False

        self.bfs(source, visited)

        try:
            reach_dest = visited[destination]
        except:
            reach_dest = False
        
        return reach_dest
    

def discard_edge(edges, restricted):
    g = Graph()
    for edge in edges:
        g.add_edge(edge[0], edge[1])
        for restricted_edge in restricted:
            if g.is_reachable(restricted_edge[0], restricted_edge[1]):
                print("Discarded Edge: {} -- {}".format(restricted_edge[0], restricted_edge[1]))
                g.remove_edge(edge[0], edge[1])


discard_edge([(1, 2), (2, 3), (3, 4)], [(1, 4)])
