def create_lcp_array_kasai(text, suffix_arr):
    n = len(suffix_arr)

    # LCP Araay to store LCPs.
    lcp_arr = [0]*n     

    # Create an inverse of suffix array, it is used to get next suffix string from suffix array.
    # Example:- if suffix_arr[0] is 5, the inv_suffix_arr[5] would store 0.
    inv_suffix_arr = [0]*n
    for i in range(n):
        inv_suffix_arr[suffix_arr[i]] = i
    
    # Initialize length of previous LCP
    k = 0

    # Process all suffixes one by one starting from first suffix in text[].
    for i in range(n):
        # If current suffix is at n-1, then we don’t have next substring to consider.
        # So lcp is not defined for this substring, we put zero.
        if inv_suffix_arr[i] == n-1:
            k = 0
            continue

        # j contains index of the next substring to be considered  to compare with the present 
        # substring, i.e., next string in suffix array.
        j = suffix_arr[inv_suffix_arr[i] + 1]

        # Directly start matching from k'th index as at-least k-1 characters will match
        while (i+k<n and j+k<n and text[i+k]==text[j+k]):
            k += 1
        
        # LCP for the present suffix.
        lcp_arr[inv_suffix_arr[i]] = k

        # Delete the starting character from the string. 
        if k>0: k -= 1
    
    print("Inverse Suffix Array: {}".format(inv_suffix_arr))
    print("LCP Array: {}".format(lcp_arr))

    

print("Kasai - LCP Array Construction Example:")
text = "banana"
suffixes = ["banana", "anana", "nana", "ana", "na", "a"]
sorted_suffixes = ["a", "ana", "anana", "banana", "na", "nana"]
suffix_arr = [5, 3, 1, 0, 4, 2]
print("Given Text: '{}'".format(text))
print("Suffixes: {}".format(suffixes))
print("Sorted Suffixes: {}".format(sorted_suffixes))
print("\nSuffix Array: {}".format(suffix_arr))
create_lcp_array_kasai("banana", [5, 3, 1, 0, 4, 2])

