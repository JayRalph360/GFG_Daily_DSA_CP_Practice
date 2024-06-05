def min_swap(nums):
    n = len(nums)
    temp = sorted(nums)
    freq = dict()

    for i in range(n):
        freq[nums[i]] = i

    swap = 0
    for i in range(n):
        if nums[i] != temp[i]:
            swap += 1
            
            a, b = nums[i], temp[i]
            
            nums[i], nums[freq[b]] = nums[freq[b]], nums[i]
            freq[a], freq[b] = freq[b], freq[a]
            
    return swap

nums = [int(x) for x in input().split()]
print(min_swap(nums))


# 7 16 14 17 6 9 5 3 18
# 5 not 6

# 2, 8, 5, 4
# 1

# 10, 19, 6, 3, 5
# 2