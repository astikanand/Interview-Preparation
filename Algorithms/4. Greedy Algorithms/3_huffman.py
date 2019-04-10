import heapq


class HeapNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(chars, frequencies):
    # Create a leaf node for each unique character and build a min heap of all leaf nodes
    n = len(chars)
    custom_heap = []
    for i in range(n):
        heap_node = HeapNode(chars[i], frequencies[i])
        heapq.heappush(custom_heap, heap_node)
    
    # Extract two nodes with the minimum frequency from the min heap and start merging
    while(len(custom_heap) > 1):
        node_left  = heapq.heappop(custom_heap)
        node_right = heapq.heappop(custom_heap)
        merged_node = HeapNode(None, node_left.frequency+node_right.frequency)
        merged_node.left = node_left
        merged_node.right = node_right
        heapq.heappush(custom_heap, merged_node)
    
    # Root Node of the Heap
    root_node = heapq.heappop(custom_heap)

    return root_node


def print_huffman_code(node, code):
    if(node.left == None and node.right == None):
        print("{}: {}".format(node.char, code))
        return
    
    print_huffman_code(node.left, code+"0")
    print_huffman_code(node.right, code+"1")


def generate_huffman_code(chars, frequencies):
    root_node = build_huffman_tree(chars, frequencies)

    print_huffman_code(root_node, "")




print("Huffman Codes for characters:")
chars = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
generate_huffman_code(chars, frequencies)


# Time Complexity : O(nlogn) where n is the number of unique characters. 
#                 : To extract Min using heappop() takes O(logn) and as there are n nodes, it is called 2*(n – 1) times.
# Space Complexity: O(n) :-> Storing n nodes in heap
