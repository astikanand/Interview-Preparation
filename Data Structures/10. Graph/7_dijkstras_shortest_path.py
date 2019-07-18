import sys

class Graph:
    def __init__(self):
        self.graph = {}
    

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    

    def add_edge(self, u, v, w):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    

    def get_min_distant_vertex_not_in_spt(self, spt_set, vertex_distance):
        min_vertex_distance = sys.maxsize
        min_distant_vertex = None
        for v in vertex_distance:
            if(vertex_distance[v] < min_vertex_distance and spt_set[v] == False):
                min_vertex_distance = vertex_distance[v]
                min_distant_vertex = v
        
        return min_distant_vertex
                
    

    def dijkstras_spt(self, start_vertex):
        # Initially, set spt_set of every vertex as False, vertex_distance of every vertex as "MAX" and parent of every vertex as "-".
        spt_set = {}; vertex_distance = {}; parent = {}
        for vertex in self.graph:
            spt_set[vertex] = False
            vertex_distance[vertex] = sys.maxsize
            parent[vertex] = "-"
        
        # Set the vertex_distance[start_vertex] = 0 and min_distant_vertex = start_vertex :- From this vertex we will start the SPT.
        vertex_distance[start_vertex] = 0
        min_distant_vertex = start_vertex

        while(min_distant_vertex is not None):
            # Add the min_distant_vertex to the spt_set
            spt_set[min_distant_vertex] = True

            # See all the connected vertices to min_distant_vertex one by one
            for connected_vertex in self.graph[min_distant_vertex]:
                con_vertex = connected_vertex[0]
                con_vertex_weight = connected_vertex[1]
                # If the connected_vertex is not in spt_set and also weight of connected_vertex + vertex_distance[min_distant_vertex] < vertex_distance[connected vertex],
                # then update the vertex_distance of connected_vertex and also it's parent to be the min_distant_vertex
                if(spt_set[con_vertex] == False and  con_vertex_weight + vertex_distance[min_distant_vertex] < vertex_distance[con_vertex]):
                    vertex_distance[con_vertex] = con_vertex_weight + vertex_distance[min_distant_vertex]
                    parent[con_vertex] = min_distant_vertex
            
            # Again call the function to get new min_distant_vertex with updated spt_set and vertex_distance
            min_distant_vertex = self.get_min_distant_vertex_not_in_spt(spt_set, vertex_distance)
        

        # Print the edges and their respective weights using parent and vertex_distance dicts.
        ordered_parent = sorted(parent.items(), key=lambda k: (k[0]))
        print("="*56 + "\nVertex\t:\tDistance from source\t:\tReach By\n" + "="*56)
        for vertex, parent_vertex in ordered_parent:
            print("{}\t:\t\t{}\t\t:\t{} --> {}".format(vertex, vertex_distance[vertex], parent_vertex, vertex))
        


print("Example: Dijkstra's Shortest Path from vertex-A:")
g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "H", 8)
g.add_edge("B", "C", 8)
g.add_edge("B", "H", 11)
g.add_edge("C", "D", 7)
g.add_edge("C", "F", 4)
g.add_edge("C", "I", 2)
g.add_edge("D", "E", 9)
g.add_edge("D", "F", 14)
g.add_edge("E", "F", 10)
g.add_edge("F", "G", 2)
g.add_edge("G", "H", 1)
g.add_edge("G", "I", 6)
g.add_edge("H", "I", 7)
g.dijkstras_spt("A")
