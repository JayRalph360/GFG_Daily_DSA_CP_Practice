def max_size(arr, k):
    n = len(arr)
    ans = n
    prefixsum = 0
    start = 0
    not_possible = False
    
    for end in range(n):
        prefixsum += arr[end]
    
        while prefixsum > k:
            prefixsum -= arr[start]
            start += 1
            ans = min(ans, end + 1 - start)
            
            if prefixsum == 0:
                not_possible = True
                break
            
        if not_possible:
            ans = -1
            break
        
    return ans


k = int(input())
arr = list(map(int, input().split(",")))
print(max_size(arr, k))


# Input
# 8
# 0, 2, 3, 4

# Output
# 2

# Input
# 14
# 1, 2, 10, 4

# Output
# 2

# Input
# 8
# 1, 2, 10, 4

# Output
# -1