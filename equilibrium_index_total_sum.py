def equilibrium(arr):
    n = len(arr)
    total_sum = 0
    
    for i in arr:
        total_sum += i
    
    prefix_sum, suffix_sum = 0, 0
    for i in range(n):
        suffix_sum = total_sum - prefix_sum - arr[i]
        if prefix_sum == suffix_sum:
            return i
        prefix_sum += arr[i]
        
    return -1
    
    
arr = list(map(int, input().split(",")))
print(equilibrium(arr))


# Approach 2

def equilibrium(arr):
    n = len(arr)
    total_sum = 0
    
    for i in arr:
        total_sum += i
    
    prefix_sum, suffix_sum = 0, 0
    for i in range(n):
        total_sum -= arr[i]
        if prefix_sum == total_sum:
            return i
        prefix_sum += arr[i]
        
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