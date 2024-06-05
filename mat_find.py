arr = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12] ]
n = len(arr)
m = len(arr[1])

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()

# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 