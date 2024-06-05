def matrixDiagonally(mat):
    n = len(mat)
    d = {}
    for i in range(n):
        for j in range(n):
            if (i+j) not in d:
                d[i+j] = []
            d[i+j].append(mat[i][j])
            
    ans = []
    for key in d:
        if key%2 == 0:
            ans.extend(d[key][::-1])
        else:
            ans.extend(d[key])
    return ans


# For Input: 
# 5
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# Your Output: 
# 1 2 6 11 7 3 4 8 12 16 21 17 13 9 5 10 14 18 22 23 19 15 20 24 25