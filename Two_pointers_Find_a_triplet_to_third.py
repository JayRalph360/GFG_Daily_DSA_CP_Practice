def tripleT(arr):
  n = len(arr)-1
  arr.sort()
  
  for i in range(n,-1,-1):
    l, r = 0, i-1
    while l <= r:
      if arr[i] == arr[l] + arr[r]:
        print(arr[i], arr[l], arr[r])
        l, r = l+1, r-1
      elif arr[i] > arr[l] + arr[r]:
        l += 1
      else:
        r -= 1


arr = list(map(int, input().split(",")))
print(tripleT(arr))

# Input:
# 5, 32, 1, 7, 10, 50, 19, 21, 2

# Output:

# 21 2 19
# 10 5 5
# 7 2 5
# 2 1 1
# None
