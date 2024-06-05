def bin_sort(A):
    N = len(A)
    z = 0
    
    for i in range(N-1, -1, -1):
        if A[i] == 0:
            z += 1
        else:
            A[i], A[i+z] = A[i+z], A[i]
    return A

A = [int(i) for i in input().split()]
print(bin_sort(A))

# Eg.1
# 1 0 1 1 0
# [0, 0, 1, 1, 1] Ans
