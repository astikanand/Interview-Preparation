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
    

    def get_min_key_vertex_not_in_mst(self, mst_set, key):
        min_key = sys.maxsize
        min_vertex = None
        for k in key:
            if(key[k] < min_key and mst_set[k] == False):
                min_key = key[k]
                min_vertex = k
        
        return min_vertex
                
    

    def prims_mst(self, start_vertex):
        # Initially, set mst_set of every vertex as False, key of every vertex as "MAX" and parent of every vertex as "-".
        mst_set = {}; key = {}; parent = {}
        for vertex in self.graph:
            mst_set[vertex] = False
            key[vertex] = sys.maxsize
            parent[vertex] = "-"
        
        # Set the key[start_vertex] = 0 and min_vertex = start_vertex : From this vertex we will start the MST
        key[start_vertex] = 0
        min_vertex = start_vertex

        while(min_vertex is not None):
            # Add the min_vertex to the mst_set
            mst_set[min_vertex] = True

            # See all the connected vertices to min_vertex one by one
            for connected_vertex in self.graph[min_vertex]:
                con_vertex = connected_vertex[0]
                con_vertex_weight = connected_vertex[1]
                # If the connected_vertex is not in mst_set and also weight of the connected_vertex < key[connected vertex],
                # then update the key of connected vertex and also it's parent to be the min_vertex
                if(mst_set[con_vertex] == False and con_vertex_weight < key[con_vertex]):
                    key[con_vertex] = con_vertex_weight
                    parent[con_vertex] = min_vertex
            
            # Again call the function to get new min_vertex with updated mst_set and key
            min_vertex = self.get_min_key_vertex_not_in_mst(mst_set, key)
        

        # Print the edges and their respective weights using parent and key dicts.
        ordered_parent = sorted(parent.items(), key=lambda k: (k[1]))
        print("="*23 + "\nEdges\t:\tWeights\n" + "="*23)
        for vertex, parent_vertex in ordered_parent:
            print("{} -- {} \t:\t {}".format(parent_vertex, vertex, key[vertex]))
        


print("Example: Prim's MST from vertex-A:")
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
g.prims_mst("A")
