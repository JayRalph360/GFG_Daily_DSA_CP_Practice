def equilibrium(arr):
    n = len(arr)
    
    for i in range(1, n-1):
        l_sum, r_sum = 0, 0
        for l in range(i):
            l_sum += arr[l]
        
        for r in range(i+1, n):
            r_sum += arr[r]
            
        if l_sum == r_sum:
            return i
    return -1
            

arr = list(map(int, input().split(",")))
print(equilibrium(arr))

# Eg.1
# -7, 1, 5, 2, -4, 3, 0

# Eg.2
# 1, 2, 3, 4, 5, -1, -3, -2

# Eg.3
# 1, 2, 3, 4, 5, -1, -3, -2, -3

# Eg.4
# 1, 2, 3