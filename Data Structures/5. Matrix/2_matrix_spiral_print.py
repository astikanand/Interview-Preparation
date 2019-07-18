def matrix_spiral_print(matrix):
    ## Some Important Variables
    #   • row_start - starting row index
    #   • row_end - ending row index
    #   • col_start - starting column index
    #   • col_end - ending column index
    #   • i - iterator
    row_start = 0; row_end = len(matrix)
    col_start = 0; col_end = len(matrix[0])
  
    while (row_start<row_end and col_start<col_end) : 
        # Print the first row, after printing done increment the row_start
        for i in range(col_start, col_end) : 
            print(matrix[row_start][i], end = " ") 
              
        row_start += 1
  
        # Print the last column, after printing done decrement the col_end
        for i in range(row_start, row_end) : 
            print(matrix[i][col_end-1], end = " ")

        col_end -= 1
  
        # Print the last row, after printing done decrement the row_end
        if row_start < row_end: 
            for i in range(col_end - 1, (col_start - 1), -1) : 
                print(matrix[row_end - 1][i], end = " ") 
              
            row_end -= 1
          
        # Print the first column, after printing done increment the col_start
        if (col_start < col_end) : 
            for i in range(row_end - 1, row_start - 1, -1) : 
                print(matrix[i][col_start], end = " ") 
              
            col_start += 1
        
    print()



print("Example-1: matrix_spiral_print(matrix)")
mat = [ [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16] ]
matrix_spiral_print(mat)
