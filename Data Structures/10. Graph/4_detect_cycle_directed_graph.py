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
            if(visited[vertex] == "white"):
                return vertex
        return None

    
    def detect_cycle_directed_graph_util(self, current_vertex, color):
        # Mark the current_vertex as "gray" i.e. processing
        color[current_vertex] = "gray"

        # See the connected vertices to current_vertex one by one
        for connected_vertex in self.graph[current_vertex]:
            # If connected_vertex is "white" i.e. still to be processed then make recursive call from the connected_vertex
            # and return True if it returns True                                                   
            if(color[connected_vertex] == "white"):
                if(self.detect_cycle_directed_graph_util(connected_vertex, color) == True):
                    return True
            # Else if connected_vertex is "gray" i.e. in processing then we have found the cycle return True
            elif(color[connected_vertex] == "gray"):
                print("Cycle Exists coz of {} -----> {}". format(current_vertex, connected_vertex))
                return True
        
        # If reaches here that means processing of current vertex is done, mark it black
        # return False to show that cycle was not found while processing this current_vertex
        color[current_vertex] = "black"
        return False
    

    def detect_cycle_directed_graph(self, start_vertex):
        # Mark every every vertex as "white" i.e. still to be processed
        color = {}
        for vertex in self.graph:
            color[vertex] = "white"
        
        # Call the detect_cycle_directed_graph_util with start_vertex
        cycle_exists = self.detect_cycle_directed_graph_util(start_vertex, color)

        # Check if there is still any "white” vertex and cycle still not found
        # Only when graph is UNREACHABLE or DISCONNECTED below lines will be executed
        while(self.unvisited(color) is not None and cycle_exists == False):
            # Call the detect_cycle_directed_graph_util from the "white" vertex
            cycle_exists = self.detect_cycle_directed_graph_util(self.unvisited(color), color)
        
        if(not cycle_exists):
            print("Cycle doesn't exist!")
        



print("Example-1: Detect Cycle in Directed Graph:")
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
g.detect_cycle_directed_graph(1)

print("\nExample-2: Detect Cycle in Directed Graph:")
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.detect_cycle_directed_graph(1)

print("\nExample-3: Detect Cycle in Directed Graph:")
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("D", "E")
g.add_edge("E", "G")
g.add_edge("F", "D")
g.add_edge("G", "H")
g.add_edge("H", "E")
g.detect_cycle_directed_graph("A")
