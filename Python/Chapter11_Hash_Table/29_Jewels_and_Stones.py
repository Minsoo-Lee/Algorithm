
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        result = 0
        
        for stone in stones:
            if stone in dic:
                dic[stone] += 1
            else:
                dic[stone] = 1
        
        for jewel in jewels:
            if jewel in dic:
                result += dic[jewel]
                
        return result