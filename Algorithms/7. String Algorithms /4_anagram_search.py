def anagram_search(pat, text):
    m = len(pat)
    n = len(text)
    count_pat = [0]*256     # Total 256 characters
    count_text_window = [0]*256

    # fill the count_pat and count_text_window array
    for i in range(m):
        count_pat[ord(pat[i])] += 1
        count_text_window[ord(pat[i])] += 1
    
    # Starts searching anagrams or permutations
    for i in range(m, n):
        if(count_pat == count_text_window):
            print("Found at index {}".format(i-m))
        
        # Increase the frequency of next character and decrease the frequncy of first character in window
        count_text_window[ord(text[i])] += 1
        count_text_window[ord(text[i-m])] -= 1
    
    # Check for last window as it will be left in this loop
    if(count_pat == count_text_window):
            print("Found at index {}".format(n-m))


print("Anagram Search Example-1:")
txt = "BACDGABCDA"
pat = "ABCD"       
anagram_search(pat, txt)
