def merge(arr, l, m, r):
    n1, n2 = m-l+1, r-m
    
    L, R = [], []
    for i in range(n1):
        L += [arr[l + i]]

    for j in range(n2):
        R += [arr[m + 1 + j]]

    i, j, k = 0, 0, l
    while (i < n1) and (j < n2):
        if (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def mergesort(arr, l, r):
    if l < r:
        m = l + (r-l)//2
        
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        
        merge(arr, l, m, r)
        
    return arr

arr = [int(e) for e in input().split(",")]
n = len(arr)
l, r = 0, n-1
print(mergesort(arr, 0, len(arr)-1))

# E.g 1
# 4, 7, 2, 8, 2, 1, 9, 3, 14

# E.g 2
# 12, 11, 13, 5, 6, 7