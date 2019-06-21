def generate_1_to_n_binary_using_queue(n):
    binary = []
    queue = ["1"]

    while(n > 0):
        # Dequeue from the queue, add current to the list of binary numbers, then
        # append "0" to it and enqueue and again append "1" to it and enqueue to queue
        current = queue.pop(0)
        binary.append(current)

        queue.append(current+"0")
        queue.append(current+"1")
        
        n -= 1
    
    return binary



print("Example-1: generate_1_to_n_binary_using_queue(5)")
print(generate_1_to_n_binary_using_queue(5))
        
print("\nExample-2: generate_1_to_n_binary_using_queue(10)")
print(generate_1_to_n_binary_using_queue(10))