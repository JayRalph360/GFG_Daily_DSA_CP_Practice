def merger(A, B, C):
    D = []
    i = j = k = 0
    max_ = max(A) + max(B) + max(C)
    
    while i < len(A) or j < len(B) or k < len(C):
        a = b = c = max_
        
        if i < len(A):
            a = A[i]
        if j < len(B):
            b = B[j]
        if k < len(C):
            c = C[k]
            
        if a <= b and a <= c:
            D += [a]
            i += 1
        if b <= c:
            D += [b]
            j += 1
        else:
            D += [c]
            k += 1
            
    return D

A = list(map(int, input().split(",")))
B = list(map(int, input().split(",")))
C = list(map(int, input().split(",")))

print(merger(A, B, C))


# 1, 2, 3, 4, 5
# 2, 3, 4
# 4, 5, 6, 7


# 1, 2, 3, 5
# 6, 7, 8, 9 
# 10, 11, 12