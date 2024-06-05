def majority(arr):
    n = len(arr)
    freq = {}
    
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for i in freq:
        if freq[i] > n//2:
            return i
    return None


arr = [int(e) for e in input().split(",")]
print(majority(arr))


# Eg.1
# 3, 4, 3, 4, 3, 1, 3

# Eg.2
# 3, 4, 3, 2, 4, 4, 4, 4

# Eg.3
# 1, 3, 3, 1, 2