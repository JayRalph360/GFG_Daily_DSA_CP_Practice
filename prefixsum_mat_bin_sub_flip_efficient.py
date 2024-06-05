def flipfunc(mat, dp):
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            
            if dp[i][j] % 2 != 0:
                mat[i-1][j-1] = int(mat[i-1][j-1])^1

def binmat(mat, n, m, Q, q):
    dp = [[0 for i in range(m+2)] for i in range(n+2)]
    
    for k in q:
        x1, y1, x2, y2 = k
        
        dp[x1][y1] += 1
        dp[x2+1][y2+1] += 1
        dp[x1][y2+1] -= 1
        dp[x2+1][y1] -= 1
        
    flipfunc(mat, dp)
    
    return mat


n = int(input())
m = int(input())
nums = list(map(int, input().split(",")))
mat = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        mat[i][j] = nums[i*m+j]
        
Q = int(input())
qnums = list(map(int, input().split(",")))
q = [[0 for i in range(4)] for i in range(Q)]
for i in range(Q):
    for j in range(4):
        q[i][j] = qnums[i*4+j]

print(binmat(mat, n, m, Q, q))


# Input 1
# 2
# 3
# 0, 1, 0, 1, 1, 0
# 3
# 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 3

# Output 1
# [[0, 1, 0], [0, 1, 0]]

# Input 2
# 2
# 3
# 0, 1, 0, 1, 1, 0
# 1
# 1, 1, 2, 3

# Output 2
# [[1, 0, 1], [0, 0, 1]]