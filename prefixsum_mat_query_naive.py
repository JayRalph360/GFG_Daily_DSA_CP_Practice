def matrixUpdate(x1, y1, x2, y2, k):
    
    for i in range(x1, y2+1):
        for j in range(y1, x2+1):
            mat[i][j] += k

def matrixQuery(mat, Q, q):
    
    for i in range(Q):
        x1, y1, x2, y2, k = q[i][0], q[i][1], q[i][2], q[i][3], q[i][4]
    
        matrixUpdate(x1, y1, x2, y2, k)
            
    return mat

mat = [ [ 1, 0, 1, 2 ],
        [ 0, 2, 4, 1 ],
        [ 1, 2, 1, 0 ] ]
 
Q = 1
q = [ [0, 0, 1, 1, 2 ] ]

print(matrixQuery(mat, Q, q))
