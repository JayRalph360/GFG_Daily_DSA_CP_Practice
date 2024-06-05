def abs_diff(arr):
    n = len(arr)
    prefixsum = 0
    suffixsum = sum(arr)
    
    for i in range(n):
        prefixsum += arr[i]
        diff = abs(suffixsum - prefixsum)
        suffixsum -= arr[i]
        arr[i] = diff
        
    return arr
        
        
arr = list(map(int, input().split(",")))
print(abs_diff(arr))


# Input
# 10, 4, 8, 3

# Output
# [15, 1, 11, 22]

# Input
# 5

# Output
# [0]

