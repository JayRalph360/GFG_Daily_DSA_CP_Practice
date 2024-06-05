def merge(arr, L, R):
    n1, n2 = len(L), len(R)
    i, j, k = 0, 0, 0
    
    while (i < n1) or (j < n2):
        if (i < n1) and (j < n2) and (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        elif (i < n1) and (j < n2) and (R[j] < L[i]):
            arr[k] = R[j]
            j += 1
        elif (i < n1):
            arr[k] = L[i]
            i += 1
        elif (j < n2):
            arr[k] = R[j]
            j += 1
        k += 1
    

def mergesort(arr):
    if len(arr) > 1:
        m = len(arr)//2
    
        L, R = arr[:m], arr[m:]
        
        mergesort(L)
        mergesort(R)
        
        merge(arr, L, R)
        
    return arr

arr = [int(e) for e in input().split(",")]
print(mergesort(arr))

# E.g 1
# 4, 7, 2, 8, 2, 1, 9, 3, 14

# E.g 2
# 12, 11, 13, 5, 6, 7