import math

# get_base_box gives start row or col of the mini_box
# like if row = 2 then base_row = 0 and if row = 8 then base_row = 6
def get_base_box(index, k):
    return int(index/k)*k


def find_unassigned_box(matrix):
    n = len(matrix[0])
    for row in range(n): 
        for col in range(n): 
            if(matrix[row][col]==0): 
                return (True, row, col)

    return (False, None, None)


def is_safe(matrix, row, col, num):
    n = len(matrix[0])
    status = True
    # Check if the row is safe
    for i in range(n):
        if(matrix[row][i] == num):
            status = False
            break
    
    # Check if the column is safe
    for i in range(n):
        if(matrix[i][col] == num):
            status = False
            break
    
    # Check if the individual 3*3 box is safe as n = 9 hence k = 3
    k = int(math.sqrt(n))
    base_row = get_base_box(row, k)
    base_col = get_base_box(col, k)
    for i in range(k): 
        for j in range(k): 
            if(matrix[i+base_row][j+base_col] == num): 
                status = False
                break

    return status


def solve_sudoku(matrix):
    n = len(matrix[0])
    # Check for unassigned box and return status, if status is True also return row and col of that box
    found, row, col = find_unassigned_box(matrix)

    # If No unassigned box found, we are done 
    if(not found):
        return True
    
    # Consider digits 1 to 9 
    for num in range(1, n+1):
        # Check if it is safe to put this number
        if(is_safe(matrix, row, col, num)):
            # Put this number
            matrix[row][col] = num
            # Recur to check if it leads to solution
            if(solve_sudoku(matrix) == True):
                return True
            else:
                matrix[row][col] = 0  # Backtrack
    
    return False



print("Sudoku Example-1:")
matrix = [[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]

n = len(matrix[0])
if(solve_sudoku(matrix)): 
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print() 
else: 
    print("No solution exists")
