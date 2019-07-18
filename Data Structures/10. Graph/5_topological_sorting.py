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


    def topological_sort_util(self, current_vertex, visited, result_stack):
        # Mark the current_vertex as visited
        visited[current_vertex] = True

        # See all the connected vertices to current_vertex one by one
        for connected_vertex in self.graph[current_vertex]:
            # If connected_vertex is not already visited then make recursive call from the connected_vertex
            if(visited[connected_vertex] is False):
                self.topological_sort_util(connected_vertex, visited, result_stack)
        
        # Once processing of current_vertex is done push it to result_stack
        result_stack.append(current_vertex)


    def topological_sort(self, start_vertex):
         # Mark every every vertex as unvisited
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False
        
        # Take a result_stack to store the result
        result_stack = []
        
        # Call the topological_sort_util with start_vertex
        self.topological_sort_util(start_vertex, visited, result_stack)

        # Check if there is still any unvisited vertex
        # Only when graph is UNREACHABLE or DISCONNECTED below lines will be executed
        while(self.unvisited(visited) is not None):
            # Call the topological_sort_util from the unvisited vertex
            self.topological_sort_util(self.unvisited(visited), visited, result_stack)
        
        # print the result_stack in reverse order
        result_stack.reverse()
        for vertex in result_stack:
            print("{} ".format(vertex), end="")
        print()





print("Example-1: Topological Sorting from vertex-1:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 8)
g.add_edge(8, 3)
g.add_edge(8, 6)
g.add_edge(8, 7)
g.topological_sort(1)

print("\nExample-2: Topological Sorting from vertex-6:")
g = Graph()
g.add_edge(3, 4)
g.add_edge(4, 2)
g.add_edge(5, 1)
g.add_edge(5, 2)
g.add_edge(6, 1)
g.add_edge(6, 3)
g.topological_sort(6)

print("\nExample-3: Topological Sorting from vertex-A:")
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("E", "G")
g.add_edge("F", "D")
g.add_edge("G", "H")
g.topological_sort("A")
