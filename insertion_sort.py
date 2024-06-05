def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


arr = list(map(int, input().split(",")))
print(insertion_sort(arr))

# Eg. 1
# 12, 2, 11, 13, 5, 6, 0

# Eg. 2
# 12, 11, 13, 5, 6