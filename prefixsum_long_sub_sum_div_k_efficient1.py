def longsub(arr, k):
    n = len(arr)
    maxlen = 0
    currsum = 0
    mod = [0]*n
    
    d = {}
    
    for i in range(n):
        currsum += arr[i]
        mod[i] = currsum % k
        
        if mod[i] == 0:
            maxlen = i+1
        elif mod[i] not in d:
            d[mod[i]] = i
        else:
            if (maxlen < (i-d[mod[i]])):
                maxlen = (i-d[mod[i]])
                
    # print(arr)
    # print(mod)
    # print(d)
    
    return maxlen
    
    
k = int(input())
arr = list(map(int, input().split(",")))
print(longsub(arr, k))

# Input
# 3
# 2, 7, 6, 1, 4, 5
# Output
# 4
