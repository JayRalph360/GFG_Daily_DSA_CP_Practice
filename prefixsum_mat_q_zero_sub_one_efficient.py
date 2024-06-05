def updateMatrix(mat):
    for i in range(n):
        for j in range(1, n):
            mat[i][j] += mat[i][j-1]
            
    for i in range(n):
        for j in range(1, n):
            mat[j][i] += mat[j-1][i]

def queryMatrix(mat, a, b, c, d):
    mat[a][b] += 1
    if c+1 < n:
        mat[c+1][b] -= 1
    if c+1 < n and d+1 < n:
        mat[c+1][d+1] += 1
    if d+1 < n:
        mat[a][d+1] -= 1
    

def matrixQuery(n, Q, q):
    mat = [[0 for i in range(n)] for i in range(n)]
    
    for i in range(Q):
        a, b, c, d = q[i][0], q[i][1], q[i][2], q[i][3]
        
        queryMatrix(mat, a, b, c, d)
    updateMatrix(mat)
        
    return mat
    
n = int(input())
Q = int(input())
qnums = list(map(int, input().split(",")))
q = [[0 for i in range(4)] for i in range(n)]

for i in range(Q):
    for j in range(4):
        q[i][j] = qnums[(i*4)+j]

print(matrixQuery(n, Q, q))

# Input 1
# 6
# 6
# 4, 0, 5, 3, 0, 0, 3, 4, 1, 2, 1, 2, 1, 1, 2, 3, 0, 0, 3, 1, 1, 0, 2, 4

# Output 1
# [[2, 2, 1, 1, 1, 0], 
# [3, 4, 4, 3, 2, 0], 
# [3, 4, 3, 3, 2, 0], 
# [2, 2, 1, 1, 1, 0], 
# [1, 1, 1, 1, 0, 0], 
# [1, 1, 1, 1, 0, 0]]

# Input 2
# 4
# 2
# 0, 0, 3, 3, 0, 0, 2, 2

# Output 2
# [[2, 2, 2, 1], 
# [2, 2, 2, 1], 
# [2, 2, 2, 1], 
# [1, 1, 1, 1]]