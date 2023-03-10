# 1. Two Sum

nums = list(map(int, input().split()))
target = int(input())

def sum_two(nums, target):
    for i, num in enumerate(nums):
        find = target - num
        if find in nums[i + 1:]:
            return [i, nums[i + 1:].index(find) + i + 1]
        
print(sum_two(nums, target))