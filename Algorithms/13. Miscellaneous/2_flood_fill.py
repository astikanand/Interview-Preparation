def flood_fill(screen, x, y, prev_color, new_color):
    m = len(screen)
    n = len(screen[0])

    # If x or y is outside the screen, then return.
    if(x < 0 or x >= m or y < 0 or y >= n):
        return
    
    # If color of screen[x][y] is not same as prev_color, then return
    if(screen[x][y] != prev_color):
        return
    
    # Replace the color at (x, y)
    screen[x][y] = new_color

    # Recur for north, south, east and west
    flood_fill(screen, x, y+1, prev_color, new_color)
    flood_fill(screen, x, y-1, prev_color, new_color)
    flood_fill(screen, x+1, y, prev_color, new_color)
    flood_fill(screen, x-1, y, prev_color, new_color)



print("Example-1: Flood Fill Algorithm")
screen = [ [1, 1, 1, 1, 1, 1, 1, 1], 
           [1, 1, 1, 1, 1, 1, 0, 0], 
           [1, 0, 0, 1, 1, 0, 1, 1], 
           [1, 2, 2, 2, 2, 0, 1, 0], 
           [1, 1, 1, 2, 2, 0, 1, 0], 
           [1, 1, 1, 2, 2, 2, 2, 0], 
           [1, 1, 1, 1, 1, 2, 1, 1], 
           [1, 1, 1, 1, 1, 2, 2, 1] ]



flood_fill(screen, 4, 4, 2, 3); 
m = len(screen)
n = len(screen[0])

for i in range(m):
    for j in range(n):
        print(screen[i][j], end=" ")
    print()
