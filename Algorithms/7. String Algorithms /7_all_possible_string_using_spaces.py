def to_string(str_list): 
    s = "" 
    for x in str_list: 
        if x == "$": 
            break
        s += x 
    return s 


def print_pattern_util(string, buffer, i, j, n):
    if(i==n):
        buffer[j] = "$"
        print(to_string(buffer))
        return
    
    # Either put the character 
    buffer[j] = string[i] 
    print_pattern_util(string, buffer, i+1, j+1, n) 
  
    # Or put a space followed by next character 
    buffer[j] = " "
    buffer[j+1] = string[i] 
  
    print_pattern_util(string, buffer, i+1, j+2, n)
    


def print_pattern(string):
    n = len(string)
    buffer = [0]*(2*n)
    buffer[0] = string[0]

    print_pattern_util(string, buffer, 1, 1, n)



print("Example-1:")
string = "ABCD"
print_pattern(string)

print("Example-2:")
string = "12345"
print_pattern(string)
