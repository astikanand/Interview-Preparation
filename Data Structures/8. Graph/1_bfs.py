class Graph:
    def __init__(self):
        self.graph = {}
    

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
    

    def unvisited(self, visited):
        for vertex in visited:
            if(visited[vertex] is False):
                return vertex
        return None
    

    def bfs_traversal_util(self, start_vertex, visited):
        # Take a queue and enqueue the start_vertex and mark it as visited
        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True

        # Dequeue out the current_vertex from queue and print it
        while(queue):
            current_vertex= queue.pop(0)
            print("{}".format(current_vertex), end=" ")
            # See all the connected vertices to current_vertex
            for connected_vertex in self.graph[current_vertex]:
                # If any connected_vertex is not visited enqueue to the queue and mark it visited
                if(visited[connected_vertex] is False):
                    queue.append(connected_vertex)
                    visited[connected_vertex] = True

       
    def bfs_traversal(self, start_vertex):
        # Mark every every vertex as unvisited
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False
        
        # Call the bfs_traversal_util with start_vertex
        self.bfs_traversal_util(start_vertex, visited)

        # Check if there is still any unvisited vertex
        # Only when graph is UNREACHABLE or DISCONNECTED below lines will be executed
        while(self.unvisited(visited) is not None):
            # Call the bfs_traversal_util from the unvisited vertex
            self.bfs_traversal_util(self.unvisited(visited), visited)
        print()



print("Example-1: BFS Traversal of Graph from vertex-1:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 8)
g.add_edge(8, 3)
g.add_edge(8, 6)
g.add_edge(8, 7)
g.bfs_traversal(1)

print("Example-2: BFS Traversal of Graph from vertex-2:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.bfs_traversal(2)

print("Example-3: BFS Traversal of Graph from vertex-A:")
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("E", "G")
g.add_edge("F", "D")
g.add_edge("G", "H")
g.add_edge("H", "E")
g.bfs_traversal("A")
