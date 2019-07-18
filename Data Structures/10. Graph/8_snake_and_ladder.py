def get_min_dice_throws_snake_ladder(N, moves):
    # Mark every cell as unvisited and take an empty queue
    visited = [False]*(N)
    queue = []

    # Mark the first_cell as visited and enqueue the first cell to the queue with dice_count=0 : We start from here. 
    visited[0] = True
    queue.append((0, 0))

    while(queue):
        # Get the current element from the queue and then fetch the current_cell and current_dice_count from it.
        current = queue.pop(0)
        current_cell = current[0]
        current_dice_count = current[1]

        # if current_cell is last cell we are done, print the dice_count and break
        if(current_cell == N-1):
            print("No. of min dice count: {}".format(current_dice_count))
            break
        
        # Start seeing all the 6 reachable_cell from current_cell one by one
        for reachable_cell in range(current_cell+1, current_cell+6):
            # If reachable_cell is lesser than last cell and still not visited then mark the recahable_cell as visited
            if(reachable_cell < N and visited[reachable_cell] is False):
                visited[reachable_cell] = True
                # If any of ladder or snake is available at reachable_cell modify the reachable_cell with the moves value
                if(moves[reachable_cell] != -1):
                    reachable_cell = moves[reachable_cell]
                
                # Update the queue with reachable_cell and dice_count needed to reach there.
                queue.append((reachable_cell, current_dice_count+1))



print("Example-1:- Snake and Ladder:")
N = 30
moves = [-1] * N 
  
# Ladders 
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28
  
# Snakes 
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
get_min_dice_throws_snake_ladder(N, moves)
