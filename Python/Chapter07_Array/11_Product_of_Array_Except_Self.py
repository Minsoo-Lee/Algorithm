# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i = 0
        result = []
        tmp_lst = []
        tmp = 1
        for i in range(0, len(nums)):
            tmp_lst.append(tmp)
            tmp *= nums[i]
        print(tmp_lst)
        tmp = 1
        for i in range(len(nums) -  1, -1, -1):
            result.append(tmp_lst[i] * tmp)
            tmp *= nums[i]
            
        output = list(reversed(result))
        return output