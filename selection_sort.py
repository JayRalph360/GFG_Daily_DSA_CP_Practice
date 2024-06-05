def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_element = arr[i]
        min_index = i
        for j in range(i+1, n):
            if arr[j] < min_element:
                min_element = arr[j]
                min_index = j
                
        # arr[i], arr[min_index] = arr[min_index], arr[i]
        arr[min_index] = arr[i]
        arr[i] = min_element
        
    return arr
    
arr = [int(e) for e in input().split(",")]
print(selection_sort(arr))

# Eg. 1
# 2, 6, 1, 8, 4

# Eg. 2
# 3, 4, 3, 8, 9, 6, 8