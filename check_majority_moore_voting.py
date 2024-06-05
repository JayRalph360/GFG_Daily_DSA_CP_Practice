def majority(arr):
    n = len(arr)
    
    major, major_count = arr[0], 0
    for i in range(n):
        if arr[i] == major:
            major_count += 1
        else:
            major_count -= 1
        if major_count == 0:
            major_count = 1
            major = arr[i]
    return major, major_count
    
    count = 0
    for i in range(n):
        if arr[i] == major:
            count += 1
        if count > n//2:
            return True
    return False
    
arr = [int(e) for e in input().split(",")]
print(majority(arr))


# Eg.1
# 3, 4, 3, 4, 3, 1, 3

# Eg.2
# 3, 4, 3, 2, 4, 4, 4, 4

# Eg.3
# 1, 3, 3, 1, 2