def find(arr, x):
    n = len(arr)
    m = len(arr[1])
    
    for i in range(n):
        if arr[i][m-1] == x:
            return f"{arr[i][m-1]} found in ({i, m-1})"
        if arr[i][m-1] > x:
            for j in range(m):
                if arr[i][j] == x:
                    return f"{arr[i][j]} found in ({i, j})"
    return f"No {x} in matrix"
    


n = int(input())
m = int(input())
nums = list(map(int, input().strip().split(",")))
arr = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = nums[(i*m)+j]
print(arr)
x = 43
print(find(arr, x))


# Input
# 3
# 4
# 1, 5, 9, 11, 14, 20, 21, 26, 0, 34, 43, 50

# Output
# [[1, 5, 9, 11], [14, 20, 21, 26], [0, 34, 43, 50]]
# 43 found in ((2, 2))
