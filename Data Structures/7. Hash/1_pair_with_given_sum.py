def find_pair_with_given_sum(arr, x):
    my_hash = {}
    sum_found = False
    for i in arr:
        if my_hash.get(x-i, False):
            print("Pair with sum {} is: [{}, {}]".format(x, i, x-i))
            sum_found = True
        else:
            my_hash[i] = True
    
    if not sum_found:
        print("Pair with sum {} is NOT Present.".format(x))


print("Example-1: find_pair_with_given_sum([1, 4, 45, 6, 10, -8], 16)")
find_pair_with_given_sum([1, 4, 45, 6, 10, -8], 16)

print("\nExample-2: find_pair_with_given_sum([1, 4, 45, 6, 10, -8], 13)")
find_pair_with_given_sum([1, 4, 45, 6, 10, -8], 13)
