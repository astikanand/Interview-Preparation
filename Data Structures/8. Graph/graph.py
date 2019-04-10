from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        self.graph[u].append(v)


    def print_graph(self):
        for vertex in self.graph:
            print("[{}]".format(vertex), end="")
            for connected_vertex in self.graph[vertex]:
                print("--->{}".format(connected_vertex), end="")
            print()
    
    
    def bfs_traversal(self, initial_vertex):
        visited = {}
        for v in self.graph:
            visited[v] = False

        queue = []

        # Start BFS Traversal
        visited[initial_vertex] = True
        print(initial_vertex, end=" ")

        queue.append(initial_vertex)

        while(queue):
            current_vertex = queue.pop(0)
            for connected_vertex in self.graph[current_vertex]:
                if visited[connected_vertex] is False:
                    visited[connected_vertex] = True
                    print(connected_vertex, end=" ")
                    queue.append(connected_vertex)

        print()
    

    def dfs_traversal(self, initial_vertex):
        visited = {}
        for v in self.graph:
            visited[v] = False

        stack = []

        # Start DFS Traversal
        visited[initial_vertex] = True
        stack.append(initial_vertex)

        while(stack):
            current_vertex = stack.pop()
            print(current_vertex, end=" ")
            for connected_vertex in self.graph[current_vertex]:
                if visited[connected_vertex] is False:
                    visited[connected_vertex] = True
                    stack.append(connected_vertex)
        
        print()
    
    def dfs_recursive_traversal(self, initial_vertex):
        visited = {}
        for v in self.graph:
            visited[v] = False
        
        self._dfs_recursive_util(initial_vertex, visited)
        print()
    

    def _dfs_recursive_util(self, current_vertex, visited):
        visited[current_vertex] = True
        print(current_vertex, end="")

        for connected_vertex in self.graph[current_vertex]:
                if visited[connected_vertex] is False:
                    self._dfs_recursive_util(connected_vertex, visited)
    

    def detect_cycle(self):
        visited = {}
        for v in self.graph:
            visited[v] = False
        
        stack = []
        initial_vertex = 0
        stack.append(initial_vertex)
        visited[v] = True

        cycle_exist = False
        while stack:
            current_vertex = stack.pop()
            for connected_vertex in self.graph[current_vertex]:
                if visited[connected_vertex] is True:
                    cycle_exist = True
                else:
                    visited[connected_vertex] = True
                    stack.append(connected_vertex)
        
        return cycle_exist


   
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

 
print("Here is the graph:")
g.print_graph()

print ("\nFollowing is Breadth First Traversal starting from vertex [2]:")
g.bfs_traversal(2)

print ("\nFollowing is Depth First Traversal starting from vertex [2]:")
g.dfs_traversal(2)

print ("\nFollowing is Depth First Recursive Traversal starting from vertex [2]:")
g.dfs_traversal(2)

print("\nCycle exists in graph? \n{}".format(g.detect_cycle()))

