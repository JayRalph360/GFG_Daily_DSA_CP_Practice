def isMajority(arr, x):
    i, count = 0, 0
    n = len(arr)
    
    while i < n:
        if arr[i] == x:
            count += 1
            i += 1
        else:
            i += 1
    
    if 2 * count > n:
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