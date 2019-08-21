import heapq


def connect_n_ropes_min_cost(ropes):
    total_cost = 0
    heapq.heapify(ropes)

    while(len(ropes) >= 2):
        new_connected_rope = heapq.heappop(ropes) + heapq.heappop(ropes)
        total_cost += new_connected_rope
        heapq.heappush(ropes, new_connected_rope)
    
    print(total_cost)


print("Example-1: connect_n_ropes_min_cost([4, 3, 2, 6])")
connect_n_ropes_min_cost([4, 3, 2, 6])
