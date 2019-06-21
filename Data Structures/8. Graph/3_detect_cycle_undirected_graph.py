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
        self.graph[v].append(u)


    def unvisited(self, visited):
        for vertex in visited:
            if(visited[vertex] == False):
                return vertex
        return None


    def detect_cycle_undirected_graph_util(self, current_vertex, parent, visited):
        # Mark the current_vertex as visited
        visited[current_vertex] = True

        # See the connected vertices to current_vertex one by one
        for connected_vertex in self.graph[current_vertex]:
            # If connected_vertex is not visited then make recursive call from the connected_vertex
            # with current_vertex as parent and return True if it returns True.
            if(visited[connected_vertex] == False):
                if(self.detect_cycle_undirected_graph_util(connected_vertex, current_vertex, visited) == True):
                    return True
            # Else if connected_vertex is already visited and it is not parent then cycle found return True.
            elif(connected_vertex != parent):
                print("Cycle Exists coz of {} ----- {}".format(current_vertex, connected_vertex))
                return True
        
        # Once the current_vertex is processed return False to show that cycle was not found while processing this current_vertex.
        return False


    def detect_cycle_undirected_graph(self, start_vertex):
        # Mark every every vertex as unvisited initially
        visited = {}
        for vertex in self.graph:
            visited[vertex] = False

        # Call the detect_cycle_undirected_graph_util with start_vertex
        cycle_exists = self.detect_cycle_undirected_graph_util(start_vertex, None, visited)

        # Check if there is still any unvisited vertex and cycle still not found
        # Only when graph is DISCONNECTED below lines will be executed
        while(self.unvisited(visited) is not None and cycle_exists == False):
            # Call the detect_cycle_undirected_graph_util from the unvisited vertex
            cycle_exists = self.detect_cycle_undirected_graph_util(self.unvisited(visited), None, visited)

        if(not cycle_exists):
            print("Cycle doesn't exist!")


print("Example-1: Detect Cycle in Undirected Graph:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.detect_cycle_undirected_graph(1)

print("\nExample-2: Detect Cycle in Undirected Graph:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.detect_cycle_undirected_graph(1)

print("\nExample-3: Detect Cycle in Undirected Graph:")
g = Graph()
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "G")
g.add_edge("E", "H")
g.add_edge("G", "H")
g.detect_cycle_undirected_graph("A")
