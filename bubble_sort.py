def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
    
    
arr = [int(e) for e in input().split(",")]
print(bubble_sort(arr))


# Eg. 1
# 2, 6, 1, 8, 4

# Eg. 2
# 3, 4, 3, 8, 9, 6, 8