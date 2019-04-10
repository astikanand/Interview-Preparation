def manacher_longest_palindromic_substring(text):
    # Preprocess the given text
    new_text = "#"
    for ch in text:
        new_text += ch
        new_text += "#"
    
    n = len(new_text)
    P = [0]*n    # Array to store palindromic values

    # Center(C) : Index of mirror line
    # Right(R)  : Where we are going to end our bounds on right hand side
    # Left(L)   : No need to store Left(L) as it can be calculated using something like i_mirror
    C = 0
    R = 0

    # Iterate through entire new_text
    for i in range(n):
        i_mirror = C - (i-C)  # Mirror index of the value currently pointing

        # If the right bound(R) is greater than value currently pointing
        if(R > i):
            P[i] = min(R-i, P[i_mirror])
        else:
            P[i] = 0
        
        # Expansion around the currently pointing index
        while((i + P[i] + 1) < n and new_text[i + P[i] + 1] == new_text[i - P[i] - 1]):
            P[i] += 1
        
        # Updating C and R
        if(P[i] > R-i):
            C = i
            R = i + P[i]

    # Find the length of largest palindrome and center_index
    max_pal_len = max(P)
    center_index = P.index(max_pal_len)

    # Print the longest palindrome
    start = int((center_index-max_pal_len)/2)
    end = int((center_index+max_pal_len)/2)

    print("Largest Palindromic Susbtring: {}".format(text[start:end]))




print("Manacher Example-1:")
txt = "abaabc"
manacher_longest_palindromic_substring(txt)

print("Manacher Example-2:")
txt = "babcbabcbaccba"
manacher_longest_palindromic_substring(txt)

print("Manacher Example-3:")
txt = "abaaba"
manacher_longest_palindromic_substring(txt)

print("Manacher Example-4:")
txt = "abababa"
manacher_longest_palindromic_substring(txt)

print("Manacher Example-5:")
txt = "forgeeksskeegfor"
manacher_longest_palindromic_substring(txt)
