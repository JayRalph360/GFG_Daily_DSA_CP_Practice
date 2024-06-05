def highest(m, q):
    prefixsum = [0]*n
    high = 0
    
    for i in range(m):
        a, b = q[i][0], q[i][1]
        
        prefixsum[a-1] += 100
        prefixsum[b] -= 100
        
    for i in range(1, n):
        prefixsum[i] += prefixsum[i-1]
        
        high = max(prefixsum[i], high)
    
    return high

n = 5
m = 3
q = [[2, 4], [1, 3], [1, 2]]
print(highest(m, q))
