def partition(arr, l, r):
    i = l

    for j in range(l, r+1):
        if arr[j] <= arr[r]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    return i-1


def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)

        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)
        
    return arr


arr = [int(e) for e in input().split(",")]
print(quicksort(arr, 0, len(arr)-1))



# E.g 1
# 10, 7, 8, 9, 1, 5

# E.g 2
# 4, 7, 2, 8, 2, 1, 9, 3, 14