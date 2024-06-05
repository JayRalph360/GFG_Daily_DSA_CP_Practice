def longsub(arr, k):
    n = len(arr)
    maxlen = 0
    currsum = 0
    mod = 0
    
    d = {}
    
    for i in range(n):
        currsum += arr[i]
        mod = currsum % k
        
        if mod == 0:
            maxlen = i+1
        elif mod in d:
            if (maxlen < (i-d[mod])):
                maxlen = (i-d[mod])
        else:
            d[mod] = i

    return maxlen
    
    
k = int(input())
arr = list(map(int, input().split(",")))
print(longsub(arr, k))

# Input
# 3
# 2, 7, 6, 1, 4, 5
# Output
# 4
