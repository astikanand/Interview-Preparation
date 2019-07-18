def max_sum_with_no_adjacents(arr):
    included = excluded = 0

    for current in arr:
        # Get the new excluded which is max(included, excluded) as current element is 
        # still not added to the included
        new_excluded = max(included, excluded)

        # Now change the included by adding current to excluded as no two adjacents should be present.
        included = excluded + current

        # Finally update the exluded with new_excluded
        excluded = new_excluded
    
    print("Max sum: {}".format(max(included, excluded)))



print("Example-1: max_sum_with_no_adjacents([5, 5, 10, 100, 10, 5])")
max_sum_with_no_adjacents([5, 5, 10, 100, 10, 5])

print("\nExample-2: max_sum_with_no_adjacents([1, 2, 3])")
max_sum_with_no_adjacents([1, 2, 3])

print("\nExample-3: max_sum_with_no_adjacents([1, 20, 3])")
max_sum_with_no_adjacents([1, 20, 3])
