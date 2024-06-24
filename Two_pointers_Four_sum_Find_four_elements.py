def foursum(arr, X):
    n = len(arr)
    mp = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    for i in range(n - 1):
        for j in range(i + 1, n):
            summ = arr[i] + arr[j]

            if (X - summ) in mp:
                p = mp[X - summ]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                    print(arr[i], ", ", arr[j], ", ",
                          arr[p[0]], ", ", arr[p[1]], sep="")
                    return


arr = list(map(int, input().split(",")))
X = int(input())
foursum(arr, X)


# Input
# 1, 4, 45, 6, 10, 8
# 21

# Output:
# 1, 4, 6, 10
