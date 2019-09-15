def substring_palindrome_common_cut(A, B):
    n = len(A)
    flag = False
    for i in range(n):
        if is_palindrome(A[:i]+B[i:]):
            print("Common Point: {} and Palindrome : {}".format(i, A[:i]+B[i:]))
            flag = True
    
    if not flag:
        print("No common point found!")


def substring_palindrome_any_cut(A, B):
    n = len(A)
    for i in range(1, n, 1):
        for j in range(n-1, -1, -1):
            if is_palindrome(A[:i]+B[j:]):
                print("Common Points: {} {} and Palindrome : {}".format(i, j, A[:i]+B[j:]))



def is_palindrome(string):
    n = len(string)
    flag = True
    for i in range(n//2):
        if(string[i] != string[n-i-1]):
            flag = False
            break
    
    return flag


# substring_palindrome_common_cut("astik", "bmksa")
# substring_palindrome_common_cut("astik", "bmksaz")

substring_palindrome_any_cut("astik", "bmksa")
# substring_palindrome_any_cut("astik", "bmksaz")
