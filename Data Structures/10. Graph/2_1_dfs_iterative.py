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
    

    def dfs_traversal_iterative_util(self, start_vertex, visited):
        # Take a stack and push the start_vertex
        stack = []
        stack.append(start_vertex)

        # Pop out the current_vertex from stack and print it
        while(stack):
            current_vertex= stack.pop()
            # Stack may contain some vertex more than once, so we need to print the popped item only if it is not visited.
            # This may happen if some vertex was discovered by some earlier vertex and at later point it is visited by some other vertex.
            # Example: In Graph-1: vertex-2 and vertex-6 was discovered by previous vertex and visited later by other.
            if(visited[current_vertex] is False):
                visited[current_vertex] = True
                print("{}".format(current_vertex), end=" ")

            # See all the connected vertices to current_vertex
            for connected_vertex in self.graph[current_vertex]:
                # If any connected_vertex is not visited push to the stack
                if(visited[connected_vertex] is False):
                    stack.append(connected_vertex)
    

    def dfs_traversal_iterative(self, start_vertex):
        # Mark every every vertex as unvisited
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False
        
        # Call the dfs_traversal_iterative_util with start_vertex
        self.dfs_traversal_iterative_util(start_vertex, visited)

        # Check if there is still any unvisited vertex
        # Only when graph is UNREACHABLE or DISCONNECTED below lines will be executed
        while(self.unvisited(visited) is not None):
            # Call the dfs_traversal_iterative_util from the unvisited vertex
            self.dfs_traversal_iterative_util(self.unvisited(visited), visited)
        print()



print("Example-1: DFS Traversal of Graph (Iterative) from vertex-1:")
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
g.dfs_traversal_iterative(1)

print("Example-2: DFS Traversal of Graph (Iterative) from vertex-2:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.dfs_traversal_iterative(2)

print("Example-3: DFS Traversal of Graph (Iterative) from vertex-A:")
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("E", "G")
g.add_edge("F", "D")
g.add_edge("G", "H")
g.add_edge("H", "E")
g.dfs_traversal_iterative("A")
