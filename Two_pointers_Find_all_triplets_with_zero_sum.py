def tripleZ(arr):
  n = len(arr)
  
  for i in range(n-1):
    s = set()
    # print(s)
    for j in range(i+1, n):
      x = -(arr[i] + arr[j])
      # print("x",x)
      
      if x in s:
        print(x, arr[i], arr[j])
      else:
        s.add(arr[j])
        # print("s",s)
        

arr = list(map(int, input().split(",")))
print(tripleZ(arr))


# Input:
# 1, 2, -3, 4, -1, -2, 0

# Output:
# 2 1 -3
# -1 1 0
# -2 2 0
# 4 -3 -1
# None
