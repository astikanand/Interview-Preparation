def generate_permutations_util(string, left, right):
    if(left == right):
        print("{}".format("".join(string)))
        return
    
    for i in range(left, right):
        string[left], string[i] = string[i], string[left]
        generate_permutations_util(string, left+1, right)
        string[left], string[i] = string[i], string[left]    # Backtrack


def generate_permutations(string):
    n = len(string)
    generate_permutations_util(list(string), 0, n)



print("Example-1:")
generate_permutations("ABC")

print("\nExample-2")
generate_permutations("ABCD")


# Complexity:
#    • Time: O(n*n!) :- There are n! permutations and it requires O(n) time to print a permutation.
#    • Space: O(1)
