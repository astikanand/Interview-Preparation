def check_subsequence(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    i = j = 0

    while(i < n1 and j < n2):
        if(str1[i] == str2[j]):
            i += 1

        j += 1
    

    print(i==n1)


print("Example-1: check_subsequence('AXY', 'ADXCPY')")
check_subsequence('AXY', 'ADXCPY')

print("\nExample-2: check_subsequence('AXY', 'YADXCP')")
check_subsequence('AXY', 'YADXCP')

print("\nExample-3: check_subsequence('mtsdet', 'meetsandmeets')")
check_subsequence('mtsdet', 'meetsandmeets')
