def leader(arr):
    n = len(arr)-1
    i, lead, leaders = 1, arr[n], [arr[n]]
    
    while i < n:
        if (arr[n-i] > lead):
            lead = arr[n-i]
            leaders += [lead]
        i += 1
        
    leaders = leaders[::-1]
    print(leaders)
        
arr = [int(e) for e in input().split(",")]
leader(arr)

# E.g 1
# 16, 17, 4, 3, 5, 2

# Eg.2
# 1, 2, 3, 4, 5, 2