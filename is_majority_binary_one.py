def isMajority(arr, x):
    n = len(arr)
    l, r = 0, n-1
    
    while l < r:
        mid = l + (r-l)//2
        
        if arr[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1

    if (r + n//2 < n) and (arr[r + n//2] == x):
        return True
    else:
        return False
        

arr = [int(e) for e in input().split(",")]
x = int(input())
print(isMajority(arr, x))


# Eg.1
# 1, 2, 3, 3, 3, 3, 10
# 3

# Eg.2
# 1, 1, 2, 4, 4, 4, 6, 6
# 4

# Eg.3
# 1, 1, 1, 2, 2
# 1

# Eg.4
# 2, 2, 2, 2, 3, 3, 10
# 2