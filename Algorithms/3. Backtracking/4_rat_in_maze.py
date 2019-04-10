def rat_in_maze_util(solution_maze, x, y):
    if(x == N-1 and y == N-1):
        return True
    
    # Make a move in forward direction if it is_safe to move
    if(given_maze[x][y+1] == 1):
        solution_maze[x][y+1] = 1
        if(rat_in_maze_util(solution_maze, x, y+1) == True):
            return True
        else:
            solution_maze[x][y+1] = 0   # Backtrack
    
    # Make a move in downward direction if it is_safe to move
    if(given_maze[x+1][y] == 1):
        solution_maze[x+1][y] = 1
        if(rat_in_maze_util(solution_maze, x+1, y) == True):
            return True
        else:
            solution_maze[x][y+1] = 0   # Backtrack
    
    return False


def rat_in_maze():
    solution_maze = [[0]*N for i in range(N)]
    solution_maze[0][0] = 1

    if(rat_in_maze_util(solution_maze, 0, 0)):
        for i in range(N):
            print(solution_maze[i])
    else:
        print("No Solution exist.")



print("Rat in Maze Example-1: 4*4 Matrix")
N = 4
given_maze = [ [1, 0, 0, 0], 
               [1, 1, 0, 1], 
               [0, 1, 0, 0], 
               [1, 1, 1, 1] ]
rat_in_maze()
