# To check if a queen can be placed on board[row][col]. 
# Note that this function is called when "col" number of queens are already placed in columns from 0 to col -1. 
# So we need to check only left side for attacking queens.
def is_safe(board, row, col):
    safe = True
    # Check this row on left side.
    for j in range(col):
        if(board[row][j] == 1):
            safe = False
            break
    
    # Check upper diagonal on left side
    i = row; j=col
    while(i>=0 and j>=0):
        if(board[i][j]==1):
            safe = False
            break
        i-=1; j-=1
    
    # Check lower diagonal on left side
    i = row; j = col
    while(i<N and j>=0 and safe):
        if(board[i][j]==1):
            safe = False
            break
        i+=1; j-=1

    return safe
    

def n_queen_util(board, col):
    # Base case: If all queens are placed then return true 
    if(col == N):
        return True
    
    # Consider this column and try placing this queen in all rows one by one 
    for i in range(N):
        if(is_safe(board, i, col)):
            # Place this queen in board[i][col] 
            board[i][col] = 1
            # Recur to place rest of the queens 
            if(n_queen_util(board, col+1) == True):
                return True
            else:
                board[i][col] = 0   # Backtrack
    
    # If the queen can not be placed in any row in this colum col  then return false
    return False


def n_queen():
    board = [[0]*N for i in range(N)]

    if(n_queen_util(board, 0) == True):
        for i in range(N):
            print(board[i])
    else:
        print("No solution exists")



print("N-Queen Example-1: 3*3 Matrix")
N = 3
n_queen()

print("\nN-Queen Example-2: 4*4 Matrix")
N = 4
n_queen()

print("\nN-Queen Example-3: 5*5 Matrix")
N = 5
n_queen()

print("\nN-Queen Example-4: 8*8 Matrix")
N = 8
n_queen()


# Complexity:
#    • Time: 
#    • Space:
