def wave(arr):
    i, n = 1, len(arr)
    while i < n:
        if (i > 0) and (arr[i-1] < arr[i]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        elif (i+1 < n) and (arr[i+1] < arr[i]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
        
    return arr

arr = list(map(int, input().split(",")))
print(wave(arr))


# E.gs
# 10, 5, 6, 3, 2, 20, 100, 80
# 4, 7, 2, 8, 2, 1, 9, 3, 14