def calculate_lps(pat):
    m = len(pat)
    lps = [0]*m
    i = 1; j = 0

    while(i < m):
        if(pat[i] == pat[j]):
            lps[i] = j+1
            i+=1
            j+=1
        elif(j>0):
            j = lps[j-1]
        else:
            lps[i] = 0
            i+=1
    
    return lps


# print("LPS Example-1:")
# pat = "ababaca"
# print(str(calculate_lps(pat)))

# print("\nLPS Example-2:")
# pat = "abcdabeabf"
# print(str(calculate_lps(pat)))

# Complexity:
# Time: O(m)
# Space: O(m)


def KMP_search(pat, text):
    lps = calculate_lps(pat)
    i=0; j=0
    m = len(pat)
    n = len(text)

    while(i<n):
        if(text[i] == pat[j]):
            i+=1
            j+=1
            if(j == m):
                print("Found at index {}".format(i-j))
                j = lps[j-1]
        elif(j>0):
            j = lps[j-1]
        else:
            i+=1

print("KMP Example-1:")
txt = "bacbabababacaca"
pat = "ababaca"
KMP_search(pat, txt)

print("\nKMP Example-2:")
txt = "abracadabra"
pat = "ab"
KMP_search(pat, txt)

print("\nKMP Example-3:")
txt = "AABAACAADAABAABA"
pat = "AABA"
KMP_search(pat, txt)

# Complexity:
# Time: O(m+n)
# Space: O(m)