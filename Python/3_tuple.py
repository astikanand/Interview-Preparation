# creation of tuple
tup1 = ('physics', 'chemistry', 1997, 2000)

# Convert to tuple
tup2 = tuple([2, 3, 4, 1, 2, 6])

# Both tuple initially
print("Tuple tup1 : {}".format(tup1))
print("Tuple tup2 : {}\n".format(tup2))

# access
print("4th Element in tup1 : {}".format(tup1[3]))
print("4th Element in tup2 : {}\n".format(tup2[3]))

# Size of tup1
print("Size of tup1: {}".format(len(tup1)))

# Concatenation
tup3 = tup1 + tup2
print("Concatenated Tuple tup3 : {}\n".format(tup3))

# Membership
print("chemistry present in tup1 ? : {}".format('chemistry' in tup1))
print("chemistry present in tup2 ? : {}\n".format('chemistry' in tup2))

# Max-Min
print("Max of tup2 : {}".format(max(tup2)))
print("Min of tup2 : {}".format(min(tup2)))

# Slicing
print("tup2[2:5] : {}\n".format(tup2[2:5]))


# Delete
del tup1
print("Tuple tup1 after deleting: {}".format(tup1))