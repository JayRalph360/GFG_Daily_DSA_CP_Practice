def min_swap(arr):
    n = len(arr)-1
    count, z = 0, 0
    for i in range(n, -1, -1):
        if arr[i] == 0:
            z += 1
        else:
            count += z

    return count 

arr = list(map(int, input().split(",")))
print(min_swap(arr))


# E.gs
# 1, 0, 1, 1, 1, 0, 0, 1
# 9

# 0, 1, 0, 1, 0
# 3

# 0, 0, 1, 0, 1, 0, 1, 1
# 3

# 1, 0, 0, 1, 0, 1, 0, 1, 1
# 7