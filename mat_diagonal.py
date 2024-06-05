def diagonal(mat, n, m):
    prime = []
    sec = []
    for i in range(n):
        prime += [mat[i][i]]
        sec += [mat[i][m-1-i]]
    print("Primary diagonal: ", prime)
    print("Secondary diagonal: ", sec)
    

n = int(input())
m = int(input())
nums = [int(i) for i in input().split()]
mat = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        mat[i][j] = nums[(i*m)+j]
print(mat)
diagonal(mat, n, m)


# Input
# 4
# 4
# 1 2 3 4 4 3 2 1 7 8 9 6 6 5 4 3

# Output
# [[1, 2, 3, 4], [4, 3, 2, 1], [7, 8, 9, 6], [6, 5, 4, 3]]
# Primary diagonal:  [1, 3, 9, 3]
# Secondary diagonal:  [4, 2, 8, 6]


