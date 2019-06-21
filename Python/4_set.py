# set(): initilaize
set1 = set() 

# set(): convert to set
set2 = set([3, 4, 5, 3, 6, 5, 7, 5, 8])
  
# add(): Insert in set 
for i in range(1, 6): 
    set1.add(i) 
  
print("Set1 = {}\nSet2 = {}".format(set1, set2))

# discard(): Remove 8 from set2
set2.discard(8)
print("Set2 after 8 is removed = {}\n".format(set2))
  
# union(): Union of set1 and set2 
set3 = set1 | set2     # set1.union(set2) 
print("Union of Set1 & Set2: Set3 = {}".format(set3))
  
# intersection(): Intersection of set1 and set2 
set4 = set1 & set2     # set1.intersection(set2) 
print("Intersection of Set1 & Set2: Set4 = {}\n".format(set4))

# in : check membership
print("Is 7 present in set1 ? : {}".format(7 in set1))
print("Is 7 present in set2 ? : {}\n".format(7 in set2))

# Comparison Operators
# Checking relation between set3 and set4 
if set3 > set4:        # set3.issuperset(set4) 
    print("Set3 is superset of Set4.") 
elif set3 < set4:      # set3.issubset(set4) 
    print("Set3 is subset of Set4.") 
else : # set3 == set4 
    print("Set3 is same as Set4.") 
  
# displaying relation between set4 and set3 
if set4 < set3:        # set4.issubset(set3) 
    print("Set4 is subset of Set3.\n") 
  
# difference: between set3 and set4 
set5 = set3 - set4 
print("Elements in Set3 and not in Set4: Set5 = {}.".format(set5))
  
# isdisjoint(): Check if set4 and set5 are disjoint sets 
if set4.isdisjoint(set5): 
    print("Set4 and Set5 have nothing in common.") 
  
# clear(): Remove all the values of set5 
set5.clear() 
print("After applying clear on set5 now set5 = {}.".format(set5))