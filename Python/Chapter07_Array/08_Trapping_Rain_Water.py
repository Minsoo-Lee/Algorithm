# 

import copy

class Solution:
    def get_max_right_left(self, height, max):
        left = -1;
        right = -1;
        for i in range(len(height)):
            if height[i] == max:
                if left == -1:
                    left = i
                right = i
        return left, right
        
    def fill_water(self, trap_water, left, right, max):
        for i in range(left, right):
            trap_water[i] = max;
            
    def get_max_and_index(self, nums, index):
        max = 0
        max_index = 0
        for i in range(len(nums)):
            if max <= nums[i]:
                max = nums[i]
                max_index = i
        return max, index + max_index
    
    def trap(self, height: list[int]) -> int:
        trap_water = copy.deepcopy(height)
        print(height)
        max_height = max(height)
        left, right = self.get_max_right_left(height, max_height)
        self.fill_water(trap_water, left, right, max_height)
        if sorted(height) == height or sorted(height, reverse=True) == height:
            return 0
        else:
            while right > 0:
                print("1")
                right = left
                max_height, left = self.get_max_and_index(height[:right], 0)
                self.fill_water(trap_water, left, right, max_height)
            left, right = self.get_max_right_left(height, max(height))
            print(left, right)
            while left < len(height):
                print("2")
                left = right + 1
                max_height, right = self.get_max_and_index(height[left:], left)
                self.fill_water(trap_water, left, right, max_height)
        count = 0
        print(trap_water)
        for i in range(len(height)):
            count += (trap_water[i] - height[i])
        return count
            
        
        