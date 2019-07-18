from heapq import heapify, nlargest, nsmallest

def find_k_largest(arr, k):
    heapify(arr)
    print("The {} largest numbers in list are : {}".format(k, nlargest(k, arr)))

def find_k_smallest(arr, k):
    heapify(arr)
    print("The {} smallest numbers in list are : {}".format(k, nsmallest(k, arr)))


print("Example-1: find_k_largest([1, 23, 12, 9, 30, 2, 50], 3)")
find_k_largest([1, 23, 12, 9, 30, 2, 50], 3)

print("\nExample-2: find_k_smallest([1, 23, 12, 9, 30, 2, 50], 2)")
find_k_smallest([1, 23, 12, 9, 30, 2, 50], 2)
