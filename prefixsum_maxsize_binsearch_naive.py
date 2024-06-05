def binsearch(prefixsum, n, k):
    l, r = 1, n
    ans = -1
    
    while l <= r:
        mid = l + (r-l)//2
        
        for i in range(mid, n+1):
            if prefixsum[i] - prefixsum[i-mid] > k:
                i -= 1
                break
        
        if i == n:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
            
    return ans

def max_size(arr, k):
    n = len(arr)
    prefixsum = [0]*(n+1)
    
    for i in range(n):
        prefixsum[i+1] = prefixsum[i] + arr[i]
        
    return binsearch(prefixsum, n, k)


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
