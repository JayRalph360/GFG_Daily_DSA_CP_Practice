def wave(arr):
    i, n = 1, len(arr)
    
    if (n == 2) and (arr[i-1] < arr[i]):
        arr[i], arr[i-1] = arr[i-1], arr[i]

    while (i+1 < n):
        if (arr[i] <= arr[i-1]) and (arr[i] <= arr[i+1]):
            i += 2
        if (i < n) and (arr[i-1] < arr[i]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        elif (i+1 < n) and (arr[i+1] < arr[i]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

arr = list(map(int, input().split(",")))
print(wave(arr))

# E.gs
# 10, 5, 6, 3, 2, 20, 100, 80
# 4, 7, 2, 8, 2, 1, 9, 3, 14