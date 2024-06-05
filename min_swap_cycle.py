def minSwaps(arr): 
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
  
    arrpos.sort(key=lambda it: it[1]) 
  
    vis = {k: False for k in range(n)} 
  
    ans = 0
    for i in range(n): 

        if vis[i] or arrpos[i][0] == i: 
            continue
  
        cycle_size = 0
        j = i 
  
        while not vis[j]: 
  
            vis[j] = True
  
            j = arrpos[j][0] 
            cycle_size += 1

        if cycle_size > 0: 
            ans += (cycle_size - 1) 
  
    return ans


arr = list(map(int, input().split(",")))
print(minSwaps(arr))

# 4, 3, 2, 1
# 2

# 1, 5, 4, 3, 2
# 2

# 2, 4, 5, 1, 3
# 3

# 101, 758, 315, 730, 472, 619, 460, 479
# 5

# 5, 1, 3, 2, 4
# 3