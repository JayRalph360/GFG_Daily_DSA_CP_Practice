def naimerger(A, B, C):
    D = A + B + C
    D.sort()
    return D


A = list(map(int, input().split(",")))
B = list(map(int, input().split(",")))
C = list(map(int, input().split(",")))

print(naimerger(A, B, C))


# 1, 2, 3, 4, 5
# 2, 3, 4
# 4, 5, 6, 7


# 1, 2, 3, 5
# 6, 7, 8, 9 
# 10, 11, 12