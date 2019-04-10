def next_greater_same_digits(n):
    n = list(str(n))
    k = len(n)

    # Finding a  digit which is smaller than the previously traversed digit
    for i in range(k-1, -1, -1):
        if(n[i-1] < n[i]):
            break
    
    if(i==0):
        return "Not possible"
    
    # Find the smallest digit on the right side of (i-1)'th digit that is greater than x 
    x = n[i-1]
    smallest = i
    for j in range(i+1, k):
        if(n[j] < n[smallest] and  n[j] > x):
            smallest = j
    
    # Swapping the above found smallest digit with (i-1)'th
    n[i-1], n[smallest] = n[smallest], n[i-1]

    # Sort all the digits from ith digit and concatenate it with left_part
    result_num = n[:i] + sorted(n[i:])

    # Join all the array element to create a number
    result_num = "".join(result_num)

    return result_num

    

print("Example-1: next_greater_same_digits(218765)")
print(next_greater_same_digits(218765))

print("\nExample-2: next_greater_same_digits(1234)")
print(next_greater_same_digits(1234))

print("\nExample-3: next_greater_same_digits(4321)")
print(next_greater_same_digits(4321))

print("\nExample-4: next_greater_same_digits(534976)")
print(next_greater_same_digits(534976))
