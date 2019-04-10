def rabin_karp_search(pat, text):
    base = 256         # Total number of characters, if you consider less numbers of characters base can be set accordingly
    q = 101            # Prime to take modulo
    p_hash = 0         # Hash value for pattern
    t_hash = 0         # Hash value for text
    m = len(pat)
    n = len(text)

    # Calculating h that will be used for rehashing:  h = pow(base, m-1)%q
    h = 1
    for i in range(m-1):
        h = (h*base)%q
    
    # Calculating hash for pat and initial text
    for i in range(m):
        p_hash = (p_hash*base + ord(pat[i]))%q      # ord(char) : gives ascii value of char
        t_hash = (t_hash*base + ord(text[i]))%q

    # Slide the pattern over text one by one 
    for i in range(n-m+1):
        # Check the hash values of current window of text and pattern
        if t_hash == p_hash:   # if the hash values match then only check for characters one by one 
            for j in range(m):
                if(text[i+j] != pat[j]):
                    break
            if(j==m-1):
                print("Found at index {}".format(i))
        
        # Calculate hash value for next window of text: Remove leading digit, add trailing digit 
        if i+m < n:
            t_hash = ((t_hash - h*ord(text[i]))*base + ord(text[i+m]))%q

            # We might get negative values of t_hash, converting it to positive 
            if t_hash < 0: 
                t_hash = t_hash+q 


print("Rabin-Karp Example-1:")
txt = "bacbabababacaca"
pat = "ababaca"
rabin_karp_search(pat, txt)

print("\nRabin-Karp Example-2:")
txt = "abracadabra"
pat = "ab"
rabin_karp_search(pat, txt)

print("\nRabin-Karp Example-3:")
txt = "AABAACAADAABAABA"
pat = "AABA"
rabin_karp_search(pat, txt)

# Complexity:
# Time: O(n)
# Space: O(1)