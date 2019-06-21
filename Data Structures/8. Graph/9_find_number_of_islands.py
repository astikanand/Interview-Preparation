POSSIBLE_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

class Graph:
    def __init__(self, matrix):
        self.graph = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
    

    def is_safe_cell(self, x, y, visited):
        # Cell is safe if x is in range(row), y is in range(column), cell is still not visited and value of cell is 1.
        return (x>=0 and x<self.row and 
                y>=0 and y<self.col and 
                not visited[x][y] and self.graph[x][y] ==1)
    

    # Function to do DFS for a 2D boolean matrix, considers all the 8 neighbours as adjacent vertices.
    def DFS(self, i, j, visited):
        # Mark current_cell as visited
        visited[i][j] = True

        # For all neighbours check if the cell is safe then call the DFS again from that safe_cell.
        for x_move, y_move in POSSIBLE_MOVES:
            if(self.is_safe_cell(i+x_move, j+y_move, visited)):
                self.DFS(i+x_move, j+y_move, visited)


    def find_number_of_islands(self):
        # Mark all cells as unvisited initially
        visited = [[False]*self.col for i in range(self.row)]

        islands_count = 0
        for i in range(self.row):
            for j in range(self.col):
                # If a cell with value 1 is not visited yet, then new island is found
                # Visit all cells in this island and increment islands_count
                if(self.graph[i][j] == 1 and visited[i][j] is False):
                    self.DFS(i, j, visited)
                    islands_count += 1
        
        print("Total islands: {}".format(islands_count))



print("Example-1:- Find number of Islands:")
matrix=[[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]]
g = Graph(matrix)
g.find_number_of_islands()
