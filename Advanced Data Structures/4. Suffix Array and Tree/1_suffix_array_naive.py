def build_suffix_array_naive(word):
    suffixes = []
    n = len(word)
    for i in range(n):
        suffixes.append((i, word[i:]))
    
    suffixes.sort(key=lambda k: k[1])

    suffix_arr = []
    for i, _ in suffixes:
        suffix_arr.append(i)

    print("Built Suffix Array: {}".format(suffix_arr))
    return suffix_arr


def search(pat, suffix_arr, word):
    n = len(suffix_arr)
    l = 0; r = n-1
    flag = False
    while(l<=r):
        mid = (l+r)//2
        if(pat == word[suffix_arr[mid]:]):
            flag = True
            break
        if(pat < word[suffix_arr[mid]:]):
            r = mid-1
        else:
            l = mid+1
    
    if(flag):
        print("Pattern '{}' Found at index: {}.".format(pat, mid))
    else:
        print("Pattern '{}' NOT Found.".format(pat))



print("Suffix Array Naive Example:")
suffix_arr = build_suffix_array_naive("banana")
search("ana", suffix_arr, "banana")
search("nana", suffix_arr, "banana")
search("axy", suffix_arr, "banana")
