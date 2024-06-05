def find(mat, n, m, x):
    l = 0
    h = n-1
    
    while l <= h:
        mid = l + (h-l)//2
        
        if x == mat[mid][0]:
            return f"{x} can be found in ({mid, 0})"
            
        if x == mat[mid][m-1]:
            return f"{x} can be found in ({mid, m-1})"
            
        if x > mat[mid][0] and x < mat[mid][m-1]:
            return binsearch(mat[mid], mid, x)
            
        if x < mat[mid][0]:
            h = mid - 1
        if x > mat[mid][m-1]:
            l = mid + 1

    return f"{x} not in mat"


def binsearch(arr, i, x):
    l = 0
    r = m-1
    
    while l <= r:
        mid = l + (r-l)//2
        
        if x == arr[mid]:
            return f"{x} can be found in ({i, mid})"
        if x < arr[mid]:
            r = mid - 1
        elif x > arr[mid]:
            l = mid + 1
            
    return f"{x} not in mat"
    


x = int(input())
n = int(input())
m = int(input())
nums = [int(i) for i in input().split(",")]
mat = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        mat[i][j] = nums[(i*m)+j]
        # mat[i][j] = nums[(i*m)+(j%m)]

print(mat)        
print(find(mat, n, m, x))

# a = [[ 0, 6, 8, 9, 11], [20, 22, 28, 29, 31], [36, 38, 50, 61, 63 ], [64, 66, 100, 122, 128]]

# Input
# 22
# 4
# 5
# 0, 6, 8, 9, 11, 20, 22, 28, 29, 31, 36, 38, 50, 61, 63, 64, 66, 100, 122, 128

# Output
# [[0, 6, 8, 9, 11], [20, 22, 28, 29, 31], [36, 38, 50, 61, 63], [64, 66, 100, 122, 128]]
# 66 can be found in ((3, 1))


# Input
# 3
# 4
# 1, 5, 9, 11, 14, 20, 21, 26, 0, 34, 43, 50

# Output
# [[1, 5, 9, 11], [14, 20, 21, 26], [0, 34, 43, 50]]
# 43 found in ((2, 2))