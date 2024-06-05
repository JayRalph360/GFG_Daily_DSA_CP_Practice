def heapify(arr, i, j):
    idx = j
    while idx == j:
            idx = 2*j + 1
            
            if (idx < i-1) and (arr[idx] < arr[idx+1]):
                idx += 1
                
            if (idx < i) and (arr[int((idx-1)/2)] < arr[idx]):
                arr[idx], arr[int((idx-1)/2)] = arr[int((idx-1)/2)], arr[idx]
                j = idx


def maxheap(arr, n):
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr):
    n = len(arr)
    
    maxheap(arr, n)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    return arr

arr = list(map(int, input().split(",")))
print(heapsort(arr))



# E.g 1
# 9, 7, 5, 10, 11, 12, 20, 2, 1, 4

# E.g 2
# 10, 20, 15, 17, 9, 21