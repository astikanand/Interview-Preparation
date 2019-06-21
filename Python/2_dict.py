# initialize
dict1 = {1: "abcd", "apples": 3, "fruits": ["apples", "mangoes"], }
print("Initial Dict = {}".format(dict1))

# Insert
dict1[2] = 7
print("Modified Dict after insertion = {}".format(dict1))

# len(): size of the dict
print("Size of the dict = {}\n".format(len(dict1)))

# get(): access
print("Key = {} and Val = {}".format("apples", dict1["apples"]))
print("Key = {} and Val = {}".format("fruits", dict1.get("fruits", False)))
print("Key = {} and Val = {}\n".format("mangoes", dict1.get("mangoes", False)))

# key in dict: Membership check
print("mangoes present in dict1 ? : {}".format("mangoes" in dict1))
print("apples present in dict1 ? : {}\n".format("apples" in dict1))

# items(): set of key, val 
print("Items = {}".format(dict1.items()))

# keys(): all the keys of dict
print("Keys = {}".format(dict1.keys()))

# values(): all the values of dict
print("Values = {}\n".format(dict1.values()))

# setdefault(): get the value if key present else sets the default value to key
print("Key = {} and Val = {}".format("apples", dict1.setdefault("apples", 0)))
print("Key = {} and Val = {}\n".format("mangoes", dict1.setdefault("mangoes", 0)))

print("Dict Now = {}".format(dict1))

# update(): update from other dictionary
dict2 = {"mangoes": 5, "oranges": 3}
dict1.update(dict2)
print("Dict after Updated from Dict2 = {}".format(dict1))

# del: delete the key
del dict1["fruits"]
print("Dict after deleting 'fruits' = {}\n".format(dict1))

# copy(): copy the dict
dict2 = dict1.copy()
print("Copied Dict = {}".format(dict2))

# clear(): clear the dict
dict1.clear()
print("Dict after clearing = {}\n".format(dict1))

# fromkeys(): dict from keys
seq = ('name', 'age', 'sex')
print ("New Dictionary from sequence: {}".format(dict.fromkeys(seq)))
print ("New Dictionary from sequence: {}".format(dict.fromkeys(seq, 10)))