def merge(arr, L, R, n1, n2):
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
    

def mergesort(arr, l, r):
    l, r = 0, len(arr)-1
    if l < r:
        m = l + (r-l)//2
        
        n1, n2 = m-l+1, r-m
    
        L, R = [], []
        for i in range(n1):
            L += [arr[l + i]]
    
        for j in range(n2):
            R += [arr[m + 1 + j]]
            
        
        mergesort(L, l, r)  # (L, 0, len(L)-1)
        mergesort(R, l, r)  # (R, 0, len(R)-1)
        
        merge(arr, L, R, n1, n2)
        
    return arr

arr = [int(e) for e in input().split(",")]
print(mergesort(arr, 0, len(arr)-1))

# E.g 1
# 4, 7, 2, 8, 2, 1, 9, 3, 14

# E.g 2
# 12, 11, 13, 5, 6, 7