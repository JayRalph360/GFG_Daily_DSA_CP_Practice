def find_common(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    
    p1 = p2 = 0
    arr = []
    
    while (p1 < n1) and (p2 < n2):
        if arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr1[p1]:
            p2 += 1
        else:
            arr += [arr1[p1]]
            p1 += 1
            p2 += 1
    
    return arr
            

arr1 = list(map(int, input().split(",")))
arr2 = list(map(int, input().split(",")))
arr3 = list(map(int, input().split(",")))

arr = find_common(arr1, arr2)
print(find_common(arr, arr3))


# Eg.1
# 1, 5, 10, 20, 40, 80
# 6, 7, 20, 80, 100
# 3, 4, 15, 20, 30, 70, 80, 120


# Eg.2
# 1, 5, 5
# 3, 4, 5, 5, 10
# 5, 5, 10, 20