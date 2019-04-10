def subset_sum(given_set, num):
    if num < 1 or len(given_set) == 0:
        return False

    if num == given_set[0]:
        return [given_set[0]]

    with_v = subset_sum(given_set[1:], num-given_set[0])
    if with_v:
        return [given_set[0]] + with_v
    else:
        return subset_sum(given_set[1:], num)
    


print("Subset Sum Example-1:")
given_set = [10, 7, 5, 18, 12, 20, 15]
print(subset_sum(given_set, 35))

print("Subset Sum Example-2:")
given_set = [15, 22, 14, 26, 32, 9, 16, 8]
print(subset_sum(given_set, 53))
