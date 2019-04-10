POSSIBLE_MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2,1)]

def valid_move(x, y, tour_matrix):
    return (x>=0 and x<N and y>=0 and y<N and tour_matrix[x][y]==-1)


def knight_tour_util(current_x, current_y, move_number, tour_matrix):
    if(move_number == N*N):
        return True
    
    # Try all possible moves
    for x_move, y_move in POSSIBLE_MOVES:
        next_x = current_x + x_move
        next_y = current_y + y_move
        if(valid_move(next_x, next_y, tour_matrix)):
            tour_matrix[next_x][next_y] = move_number
            if(knight_tour_util(next_x, next_y, move_number+1, tour_matrix) == True):
                return True
            else:
                tour_matrix[next_x][next_y] = -1  # Backtrack
    return False


def knight_tour():
    # Create a 2-D Matrix(N*N)
    tour_matrix = [[-1]*N for _ in range(N)]

    #  Knight is initially at the first block 
    tour_matrix[0][0]  = 0

    if(knight_tour_util(0, 0, 1, tour_matrix) == True):
        for i in range(N):
            for j in range(N):
                print("{0: =2d}".format(tour_matrix[i][j]), end=" ")
            print()
        print()
    else:
        print("No solution exist")



print("Knight Tour Example-1: 4*4 Matrix")
N = 4
knight_tour()

print("\nKnight Tour Example-2: 5*5 Matrix")
N = 5
knight_tour()

print("\nKnight Tour Example-3: 8*8 Matrix")
N = 8
knight_tour()


# Complexity:
#    • Time: O(8^(n^2)) :- There are N*N i.e., N^2 cells in the board and we have a maximum of 8 choices to make from a cell.
#    • Space: O(N^2)