def check_if_arr_is_subset(arr1, arr2):
    my_hash = {}
    for i in arr1:
        my_hash[i] = True

    status = True
    for i in arr2:
        if not my_hash.get(i, False):
            status = False
            break
    
    if status:
        print("True")
    else:
        print("False")



print("Example-1: check_if_arr_is_subset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1])")
check_if_arr_is_subset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1])
print("\nExample-2: check_if_arr_is_subset([1, 2, 3, 4, 5, 6], [1, 2, 4])")
check_if_arr_is_subset([1, 2, 3, 4, 5, 6], [1, 2, 4])
print("\nExample-3: check_if_arr_is_subset([10, 5, 2, 23, 19], [19, 5, 3])")
check_if_arr_is_subset([10, 5, 2, 23, 19], [19, 5, 3])
