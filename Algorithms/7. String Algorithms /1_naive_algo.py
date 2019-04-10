# Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(pat, txt) that prints all occurrences of pat[] in txt[]. 
# You may assume that n > m.


def naive_pattern_search(pat, text):
    m = len(pat)
    n = len(text)

    for i in range(n-m+1):
        flag = True
        for j in range(m):
            if(pat[j] != text[i+j]):
                flag = False
        
        if(flag):
            print("Pattern found at index {}".format(i))


print("Example-1:")
txt = "AABAACAADAABAABA"
pat = "AABA"
naive_pattern_search(pat, txt)

print("Example-2:")
txt = "abracadabra"
pat = "ab"
naive_pattern_search(pat, txt)


# Time Complexity:
# Best Case: O(n) - First character of pattern is not present in text
# Worst Case: O(n-m+1)(m) - All characters of the text and pattern are same OR only the last character is different.
