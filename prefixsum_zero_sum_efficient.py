def zero_sum(arr):
    n = len(arr)
    prefix_sum = []
    p_sum = 0
    
    for i in range(n):
        p_sum += arr[i]
        if p_sum == 0 or p_sum in prefix_sum:
            return True
            
        prefix_sum += [p_sum]
                
    return False
                

arr = list(map(int, input().split(",")))
print(zero_sum(arr))


# Hashing Approach
def zero_sum(arr):
    n = len(arr)
    prefix_sum = set()
    p_sum = 0
    
    for i in range(n):
        p_sum += arr[i]
        if p_sum == 0 or p_sum in prefix_sum:
            return True
            
        prefix_sum.add(p_sum)
                
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