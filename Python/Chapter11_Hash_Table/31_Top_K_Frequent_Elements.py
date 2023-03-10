# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        sorted_dict = sorted(dic.items(), key = lambda item: item[1], reverse = True)
        result = []
        for n in sorted_dict:
            result.append(n[0])
            if len(result) == k:
                return result