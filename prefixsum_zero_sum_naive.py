def zero_sum(arr):
    n = len(arr)
    
    for i in range(n):
        prefix_sum = arr[i]
        if prefix_sum == 0:
            return True
            
        for j in range(1, n):
            prefix_sum += arr[j]
            if prefix_sum == 0:
                return True
                
    return False
                

arr = list(map(int, input().split(",")))
print(zero_sum(arr))


# Input
# 1, 4, -2, -2, 5, -4, 3
# Output
# True

# Input
# -3, 2, 3, 1, 6
# Output
# False

# Input
# 4, 2, -3, 1, 6
# Output
# True

# Input
# 4, 2, 0, 1, 6
# Output
# True