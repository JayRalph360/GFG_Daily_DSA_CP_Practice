def tripletsum(arr):
  n = len(arr)
  
  for i in range(n-1):
    s = set()
    currsum = x-arr[i]
    for j in range(i+1, n):
      req = currsum-arr[j]
      if req in s:
        return (arr[i], req, arr[j])
      else:
        s.add(arr[j])
        

arr = list(map(int, input().split(",")))
x = int(input())
print(tripletsum(arr))


# Input
# 1, 4, 45, 6, 10, 8
# 22

# Output:
# (4, 10, 8)
