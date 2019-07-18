def search_row_column_wise_sorted_matrix(matrix, key):
    n = len(matrix)

    # Start with top right corner
    i = 0; j = n - 1

    while i < n and j >= 0:
        # If righmost element is lesser than key, skip that row
        if matrix[i][j] < key:
            i += 1
        # Else if righmost element is greater than key, skip that column
        elif matrix[i][j] > key: 
            j -= 1
        # Else if righmost element is equal to key, the key is found.
        else:
            print("Key {}: Found at ({}, {})".format(key, i, j)) 
            return
      
    print("Key {}: Not Found".format(key))
  


mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ]

print("Example-1: search_row_column_wise_sorted_matrix(matrix, key)")
search_row_column_wise_sorted_matrix(mat, 29)

print("\nExample-2: search_row_column_wise_sorted_matrix(matrix, key)")
search_row_column_wise_sorted_matrix(mat, 38)
