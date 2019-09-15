# Q2. Given various subsequences of an array, print the overall array:
# Example: [1, 3, 5], [1, 3, 9], [9, 5]
# Array : [1, 3, 9, 5]


class Graph:
    def __init__(self):
        self.graph = {}


    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        
        if v not in self.graph:
            self.graph[v] = []
        
        if v not in self.graph[u]:
            self.graph[u].append(v)

    
    def unvisited(self, visited):
        for vertex in visited:
            if not visited[vertex]:
                return vertex
        
        return None

    
    def topological_sort(self, current_vertex, visited, stack):
        visited[current_vertex] = True

        for connected_vertex in self.graph[current_vertex]:
            if not visited[connected_vertex]:
                self.topological_sort(connected_vertex, visited, stack)

        # Every connected_vertex covered, push current_vertex to stack
        stack.append(current_vertex)


def get_array_from_subsequences(subsequences, start_vertex):
    g = Graph()
    for subsequence in subsequences:
        n = len(subsequence)
        for i in range(n-1):
            u = subsequence[i]; v = subsequence[i+1]
            g.add_edge(u, v)
    
    visited = {}
    for vertex in g.graph:
        visited[vertex] = False

    stack = []

    g.topological_sort(start_vertex, visited, stack)

    while(g.unvisited(visited) is not None):
        g.topological_sort(g.unvisited(visited), visited, stack)

    stack.reverse()
    
    print("Correct Array: {}".format(stack))


# Main Program
get_array_from_subsequences([[1, 3, 5], [1, 3, 9], [9, 5]], 1)
