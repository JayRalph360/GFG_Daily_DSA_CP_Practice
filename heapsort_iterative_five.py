def heapify(arr, i, n):
    while True:
        rt = i
        l = i*2 + 1
        r = i*2 + 2
        
        if (l < n) and (arr[l] > arr[rt]):
            rt = l
        if (r < n) and (arr[r] > arr[rt]):
            rt = r
        
        if rt != i:
            arr[rt], arr[i] = arr[i], arr[rt]
            i = rt
        else:
            break
    

def maxheap(arr, n):
    for j in range(n//2-1, -1, -1):
        heapify(arr, j, n)


def heapsort(arr, l, n):
    maxheap(arr, n)
    
    
    for i in range(1, n):
        arr[0], arr[n-i] = arr[n-i], arr[0]
        heapify(arr, 0, n-i)
        
    return arr


arr = [int(i) for i in input().split(",")]
print(heapsort(arr, 0, len(arr)))
