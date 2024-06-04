def closest(arr1, arr2, x):
  m, n = len(arr1), len(arr2)
  l, r = 0, n-1
  d = x
  
  while l < m and r > 0:
    if abs(arr1[l] + arr2[r]-x) < d:
      ans_l, ans_r = arr1[l], arr2[r]
      d = abs(arr1[l] + arr2[r] - x)
      
    if arr1[l] + arr2[r] < x:
      l += 1
    else:
      r -= 1
    
  return ans_l, ans_r

arr1 = list(map(int, input().split(",")))
arr2 = list(map(int, input().split(",")))
x = int(input())

print(closest(arr1, arr2, x))

# Input
# 1, 4, 5, 7
# 10, 20, 30, 40
# 38

# Output
# (7, 30)
