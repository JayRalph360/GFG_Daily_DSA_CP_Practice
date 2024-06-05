def heapify(arr, i, n):
    
    root = i
    l = 2*i + 1
    r = 2*i + 2
    
    if (l < n) and (arr[root] < arr[l]):
        root = l
    if (r < n) and (arr[root] < arr[r]):
        root = r
        
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        i = root
        heapify(arr, i, n)


def maxheap(arr, n):
    for j in range(n//2-1, -1, -1):
        heapify(arr, j, n)
        

def heap_sort(arr):
    n = len(arr)
    
    maxheap(arr, n)
        
    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, 0, j)
        
    return arr
    
    
arr = list(map(int, input().split(",")))
print(heap_sort(arr))


# E.g 1
# 9, 7, 5, 10, 11, 12, 20, 2, 1, 4

# E.g 2
# 10, 20, 15, 17, 9, 21