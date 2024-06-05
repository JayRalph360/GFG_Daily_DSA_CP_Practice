def cswap(arr):
    n = len(arr)
    s = sorted(arr)
    d = {}
    
    for i in range(n):
        d[arr[i]] = i
    
    c = 0
    for i in range(n):
        if arr[i] != s[i]:
            c += 1
            a, b = arr[i], s[i]
            arr[i], arr[d[s[i]]] = arr[d[s[i]]], arr[i]
            d[a], d[b] = d[b], d[a]
            
    return c

arr = list(map(int, input().split(",")))
print(cswap(arr))


# 4, 3, 2, 1
# 2

# 1, 5, 4, 3, 2
# 2

# 2, 4, 5, 1, 3
# 3

# 101, 758, 315, 730, 472, 619, 460, 479
# 5

# 5, 1, 3, 2, 4
# 3