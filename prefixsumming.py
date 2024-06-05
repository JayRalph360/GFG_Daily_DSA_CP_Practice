def prefixsumming(arr, n):
    prefixsum = [arr[0]]
    
    for i in range(n-1):
        prefixsum += [prefixsum[i]+arr[i+1]]
    
    return prefixsum

n = int(input())
arr = list(map(int, input().split(",")))
print(prefixsumming(arr, n))


# Input
# 4
# 10, 4, 16, 20

# Output
# [10, 14, 30, 50]