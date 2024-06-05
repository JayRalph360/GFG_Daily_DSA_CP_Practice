def wave(arr):
    n = len(arr)
    arr.sort()
    print(arr)
    
    for i in range(1, n, 2):
        arr[i-1], arr[i] = arr[i], arr[i-1]
        
    return arr

arr = list(map(int, input().split(",")))
print(wave(arr))


# E.gs
# 10, 5, 6, 3, 2, 20, 100, 80
# 4, 7, 2, 8, 2, 1, 9, 3, 14