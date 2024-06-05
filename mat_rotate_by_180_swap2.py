def rotate(matrix):
    n = len(matrix)
    if n % 2:
        m = n//2+1
    else:
        m = n//2
        
    for i in range(m):
        
        if n % 2 and i == n//2:
            l, r = 0, n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l, r = l+1, r-1
        else:
            for j in range(n):
                matrix[i][j], matrix[n-1-i][n-1-j] = matrix[n-1-i][n-1-j], matrix[i][j]


    return mat


n = int(input())
nums = list(map(int, input().split()))
mat = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = nums[(i*n)+j]
print(mat)        
print(rotate(mat, n))

# Input
# 2
# 1 2 3 4
# [[1, 2], [3, 4]]

# Output
# [[4, 3], [2, 1]]


# Input
# 3
# 1 2 3 4 5 6 7 8 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Output
# [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


# Input
# 4
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6

# Output
# [[6, 5, 4, 3], [2, 1, 0, 9], [8, 7, 6, 5], [4, 3, 2, 1]]


# Input
# 5
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

# Output
# [[25, 24, 23, 22, 21], [20, 19, 18, 17, 16], [15, 14, 13, 12, 11], [10, 9, 8, 7, 6], [5, 4, 3, 2, 1]]
