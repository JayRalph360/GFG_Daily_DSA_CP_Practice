def matrixUpdate(mat, aux):
    
    for i in range(n):
        for j in range(1, m):
            aux[i][j] += aux[i][j-1]
            
    for i in range(m):
        for j in range(1, n):
            aux[j][i] += aux[j-1][i]
            
    for i in range(n):
        for j in range(m):
            aux[i][j] += mat[i][j]


def updateQuery(aux, x1, y1, x2, y2, k, n, m):
    
    aux[x1][y1] += k
    if y2+1 < m:
        aux[x1][y2+1] -= k
    if x2+1 < n:
        aux[x2+1][y1] -= k
    if x2+1 < n and y2+1 < m:
        aux[x2+1][y2+1] += k
    

def matrixQuery(mat, Q, q, n, m):
    aux = [[0 for i in range(m)] for i in range(n)]
    
    for i in range(Q):
        x1, y1, x2, y2, k = q[i][0], q[i][1], q[i][2], q[i][3], q[i][4]
        updateQuery(aux, x1, y1, x2, y2, k, n, m)
        
    matrixUpdate(mat, aux)
        
    return aux

n = int(input())
m = int(input())
nums = list(map(int, input().split(",")))
mat = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        mat[i][j] = nums[(i*m)+j]

Q = int(input())
qnums = list(map(int, input().split(",")))
q = [[0 for i in range(5)] for i in range(Q)]

for i in range(Q):
    for j in range(5):
        q[i][j] = qnums[(i*5)+j]
        
print(matrixQuery(mat, Q, q, n, m))


# Input 1
# 3
# 4
# 1, 0, 1, 2, 0, 2, 4, 1, 1, 2, 1, 0
# 1
# 0, 0, 1, 1, 2

# Output 2
# [[3, 2, 1, 2], [2, 4, 4, 1], [1, 2, 1, 0]]

# Input 2
# 2
# 3
# 3, 2, 1, 2, 4, 4
# 2
# 0, 1, 1, 2, -1, 0, 0, 1, 1, 5

# Output 2
# [[8, 6, 0], [7, 8, 3]]
