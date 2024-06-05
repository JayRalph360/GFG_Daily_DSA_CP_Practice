def equilibrium(A):
        N = len(A)
        l, r = 0, N-1
        prefix, suffix = A[l], A[r]
        
        while l <= r:
            if (prefix == suffix) and (l == r):
                return l+1
                
            if (prefix <= suffix) and (prefix + A[l+1] >= prefix):
                if (prefix + A[l+1] == prefix):
                    l += 1
                    prefix += 1
                else:
                    l += 1
                    prefix += A[l]
            else:
                if (suffix + A[r-1] == suffix):
                    r -= 1
                    suffix += 1
                else:
                    r -= 1
                    suffix += A[r]
        return -1


A = list(map(int, input().split(",")))
print(equilibrium(A))


# Eg.1
# -7, 1, 5, 2, -4, 3, 0

# Eg.2
# 1, 2, 3, 4, 5, -1, -3, -2

# Eg.3
# 1, 2, 3, 4, 5, -1, -3, -2, -3

# Eg.4
# 1, 2, 3