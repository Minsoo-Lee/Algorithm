# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        max_num = 0
        
        for i, ch in enumerate(s):
            if ch in dic and start <= dic[ch]:
                start = dic[ch] + 1
            else:
                max_num = max(max_num, i - start + 1)
            dic[ch] = i
            
            
        return max_num