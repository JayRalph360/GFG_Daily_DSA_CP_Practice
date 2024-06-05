def longsub(arr, k):
    n = len(arr)
    maxlen = 0
    
    for i in range(n):
        sums = 0
        
        for j in range(i, n):
            sums += arr[j]
            if sums % k == 0:
                maxlen = max(maxlen, j+1-i)
    
    return maxlen
    
    
k = int(input())
arr = list(map(int, input().split(",")))
print(longsub(arr, k))

# Input
# 3
# 2, 7, 6, 1, 4, 5
# Output
# 4